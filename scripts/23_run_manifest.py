#!/usr/bin/env python3
"""v4: run manifest with tool versions, model identifiers, prompt hashes, policy tags, annotation counts and costs per annotation folder."""
import json, glob, subprocess, datetime, os, collections
B="/home/user/embodied-ai-governance-v5/"
man={"generated":datetime.datetime.now(datetime.timezone.utc).isoformat(),"python":subprocess.run(["python3","--version"],capture_output=True,text=True).stdout.strip(),"claude_cli":subprocess.run(["claude","--version"],capture_output=True,text=True).stdout.strip() or "unknown","folders":{}}
for d in sorted(glob.glob(B+"annotations/*/")):
    files=glob.glob(d+"*.json"); 
    if not files: continue
    models=collections.Counter(); hashes=collections.Counter(); policies=collections.Counter(); cost=0.0
    for f in files:
        try: j=json.load(open(f))
        except Exception: continue
        models[j.get("model")]+=1; hashes[j.get("prompt_hash")]+=1; policies[str(j.get("policy"))]+=1; cost+=float((j.get("usage") or {}).get("cost_usd") or 0)
    man["folders"][os.path.basename(d.rstrip("/"))]={"n":len(files),"models":dict(models),"prompt_hashes":dict(hashes),"policies":dict(policies),"cost_usd":round(cost,2),"inputs_stored":os.path.isdir(d+"_inputs")}
json.dump(man,open(B+"data/run_manifest.json","w"),indent=1)
print(json.dumps({k:(v["n"],v["cost_usd"]) for k,v in man["folders"].items()}))
