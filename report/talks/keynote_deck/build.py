"""Keynote deck: 'Who governs the robots?' for an AI research / AI governance conference. Non-technical, headline-first.
Writes project/deck.json and project/slides/<id>.html (1920x1080, inline styles)."""
import json, os
ROOT = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(ROOT, "project"); S = os.path.join(P, "slides")
os.makedirs(S, exist_ok=True)
# palette: warm paper, deep green ink, copper accent, slate text
PAPER, INK, COPPER, SLATE, MIST, WHITE, SEA = "#F4F1EA", "#123D33", "#B5552D", "#4A5550", "#E4DED2", "#FFFFFF", "#1F6F8B"
SANS = "'IBM Plex Sans', Arial, sans-serif"; SERIF = "'Fraunces', Georgia, serif"
slides = []
def sec(id_, body, bg=PAPER, fg=INK, pad="112px 128px 140px", gap=28, extra=""):
    slides.append((id_, f'<section id="{id_}" data-transition="fade" style="background:{bg};color:{fg};font-family:{SANS};padding:{pad};display:flex;flex-direction:column;gap:{gap}px{extra}">\n{body}\n</section>'))
def eyebrow(t, color=COPPER): return f'<p style="font-size:24px;font-weight:600;letter-spacing:3px;text-transform:uppercase;color:{color}">{t}</p>'
def h2(t, color=None, size=64): return f'<h2 style="font-family:{SERIF};font-size:{size}px;font-weight:500;line-height:1.1;width:1600px{";color:"+color if color else ""}">{t}</h2>'
def lead(t, color=SLATE, size=30, width=1500): return f'<p style="font-size:{size}px;line-height:1.4;color:{color};width:{width}px">{t}</p>'
def foot(t, color="#6B7280"): return f'<p style="position:absolute;left:128px;bottom:60px;font-size:22px;color:{color}">{t}</p>'
def bignum(n, label, color=COPPER, nsize=150, width=520, lcolor=SLATE):
    return f'<div style="display:flex;flex-direction:column;gap:6px;width:{width}px"><p style="font-family:{SERIF};font-size:{nsize}px;font-weight:500;line-height:1;color:{color}">{n}</p><p style="font-size:28px;line-height:1.3;color:{lcolor}">{label}</p></div>'
def bar(label, pct, value, color=COPPER, track=MIST, maxw=1100, fg=INK, lw=460):
    w = int(maxw * pct / 100)
    return (f'<div style="display:flex;align-items:center;gap:24px"><p style="font-size:28px;width:{lw}px;color:{fg}">{label}</p>'
            f'<div style="width:{maxw}px;height:38px;background:{track};border-radius:4px;position:relative"><div style="width:{w}px;height:38px;background:{color};border-radius:4px"></div></div>'
            f'<p style="font-size:28px;width:150px;color:{fg};font-weight:600">{value}</p></div>')
def dual(label, a, b, maxw=560, ca=SEA, cb=COPPER, fg=INK):
    wa, wb = int(maxw * a / 100), int(maxw * b / 100)
    return (f'<div style="display:flex;align-items:center;gap:20px"><p style="font-size:28px;width:420px;color:{fg}">{label}</p>'
            f'<div style="width:{maxw}px;display:flex;justify-content:flex-end"><div style="width:{wa}px;height:34px;background:{ca};border-radius:4px 0 0 4px"></div></div><p style="font-size:26px;width:80px;text-align:right;color:{ca};font-weight:600">{a}%</p>'
            f'<p style="font-size:26px;width:80px;color:{cb};font-weight:600">{b}%</p><div style="width:{maxw}px"><div style="width:{wb}px;height:34px;background:{cb};border-radius:0 4px 4px 0"></div></div></div>')

