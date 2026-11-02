#!/usr/bin/env python3
"""Coverage accounting: collector rows vs captured vs usable, plus download gaps. Outputs data/coverage_summary.csv, data/not_captured.csv, data/download_gaps.csv"""
import re, os, glob, pandas as pd
SRC="/home/user/drive-src/AI Robotics (Filtered Sources)/Filtered Sources/"; B="/home/user/embodied-ai-governance-v5/"
# 1) README tables: rows/captured per set and region, plus not-captured lists
summary=[]; notcap=[]
for readme in glob.glob(SRC+"*/README.md")+glob.glob(SRC+"6. Europe/Oct 15 - Version 1/README.md"):
    region=readme.replace(SRC,"").split("/")[0]; txt=open(readme,encoding="utf8").read()
    for m in re.finditer(r"\|\s*\*{0,2}(Robotics sprint|Database, non-sprint)\*{0,2}[^|]*\|[^|]*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|",txt):
        summary.append(dict(region=region,set=("sprint" if "sprint" in m.group(1) and "non" not in m.group(1) else "database"),rows=int(m.group(2)),captured=int(m.group(3)),pdf=int(m.group(4)),html=int(m.group(5))))
    for sec,setname in [("Sprint sources not captured","sprint"),("non-sprint sources","database"),("Non-sprint sources not captured","database")]:
        i=txt.find(sec)
        if i<0: continue
        block=txt[i:]
        for m in re.finditer(r"^\|\s*(D?\d{3})\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|",block,re.M):
            notcap.append(dict(region=region,set=setname,number=m.group(1),tier=m.group(2).strip(),title=m.group(3).strip(),reason=m.group(4).strip(),url=m.group(5).strip()))
