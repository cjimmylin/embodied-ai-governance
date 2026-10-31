#!/usr/bin/env python3
"""Fold documents that exceeded the Drive download cap but were readable through the Drive text reader into the corpus.
Reads the saved reader JSON files, converts raw HTML with pandoc, writes Markdown under drive-md-out/_recovered, and
writes data/recovered_docs.csv (file-level rows in the same shape as files.csv, text_status='reader')."""
import os, re, json, subprocess, hashlib, pandas as pd, openpyxl
TR="/root/.claude/projects/-home-user/92a26033-b014-57db-85f3-dc52d2f52803/tool-results/"
OUTMD="/home/user/drive-md-out/_recovered/"
B="/home/user/embodied-ai-governance-v4/"
# (json file, drive id, region_code, set, region folder, subpath, filename)
EU2="6. Europe/Oct 29 - Version 2/Europe"
idx=openpyxl.load_workbook("/home/user/drive-src/AI Robotics (Filtered Sources)/Filtered Sources/6. Europe/Oct 29 - Version 2/Europe/INDEX.xlsx",read_only=True,data_only=True)["Index"]
it=idx.iter_rows(values_only=True); hdr=[str(h) for h in next(it)]; eu={r[0]:dict(zip(hdr,r)) for r in it if r and r[0]}
def eu2(ccode):
    f=eu[ccode]["File"]  # e.g. Sprint/1_Official_documents/Italy/Strategic Program AI_web [C10144].pdf
    parts=f.split("/"); return ("database" if parts[0]=="Non-sprint" else "sprint", EU2+"/"+"/".join(parts[:-1]), parts[-1])
R=[
 ("mcp-Google_Drive-read_file_content-1793369523057.txt","1V34Bz_X0R6h99gIUL9hwiuWoTcfzqCnD","OC","sprint","7. Oceania","","044_PDF-Shaping-A-Future-New-Zealand.pdf"),
 ("mcp-Google_Drive-read_file_content-1793369523284.txt","10HtReOPIriC3TCqlEhkgTwXDAOF3T82U","AF","database","1. Africa","Database (non-sprint)","D072_The-Smart-Africa-S-Board-Unveils-The-Inaugural-Africa-AI-C.html"),
 ("mcp-Google_Drive-read_file_content-1793369575395.txt","1DVLxclwPYWqFa8bQ7znQnnm14Rs2UQAP","AF","sprint","1. Africa","","002_PDF-REPUBLIC-OF-GHANA-NATIONAL-ARTIFICIAL-INTELLIGENCE.pdf"),
 ("mcp-Google_Drive-read_file_content-1793369576938.txt","118vCohR72aRRw30UP17cWMds08yCMHGr","AF","sprint","1. Africa","","008_Relatório.pdf"),
 ("mcp-Google_Drive-read_file_content-1793369578345.txt","1UGxtodBp0cUcAojZr5EVGiq28BAv1rEl","LA","sprint","3. Latin America - Caribbean","","011_Relatório.pdf"),
 ("mcp-Google_Drive-read_file_content-1793369579161.txt","1gLVHZx3YqRjClAYBbA4NWBr-YqaeSGWY","ME","database","5. Middle East","Database (non-sprint)","D039_Make-An-Impact-On-The-Future-AI-Strategy-Of-The-Israeli-Hi.pdf"),
 ("mcp-Google_Drive-read_file_content-1793369579484.txt","1SGZZ2D5FhcUACt74-GOOBDJaDBT7qqwT","AF","database","1. Africa","Database (non-sprint)","D062_Kenya-AI-Strategy-2025-2030.pdf"),
 ("mcp-Google_Drive-read_file_content-1793369580284.txt","1u2gUGUAqrREfEF9ZRYJysKpRrACCRDWB","AF","database","1. Africa","Database (non-sprint)","D007_Egypt.pdf"),
 ("mcp-Google_Drive-read_file_content-1793369581334.txt","1cGX_qPLOzB3D75WbzBqKA5ow-d9TN8N8","AF","database","1. Africa","Database (non-sprint)","D032_Second-Edition-Published-By-MCIT-January-2025.pdf"),
 ("mcp-Google_Drive-read_file_content-1793369583175.txt","1Z_RMyH7nHS9eqoiKkJFGX4fHqcvEvqtj","AF","database","1. Africa","Database (non-sprint)","D040_AI-READINESS-ASSESSMENT-KENYA-2REDO-OK_Codee-Pdf.pdf"),
 ("mcp-Google_Drive-read_file_content-1793369584319.txt","1I9LiRpPCsgcT7BnPSBhsE2X3a7Q4ZufY","AF","database","1. Africa","Database (non-sprint)","D070_Smart-Africa-And-Wadhwani-AI-Global-Partner-To-Advance-Res.html"),
 ("mcp-Google_Drive-read_file_content-1793369585329.txt","1WLB5EwqLo3GzfyqapZdQYwfrH1aG21oR","AF","database","1. Africa","Database (non-sprint)","D078_Smart-Africa-Convened-Technical-Experts-To-Discuss-The.html"),
 ("mcp-Google_Drive-read_file_content-1793369585885.txt","1l0pXyHTJIzT6SKWYCgrrnFIZVCog0jo0","AF","database","1. Africa","Database (non-sprint)","D069_Artificial-Intelligence-For-Africa-Smart-Africa.html"),
 ("mcp-Google_Drive-read_file_content-1793369586751.txt","1MJcWIn0mzQKqHBvW0X2Rmgl_1163a0Ob","AF","database","1. Africa","Database (non-sprint)","D079_Artificial-Intelligence-Smart-Africa.html"),
 ("mcp-Google_Drive-read_file_content-1793369587593.txt","1BgAAdlajyMXBKAKUPiQax7H_OV541or6","AF","database","1. Africa","Database (non-sprint)","D071_Smart-Africa-Steering-Committee-Convenes-In-Kigali-And-End.html"),
 ("mcp-Google_Drive-read_file_content-1793369588998.txt","1OqmP8Ipd4hojdkhMMteS2BpPIsWPKdUF","US","sprint","2a. North America - USA","","005_Blueprint-For-An-AI-Bill-Of-Rights-OSTP-The-White-House.pdf"),
 ("mcp-Google_Drive-read_file_content-1793369589604.txt","1rmLt_iXdmRW4giw2DBtexgB5AC0Nqg5z","US","sprint","2a. North America - USA","","095_Spoken-Language-Interaction-With-Virtual-Agents-And-Robots.pdf"),
 ("mcp-Google_Drive-read_file_content-1793369590745.txt","1Z2VZ08YKCugWJxiiAQ1Kx3t_F9J8PgKC","AS","sprint","4. Asia","","186_Spoken-Language-Interaction-With-Virtual-Agents-And-Robots.pdf"),
]
for jf,did,cc in [("mcp-Google_Drive-read_file_content-1793373363584.txt","1hzM7TPuXf-1nyxytR6pVrQl-WbcU3LL2","C10144"),
                  ("mcp-Google_Drive-read_file_content-1793373364436.txt","1kyfE0vfD2R1WFjkEkRmo-rk3ECYPsV88","C08364"),
                  ("mcp-Google_Drive-read_file_content-1793373365098.txt","1nCdCo2n-17qZPAomqv8hnpugU1JKPmuF","C08363"),
                  ("mcp-Google_Drive-read_file_content-1793373366075.txt","1lEnflbeJ-6HRkyccw64JWbImc49E5zzo","C08362"),
                  ("toolu_01WqTGwdV3rDFvEvPe3s5od4.txt","1GcUXnaR3gVuO7BQQyuZEXFJxiszd2eXs","C06938"),
                  ("mcp-Google_Drive-read_file_content-1793373367967.txt","1lQVuECIpZFJfiuLS8y0etHdKgbHxB4k0","C07550"),
                  ("mcp-Google_Drive-read_file_content-1793373369084.txt","1ikBdegD-E4gzeUIjhR5kDH4JM-dNClcl","C11484"),
                  ("mcp-Google_Drive-read_file_content-1793373369725.txt","124AYIsQSJ7e_XwW4XJjWTTA3csXUd9cp","C02843")]:
    s,folder,fn=eu2(cc); R.append((jf,did,"EU2",s,folder,"",fn))