# 1 cover
sec("cover", f'''
{eyebrow("Keynote · AI research and AI governance", "#E7B98F")}
<div style="display:flex;flex-direction:column;gap:30px;width:1500px">
<h1 style="font-family:{SERIF};font-size:140px;font-weight:500;line-height:1.02">Who governs<br>the robots?</h1>
<p style="font-size:38px;line-height:1.35;color:#CFE3DC;width:1350px">What 3,320 documents from 119 countries say about the rules for machines that act in the physical world, and the gap those rules leave open</p>
</div>
<div style="display:flex;justify-content:space-between;align-items:flex-end">
<p style="font-size:24px;color:#CFE3DC;line-height:1.5">Centre for Enterprise Innovation (CEI), AI Robotics project<br>Study version 5, November 2026</p>
<p style="font-size:24px;color:#CFE3DC">A talk for people who are new to robots, to AI and to law</p>
</div>''', bg=INK, fg=WHITE, pad="128px", gap=56, extra=";justify-content:space-between")

# 2 the question
sec("question", f'''
{eyebrow("The question")}
{h2("Software AI makes decisions. Embodied AI makes decisions and then moves.")}
{lead("A chatbot that goes wrong produces a bad sentence. A robot, a drone or a self-driving car that goes wrong produces a bad event: a collision, a crushed hand, a fall. The questions change the moment the AI has a body.")}
<div style="display:flex;gap:40px;margin-top:12px">
<div style="flex:1;background:{WHITE};border-left:10px solid {COPPER};padding:30px 34px"><p style="font-family:{SERIF};font-size:40px;line-height:1.2">Can it hurt someone?</p></div>
<div style="flex:1;background:{WHITE};border-left:10px solid {COPPER};padding:30px 34px"><p style="font-family:{SERIF};font-size:40px;line-height:1.2">How close may it work to people?</p></div>
<div style="flex:1;background:{WHITE};border-left:10px solid {COPPER};padding:30px 34px"><p style="font-family:{SERIF};font-size:40px;line-height:1.2">Who pays when it breaks something?</p></div>
<div style="flex:1;background:{WHITE};border-left:10px solid {COPPER};padding:30px 34px"><p style="font-family:{SERIF};font-size:40px;line-height:1.2">How much may it decide alone?</p></div>
</div>
{lead("So we asked a plain question: anywhere in the world, what rules exist for AI with a body, and what do they actually say?")}
''')

# 3 what we did
sec("method", f'''
{eyebrow("What we did")}
{h2("We built a map of the world's robot rules, and let AI read it")}
<div style="display:flex;gap:56px;margin-top:8px">
{bignum("3,320", "documents: laws, standards, strategies, research papers and news", width=420)}
{bignum("119", "countries, the EU and the international bodies", width=380)}
{bignum("3", "collection rounds: regional teams, then AI agents searching legal databases, then recovering what was blocked", width=520)}
{bignum("39", "questions put to every document by an AI reader, the same for all", width=380)}
</div>
{lead("Two things to hold in mind. The collection is a map, not a census: it is a lower bound on what exists. And no person read every document; the labels were produced by AI, checked by a second AI, and audited by an independent AI reader. Treat them as consistent, not certified.", size=28, width=1600)}
{foot("Study version 5, November 2026. Methods, data and every table: github.com/cjimmylin/embodied-ai-governance")}
''')

# 4 headline 1 - sideways
sec("sideways", f'''
{eyebrow("Headline one")}
{h2("Robots are governed sideways")}
<div style="display:flex;gap:64px;align-items:flex-start;margin-top:8px">
{bignum("278", "binding rules in the world that reach robots: statutes, regulations and decrees with legal force, counted once each", width=560)}
{bignum("25", "of them name artificial intelligence at all", width=440)}
{bignum("201", "contain any provision on autonomy or automation", width=460)}
</div>
{lead("The rest are aviation law, road-traffic law, machinery law, product-safety law and medical-device law. They reach robots because a drone is an aircraft, a self-driving car is a vehicle and a robot arm is a machine. Almost none of them were written with 'AI' in mind.", width=1600)}
{foot("Principal binding embodied instruments, v5. Full count depends on the counting unit: see the study's Table 53b.")}
''')

