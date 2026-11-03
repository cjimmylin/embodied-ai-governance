"""TED-style main-stage deck: 'Who governs the robots?'. Dark stage, one idea per slide, big type, v5 numbers.
Writes project/deck.json and project/slides/<id>.html (1920x1080, inline styles)."""
import json, os
ROOT = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(ROOT, "project"); S = os.path.join(P, "slides")
os.makedirs(S, exist_ok=True)
BG, IVORY, AMBER, DIM, LINE = "#0E0E10", "#F5F1E8", "#F2A93B", "#9A968C", "#2A2A2E"
SANS = "'Inter', Arial, sans-serif"; SERIF = "'DM Serif Display', Georgia, serif"
slides = []
def sec(id_, body, pad="120px 140px", gap=36, extra=";justify-content:center"):
    slides.append((id_, f'<section id="{id_}" data-transition="fade" style="background:{BG};color:{IVORY};font-family:{SANS};padding:{pad};display:flex;flex-direction:column;gap:{gap}px{extra}">\n{body}\n</section>'))
def kicker(t, color=AMBER): return f'<p style="font-size:26px;font-weight:600;letter-spacing:4px;text-transform:uppercase;color:{color}">{t}</p>'
def statement(t, size=108, width=1640, color=IVORY): return f'<h2 style="font-family:{SERIF};font-size:{size}px;font-weight:400;line-height:1.08;width:{width}px;color:{color}">{t}</h2>'
def sub(t, size=36, width=1500, color=DIM): return f'<p style="font-size:{size}px;line-height:1.4;color:{color};width:{width}px">{t}</p>'
def num(n, label, color=AMBER, nsize=300, width=520, lsize=32):
    return f'<div style="display:flex;flex-direction:column;gap:10px;width:{width}px"><p style="font-family:{SERIF};font-size:{nsize}px;line-height:0.95;color:{color}">{n}</p><p style="font-size:{lsize}px;line-height:1.3;color:{IVORY}">{label}</p></div>'
def foot(t): return f'<p style="position:absolute;left:140px;bottom:56px;font-size:22px;color:{DIM}">{t}</p>'

# 1 title
sec("title", f'''
{kicker("A talk about the machines that are about to move in")}
<h1 style="font-family:{SERIF};font-size:168px;font-weight:400;line-height:1.0;width:1500px">Who governs<br>the robots?</h1>
{sub("What we found when we read every rule on Earth for machines that think and move", 38, 1300)}
''', gap=44)

# 2 scene
sec("scene", f'''
{statement("Somewhere, right now, a robot is being built to live in your mother's room.", 112)}
{sub("Not a factory arm behind a fence. A machine that lifts, carries, reminds, watches, and talks back.", 36, 1500)}
''')

# 3 we went looking
sec("looking", f'''
{kicker("So we went looking for the rules")}
<div style="display:flex;gap:80px;margin-top:10px">
{num("3,320", "documents: laws, standards, strategies, studies, news", nsize=200, width=560, lsize=30)}
{num("119", "countries, plus the EU and the UN system", nsize=200, width=420, lsize=30)}
{num("0", "humans who read them all. An AI did, 39 questions per document, and other AIs checked its work.", nsize=200, width=620, lsize=30)}
</div>
''', gap=40)

# 4 278
sec("n278", f'''
<p style="font-family:{SERIF};font-size:460px;line-height:0.9;color:{AMBER}">278</p>
{statement("binding rules on Earth that reach a robot.", 84, 1500)}
{sub("Laws with teeth: break them and something happens to you. Each counted once, paperwork excluded.", 32, 1400)}
''', gap=30)

# 5 25
sec("n25", f'''
<p style="font-family:{SERIF};font-size:460px;line-height:0.9;color:{AMBER}">25</p>
{statement("of them mention artificial intelligence.", 84, 1500)}
{sub("The other 253 were written for aircraft, vehicles, machinery, products and medical devices. Robots are governed sideways.", 32, 1500)}
''', gap=30)

# 6 sideways list
sec("sideways", f'''
{kicker("Governed sideways")}
<div style="display:flex;flex-direction:column;gap:34px;margin-top:6px">
<div style="display:flex;align-items:baseline;gap:40px"><p style="font-family:{SERIF};font-size:150px;line-height:1;color:{AMBER};width:300px;text-align:right">146</p><p style="font-family:{SERIF};font-size:64px;line-height:1.1">rules for drones. <span style="color:{DIM}">A drone is an aircraft.</span></p></div>
<div style="display:flex;align-items:baseline;gap:40px"><p style="font-family:{SERIF};font-size:150px;line-height:1;color:{AMBER};width:300px;text-align:right">109</p><p style="font-family:{SERIF};font-size:64px;line-height:1.1">rules for self-driving cars. <span style="color:{DIM}">A car is a vehicle.</span></p></div>
<div style="display:flex;align-items:baseline;gap:40px"><p style="font-family:{SERIF};font-size:150px;line-height:1;color:{AMBER};width:300px;text-align:right">13</p><p style="font-family:{SERIF};font-size:64px;line-height:1.1">rules for factory robot arms. <span style="color:{DIM}">An arm is a machine.</span></p></div>
</div>
''', gap=30)

