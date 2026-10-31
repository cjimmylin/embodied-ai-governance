"""Direct harvests from legal databases with open endpoints. Each source writes candidates/API_<source>.csv in the candidate schema."""
import requests, csv, re, time, json, sys, html, os
from urllib.parse import quote, urlencode
B="/home/user/collection-round-2/"; OUT=B+"candidates/"
UA={"User-Agent":"Mozilla/5.0 (research crawler; CEI embodied-AI governance study; contact mail@drjimmylin.com)"}
COLS=["candidate_id","title_original","title_en","jurisdiction","subnational","issuer","year","instrument_type","binding_nature","status","robot_types","language","url_primary","url_secondary","source_database","confidence","notes"]
def write(src,rows):
    with open(OUT+f"API_{src}.csv","w",newline="",encoding="utf8") as fh:
        w=csv.DictWriter(fh,fieldnames=COLS); w.writeheader()
        for i,r in enumerate(rows,1):
            r=dict(r); r.setdefault("candidate_id",f"{src.upper()[:2]}A-{i:03d}"); 
            for c in COLS: r.setdefault(c,"")
            w.writerow(r)
    print(src,len(rows),flush=True)
def get(url,**kw):
    for a in range(3):
        try:
            r=requests.get(url,headers={**UA,**kw.pop("headers",{})},timeout=60,**kw)
            if r.status_code==200: return r
            if r.status_code in (429,503): time.sleep(5*(a+1)); continue
            return r
        except Exception as e:
            time.sleep(3)
    return None
ROBOT_HINT=[("robot","other_embodied"),("humanoid","humanoid_general_purpose"),("unmanned aircraft","drones_uas"),("drone","drones_uas"),("remotely piloted","drones_uas"),("automated driving","autonomous_road_vehicles"),("automated vehicle","autonomous_road_vehicles"),("autonomous vehicle","autonomous_road_vehicles"),("driver assistance","autonomous_road_vehicles"),("lane keeping","autonomous_road_vehicles"),("machinery","industrial_manipulators"),("surgical","surgical_medical_robots"),("exoskeleton","rehabilitation_exoskeleton_prosthetic"),("lethal autonomous","military_autonomous_weapons"),("autonomous weapon","military_autonomous_weapons"),("toy","toys_entertainment_robots"),("maritime autonomous","autonomous_maritime_or_rail"),("自動運転","autonomous_road_vehicles"),("特定自動運行","autonomous_road_vehicles"),("無人航空機","drones_uas"),("遠隔操作型小型車","delivery_robots"),("産業用ロボット","industrial_manipulators"),("ロボット","other_embodied"),("人形机器人","humanoid_general_purpose"),("具身智能","humanoid_general_purpose"),("机器人","other_embodied"),("自动驾驶","autonomous_road_vehicles"),("智能网联汽车","autonomous_road_vehicles"),("无人驾驶航空器","drones_uas"),("无人机","drones_uas"),("로봇","other_embodied"),("자율주행","autonomous_road_vehicles"),("드론","drones_uas"),("무인항공기","drones_uas"),("휴머노이드","humanoid_general_purpose"),("robô","other_embodied"),("veículo autônomo","autonomous_road_vehicles"),("veículos autônomos","autonomous_road_vehicles"),("aeronave","drones_uas"),("exoesqueleto","rehabilitation_exoskeleton_prosthetic"),("humanoide","humanoid_general_purpose"),("Roboter","other_embodied"),("Drohne","drones_uas"),("automatisiert","autonomous_road_vehicles")]
def hint(title):
    t=title.lower(); return "; ".join(sorted({c for k,c in ROBOT_HINT if k.lower() in t}))