# 5 what the rules are about
rows = [("Drones", 146), ("Self-driving road vehicles", 109), ("Sidewalk delivery robots", 29), ("Security and policing robots", 14), ("Factory robot arms", 13), ("Warehouse and logistics robots", 12), ("Farm robots", 9), ("Care and assistive robots", 4), ("Companion robots", 0), ("Humanoids", 0)]
sec("whatrules", f'''
{eyebrow("Headline one, continued")}
{h2("The law reaches the machines that move through public space")}
{lead("Number of binding rules that address each kind of robot (a rule can address several). Drones and vehicles dominate; the robots meant for homes and care facilities sit at the bottom.", size=26)}
<div style="display:flex;flex-direction:column;gap:12px;margin-top:4px">
{"".join(bar(l, 100*v/146, str(v), color=(COPPER if v<=4 else INK)).replace("height:38px","height:30px") for l, v in rows)}
</div>
{foot("Binding principal instruments by robot type, v5 master table.")}
''', pad="96px 128px 120px", gap=14)

# 6 headline 2 - lived-with robots
sec("livedwith", f'''
{eyebrow("Headline two", "#E7B98F")}
{h2("The robots we will live with have almost no rules", color=WHITE)}
<div style="display:flex;gap:64px;margin-top:16px">
{bignum("0", "binding rules for companion and social robots", color="#E7B98F", width=460, lcolor="#CFE3DC")}
{bignum("0", "binding rules for humanoids", color="#E7B98F", width=420, lcolor="#CFE3DC")}
{bignum("4", "binding rules for care and assistive robots", color="#E7B98F", width=460, lcolor="#CFE3DC")}
</div>
<p style="font-size:30px;line-height:1.4;color:#CFE3DC;width:1600px">Across the collection, 429 documents discuss these three kinds of robot. Four of them are binding rules, and those four are general laws that mention care robots in passing: a Salvadoran robotics law, a Korean robot-industry act, two Japanese special-zone ordinances. The one text written specifically for care robots is a voluntary standard, ISO 13482, from 2014.</p>
{foot("Embodied set, v5: 429 documents mentioning companion, care or humanoid robots; 4 principal binding instruments among them.", "#9DB8B0")}
''', bg=INK, fg=WHITE)

# 7 the gap chart
gap = [("Companion and social robots", 43, 3), ("Care and assistive robots", 28, 9), ("Humanoids", 23, 4), ("Surgical robots", 15, 6), ("Factory robot arms", 10, 12), ("Self-driving road vehicles", 12, 41), ("Drones", 6, 43)]
sec("gap", f'''
{eyebrow("Headline two, continued")}
{h2("Research and rules point at different robots")}
{lead("Share of 509 research papers (left, blue) and of 598 governance instruments (right, copper) that address each kind of robot.", size=28)}
<div style="display:flex;flex-direction:column;gap:14px;margin-top:4px">
<div style="display:flex;align-items:center;gap:20px"><p style="width:420px"></p><p style="font-size:24px;width:560px;text-align:right;color:{SEA};font-weight:600;letter-spacing:2px;text-transform:uppercase">Research papers</p><p style="width:80px"></p><p style="width:80px"></p><p style="font-size:24px;width:560px;color:{COPPER};font-weight:600;letter-spacing:2px;text-transform:uppercase">Rules and policies</p></div>
{"".join(dual(l, a, b) for l, a, b in gap)}
</div>
{lead("Scientists study the robots people will live with. Lawmakers regulate the things that already move through streets and skies. The gap for companions, carers and humanoids holds whichever way the instruments were collected.", size=28, width=1600)}
{foot("Governance-gap index, v5 Table 7 and Table 7b (split by collection source).")}
''', pad="100px 128px 130px", gap=18)