# 7 lived with
sec("zeros", f'''
{kicker("And the robots we will live with?")}
<div style="display:flex;gap:90px;margin-top:10px;align-items:flex-end">
{num("0", "binding rules for companion robots", nsize=320, width=480, lsize=34)}
{num("0", "for humanoids", nsize=320, width=420, lsize=34)}
{num("4", "for care robots, all of them laws about something else that mention care robots in passing", nsize=320, width=620, lsize=34)}
</div>
{foot("Among 429 documents about companion, care and humanoid robots. The one text written for care robots is a voluntary standard from 2014.")}
''', gap=24)

# 8 gap
sec("gap", f'''
{kicker("Companion robots")}
<div style="display:flex;gap:120px;align-items:flex-end;margin-top:10px">
<div style="display:flex;flex-direction:column;gap:16px"><p style="font-family:{SERIF};font-size:300px;line-height:0.95;color:{IVORY}">43%</p><p style="font-size:36px;line-height:1.3;color:{IVORY};width:600px">of the research papers are about them</p></div>
<div style="display:flex;flex-direction:column;gap:16px"><p style="font-family:{SERIF};font-size:300px;line-height:0.95;color:{AMBER}">3%</p><p style="font-size:36px;line-height:1.3;color:{IVORY};width:600px">of the rules are</p></div>
</div>
{sub("Scientists study the robots we will live with. Lawmakers regulate the ones already in the street.", 36, 1500)}
''', gap=36)

# 9 after the accident
sec("after", f'''
{statement("Rules follow machines into public space. Usually after the first accident.", 100)}
<div style="display:flex;gap:70px;margin-top:10px">
<div style="width:500px;border-top:4px solid {AMBER};padding-top:20px"><p style="font-family:{SERIF};font-size:44px;line-height:1.15">Drones</p><p style="font-size:30px;line-height:1.35;color:{DIM}">Rules mostly 2016 to 2021, after the near-misses at airports</p></div>
<div style="width:500px;border-top:4px solid {AMBER};padding-top:20px"><p style="font-family:{SERIF};font-size:44px;line-height:1.15">Self-driving cars</p><p style="font-size:30px;line-height:1.35;color:{DIM}">Rules from 2017, after the test fleets, and the first deaths</p></div>
<div style="width:500px;border-top:4px solid {AMBER};padding-top:20px"><p style="font-family:{SERIF};font-size:44px;line-height:1.15">Sidewalk robots</p><p style="font-size:30px;line-height:1.35;color:{DIM}">State laws 2018 to 2022, after the robots were already on the pavement</p></div>
</div>
{foot("Three quarters of the 278 rules date from 2019 or later; 105 of them from 2024 to 2026.")}
''', gap=40)

# 10 the body changes the question
sec("body", f'''
{kicker("When the intelligence has a body, the questions change")}
<div style="display:flex;flex-wrap:wrap;gap:40px;margin-top:6px;width:1640px">
<div style="width:800px;border-left:6px solid {AMBER};padding-left:32px"><p style="font-family:{SERIF};font-size:60px;line-height:1.1">Can it hurt you?</p></div>
<div style="width:800px;border-left:6px solid {AMBER};padding-left:32px"><p style="font-family:{SERIF};font-size:60px;line-height:1.1">How close may it come?</p></div>
<div style="width:800px;border-left:6px solid {AMBER};padding-left:32px"><p style="font-family:{SERIF};font-size:60px;line-height:1.1">Who pays when it breaks something?</p></div>
<div style="width:800px;border-left:6px solid {AMBER};padding-left:32px"><p style="font-family:{SERIF};font-size:60px;line-height:1.1">How much may it decide alone?</p></div>
</div>
{sub("Physical safety is spelled out in 167 of the 278 rules. Fairness in 3. Human dignity in 1. The rulebook for a body is about the body.", 34, 1600)}
''', gap=40)

# 11 mention is not detail
sec("mention", f'''
{kicker("The hardest question: how much may it decide alone?")}
<div style="display:flex;gap:120px;align-items:flex-end;margin-top:10px">
<div style="display:flex;flex-direction:column;gap:16px"><p style="font-family:{SERIF};font-size:300px;line-height:0.95;color:{IVORY}">171</p><p style="font-size:36px;line-height:1.3;width:560px">rules raise it</p></div>
<div style="display:flex;flex-direction:column;gap:16px"><p style="font-family:{SERIF};font-size:300px;line-height:0.95;color:{AMBER}">73</p><p style="font-size:36px;line-height:1.3;width:560px">rules answer it: what is allowed, by whom, checked how</p></div>
</div>
{statement("Mention is not detail.", 84, 1500, AMBER)}
''', gap=36)

