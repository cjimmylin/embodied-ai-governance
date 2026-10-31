#!/usr/bin/env python3
"""Deterministic multilingual lexicon features over the FULL text of each document's primary file.
Outputs data/lexicon_features.csv: for each lexicon, raw count, density per 1,000 words, and presence."""
import re, os, json, pandas as pd
B="/home/user/embodied-ai-governance-v4/"
reg=pd.read_csv(B+"data/registry.csv")
L={}
# embodied categories
L["lex_robot_any"]=r"robot|robót|robotik|ロボット|机器人|機器人|로봇|робот|روبوت|רובוט|หุ่นยนต์"
L["lex_humanoid"]=r"humanoid|android|humanoide|휴머노이드|人形机器人|人型机器人|ヒューマノイド|人型ロボット|гуманоид|أندرويد"
L["lex_cobot"]=r"\bcobot|collaborative robot|robot colaborativo|robot collaboratif|kollaborative[rn]? Roboter|協働ロボット|协作机器人|협동\s?로봇"
L["lex_industrial_robot"]=r"industrial robot|robot industrial|robot industriel|Industrieroboter|産業用ロボット|工业机器人|산업용\s?로봇|промышленн\w* робот"
L["lex_logistics_mobile"]=r"\bAGV\b|\bAMRs?\b|autonomous mobile robot|warehouse robot|mobile robot|industrial truck|robot móvil|mobiler Roboter|搬送ロボット|移动机器人|이동\s?로봇"
L["lex_delivery_robot"]=r"delivery robot|sidewalk robot|last-mile robot|robot de reparto|robot de entrega|配送ロボット|配送机器人|배달\s?로봇|실외이동로봇"
L["lex_service_robot"]=r"service robot|robot de servicio|robot de service|Serviceroboter|サービスロボット|服务机器人|서비스\s?로봇"
L["lex_domestic_robot"]=r"household robot|domestic robot|home robot|robot vacuum|robotic vacuum|robot doméstico|家庭用ロボット|家用机器人|가정용\s?로봇"
L["lex_social_robot"]=r"social robot|companion robot|socially assistive|robot social|robot compagnon|ソーシャルロボット|社交机器人|陪伴机器人|소셜\s?로봇|반려\s?로봇"
L["lex_care_robot"]=r"care robot|nursing robot|assistive robot|eldercare robot|elder-care robot|robot de cuidado|robot asistencial|Pflegeroboter|介護ロボット|护理机器人|养老机器人|돌봄\s?로봇|간병\s?로봇"
L["lex_educational_robot"]=r"educational robot|robot in education|robots in education|robot educativo|教育用ロボット|教育机器人|교육용\s?로봇"
L["lex_sex_robot"]=r"sex robot|sexbot|sex doll|robot sexual|robot sexuel|Sexroboter|セックスロボット|性爱机器人|섹스\s?로봇"
L["lex_surgical_robot"]=r"surgical robot|robotic surgery|robot-assisted surgery|robotic-assisted|da Vinci|medical robot|cirugía robótica|chirurgie robotique|Operationsroboter|手術ロボット|手术机器人|의료\s?로봇|수술\s?로봇|хирургическ\w* робот"
L["lex_exoskeleton"]=r"exoskeleton|exosuit|prosthe|wearable robot|exoesqueleto|exosquelette|Exoskelett|外骨格|外骨骼|외골격"
L["lex_autonomous_vehicle"]=r"autonomous vehicle|self-driving|driverless|automated driving|automated vehicle|autonomous car|autonomous driving|vehículo autónomo|conducción autónoma|véhicule autonome|autonomes Fahr|自動運転|自动驾驶|무인\s?차량|자율주행|беспилотн\w* (автомобил|транспорт)"
L["lex_drone"]=r"\bdrones?\b|\bUAVs?\b|\bUAS\b|unmanned aerial|unmanned aircraft|\bdron(es)?\b|ドローン|无人机|無人機|드론|беспилотн\w* летательн|طائرة بدون طيار"
L["lex_maritime_rail"]=r"autonomous ship|unmanned surface|autonomous vessel|maritime autonomous|unmanned underwater|autonomous train|自律航行|自动驾驶船|자율운항"
L["lex_agri_robot"]=r"agricultural robot|agri-robot|farm robot|agrobot|robot agrícola|農業用ロボット|农业机器人|농업용\s?로봇|milking robot"
L["lex_space_extreme"]=r"space robot|planetary rover|underwater robot|nuclear decommissioning|mining robot|rescue robot|search and rescue robot|宇宙ロボット|救援机器人"
L["lex_military_laws"]=r"lethal autonomous|autonomous weapon|killer robot|military robot|armed drone|\bLAWS\b|weapon system|armas autónomas|robots asesinos|autonome Waffen|自律型致死|自律型兵器|致命性自主武器|자율\s?무기|автономн\w* оружи|الأسلحة الذاتية"
L["lex_police_security"]=r"police robot|policing robot|security robot|law enforcement robot|surveillance robot|robot policial|警備ロボット|安防机器人|경찰\s?로봇"
L["lex_embodied_ai_term"]=r"embodied AI|embodied intelligence|physical AI|embodied agent|具身智能|身体性|エンボディド|IA incorporada|IA encarnada|физическ\w* ИИ"
# named instruments
L["lex_eu_ai_act"]=r"\bAI Act\b|Artificial Intelligence Act|Regulation \(EU\) 2024/1689|2024/1689|Ley de (Inteligencia Artificial|IA) de la UE|KI-Verordnung|KI-Gesetz|AI法|人工智能法案|AI 법|règlement sur l'IA|Reglamento de IA"
L["lex_eu_machinery"]=r"Machinery Regulation|Regulation \(EU\) 2023/1230|2023/1230|Machinery Directive|2006/42/EC|Maschinenverordnung|Reglamento de Máquinas"
L["lex_product_liability"]=r"Product Liability Directive|85/374|2024/2853|product liability|Produkthaftung|responsabilidad por productos|製造物責任|产品责任|제조물\s?책임"
L["lex_civil_law_rules_robotics"]=r"Civil Law Rules on Robotics|2015/2103\(INL\)|P8_TA\(2017\)0051|electronic person"
L["lex_gdpr"]=r"\bGDPR\b|General Data Protection Regulation|2016/679|RGPD|DSGVO"
L["lex_unesco_rec"]=r"UNESCO.{0,40}Recommendation on the Ethics|Recommendation on the Ethics of Artificial Intelligence|Recomendación sobre la ética de la inteligencia artificial|Recommandation sur l'éthique de l'IA"
L["lex_oecd_principles"]=r"OECD.{0,30}(AI )?Principles|OECD Recommendation on Artificial Intelligence|Principios de la OCDE|OCDE"
L["lex_nist_rmf"]=r"NIST.{0,20}(AI )?RMF|AI Risk Management Framework|NIST AI 100-1"
L["lex_iso_10218"]=r"ISO\s?10218"
L["lex_iso_13482"]=r"ISO\s?13482"
L["lex_iso_ts_15066"]=r"ISO/?TS\s?15066"
L["lex_iso_3691"]=r"ISO\s?3691"
L["lex_iso_42001"]=r"ISO/?IEC\s?42001"
L["lex_iso_23894"]=r"ISO/?IEC\s?23894"
L["lex_iso_22989"]=r"ISO/?IEC\s?22989"
L["lex_iso_any"]=r"\bISO\b|\bIEC\b|Organización Internacional de Normalización|国際標準化機構|国际标准化组织"
L["lex_ieee_7000"]=r"IEEE\s?(P)?70\d\d|IEEE 7000|Ethically Aligned Design"
L["lex_ansi_r1506"]=r"R15\.06|ANSI/?A3|ANSI/?RIA"
L["lex_asimov"]=r"Asimov|Three Laws of Robotics|three laws|leyes de la robótica|lois de la robotique|ロボット三原則|机器人三定律|로봇\s?3원칙"
L["lex_coe_convention"]=r"Council of Europe.{0,40}(Framework )?Convention|Framework Convention on Artificial Intelligence|CETS 225"
L["lex_bletchley"]=r"Bletchley"
L["lex_hiroshima"]=r"Hiroshima (AI )?Process"
L["lex_ccw_gge"]=r"\bCCW\b|Group of Governmental Experts|Convention on Certain Conventional Weapons"
L["lex_eo_14110"]=r"Executive Order 14110|EO 14110|Safe, Secure, and Trustworthy"
L["lex_korea_robot_act"]=r"Intelligent Robots? (Development and Distribution Promotion )?Act|지능형\s?로봇\s?(개발\s?및\s?보급\s?촉진)?법"
# principles (coarse multilingual stems)
L["lex_p_transparency"]=r"transparen|explainab|explicab|erklärbar|透明|説明可能|可解释|투명|설명\s?가능|прозрачн|شفافية"
L["lex_p_fairness"]=r"\bfair|\bbias|discriminat|equit|non-discrimination|Gerechtigkeit|Diskriminierung|公平|公正|差別|歧视|偏见|공정|차별|справедлив|дискримин|عدالة|تمييز"
L["lex_p_safety"]=r"\bsafe|\bsafety|\bharm|seguridad|sécurité|Sicherheit|sicurezza|安全|危害|안전|безопасн|سلامة|אבטחה"
L["lex_p_accountability"]=r"accountab|liabil|responsib|responsabil|Haftung|Verantwort|責任|责任|책임|ответствен|подотчет|مسؤولية|مساءلة"
L["lex_p_privacy"]=r"privacy|data protection|personal data|privacidad|datos personales|vie privée|données personnelles|Datenschutz|プライバシー|個人情報|隐私|个人信息|개인정보|프라이버시|персональн|конфиденциальн|خصوصية"
L["lex_p_beneficence"]=r"well-being|wellbeing|welfare|benefit|social good|bienestar|bien-être|Wohl|福祉|幸福|福利|복지|благополуч|رفاه"
L["lex_p_autonomy"]=r"human autonomy|informed consent|\bconsent\b|self-determination|manipulat|autonomía humana|consentimiento|Selbstbestimmung|自己決定|同意|自主|자율성|동의|автономи"
L["lex_p_trust"]=r"\btrust|confianza|confiance|Vertrauen|fiducia|信頼|信任|신뢰|довери|ثقة"
L["lex_p_sustainability"]=r"sustainab|environmental|climate|sostenib|durabilit|nachhaltig|持続可能|環境|可持续|环境|지속\s?가능|устойчив|экологи|استدامة"
L["lex_p_dignity"]=r"dignity|dignidad|dignité|Würde|dignità|尊厳|尊严|존엄|достоинств|كرامة"
L["lex_p_solidarity"]=r"solidarit|inclusion|inclusive|social cohesion|inclusión|cohesión|Inklusion|包摂|包容|포용|солидарн|инклюзив|تضامن"
L["lex_p_human_oversight"]=r"human oversight|human control|human-in-the-loop|human in the loop|meaningful human control|human supervision|supervisión humana|control humano|contrôle humain|menschliche Aufsicht|人間の関与|人間による監視|人工监督|人类监督|인간의\s?감독|человеческ\w* контрол|الإشراف البشري"
L["lex_p_robustness"]=r"robust|cybersecur|cyber security|reliab|resilien|ciberseguridad|fiabilidad|robustesse|Robustheit|Cybersicherheit|堅牢|サイバーセキュリティ|信頼性|鲁棒|网络安全|可靠|견고|사이버\s?보안|надежн|кибербезопас|موثوقية"
L["lex_p_inclusive_growth"]=r"innovation|competitiveness|economic growth|productivity|innovación|competitividad|Innovation|Wettbewerbsfähig|イノベーション|競争力|创新|竞争力|혁신|경쟁력|инновац|конкурентоспособ|ابتكار"
L["lex_p_physical_safety"]=r"collision|injur|bodily|physical harm|physical safety|force limit|power and force|machine safety|protective stop|speed and separation|lesion|daño físico|seguridad física|Verletzung|Maschinensicherheit|衝突|身体的|傷害|碰撞|人身伤害|충돌|상해|신체적|травм|физическ\w* вред"
L["lex_p_proximity"]=r"human-robot interaction|human–robot interaction|\bHRI\b|human-robot collaboration|shared workspace|proximity|physical interaction|interacción humano-robot|collaboration homme-robot|Mensch-Roboter|人間とロボット|人とロボット|人机交互|人机协作|인간-로봇|взаимодейств\w* человека и робота"
L["lex_p_liability_physical"]=r"strict liability|product liability|damage caused by|tort|negligence|responsabilidad civil|responsabilidad objetiva|responsabilité civile|Gefährdungshaftung|Produkthaftung|不法行為|製造物責任|侵权|产品责任|불법행위|제조물\s?책임|деликт|гражданск\w* ответствен"
L["lex_p_autonomy_level"]=r"level(s)? of autonomy|degree of automation|autonomy level|SAE level|levels of automation|autonomous operation|fully autonomous|nivel de autonomía|Autonomiegrad|自律レベル|自動化レベル|自主等级|自动化程度|자율성\s?수준|уровень автономности"
L["lex_p_certification"]=r"certif|conformity assessment|CE mark|type approval|conformité|Konformitätsbewertung|Zertifizier|certificación|evaluación de la conformidad|認証|適合性評価|认证|合格评定|인증|적합성\s?평가|сертифик|оценк\w* соответств"
L["lex_p_dual_use"]=r"dual-use|dual use|weapon|military|defen[cs]e|warfare|armament|doble uso|militar|arma|double usage|militaire|Dual-Use|militärisch|Waffe|軍事|兵器|武器|军事|军用|군사|무기|двойного назначения|военн|оружи|عسكري|سلاح"
pat={k:re.compile(v,re.I) for k,v in L.items()}
rows=[]
# incremental: reuse rows computed earlier for documents whose text length is unchanged (the lexicon list itself is fixed)
cache={}
if os.path.exists(B+"data/lexicon_features.csv") and os.path.exists(B+"data/lexicon_cache_key.json"):
    try:
        key=json.load(open(B+"data/lexicon_cache_key.json"))
        if key.get("lexicons")==sorted(L):
            old=pd.read_csv(B+"data/lexicon_features.csv"); chars=dict(zip(key["doc_id"],key["text_chars"]))
            cache={r.doc_id:(chars.get(r.doc_id),r) for r in old.itertuples(index=False)}
    except Exception as e: print("cache unusable:",e); cache={}