# ---------------- EUR-Lex via CELLAR SPARQL
def eurlex():
    kws=["robot","unmanned aircraft","drone","automated driving","automated vehicle","autonomous vehicle","driver assistance","lane keeping","remotely piloted","machinery","toy safety","product liability","medical devices","lifts","emergency braking","automated lane","unmanned","vehicle automation","artificial intelligence","cyber resilience","general product safety","u-space","type-approval of motor vehicles","autonomous weapon","lethal autonomous"]
    types={"REG":"regulation_or_decree","REG_IMPL":"regulation_or_decree","REG_DEL":"regulation_or_decree","DIR":"regulation_or_decree","DIR_IMPL":"regulation_or_decree","DIR_DEL":"regulation_or_decree","DEC":"regulation_or_decree","DEC_IMPL":"regulation_or_decree","DEC_DEL":"regulation_or_decree","RES":"parliamentary_material","PROP_REG":"bill_or_draft_law","PROP_DIR":"bill_or_draft_law","COM":"consultation_or_white_paper","RECO":"intergovernmental_recommendation_or_resolution","RES_EP":"parliamentary_material","REC":"intergovernmental_recommendation_or_resolution"}
    rows={}; 
    for kw in kws:
        q=f'''PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
SELECT DISTINCT ?celex ?title ?date ?rt WHERE {{
 ?work cdm:resource_legal_id_celex ?celex ; cdm:work_has_resource-type ?rt ; cdm:work_date_document ?date .
 ?exp cdm:expression_belongs_to_work ?work ; cdm:expression_title ?title ; cdm:expression_uses_language <http://publications.europa.eu/resource/authority/language/ENG> .
 FILTER(CONTAINS(LCASE(STR(?title)),"{kw}"))
 FILTER(REGEX(STR(?rt),"/resource-type/(REG|REG_IMPL|REG_DEL|DIR|DIR_IMPL|DIR_DEL|DEC|DEC_IMPL|DEC_DEL|RES|RES_EP|PROP_REG|PROP_DIR|COM|RECO|REC)$"))
}} LIMIT 400'''
        r=get("https://publications.europa.eu/webapi/rdf/sparql",params={"query":q,"format":"json"})
        if not r: print("eurlex fail",kw); continue
        try: b=r.json()["results"]["bindings"]
        except Exception: print("eurlex parse fail",kw); continue
        for x in b:
            celex=x["celex"]["value"]; title=x["title"]["value"]; date=x["date"]["value"][:4]; rt=x["rt"]["value"].rsplit("/",1)[-1]
            if celex in rows: continue
            if re.search(r"written question|parliamentary question|answer given",title,re.I): continue
            rows[celex]=dict(title_original=title,title_en=title,jurisdiction="EU",issuer="European Union",year=date,instrument_type=types.get(rt,"regulation_or_decree"),
                binding_nature="legally_binding" if rt.startswith(("REG","DIR","DEC")) else ("voluntary_soft_law" if rt in ("RECO","REC") else "not_applicable"),
                status="published_current" if rt.startswith(("REG","DIR","DEC")) else "unknown",robot_types=hint(title),language="en",
                url_primary=f"https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:{celex}",url_secondary=f"https://publications.europa.eu/resource/celex/{celex}",source_database=f"EUR-Lex SPARQL ({kw})",confidence="medium",notes=f"CELEX {celex}; resource type {rt}")
        time.sleep(1)
    write("eurlex",list(rows.values()))

# ---------------- UK legislation.gov.uk (title search CSV)
def uk():
    kws=["automated vehicles","automated and electric","unmanned aircraft","drone","robot","autonomous","air navigation","product safety","machinery","supply of machinery","vehicle technology","self-driving","remotely piloted","toys (safety)","medical devices"]
    rows={}
    for kw in kws:
        for page in (1,2,3):
            r=get(f"https://www.legislation.gov.uk/title/{quote(kw)}/data.csv?page={page}")
            if not r or r.status_code!=200: break
            lines=r.text.splitlines()
            if len(lines)<2: break
            rd=csv.DictReader(lines)
            n=0
            for d in rd:
                n+=1; link=d.get("LINK") or d.get("Link") or ""; title=d.get("TITLE") or d.get("Title") or ""; year=d.get("YEAR") or d.get("Year") or ""; typ=d.get("DocumentMainType") or d.get("Type") or ""
                if typ.startswith("EuropeanUnion"): continue
                if not link or link in rows: continue
                rows[link]=dict(title_original=title,title_en=title,jurisdiction="GB",issuer="United Kingdom",year=year,instrument_type="statute_or_act" if "Act" in typ else "regulation_or_decree",binding_nature="legally_binding",status="unknown",robot_types=hint(title),language="en",url_primary=link,url_secondary=link.rstrip("/")+"/data.htm",source_database=f"legislation.gov.uk title search ({kw})",confidence="medium",notes=typ)
            if n<20: break
            time.sleep(0.5)
    write("uk",list(rows.values()))