# 8 headline 3 - the body changes the rulebook
sec("body", f'''
{eyebrow("Headline three")}
{h2("The body changes the rulebook")}
{lead("What the 278 binding rules talk about, and how often they spell it out in detail rather than name it. The top of the list is physical; the values that dominate AI ethics are at the bottom.", size=28)}
<div style="display:flex;gap:60px;margin-top:4px">
<div style="display:flex;flex-direction:column;gap:12px;width:780px">
<p style="font-size:24px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{INK}">Physical, in most rules</p>
{bar("Physical safety", 100*167/278, "167 in detail", maxw=380, lw=300)}
{bar("Testing and certification", 100*132/278, "132", maxw=380, lw=300)}
{bar("Who is accountable", 100*130/278, "130", maxw=380, lw=300)}
{bar("Human oversight", 100*83/278, "83", maxw=380, lw=300)}
{bar("Level of autonomy allowed", 100*73/278, "73", maxw=380, lw=300)}
{bar("Liability for damage", 100*63/278, "63", maxw=380, lw=300)}
</div>
<div style="display:flex;flex-direction:column;gap:12px;width:780px">
<p style="font-size:24px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{COPPER}">The AI-ethics vocabulary, rarely</p>
{bar("Privacy", 100*44/278, "44 in detail", maxw=380, lw=300, color=COPPER)}
{bar("Transparency", 100*8/278, "8", maxw=380, lw=300, color=COPPER)}
{bar("Fairness", 100*3/278, "3", maxw=380, lw=300, color=COPPER)}
{bar("Trust", 100*3/278, "3", maxw=380, lw=300, color=COPPER)}
{bar("Human dignity", 100*1/278, "1", maxw=380, lw=300, color=COPPER)}
{bar("Sustainability", 0, "0", maxw=380, lw=300, color=COPPER)}
</div>
</div>
{foot("Principles coded as absent, mentioned or spelled out in detail; counts are 'in detail' among 278 binding rules, v5.")}
''', pad="100px 128px 130px", gap=18)

# 9 headline 4 - mention is not detail
sec("mention", f'''
{eyebrow("Headline four")}
{h2("Mention is not detail")}
{lead("The control question, how much the machine may decide before a person must step in, is the question that makes a robot rule a robot rule. Here is how often the binding rules raise it, and how often they answer it.", size=28)}
<div style="display:flex;gap:56px;margin-top:8px">
<div style="flex:1;background:{WHITE};padding:36px 40px;display:flex;flex-direction:column;gap:14px"><p style="font-family:{SERIF};font-size:110px;line-height:1;color:{INK}">171</p><p style="font-size:28px;line-height:1.35;color:{SLATE}">rules <b>raise</b> the level of autonomy the machine may have</p></div>
<div style="flex:1;background:{WHITE};padding:36px 40px;display:flex;flex-direction:column;gap:14px"><p style="font-family:{SERIF};font-size:110px;line-height:1;color:{COPPER}">73</p><p style="font-size:28px;line-height:1.35;color:{SLATE}">rules <b>spell it out</b>: what is allowed, by whom, checked how</p></div>
<div style="flex:1;background:{WHITE};padding:36px 40px;display:flex;flex-direction:column;gap:14px"><p style="font-family:{SERIF};font-size:110px;line-height:1;color:{INK}">174</p><p style="font-size:28px;line-height:1.35;color:{SLATE}">rules <b>raise</b> human oversight</p></div>
<div style="flex:1;background:{WHITE};padding:36px 40px;display:flex;flex-direction:column;gap:14px"><p style="font-family:{SERIF};font-size:110px;line-height:1;color:{COPPER}">83</p><p style="font-size:28px;line-height:1.35;color:{SLATE}">rules <b>spell it out</b></p></div>
</div>
{lead("Six rules in ten raise the question; fewer than three in ten answer it. Most of the answers are in drone and vehicle law, where 'remote pilot' and 'fallback driver' already have legal meaning.", width=1600)}
{foot("Principle levels for autonomy_level_control and human_oversight among 278 binding rules, v5.")}
''')

# 10 headline 5 - who is bound
sec("bound", f'''
{eyebrow("Headline five")}
{h2("Whom the rules bind: the operator, not the maker, and rarely you")}
{lead("Round 3 asked every rule a new question: who, by its own words, has to obey it? Share of the 278 binding rules naming each party (a rule can name several).", size=28)}
<div style="display:flex;flex-direction:column;gap:12px;margin-top:4px">
{bar("Public bodies and governments", 63, "63%")}
{bar("Operators and deployers", 62, "62%")}
{bar("Manufacturers and producers", 39, "39%")}
{bar("Owners and users", 38, "38%")}
{bar("Pilots and drivers", 25, "25%")}
{bar("Individuals, the general public", 18, "18%", color=COPPER)}
{bar("Developers and providers of the software", 8, "8%", color=COPPER)}
</div>
{lead("The duty sits with whoever runs the machine in the world. The people who write the software that decides are named by one rule in twelve.", width=1600)}
{foot("Supplementary field 'bound parties', read from the text with a quote for each answer; v5 Table 71.")}
''', pad="100px 128px 130px", gap=18)