def load_json(p):
    raw=open(p,encoding="utf8",errors="replace").read()
    i=raw.find("{\"fileContent\""); raw=raw[i:] if i>=0 else raw
    try: return json.loads(raw)
    except Exception:
        # persisted-output wrapper may append text after the JSON; cut at last closing brace
        j=raw.rfind("}"); return json.loads(raw[:j+1])
def html_to_md(html):
    html=re.sub(r"\\([<>!&#_*\[\]()\-])",r"\1",html)  # undo markdown escaping of raw html
    html=re.sub(r"(?is)<(script|style|noscript|nav|template)\b.*?</\1\s*>"," ",html)
    r=subprocess.run(["pandoc","-f","html","-t","gfm-raw_html","--wrap=none"],input=html.encode("utf8"),capture_output=True,timeout=300)
    return r.stdout.decode("utf8","replace")
rows=[]
for jf,did,rc,setname,folder,sub,fn in R:
    j=load_json(TR+jf); txt=j.get("fileContent","") or ""
    if not txt.strip(): status="stub"; md=f"# {fn}\n\nContent could not be extracted as text from the original file.\n\nReason: Drive reader returned no text (scanned PDF).\n"
    else:
        if re.search(r"(?i)<\\?!?DOCTYPE html|<html",txt[:300]): md=html_to_md(txt)
        else: md=txt
        status="reader"
    rel=os.path.join(folder,sub,fn) if sub else os.path.join(folder,fn)
    outp=os.path.join(OUTMD,os.path.splitext(rel)[0]+".md"); os.makedirs(os.path.dirname(outp),exist_ok=True)
    open(outp,"w",encoding="utf8").write(md)
    rows.append(dict(file_rel=rel,region_code=rc,set=setname,number=(re.match(r"^(D?\d{3})_",fn).group(1) if re.match(r"^(D?\d{3})_",fn) else ""),
        ccode=(re.search(r"\[(C\d+)\]",fn).group(1) if re.search(r"\[(C\d+)\]",fn) else ""),filename=fn,ext=os.path.splitext(fn)[1].lower(),
        bytes=0,md5="reader:"+did,drive_id=did,text_status=status,text_path=outp,text_chars=len(md),title_from_filename=re.sub(r"\s*\[C\d+\]$","",re.sub(r"^D?\d{3}_","",os.path.splitext(fn)[0]).replace("-"," "))))
df=pd.DataFrame(rows); df.to_csv(B+"data/recovered_docs.csv",index=False)
print(df[["region_code","set","filename","text_status","text_chars"]].to_string())