# ---------------- Japan e-Gov law API v2 (full-text keyword search)
def japan():
    kws=["特定自動運行","無人航空機","遠隔操作型小型車","産業用ロボット","自動運転","ロボット","自動運行装置","介護ロボット","ドローン"]
    rows={}
    for kw in kws:
        off=0
        while True:
            r=get(f"https://laws.e-gov.go.jp/api/2/keyword?keyword={quote(kw)}&limit=100&offset={off}")
            if not r: break
            j=r.json(); items=j.get("items",[])
            for it in items:
                li=it["law_info"]; ri=it["revision_info"]; lid=li["law_id"]
                if lid in rows: rows[lid]["notes"]+=f"; also {kw}"; continue
                rows[lid]=dict(title_original=ri["law_title"],title_en="",jurisdiction="JP",issuer="Japan",year=str(li.get("promulgation_date",""))[:4],instrument_type="statute_or_act" if li["law_type"]=="Act" else "regulation_or_decree",binding_nature="legally_binding",status="in_force",robot_types=hint(ri["law_title"]+" "+kw),language="ja",url_primary=f"https://laws.e-gov.go.jp/law/{lid}",url_secondary=f"https://laws.e-gov.go.jp/api/2/law_data/{lid}",source_database=f"e-Gov law API keyword ({kw})",confidence="medium",notes=f"law type {li['law_type']}; full-text hit on {kw}")
            if len(items)<100 or len(rows)>600: break
            off+=100; time.sleep(0.5)
        time.sleep(0.5)
    write("japan",list(rows.values()))

# ---------------- Brazil Camara dos Deputados (bills) and Senado
def brazil():
    kws=["robô","robótica","robôs","veículo autônomo","veículos autônomos","drone","drones","aeronave não tripulada","exoesqueleto","humanoide","humanoides","carro autônomo","robótico","automação robótica","veículo autônomo de entrega"]
    rows={}
    for kw in kws:
        for page in range(1,6):
            r=get("https://dadosabertos.camara.leg.br/api/v2/proposicoes",params={"keywords":kw,"itens":100,"pagina":page,"ordem":"DESC","ordenarPor":"id"})
            if not r: break
            try: dados=r.json().get("dados",[])
            except Exception: break
            for d in dados:
                if d["siglaTipo"] not in ("PL","PLP","PEC","PDL","PRC","MPV","PLV"): continue
                key=d["id"]
                if key in rows: continue
                em=d.get("ementa","")
                if not re.search(r"rob[oô]|dron|aeronave n[aã]o tripulad|ve[ií]culo.{0,20}aut[oô]nom|exoesquelet|humanoid|autom[aá]tic[oa].{0,30}ve[ií]culo",em,re.I): continue
                rows[key]=dict(title_original=f"{d['siglaTipo']} {d['numero']}/{d['ano']} - {em[:180]}",title_en="",jurisdiction="BR",issuer="Câmara dos Deputados",year=str(d["ano"]),instrument_type="bill_or_draft_law",binding_nature="not_applicable",status="draft_or_bill_under_consideration",robot_types=hint(em),language="pt",url_primary=f"https://www.camara.leg.br/propostas-legislativas/{d['id']}",url_secondary=d["uri"],source_database=f"Camara dados abertos ({kw})",confidence="medium",notes=em[:200])
            if len(dados)<100: break
            time.sleep(0.5)
    write("brazil",list(rows.values()))

# ---------------- Switzerland Fedlex SPARQL
def fedlex():
    q='''PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
SELECT DISTINCT ?act ?title ?date WHERE { ?act a jolux:Act ; jolux:isRealizedBy ?exp . ?exp jolux:title ?title ; jolux:language <http://publications.europa.eu/resource/authority/language/DEU> . OPTIONAL { ?act jolux:dateDocument ?date } FILTER(REGEX(STR(?title),"Roboter|Drohne|automatisiert|autonom|unbemannt|Fahrzeugautomat","i")) } LIMIT 300'''
    r=get("https://fedlex.data.admin.ch/sparqlendpoint",params={"query":q},headers={"Accept":"application/sparql-results+json"})
    rows=[]
    if r:
        try:
            for x in r.json()["results"]["bindings"]:
                t=x["title"]["value"]; rows.append(dict(title_original=t,title_en="",jurisdiction="CH",issuer="Switzerland",year=x.get("date",{}).get("value","")[:4],instrument_type="regulation_or_decree",binding_nature="legally_binding",status="unknown",robot_types=hint(t),language="de",url_primary=x["act"]["value"],source_database="Fedlex SPARQL",confidence="low",notes=""))
        except Exception as e: print("fedlex parse",e, r.text[:200])
    write("fedlex",rows)