s=pd.DataFrame(summary).drop_duplicates(); nc=pd.DataFrame(notcap).drop_duplicates()
s.to_csv(B+"data/collector_coverage.csv",index=False); nc.to_csv(B+"data/not_captured.csv",index=False)
# 2) download gaps: files the collectors captured but this study could not download (>10 MB cap or permission), with recovery status
gaps=[("Africa","sprint","002_PDF-REPUBLIC-OF-GHANA-NATIONAL-ARTIFICIAL-INTELLIGENCE.pdf",11.4,"over 10 MB download cap","recovered via Drive text reader"),
("Africa","sprint","005_Africa-Has-The-Lowest-Internet-Usage-Rate-In-The-World-At.pdf",20.1,"over 10 MB download cap","text read but not persisted; not in corpus"),
("Africa","sprint","008_Relatório.pdf",18.6,"over 10 MB download cap","recovered via Drive text reader (same document as Latin America 011)"),
("Africa","database","D062_Kenya-AI-Strategy-2025-2030.pdf",23.9,"over 10 MB download cap","recovered via Drive text reader"),
("Africa","database","D007_Egypt.pdf",10.7,"over 10 MB download cap","recovered via Drive text reader"),
("Africa","database","D032_Second-Edition-Published-By-MCIT-January-2025.pdf",10.7,"over 10 MB download cap","recovered via Drive text reader"),
("Africa","database","D059_Artificial-Intelligence-Unit.pdf",66.1,"over 10 MB download cap","reader returned no text (scanned); stub"),
("Africa","database","D040_AI-READINESS-ASSESSMENT-KENYA-2REDO-OK_Codee-Pdf.pdf",29.1,"over 10 MB download cap","recovered via Drive text reader"),
("Africa","database","D072_The-Smart-Africa-S-Board-Unveils-The-Inaugural-Africa-AI-C.html",None,"Drive permission denied on download","recovered via Drive text reader"),
("Africa","database","D070_Smart-Africa-And-Wadhwani-AI-Global-Partner-To-Advance-Res.html",None,"Drive permission denied on download","recovered via Drive text reader"),
("Africa","database","D078_Smart-Africa-Convened-Technical-Experts-To-Discuss-The.html",None,"Drive permission denied on download","recovered via Drive text reader"),
("Africa","database","D069_Artificial-Intelligence-For-Africa-Smart-Africa.html",None,"Drive permission denied on download","recovered via Drive text reader"),
("Africa","database","D079_Artificial-Intelligence-Smart-Africa.html",None,"Drive permission denied on download","recovered via Drive text reader"),
("Africa","database","D071_Smart-Africa-Steering-Committee-Convenes-In-Kigali-And-End.html",None,"Drive permission denied on download","recovered via Drive text reader"),
("North America","sprint","005_Blueprint-For-An-AI-Bill-Of-Rights-OSTP-The-White-House.pdf",11.7,"over 10 MB download cap","recovered via Drive text reader"),
("North America","sprint","095_Spoken-Language-Interaction-With-Virtual-Agents-And-Robots.pdf",10.9,"over 10 MB download cap","recovered via Drive text reader"),
("Latin America & Caribbean","sprint","011_Relatório.pdf",18.6,"over 10 MB download cap","recovered via Drive text reader"),
("Latin America & Caribbean","database","D036_National-Artificial-Intelligence-Strategy-Of-Costa-Rica.pdf",55.0,"over 10 MB download cap","reader returned no text (scanned); stub"),
("Asia","sprint","186_Spoken-Language-Interaction-With-Virtual-Agents-And-Robots.pdf",10.9,"over 10 MB download cap","recovered via Drive text reader (duplicate of USA 095)"),
("Asia","sprint","021_PDF-Revolutionizing-Health-And-Safety.pdf",18.6,"over 10 MB download cap","same ILO document captured in Europe (in corpus)"),
("Asia","database","D122_India-AI-Impact-Summit-2026.pdf",13.2,"over 10 MB download cap","reader returned no text (scanned); stub"),
("Middle East","database","D039_Make-An-Impact-On-The-Future-AI-Strategy-Of-The-Israeli-Hi.pdf",13.4,"over 10 MB download cap","recovered via Drive text reader"),
("Oceania","sprint","044_PDF-Shaping-A-Future-New-Zealand.pdf",11.1,"over 10 MB download cap","recovered via Drive text reader"),
("Europe","sprint","Strategic Program AI_web [C10144].pdf (Italy)",11.6,"over 10 MB download cap","recovered via Drive text reader"),
("Europe","sprint","La Moncloa. IA ¿qué es la Estrategia de Inteligencia Artificial 2024 [C08364].pdf (Spain)",17.0,"over 10 MB download cap","recovered via Drive text reader"),
("Europe","sprint","ENIA A4-RGB largo copia [C08363].pdf (Spain)",17.0,"over 10 MB download cap","recovered via Drive text reader"),
("Europe","sprint","National AI Strategy Report [C08362].pdf (Spain)",17.1,"over 10 MB download cap","recovered via Drive text reader"),
("Europe","sprint","Guidelines for AI procurement - GOV.UK [C06938].pdf (UK)",11.7,"over 10 MB download cap","recovered via Drive text reader"),
("Europe","sprint","revolutionizing health and safety [C07461].pdf (ILO)",18.6,"over 10 MB download cap","same ILO document captured as web page in corpus"),
("Europe","sprint","Spoken Language Interaction with Virtual Agents and Robots (SLIVAR) [C04567].pdf",11.0,"over 10 MB download cap","recovered via Drive text reader (USA 095)"),
("Europe","database","Intelligenza Artificiale l'Italia lancia la strategia nazionale [C07550].pdf (Italy)",12.8,"over 10 MB download cap","recovered via Drive text reader"),
("Europe","database","Conoce la Estrategia Nacional de Inteligencia Artificial (ENIA) [C11484].pdf (Spain)",30.1,"over 10 MB download cap","recovered via Drive text reader"),
("Europe","database","Malta – The Strategy and Vision for Artificial Intelligence in Malta 2030 [C02843].pdf",11.6,"over 10 MB download cap","recovered via Drive text reader"),
("Europe (Version 1 copies)","sprint/database","397, 040, 037, 405, 120, D249, D133, D100 (eight Version 1 copies of the above)",None,"over 10 MB download cap","same documents as the Version 2 rows above")]
g=pd.DataFrame(gaps,columns=["region","set","file","size_mb","reason","status"]); g.to_csv(B+"data/download_gaps.csv",index=False)
print(s.to_string()); print("not captured rows parsed:",len(nc)); print(nc.groupby(["region","set"]).size().to_string()); print("download gaps:",len(g))