# 11 headline 6 - when
years = [(2015, 6), (2016, 5), (2017, 13), (2018, 20), (2019, 20), (2020, 13), (2021, 27), (2022, 22), (2023, 17), (2024, 35), (2025, 43), (2026, 27)]
cols = "".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px;width:110px"><p style="font-size:24px;color:{SLATE}">{v}</p><div style="width:70px;height:{int(v*9)}px;background:{COPPER if y>=2024 else INK};border-radius:4px 4px 0 0"></div><p style="font-size:24px;color:{INK}">{y}{"*" if y==2026 else ""}</p></div>' for y, v in years)
sec("when", f'''
{eyebrow("Headline six")}
{h2("The rules are new, and they arrive after the machines")}
{lead("Binding rules that reach robots, by the year they were adopted. Three quarters date from 2019 or later; 2024 to 2026 alone account for 105 of 278.", size=28)}
<div style="display:flex;align-items:flex-end;gap:14px;margin-top:4px;height:430px">{cols}</div>
{lead("Drone rules followed drones into the sky. Self-driving rules followed test fleets onto the road. Delivery-robot statutes followed sidewalk robots. Humanoids and companions have arrived in showrooms and strategies, and their rules have not followed yet.", size=28, width=1600)}
{foot("* 2026 runs to October. Year of adoption as stated in the text; consolidated statutes dated by their robot provision where known (v5 Table 73).")}
''', pad="100px 128px 130px", gap=18)

# 12 headline 7 - where
sec("where", f'''
{eyebrow("Headline seven")}
{h2("Three regions write almost all of it, and they write different things")}
<div style="display:flex;gap:56px;margin-top:8px">
<div style="display:flex;flex-direction:column;gap:12px;width:760px">
{bar("North America", 100, "85", maxw=420, lw=240)}
{bar("Europe", 100*82/85, "82", maxw=420, lw=240)}
{bar("Asia", 100*69/85, "69", maxw=420, lw=240)}
{bar("Latin America", 100*16/85, "16", maxw=420, lw=240)}
{bar("Oceania, Africa, Middle East", 100*7/85, "7, 7, 6", maxw=420, lw=240)}
{bar("International bodies", 100*6/85, "6", maxw=420, lw=240)}
</div>
<div style="display:flex;flex-direction:column;gap:22px;width:800px">
<p style="font-size:28px;line-height:1.4;color:{SLATE}"><b style="color:{INK}">The United States</b> (75 rules) legislates state by state: delivery robots, autonomous vehicles, drones over prisons.</p>
<p style="font-size:28px;line-height:1.4;color:{SLATE}"><b style="color:{INK}">The European Union</b> (40) regulates machines as products: the Machinery Regulation, drone regulations, the AI Act reaching safety components.</p>
<p style="font-size:28px;line-height:1.4;color:{SLATE}"><b style="color:{INK}">Japan, China and Korea</b> (57 together) are the only places with laws that say 'robot' in the title: Korea's Intelligent Robots Act, Japan's Level-4 traffic rules, China's city regulations for driverless cars, and the 2025 to 2026 plans for 'embodied intelligence' in Beijing and Shanghai.</p>
</div>
</div>
{foot("Binding principal instruments by region and jurisdiction, v5.")}
''', pad="100px 128px 130px", gap=20)