# ---------------- China gov.cn policy library JSON API (State Council and ministry documents)
def govcn():
    kws=["人形机器人","具身智能","机器人","自动驾驶","无人驾驶航空器","智能网联汽车","无人机","低空经济","养老机器人","手术机器人","工业机器人","服务机器人"]
    rows={}
    for t in ["zhengcelibrary_gw","zhengcelibrary_bm"]:
        for kw in kws:
            for page in range(0,8):
                r=get("https://sousuo.www.gov.cn/search-gov/data",params={"t":t,"q":kw,"timetype":"timeqb","sort":"score","sortType":"1","searchfield":"","p":page,"n":50,"type":"gwyzcwjk"})
                if not r: break
                try: lst=(r.json().get("searchVO") or {}).get("listVO") or []
                except Exception: break
                if not lst: break
                for it in lst:
                    url=it.get("url") or it.get("gname") or ""; title=(it.get("title") or "").replace("<em>","").replace("</em>","")
                    if not url or url in rows or not title: continue
                    rows[url]=dict(title_original=title,title_en="",jurisdiction="CN",issuer=(it.get("puborg") or it.get("fwdw") or "State Council / ministries"),year=str(it.get("pubtimeStr") or "")[:4],instrument_type="policy_guideline_or_code_of_practice",binding_nature="voluntary_soft_law",status="published_current",robot_types=hint(title+" "+kw),language="zh",url_primary=url,source_database=f"gov.cn policy library ({t}, {kw})",confidence="medium",notes=f"{it.get('pcode') or ''} {str(it.get('summary') or '')[:120]}")
                if len(lst)<50: break
                time.sleep(0.8)
            time.sleep(0.5)
    write("govcn",list(rows.values()))

# ---------------- Australia Federal Register of Legislation API
def australia():
    rows={}
    for kw in ["unmanned","remotely piloted","automated vehicle","autonomous","robot","drone","automated","vehicle standard","road vehicle standards"]:
        r=get("https://api.prod.legislation.gov.au/v1/titles",params={"$filter":f"contains(tolower(name),'{kw}')","$top":200})
        if not r: continue
        try: vals=r.json().get("value",[])
        except Exception: continue
        for v in vals:
            if v["id"] in rows: continue
            rows[v["id"]]=dict(title_original=v["name"],title_en=v["name"],jurisdiction="AU",issuer="Commonwealth of Australia",year=str(v.get("makingDate",""))[:4] or str(v.get("year","")),instrument_type="statute_or_act" if v.get("collection")=="Act" else "regulation_or_decree",binding_nature="legally_binding",status="in_force" if v.get("isInForce") else "superseded_or_repealed",robot_types=hint(v["name"]),language="en",url_primary=f"https://www.legislation.gov.au/{v['id']}/latest/text",source_database=f"legislation.gov.au API ({kw})",confidence="medium",notes=str(v.get("collection","")))
        time.sleep(0.5)
    write("australia",list(rows.values()))