hit=0
for _,d in reg.iterrows():
    c=cache.get(d.doc_id)
    if c and c[0]==d.text_chars:
        rows.append(c[1]._asdict()); hit+=1; continue
    rec={"doc_id":d.doc_id}
    txt=""
    if d.text_usable and isinstance(d.text_path,str) and os.path.exists(d.text_path):
        txt=open(d.text_path,encoding="utf8",errors="replace").read()
    words=max(1,len(re.findall(r"\w+",txt)))
    rec["lex_words"]=words if txt else 0
    for k,p in pat.items():
        n=len(p.findall(txt)) if txt else 0
        rec[k]=n; rec[k+"_pk"]=round(1000*n/words,3) if txt else None
    rows.append(rec)
out=pd.DataFrame(rows); out.to_csv(B+"data/lexicon_features.csv",index=False)
json.dump({"lexicons":sorted(L),"doc_id":list(reg.doc_id),"text_chars":[int(x) if pd.notna(x) else None for x in reg.text_chars]},open(B+"data/lexicon_cache_key.json","w"))
print("lexicon rows reused from cache:",hit)
json.dump(L,open(B+"codebook/lexicons.json","w"),ensure_ascii=False,indent=1)
pres=(out[[c for c in out.columns if c.startswith("lex_") and not c.endswith("_pk") and c!="lex_words"]]>0).sum().sort_values(ascending=False)
print("docs with usable text:",(out.lex_words>0).sum()); print(pres.to_string())