# 13 headline 8 - standards
sec("standards", f'''
{eyebrow("Headline eight", "#E7B98F")}
{h2("The detailed safety knowledge is in standards, and standards are for sale", color=WHITE)}
<div style="display:flex;gap:64px;margin-top:16px">
{bignum("61", "technical standards in the collection that say how to make a robot safe", color="#E7B98F", width=480, lcolor="#CFE3DC")}
{bignum("45", "declare themselves voluntary; 1 is referenced by law", color="#E7B98F", width=440, lcolor="#CFE3DC")}
{bignum("57", "could only be read from their public preview page", color="#E7B98F", width=460, lcolor="#CFE3DC")}
</div>
<p style="font-size:30px;line-height:1.4;color:#CFE3DC;width:1600px">ISO 10218 for factory arms, ISO 13482 for personal-care robots, ISO 3691-4 for driverless trucks, UL 4600 for autonomous products: this is where the engineering detail lives. A law says 'be safe'; the standard says how. Nobody can read the standard without paying for it, and neither could we. The most practical safety knowledge about robots is the least public.</p>
{foot("Technical standards among principal instruments; legal-effect field from the public page; v5 Table 72.", "#9DB8B0")}
''', bg=INK, fg=WHITE)

# 14 headline 9 - where you look
sec("look", f'''
{eyebrow("Headline nine")}
{h2("Where you look changes what you find")}
{lead("The same world, counted four times as the study improved its search and its counting rules.", size=28)}
<div style="display:flex;gap:40px;margin-top:8px;align-items:flex-end">
<div style="flex:1;display:flex;flex-direction:column;gap:12px"><p style="font-family:{SERIF};font-size:120px;line-height:1;color:{SLATE}">5</p><p style="font-size:26px;line-height:1.35;color:{SLATE}">binding robot rules after round one: regional teams searching the web</p></div>
<div style="flex:1;display:flex;flex-direction:column;gap:12px"><p style="font-family:{SERIF};font-size:120px;line-height:1;color:{SLATE}">299</p><p style="font-size:26px;line-height:1.35;color:{SLATE}">after AI agents searched legal databases, every legal text counted</p></div>
<div style="flex:1;display:flex;flex-direction:column;gap:12px"><p style="font-family:{SERIF};font-size:120px;line-height:1;color:{INK}">195</p><p style="font-size:26px;line-height:1.35;color:{SLATE}">after removing paperwork: commencement orders, fee rules, index pages</p></div>
<div style="flex:1;display:flex;flex-direction:column;gap:12px"><p style="font-family:{SERIF};font-size:120px;line-height:1;color:{COPPER}">278</p><p style="font-size:26px;line-height:1.35;color:{SLATE}">after recovering 108 texts the databases had blocked</p></div>
</div>
{lead("Every count of 'AI regulation' you have ever seen depends on where someone looked and what they decided was one rule. Ours does too. The difference is that we report it.", width=1600)}
{foot("v1 to v5 of the study; the counting unit is defined in the methods.")}
''')

# 15 headline 10 - AI read the law
sec("airead", f'''
{eyebrow("Headline ten")}
{h2("AI read the law about AI. How far can you trust it?")}
<div style="display:flex;gap:56px;margin-top:8px">
{bignum("0.86", "agreement (kappa) between two different AI readers on a sample of 160 documents; 0.92 when the same reader was run twice", color=INK, width=520, nsize=120)}
{bignum("73%", "of a random 100 of the binding rules survived an independent re-read on three strict tests, up from 54% a version earlier", color=COPPER, width=520, nsize=120)}
{bignum("0", "documents labelled by a human so far. A 200-document validation kit is ready for one.", color=INK, width=520, nsize=120)}
</div>
{lead("What failed the audit is instructive: laws that mention a drone in a list of agency duties, register pages captured instead of the statute, two copies of the same EU regulation. The machine reads consistently; it does not yet read like a lawyer. Treat every number here as a well-measured estimate with an honest error bar, not a fact.", size=28, width=1600)}
{foot("Reliability samples and the two precision audits, v5 supplement and review/v5_audit.")}
''')

