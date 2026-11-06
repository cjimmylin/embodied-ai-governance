"""Build docs/volunteers/index.html: the public, read-only copy of the volunteer sign-up sheet, from volunteers/tasks.json.
Sign-ups and progress live on the claude.ai sheet; each card links to its task there."""
import json, html, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHEET = "https://claude.ai/artifact/21o6idnP14fyQPwA7LsZ6i"
GSHEET = "https://docs.google.com/spreadsheets/d/1Y9S4a2xEwLg0HGKLu6-zRJyXm5DbrvyegGnK09Tg4AA/edit"
d = json.load(open(os.path.join(ROOT, "volunteers/tasks.json"), encoding="utf8")); B, T = d["base"], d["tree"]
e = html.escape
def url(f): return f if f.startswith("http") else ((T if "." not in f.split("/")[-1] else B) + f)
cards = []
for t in d["tasks"]:
    total = f"{t['unitsTotal']} " if t["unitsTotal"] else ""
    steps = "".join(f"<li>{e(s)}</li>" for s in t["steps"])
    files = "".join(f'<a href="{e(url(b))}">{e(a)}</a>' for a, b in t["files"])
    caut = f'<p class="small"><b>Note:</b> {e(t["caution"])}</p>' if t["caution"] else ""
    cards.append(f'''<article class="task" id="{e(t['id'])}" data-area="{e(t['area'])}">
<span class="area">{e(t['area'])}</span>
<h3><span class="n">{t['n']}.</span>{e(t['title'])}</h3>
<p class="why">{e(t['why'])}</p>
<div class="facts"><span><b>Skill:</b> {e(t['skill'])}</span><span><b>Effort:</b> {e(t['effort'])}</span><span><b>People needed:</b> {t['people']}</span><span><b>Progress counted in:</b> {e(total + t['unitLabel'])}</span></div>
<div class="signup"><a class="primary" href="{SHEET}#{e(t['id'])}">Sign up or update this task on the live sheet</a></div>
<details><summary>What to do, files and what to hand back</summary><ol>{steps}</ol><div class="files">{files}</div><p class="small"><b>Hand back:</b> {e(t['output'])}</p>{caut}</details>
</article>''')
toc = "".join(f'<li><a href="#{e(t["id"])}">{t["n"]}. {e(t["title"])}</a> <span class="mute">· {t["people"]} {"person" if t["people"]==1 else "people"} · {e(t["area"].lower())}</span></li>' for t in d["tasks"])
page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Volunteer Sign-up</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>
:root{{--bg:#F4F1EA;--bg2:#EAE5DA;--card:#FFFDF8;--fg:#123D33;--body:#4A5550;--mute:#6F7A75;--line:#D9D3C6;--acc:#A24A24;--accsoft:#F3E3D8;color-scheme:light}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#0F2823;--bg2:#153630;--card:#183F38;--fg:#F4F1EA;--body:#C9D9D3;--mute:#8FA8A0;--line:#2A5048;--acc:#E7B98F;--accsoft:#2E4A42;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#0F2823;--bg2:#153630;--card:#183F38;--fg:#F4F1EA;--body:#C9D9D3;--mute:#8FA8A0;--line:#2A5048;--acc:#E7B98F;--accsoft:#2E4A42;color-scheme:dark}}
*{{box-sizing:border-box}} [hidden]{{display:none!important}}
body{{margin:0;background:var(--bg);color:var(--fg);font-family:'IBM Plex Sans',Arial,sans-serif;font-size:15px;line-height:1.5}}
.wrap{{max-width:1080px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:28px 72px}}
a{{color:var(--acc)}}
.top{{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:.9rem;margin-bottom:14px}}
.eyebrow{{font-size:.78rem;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--acc);margin:0 0 6px}}
h1{{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:clamp(1.9rem,5vw,3rem);line-height:1.05;margin:0 0 10px;text-wrap:balance}}
h2{{font-family:'Fraunces',Georgia,serif;font-weight:500;font-size:1.45rem;margin:32px 0 10px}}
.lede{{color:var(--body);max-width:72ch;margin:0 0 8px}}
.cta{{display:flex;flex-wrap:wrap;gap:10px;margin:16px 0}}
.cta a,.signup a{{display:inline-block;border-radius:999px;padding:9px 16px;font-weight:600;text-decoration:none;border:1px solid var(--line);background:var(--card);color:var(--fg)}}
.cta a.primary,.signup a.primary{{background:var(--fg);color:var(--bg);border-color:var(--fg)}}
.note{{background:var(--accsoft);border-radius:10px;padding:12px 16px;font-size:.93rem;max-width:90ch;margin:12px 0}}
.how{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px;margin:14px 0}}
.how div{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 12px;font-size:.9rem;color:var(--body)}}
.how b{{color:var(--fg);display:block;margin-bottom:2px}}
.toc{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 14px 10px 34px;margin:0}}
.toc li{{margin:3px 0}} .mute{{color:var(--mute);font-size:.86rem}}
.task{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin-bottom:14px;display:flex;flex-direction:column;gap:10px;min-width:0;scroll-margin-top:12px}}
.task h3{{font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:1.2rem;margin:0;line-height:1.25;text-wrap:balance}}
.task h3 .n{{color:var(--acc);margin-right:6px}}
.area{{font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--mute);font-weight:600}}
.why{{margin:0;color:var(--body);max-width:80ch}}
.facts{{display:flex;flex-wrap:wrap;gap:4px 18px;font-size:.88rem;color:var(--body)}} .facts b{{color:var(--fg);font-weight:600}}
details{{border-top:1px solid var(--line);padding-top:8px}} summary{{cursor:pointer;font-weight:600;font-size:.92rem}}
details ol{{margin:8px 0;padding-left:20px;color:var(--body)}} details ol li{{margin:4px 0}}
.files{{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0}}
.files a{{background:var(--bg2);color:var(--fg);text-decoration:none;border-radius:999px;padding:3px 11px;font-size:.84rem}}
.small{{font-size:.88rem;color:var(--body);margin:6px 0}}
a:focus-visible,summary:focus-visible{{outline:2px solid var(--acc);outline-offset:2px}}
footer{{margin-top:40px;color:var(--mute);font-size:.84rem;max-width:90ch}}
</style></head><body>
<div class="wrap">
<div class="top"><a href="../index.html">← Project hub</a><a href="{B}volunteers/README.md">Task briefs as a document</a><a href="{T}volunteers/templates">Templates</a></div>
<p class="eyebrow">Who governs the robots? · volunteer team</p>
<h1>Volunteer sign-up</h1>
<p class="lede">Ten pieces of work that a person can do and the study's AI agents could not, ordered by how much they change the results. Read the tasks here; sign up, tag teammates by email and record progress on the live sheet.</p>
<div class="cta"><a class="primary" href="{SHEET}">Open the live sign-up sheet</a><a href="{GSHEET}">Same tracker as a Google Sheet</a><a href="{B}HUMAN_ASSISTANCE.md">What needs a person (full list)</a></div>
<div class="note"><b>Why two pages:</b> this site is a public, read-only copy and cannot save anything. Sign-ups, email tags, counters, statuses and updates are kept on the live sheet on claude.ai, which opens for people the coordinator has shared it with. If the live sheet does not open for you, ask the coordinator for access, or reply with the task number you want and the coordinator will tag you.</div>
<div class="how">
<div><b>1. Choose a task</b>Read the cards below; each says the skill, effort and how many people it needs.</div>
<div><b>2. Sign up</b>Press the task's sign-up button. On the live sheet, save your email at the top, then press Tag me on that task, or type teammates' emails and press Tag.</div>
<div><b>3. Do the work</b>Open "What to do" for the steps, the exact files and what to hand back. Fill the task's template.</div>
<div><b>4. Report progress</b>On the live sheet, raise the task's counter, set its status and post a one-line update when you stop.</div>
</div>
<h2>The ten tasks</h2>
<ol class="toc">{toc}</ol>
<h2>Task details</h2>
{"".join(cards)}
<footer>General rules for every task: work from official sources; never work around a login, payment or bot check; never commit source texts or standards to the public repository. This page is generated from <a href="{B}volunteers/tasks.json">volunteers/tasks.json</a>, the same data the live sheet was seeded from.</footer>
</div>
</body></html>'''
os.makedirs(os.path.join(ROOT, "docs/volunteers"), exist_ok=True)
open(os.path.join(ROOT, "docs/volunteers/index.html"), "w", encoding="utf8").write(page)
print("docs/volunteers/index.html", len(page) // 1000, "KB")