# ---------------- US eCFR search (sections -> parts)
def ecfr():
    """Part-level CFR candidates from quoted-phrase section searches; text via the versioner API (the ecfr.gov pages block crawlers)."""
    rows={}; hits={}
    KW=['"robot"','"robots"','"robotic"','"unmanned aircraft"','"automated driving"','"autonomous vehicle"','"autonomous vehicles"','"exoskeleton"','"automated vehicle"','"automated vehicles"','"small unmanned aircraft"','"remote identification"','"driverless"','"self-driving"','"unmanned aircraft system"','"automated driving system"','"lethal autonomous"','"autonomous weapon"','"unmanned vessel"','"autonomous ship"']
    TITLES={"14","49","21","29","47","15","32","33","46","48","23","16","10","19","31","22","40","24","28","6","8","2"}
    for kw in KW:
        for page in range(1,8):
            r=get("https://www.ecfr.gov/api/search/v1/results",params={"query":kw,"per_page":100,"page":page})
            if not r: break
            try: j=r.json()
            except Exception: break
            for res in j.get("results",[]):
                h=res.get("hierarchy",{}); title=h.get("title"); part=h.get("part")
                if not (title and part): continue
                key=f"{title}-{part}"; hits.setdefault(key,set()).add((h.get("section") or "",kw))
                hd=res.get("headings",{})
                if key not in rows:
                    rows[key]=dict(title_original=f"{title} CFR Part {part}: {hd.get('part') or ''}",title_en=f"{title} CFR Part {part}: {hd.get('part') or ''}",jurisdiction="US",issuer=str(hd.get("chapter") or "United States Code of Federal Regulations")[:120],year="",instrument_type="regulation_or_decree",binding_nature="legally_binding",status="in_force",robot_types=hint(kw+" "+str(hd.get("part") or "")+" "+str(hd.get("section") or "")),language="en",
                        url_primary=f"https://www.ecfr.gov/api/versioner/v1/full/2026-10-01/title-{title}.xml?part={part}",url_secondary=f"https://www.ecfr.gov/current/title-{title}/part-{part}",source_database=f"eCFR search ({kw})",confidence="low",notes="",_title=title,_part=part)
            if page>=j.get("meta",{}).get("total_pages",1): break
            time.sleep(0.5)
    out=[]
    for key,row in rows.items():
        secs={s for s,_ in hits[key]}; kws=sorted({k.strip('"') for _,k in hits[key]})
        heading=row["title_original"].lower()
        strong=any(k in ("unmanned aircraft","small unmanned aircraft","remote identification","automated driving","automated driving system","autonomous vehicle","autonomous vehicles","driverless","self-driving","exoskeleton","robotic","robot","robots","unmanned aircraft system","unmanned vessel","autonomous ship","lethal autonomous","autonomous weapon") for k in kws)
        if not strong: continue
        for c in ("title_original","title_en"): row[c]=html.unescape(re.sub(r"<[^>]+>","",row[c]))
        if row["_title"] not in TITLES and len(secs)<3 and not re.search(r"robot|unmanned|aircraft|vehicle|driving|motor",heading): continue
        row["notes"]=f"{len(secs)} section hit(s); terms: {', '.join(kws)}"[:200]; row["source_database"]=f"eCFR search ({', '.join(kws)[:60]})"
        row.pop("_title"); row.pop("_part"); out.append(row)
    write("ecfr",out)

# ---------------- Korea law.go.kr HTML search
def korea():
    from bs4 import BeautifulSoup
    rows={}
    for kw in ["로봇","자율주행","드론","무인항공기","협동로봇","휴머노이드","무인비행장치","자율운항"]:
        r=get("https://www.law.go.kr/lsSc.do",params={"menuId":"1","subMenuId":"15","tabMenuId":"81","query":kw})
        if not r: continue
        soup=BeautifulSoup(r.text,"lxml")
        for a in soup.select("a"):
            t=a.get_text(" ",strip=True); href=a.get("href","") or a.get("onclick","")
            if len(t)>5 and ("법" in t or "규칙" in t or "령" in t) and kw[:2] in t and t not in rows:
                rows[t]=dict(title_original=t,title_en="",jurisdiction="KR",issuer="Republic of Korea",year="",instrument_type="statute_or_act" if t.endswith("법") else "regulation_or_decree",binding_nature="legally_binding",status="in_force",robot_types=hint(t),language="ko",url_primary="https://www.law.go.kr/lsSc.do?menuId=1&subMenuId=15&tabMenuId=81&query="+quote(t),source_database=f"law.go.kr search ({kw})",confidence="low",notes=href[:120])
        time.sleep(1)
    write("korea",list(rows.values()))

if __name__=="__main__":
    which=sys.argv[1:] or ["eurlex","uk","japan","brazil","fedlex","govcn","australia","ecfr","korea"]
    for w in which:
        try: globals()[w]()
        except Exception as e: print("FAILED",w,e,flush=True)