# 16 for research
sec("forresearch", f'''
{eyebrow("What it means")}
{h2("For AI research: we are studying robots that nobody is regulating")}
<div style="display:flex;flex-direction:column;gap:26px;margin-top:8px;width:1600px">
<div style="display:flex;gap:28px;align-items:flex-start"><p style="font-family:{SERIF};font-size:52px;line-height:1;color:{COPPER};width:70px">1</p><p style="font-size:30px;line-height:1.4"><b>The research agenda and the legal agenda are inverted.</b> Four papers in ten on robot governance are about companion robots; three rules in a hundred are. Our evidence on human-robot interaction, deception, attachment and dependency has nowhere in law to land.</p></div>
<div style="display:flex;gap:28px;align-items:flex-start"><p style="font-family:{SERIF};font-size:52px;line-height:1;color:{COPPER};width:70px">2</p><p style="font-size:30px;line-height:1.4"><b>'Autonomy' is a legal word now, and it is underspecified.</b> 171 rules invoke it, 73 define it. Researchers who can translate levels of autonomy into testable conditions are writing the next decade of law whether they mean to or not.</p></div>
<div style="display:flex;gap:28px;align-items:flex-start"><p style="font-family:{SERIF};font-size:52px;line-height:1;color:{COPPER};width:70px">3</p><p style="font-size:30px;line-height:1.4"><b>Reading law at scale is now possible, and it needs the same rigour as any instrument.</b> Blind reading, inter-reader agreement, independent audits, counting units stated in advance. Governance science can be measured, not only argued.</p></div>
</div>
''')

# 17 for governance
sec("forgov", f'''
{eyebrow("What it means")}
{h2("For governance: three moves before the next machines arrive")}
<div style="display:flex;gap:40px;margin-top:8px">
<div style="flex:1;background:{WHITE};border-top:10px solid {COPPER};padding:36px 38px;display:flex;flex-direction:column;gap:16px"><p style="font-family:{SERIF};font-size:42px;line-height:1.15">Write the rules for the robots we will live with, before the incidents</p><p style="font-size:27px;line-height:1.4;color:{SLATE}">Companions, carers and humanoids have zero, zero and four binding rules. Drones got theirs after near-misses at airports. The pattern is avoidable.</p></div>
<div style="flex:1;background:{WHITE};border-top:10px solid {COPPER};padding:36px 38px;display:flex;flex-direction:column;gap:16px"><p style="font-family:{SERIF};font-size:42px;line-height:1.15">Answer the control question, do not just raise it</p><p style="font-size:27px;line-height:1.4;color:{SLATE}">Who may let the machine decide what, under which conditions, checked by whom. Aviation law shows it can be done; the other sectors mostly gesture at it.</p></div>
<div style="flex:1;background:{WHITE};border-top:10px solid {COPPER};padding:36px 38px;display:flex;flex-direction:column;gap:16px"><p style="font-family:{SERIF};font-size:42px;line-height:1.15">Make the safety knowledge public</p><p style="font-size:27px;line-height:1.4;color:{SLATE}">When a law points to a standard, the standard becomes law in effect. Fifty-seven of our sixty-one standards are behind a paywall. Rules people cannot read are rules people cannot follow.</p></div>
</div>
''')

# 18 what we don't know
sec("limits", f'''
{eyebrow("What we do not know")}
{h2("The honest edges of the map")}
<div style="display:flex;flex-direction:column;gap:20px;margin-top:8px;width:1640px">
<p style="font-size:30px;line-height:1.4"><b>74 official sources refused our crawler</b>, mostly France, Norway, Korea, Taiwan and Chinese provinces. They are listed for a person with a browser. Our crawler identifies itself honestly and does not pretend to be one.</p>
<p style="font-size:30px;line-height:1.4"><b>Old statutes hide their robot provisions.</b> A road-traffic act from 1960 can carry a 2023 article on automated driving; we could date the provision in only 28 of the 278 rules. Trend lines on binding law are therefore floors, not histories.</p>
<p style="font-size:30px;line-height:1.4"><b>English is 74% of the collection.</b> Chinese, Japanese, Spanish and Portuguese texts were read in the original, but the search was richest in English and in the EU.</p>
<p style="font-size:30px;line-height:1.4"><b>No human has labelled a document.</b> The next step in this study is a person, not a model.</p>
</div>
{foot("HUMAN_ASSISTANCE.md in the repository lists every item that needs a person.")}
''')