# 12 who has to obey
sec("obey", f'''
{kicker("Who has to obey these rules?")}
<div style="display:flex;flex-direction:column;gap:22px;margin-top:6px">
<div style="display:flex;align-items:center;gap:30px"><p style="font-family:{SERIF};font-size:96px;line-height:1;color:{IVORY};width:260px;text-align:right">62%</p><div style="width:{int(1100*0.62)}px;height:44px;background:{IVORY};border-radius:4px"></div><p style="font-size:34px">the companies that operate the machine</p></div>
<div style="display:flex;align-items:center;gap:30px"><p style="font-family:{SERIF};font-size:96px;line-height:1;color:{IVORY};width:260px;text-align:right">39%</p><div style="width:{int(1100*0.39)}px;height:44px;background:{IVORY};border-radius:4px"></div><p style="font-size:34px">the companies that build it</p></div>
<div style="display:flex;align-items:center;gap:30px"><p style="font-family:{SERIF};font-size:96px;line-height:1;color:{AMBER};width:260px;text-align:right">18%</p><div style="width:{int(1100*0.18)}px;height:44px;background:{AMBER};border-radius:4px"></div><p style="font-size:34px">you</p></div>
<div style="display:flex;align-items:center;gap:30px"><p style="font-family:{SERIF};font-size:96px;line-height:1;color:{AMBER};width:260px;text-align:right">8%</p><div style="width:{int(1100*0.08)}px;height:44px;background:{AMBER};border-radius:4px"></div><p style="font-size:34px">the people who wrote the software that decides</p></div>
</div>
{foot("Share of the 278 binding rules that name each party in their own text; a rule can name several.")}
''', gap=30)

# 13 AI read the law
sec("airead", f'''
{statement("We used AI to read the laws about AI. Here is how much to trust that.", 96)}
<div style="display:flex;gap:100px;margin-top:10px;align-items:flex-end">
{num("73%", "of a random hundred rules survived an independent re-read on three strict tests. Up from 54% a year ago. Not 100.", nsize=220, width=700, lsize=30)}
{num("0", "documents labelled by a human so far. A map drawn by machines, waiting for a person to walk it.", nsize=220, width=700, lsize=30, color=IVORY)}
</div>
''', gap=40)

# 14 three things
sec("three", f'''
{kicker("Three things, before the robots arrive")}
<div style="display:flex;flex-direction:column;gap:30px;margin-top:6px;width:1640px">
<div style="display:flex;gap:36px;align-items:flex-start"><p style="font-family:{SERIF};font-size:96px;line-height:0.9;color:{AMBER};width:90px">1</p><div><p style="font-family:{SERIF};font-size:54px;line-height:1.1">Write the rules first this time.</p><p style="font-size:30px;line-height:1.35;color:{DIM};width:1400px">Companions, carers, humanoids: zero, four, zero. We can see them coming. Drones did not get that courtesy.</p></div></div>
<div style="display:flex;gap:36px;align-items:flex-start"><p style="font-family:{SERIF};font-size:96px;line-height:0.9;color:{AMBER};width:90px">2</p><div><p style="font-family:{SERIF};font-size:54px;line-height:1.1">Answer the control question. Do not just raise it.</p><p style="font-size:30px;line-height:1.35;color:{DIM};width:1400px">Who may let the machine decide what, under which conditions, checked by whom. Aviation did it. Everyone else can.</p></div></div>
<div style="display:flex;gap:36px;align-items:flex-start"><p style="font-family:{SERIF};font-size:96px;line-height:0.9;color:{AMBER};width:90px">3</p><div><p style="font-family:{SERIF};font-size:54px;line-height:1.1">Make the safety knowledge public.</p><p style="font-size:30px;line-height:1.35;color:{DIM};width:1400px">The documents that say how close, how fast, how much force are standards, and 57 of our 61 are behind a paywall. Rules you cannot read are rules you cannot follow.</p></div></div>
</div>
''', gap=30)

# 15 close
sec("close", f'''
{statement("The question is not whether robots will come into our homes.", 96)}
{statement("It is whether the rules will be there when they do.", 96, 1640, AMBER)}
{foot("Data, code and every number: github.com/cjimmylin/embodied-ai-governance · Explore the 3,320 documents: claude.ai/artifact/YKsXJRaT7tSfRXseuo5kuZ")}
''', gap=44)

order = [s[0] for s in slides]
for id_, html in slides:
    open(os.path.join(S, id_ + ".html"), "w", encoding="utf8").write(html)
deck = {"v": 4, "createdOnFiles": {"v": 1, "at": "2026-11-03T08:30:00Z"}, "lists": "css", "title": "Who Governs the Robots: Main Stage", "cover": "title", "order": order,
        "sections": {"opening": {"description": "The scene and the search.", "start": "title"},
                     "findings": {"description": "Governed sideways, the robots with no rules, rules after accidents, the body's questions, mention versus detail, who obeys.", "start": "n278"},
                     "closing": {"description": "Trust, three asks and the close.", "start": "airead"}},
        "faces": {"dm-serif-display": {"family": "DM Serif Display", "href": "https://fonts.googleapis.com/css2?family=DM+Serif+Display&display=swap"},
                  "inter": {"family": "Inter", "href": "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap"}},
        "designSystems": []}
json.dump(deck, open(os.path.join(P, "deck.json"), "w"), indent=1)
print("ted slides:", len(order))