# ---------------- EUR-Lex works tagged with EuroVoc concepts (topic-tagged, not title-searched)
def eurovoc():
    concepts={"3740":"robotics","3848":"industrial robot","c_05303ddd":"autonomous vehicle","c_681e6d24":"drone","3030":"artificial intelligence"}
    types={"REG":"regulation_or_decree","REG_IMPL":"regulation_or_decree","REG_DEL":"regulation_or_decree","DIR":"regulation_or_decree","DIR_IMPL":"regulation_or_decree","DIR_DEL":"regulation_or_decree","DEC":"regulation_or_decree","DEC_IMPL":"regulation_or_decree","DEC_DEL":"regulation_or_decree","RES":"parliamentary_material","PROP_REG":"bill_or_draft_law","PROP_DIR":"bill_or_draft_law","PROP_DEC":"bill_or_draft_law","COM":"consultation_or_white_paper","RECO":"intergovernmental_recommendation_or_resolution","RES_EP":"parliamentary_material","REC":"intergovernmental_recommendation_or_resolution","OPIN":"parliamentary_material","OPIN_EESC":"parliamentary_material","OPIN_COR":"parliamentary_material","REPORT":"government_report_or_review","STAFF_WD":"government_report_or_review","CONCL":"intergovernmental_recommendation_or_resolution","GUIDELINE":"policy_guideline_or_code_of_practice","AGREE_INTERNATION":"international_agreement_or_resolution","COMMUNIC":"consultation_or_white_paper"}
    rows={}
    for cid,cname in concepts.items():
        q=f'''PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
SELECT DISTINCT ?celex ?title ?date ?rt WHERE {{
 ?work cdm:work_is_about_concept_eurovoc <http://eurovoc.europa.eu/{cid}> ; cdm:resource_legal_id_celex ?celex .
 OPTIONAL {{ ?work cdm:work_has_resource-type ?rt }} OPTIONAL {{ ?work cdm:work_date_document ?date }}
 ?exp cdm:expression_belongs_to_work ?work ; cdm:expression_title ?title ; cdm:expression_uses_language <http://publications.europa.eu/resource/authority/language/ENG> .
}} LIMIT 1000'''
        r=get("https://publications.europa.eu/webapi/rdf/sparql",params={"query":q,"format":"json"})
        if not r: print("eurovoc fail",cid); continue
        try: b=r.json()["results"]["bindings"]
        except Exception: print("eurovoc parse fail",cid); continue
        for x in b:
            celex=x["celex"]["value"]; title=x["title"]["value"]; date=(x.get("date",{}).get("value") or "")[:4]; rt=(x.get("rt",{}).get("value") or "").rsplit("/",1)[-1]
            if celex in rows: continue
            if re.match(r"^[679]",celex) or re.search(r"R\(\d\d\)$",celex): continue          # skip case law, national transposition, parliamentary questions, corrigenda
            if re.search(r"written question|parliamentary question|answer given|minutes of the sitting|notification of a concentration|non-opposition to a notified|state aid|call for proposals|vacancy notice|exchange rate|prior notification|summary of commission decision|antitrust|merger",title,re.I): continue
            rows[celex]=dict(title_original=title,title_en=title,jurisdiction="EU",issuer="European Union",year=date,instrument_type=types.get(rt,"regulation_or_decree" if celex[0]=="3" else "parliamentary_material"),
                binding_nature="legally_binding" if rt.startswith(("REG","DIR","DEC")) else ("voluntary_soft_law" if rt in ("RECO","REC","CONCL","GUIDELINE") else "not_applicable"),
                status="published_current" if rt.startswith(("REG","DIR","DEC")) else "unknown",robot_types=hint(title) or ("drones_uas" if cname=="drone" else ("autonomous_road_vehicles" if cname=="autonomous vehicle" else ("industrial_manipulators" if "robot" in cname else ""))),language="en",
                url_primary=f"https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:{celex}",url_secondary=f"https://publications.europa.eu/resource/celex/{celex}",source_database=f"EUR-Lex EuroVoc concept '{cname}'",confidence="medium",notes=f"CELEX {celex}; resource type {rt}; EuroVoc {cid}")
        time.sleep(1)
    write("eurovoc",list(rows.values()))