# 19 takeaways
sec("takeaways", f'''
{eyebrow("To remember", "#E7B98F")}
{h2("Five things to take home", color=WHITE)}
<div style="display:flex;flex-direction:column;gap:24px;margin-top:4px">
<div style="display:flex;gap:30px;align-items:flex-start"><p style="font-family:{SERIF};font-size:54px;line-height:1;color:#E7B98F;width:76px">1</p><p style="font-size:30px;line-height:1.4;width:1520px"><b>Robots are governed sideways.</b> 278 binding rules reach them; 25 name AI. They are aviation, road, machinery and product law.</p></div>
<div style="display:flex;gap:30px;align-items:flex-start"><p style="font-family:{SERIF};font-size:54px;line-height:1;color:#E7B98F;width:76px">2</p><p style="font-size:30px;line-height:1.4;width:1520px"><b>The robots we will live with have almost none.</b> Companions 0, humanoids 0, care robots 4, among 429 documents about them.</p></div>
<div style="display:flex;gap:30px;align-items:flex-start"><p style="font-family:{SERIF};font-size:54px;line-height:1;color:#E7B98F;width:76px">3</p><p style="font-size:30px;line-height:1.4;width:1520px"><b>The body changes the rulebook.</b> Physical safety, certification, accountability and liability lead; transparency, fairness and dignity barely appear.</p></div>
<div style="display:flex;gap:30px;align-items:flex-start"><p style="font-family:{SERIF};font-size:54px;line-height:1;color:#E7B98F;width:76px">4</p><p style="font-size:30px;line-height:1.4;width:1520px"><b>Mention is not detail.</b> Six rules in ten raise the control question; fewer than three in ten answer it. Duties fall on operators, rarely on the people who write the software.</p></div>
<div style="display:flex;gap:30px;align-items:flex-start"><p style="font-family:{SERIF};font-size:54px;line-height:1;color:#E7B98F;width:76px">5</p><p style="font-size:30px;line-height:1.4;width:1520px"><b>Every count depends on where you looked.</b> Ours went 5, 299, 195, 278. Ask any number about AI regulation how it was made.</p></div>
</div>
''', bg=INK, fg=WHITE, pad="100px 128px 100px", gap=20)

# 20 close
sec("close", f'''
{eyebrow("Thank you", "#E7B98F")}
<div style="display:flex;flex-direction:column;gap:30px;width:1500px">
<h2 style="font-family:{SERIF};font-size:92px;font-weight:500;line-height:1.05;color:{WHITE}">The question is not whether robots will come into our homes. It is whether the rules will be there when they do.</h2>
</div>
<div style="display:flex;justify-content:space-between;align-items:flex-end">
<p style="font-size:26px;color:#CFE3DC;line-height:1.6">Data, code, every table and the list of what still needs a person:<br>github.com/cjimmylin/embodied-ai-governance<br>Explore the 3,320 documents: claude.ai/artifact/YKsXJRaT7tSfRXseuo5kuZ</p>
<p style="font-size:24px;color:#CFE3DC;text-align:right;line-height:1.5">Centre for Enterprise Innovation (CEI)<br>AI Robotics project, November 2026</p>
</div>''', bg=INK, fg=WHITE, pad="128px", gap=56, extra=";justify-content:space-between")

order = [s[0] for s in slides]
for id_, html in slides:
    open(os.path.join(S, id_ + ".html"), "w", encoding="utf8").write(html)
deck = {"v": 4, "createdOnFiles": {"v": 1, "at": "2026-11-03T08:00:00Z"}, "lists": "css", "title": "Who Governs the Robots: Keynote", "cover": "cover", "order": order,
        "sections": {"opening": {"description": "The question and how the map was made.", "start": "cover"},
                     "headlines": {"description": "Ten headline findings, each on one slide.", "start": "sideways"},
                     "meaning": {"description": "What it means for research and for governance, the limits, and five things to remember.", "start": "forresearch"}},
        "faces": {"fraunces": {"family": "Fraunces", "href": "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&display=swap"},
                  "ibm-plex-sans": {"family": "IBM Plex Sans", "href": "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&display=swap"}},
        "designSystems": []}
json.dump(deck, open(os.path.join(P, "deck.json"), "w"), indent=1)
print("keynote slides:", len(order))
