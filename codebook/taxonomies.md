# Taxonomies (with corpus counts)

Counts are over the 3295 annotated documents. 'Any mention' counts documents carrying the label in `embodied_categories`; 'Primary' counts documents whose single most central category it is.

## 1. Robotics and embodied-AI taxonomy

Two cross-cutting axes precede the categories: **embodiment status** (physical system vs software agent called a robot) and **AI scope** (general AI only / general AI with embodied provisions / embodied AI as a class / a specific embodied category).

| Embodiment status | Documents | Share |
|---|---|---|
| physical_embodied | 1524 | 46.3% |
| none | 1488 | 45.2% |
| mixed | 236 | 7.2% |
| software_agent_called_robot | 47 | 1.4% |

| AI scope | Documents | Share |
|---|---|---|
| general_ai_only | 1026 | 31.1% |
| embodied_ai_specific_category | 997 | 30.3% |
| not_ai | 576 | 17.5% |
| embodied_ai_robotics_general | 388 | 11.8% |
| general_ai_with_embodied_provisions | 308 | 9.3% |

| Level 1 | Level 2 category | Definition | Any mention | Primary | Example documents |
|---|---|---|---|---|---|
| Industrial & logistics | `industrial_manipulators` | Fixed industrial arms and caged robots in manufacturing | 220 | 84 | R2-d864adaa Technical Safety Guideline on the Use of Industrial Robots (KOSHA GUID; R2-a476daf2 ISO 9409-1:2004 Manipulating industrial robots — Mechanical interfaces; R2-78c51a42 Directive 98/37/EC of the European Parliament and of the Council of 22 |
| Industrial & logistics | `collaborative_robots` | Cobots that share a workspace with humans | 118 | 47 | R2-f48a8103 Proposal for a Regulation of the European Parliament and of the Counci; R2-3b329b09 Collaborative Robot Systems – Planning of Installations with the Power; D0320 Guidelines for Safe Collaborative Robot Design and Implementation |
| Industrial & logistics | `mobile_industrial_logistics` | AMRs, AGVs, warehouse and forklift robots, industrial trucks | 114 | 31 | D0397 ISO/WD 26058-1 Safety requirements for industrial mobile robots — Part; D1383 ISO 3691-4:2023 Industrial trucks — Safety requirements and verificati; R2-885d8000 Commission Implementing Decision (EU) 2024/1329 of 13 May 2024 amendin |
| Industrial & logistics | `delivery_robots` | Sidewalk and last-mile delivery robots | 61 | 24 | R2-18be461c Personal Delivery Device Act (Arkansas HB 1767, Act 926 of 2021); R2-63dcc910 Section 4511.513 Operation of personal delivery device on sidewalks an; R2-b53750a0 Missouri Revised Statutes Section 304.900 – Personal delivery devices, |
| Service & social | `professional_service_robots` | Cleaning, security, hospitality, retail, inspection and rescue robots | 211 | 77 | D0005 Robotic Technologies Law (Decree No. 340); D0018 ISO 31101:2023 Robotics — Application services provided by service rob; D0508 Action Plan for the Innovation and Development of the Robotics Industr |
| Service & social | `domestic_household_robots` | Vacuum, lawn and home-assistant robots | 81 | 13 | R2-f0fbb04b National Standards Information Public Service Platform search result: ; R2-30f2fdb4 National Standards Information Public Service Platform – Search Result; R2-215234e6 National Standards Information Public Service Platform – Search result |
| Service & social | `social_companion_robots` | Companionship and emotional-interaction robots, robotic pets | 245 | 100 | D1465 Ethical Aspects of the Use of Social Robots in Elderly Care -- A Syste; D1607 Social Robots in Nursing Homes: Field Work and Ethics; D1481 Ethical perceptions towards real-world use of companion robots with ol |
| Service & social | `educational_robots` | Robots used in teaching and learning | 52 | 15 | R2-49c7c292 Educational Robots—Safety Requirements and Testing Methods (GB/T 33265; D0024 Ethical implications of emotional and psychologic ties on human-robot ; D0848 Promoting STEAM Education and AI/Robot Ethics in a Child-Robot Theater |
| Service & social | `care_assistive_robots` | Elder care, disability support and nursing assistance | 226 | 98 | D0185 ISO 13482:2014 Robots and robotic devices — Safety requirements for pe; R2-0855b2d9 Implementation Opinions of the Ministry of Commerce and Seven Other De; R2-082a618a Notice on Issuing the Several Measures on Cultivating Elderly Care Ser |
| Service & social | `toys_entertainment_robots` | Toys and entertainment robots | 11 | 4 | R2-492928d7 Entertainment robots—Safety requirements and testing methods (GB/T 413; R2-b83cc260 Revised: Internet-Connected Toys Could Present Privacy and Contact Con; D0838 Data protection for networked and robotic toys – a legal perspective |
| Service & social | `sex_robots` | Sexual and intimate-companion robots | 28 | 20 | R2-93c49f40 H.R. 1186 – Curbing Realistic Exploitative Electronic Pedophilic Robot; R2-2904db2e Curbing Realistic Exploitative Electronic Pedophilic Robots Act of 201; D0551 Current Issues with Sex Robots and Three Approaches to its Regulation |
| Medical & body-integrated | `surgical_medical_robots` | Surgical and clinical robots | 153 | 59 | D1013 Interplay between the Medical Devices Regulation (MDR) & In vitro Diag; R2-92b0acef Proposal for a Regulation amending Regulations (EU) 2017/745 and (EU) ; R2-6a674697 The contribution of the robotics metaverse in the medical sector |
| Medical & body-integrated | `rehabilitation_exoskeleton_prosthetic` | Exoskeletons, prostheses, wearable robots, BCI-driven actuators | 68 | 19 | R2-afe1f8af Three-Year Action Plan for Expanding Capacity and Improving Quality of; R2-dcb1bb49 General specifications for motion rehabilitation training robot (GB/T ; R2-9afd6f5a De Novo Classification Order for ReWalk Powered Exoskeleton (K131798) |
| Medical & body-integrated | `biohybrid_or_cyborg` | Biohybrid systems and human augmentation | 13 | 4 | D1411 Bees, Humans and Robots: Ethical and Epistemic Implications of Biohybr; D1451 Ethical Concerns Of Surviving Via And From Robots: Cyborgs And Expiry ; R2-afe1f8af Three-Year Action Plan for Expanding Capacity and Improving Quality of |
| Humanoid & general-purpose | `humanoid_general_purpose` | Humanoids, androids, general-purpose embodied agents and embodied foundation models | 171 | 95 | D0003 Bill No. 391/2026 - Regulating the manufacture, sale, possession, use ; D0460 Implementation Plan of Shanghai Municipality for the Development of th; D0464 Artificial Intelligence Basic Plan — "Japan Rebooted" through "Trustwo |
| Vehicles & field | `autonomous_road_vehicles` | Cars, trucks, buses and shuttles | 433 | 307 | D0228 Law No. (9) of 2023 Regulating the Operation of Autonomous Vehicles in; D1140 White Paper on Artificial Intelligence - A European approach to excell; R2-3f7ae081 Autonomous driving in European transport |
| Vehicles & field | `drones_uas` | Aerial drones and unmanned aircraft systems | 431 | 308 | R2-ddd7d9c2 Commission Implementing Regulation (EU) 2019/947 of 24 May 2019 on the; R2-c5427e07 Part 107—Small Unmanned Aircraft Systems (14 CFR); R2-6c14c9c2 Commission Delegated Regulation (EU) 2019/945 on unmanned aircraft sys |
| Vehicles & field | `autonomous_maritime_or_rail` | Autonomous ships, vessels and trains | 49 | 23 | R2-5c2fd4c2 Interim Guidelines for MASS Trials (MSC.1/Circ.1604); R2-f326a923 Notice of the Ministry of Transport, MIIT, SASAC and SAMR on Issuing t; R2-5538d60f ISO/TS 23860:2022 Ships and marine technology — Vocabulary related to  |
| Vehicles & field | `agricultural_robots` | Field, harvesting and livestock robots | 83 | 21 | R2-6db84260 Commission Implementing Decision (EU) 2020/480 of 1 April 2020 amendin; R2-cf87cc99 Points to Note on "Public Road Driving of Robot Agricultural Machinery; R2-626a768f ISO 18497-1:2024 Agricultural machinery and tractors — Safety of parti |
| Vehicles & field | `space_or_extreme_environment` | Space, underwater, nuclear and mining robots | 45 | 6 | R2-9ff0eb01 Notice on Issuing the Guiding Opinions on Deepening Intelligent Mine C; R2-45a27a25 Earth-moving machinery and mining—Autonomous and semi-autonomous machi; D0558 Robot-First Mars Settlement: A Conceptual Framework for Technology Gov |
| Security & military | `military_autonomous_weapons` | Lethal autonomous weapons, armed drones, military robots | 196 | 115 | R2-d7dae4f6 Lethal autonomous weapons systems; R2-11825c4e European Parliament resolution of 12 September 2018 on autonomous weap; R2-300d8ec9 European Parliament resolution of 27 February 2014 on the use of armed |
| Security & military | `security_policing_robots` | Police, border and surveillance robots | 58 | 7 | D0016 Resolution 710/2024 - Creation of the Unit of Artificial Intelligence ; R2-cd4a42b1 Artificial Intelligence and Robotics for Law Enforcement; D0831 Exploring law enforcement officers' expectations and attitudes about c |
| Other | `other_embodied` | Other physical AI systems | 43 | 36 | D1353 RAS 2020: A national strategy to capture value in a cross-sector UK RA; R2-98aa0eab Regulation (EU) 2025/14 on the approval and market surveillance of non; R2-24b73fe4 IEEE 7007-2021 IEEE Ontological Standard for Ethically Driven Robotics |

## 2. Document topic taxonomy

Documents carry one `primary_topic` and any number of `governance_topics`.

| Topic | Primary | Any mention | Example documents |
|---|---|---|---|
| `safety_physical_harm` | 429 | 1302 | D0228 Law No. (9) of 2023 Regulating the Operation of Autonomous Vehicles in; R2-c5427e07 Part 107—Small Unmanned Aircraft Systems (14 CFR); R2-9c6e8103 Commission Implementing Regulation (EU) 2020/639 of 12 May 2020 amendi |
| `industrial_policy_innovation` | 616 | 1192 | R2-0e4b6b30 A Drone Strategy 2.0 for a Smart and Sustainable Unmanned Aircraft Eco; R2-0668260a Draft resolution on integrating the definition of automated vehicles i; R2-f60a2aeb Florida Statutes s. 316.85 – Autonomous vehicles; operation; complianc |
| `ethics_principles` | 397 | 1114 | D1008 Ethically Aligned Design: A Vision for Prioritizing Human Well-being w; R2-87907601 Framework of ethical aspects of artificial intelligence, robotics and ; R2-99c420d8 Robotics for Good Care |
| `standards_interoperability` | 234 | 1016 | R2-77acbca3 Commission Implementing Decision (EU) 2024/2103 of 30 July 2024 on har; R2-3e221bc0 Commission Implementing Regulation (EU) 2021/1166 of 15 July 2021 amen; R2-a476daf2 ISO 9409-1:2004 Manipulating industrial robots — Mechanical interfaces |
| `privacy_data_protection` | 82 | 856 | R2-4c85870b Maine Revised Statutes Title 25 §4501. Regulation of unmanned aerial v; R2-84e63b91 Searches and seizure using a drone (F.S. 934.50, Freedom from Unwarran; R2-8e251575 626.19 Use of Unmanned Aerial Vehicles (2026 Minnesota Statutes) |
| `certification_conformity_assessment` | 223 | 856 | R2-6c14c9c2 Commission Delegated Regulation (EU) 2019/945 on unmanned aircraft sys; R2-b4af497c Commission Implementing Regulation (EU) 2022/425 of 14 March 2022 amen; R2-a283b42e Commission Implementing Regulation (EU) 2024/1110 amending Regulation  |
| `risk_management_risk_tiers` | 157 | 793 | R2-ddd7d9c2 Commission Implementing Regulation (EU) 2019/947 of 24 May 2019 on the; D1140 White Paper on Artificial Intelligence - A European approach to excell; D0005 Robotic Technologies Law (Decree No. 340) |
| `education_training` | 67 | 739 | R2-d2567eac Civil Aviation Directive 6011 Part (I) – Unmanned Aircraft System Remo; R2-31dc68e0 ISO 23665:2026 Uncrewed aircraft systems — Training for personnel invo; R2-00b93992 ASTM F3330-18 Standard Specification for Training and the Development  |
| `transparency_explainability` | 35 | 736 | D1538 Is honesty the best policy for mismatched partners? Aligning multi-mod; D1655 Understandable and trustworthy explainable robots: A sensemaking persp; D1656 Understanding a Robot's Guiding Ethical Principles via Automatically G |
| `human_oversight_control` | 41 | 602 | R2-0d0ca0f5 PART 124—COUNTER-UNMANNED AIRCRAFT SYSTEM AUTHORITY FOR STATE, LOCAL, ; R2-c6368219 PAS 1884:2021 Safety operators in automated vehicle testing and triall; R2-43bd35c0 Working paper on the "human element" |
| `cybersecurity` | 51 | 565 | R2-022998ee FAR Part 40—Information Security and Supply Chain Security (Subpart 40; R2-f9c66a43 15 CFR Part 791—Securing the Information and Communications Technology; R2-a061be42 General requirements for information security of service robots |
| `civil_liability` | 73 | 519 | D1299 European Parliament Resolution of 16 February 2017 with recommendation; R2-3f7ae081 Autonomous driving in European transport; R2-66142fe4 Automated and Electric Vehicles Act 2018 |
| `fairness_bias_discrimination` | 23 | 514 | R2-a85e7f8c Addressing Bias in Autonomous Weapons; D0850 Inclusion in Assistive Haircare Robotics: Practical and Ethical Consid; D1511 Gender Stereotyping of Robotic Systems in Eldercare: An Exploratory An |
| `labor_employment` | 78 | 491 | D0221 Industrial Robotic Systems & International Human Rights; D0523 Toward a Synthesis of Computational Power and Human Wisdom. Review of ; R2-d2d88408 Opinion of the European Economic and Social Committee on 'Artificial i |
| `trust_acceptance` | 39 | 444 | D0182 Humanoid Robots, Public Trust, and Ethical Algorithm Design: A Multidi; D0971 The Ethical Dimensions of Public Opinion on Smart Robots; D1517 How Ethical Issues Raised by Human–Robot Interaction can Impact the In |
| `human_robot_interaction_social_effects` | 64 | 438 | R2-740db037 ISO/TR 23049:2018 Road Vehicles — Ergonomic aspects of external visual; R2-5f61e321 ISO/PAS 23735:2025 Road vehicles — Ergonomic design guidance for exter; D0024 Ethical implications of emotional and psychologic ties on human-robot  |
| `other` | 277 | 388 | R2-0322d77f The Air Navigation (Minimum Age for Operators of Small Unmanned Aircra; R2-f3b175ef Part 48—Registration and Marking Requirements for Small Unmanned Aircr; R2-4ef7d8d3 Air Traffic Management and Unmanned Aircraft Act 2021 |
| `sustainability_environment` | 57 | 333 | R2-ce7af517 ISO/TS 25213:2026 Robotics — Test methods for measuring the energy con; D0216 Sustainable and Ethical AI-Driven Recognition in Robotics: Integrating; D1299 European Parliament Resolution of 16 February 2017 with recommendation |
| `consumer_protection` | 46 | 333 | R2-5a3159c0 The Automated Vehicles (Marketing Restrictions) Regulations 2026; R2-2b73010a The Automated Vehicles Act 2024 (Commencement No. 3) Regulations 2026; R2-30f2fdb4 National Standards Information Public Service Platform – Search Result |
| `human_dignity_autonomy` | 33 | 329 | D0183 Companion Robots, Digital Intimacy and the Purposes of Marriage in Isl; D1604 Social Assistive Robotics: An Ethical and Political Inquiry Through th; D1673 “Oh, Dignity too?” Said the Robot: Human Dignity as the Basis for the  |
| `military_use_ihl` | 98 | 212 | R2-d7dae4f6 Lethal autonomous weapons systems; R2-11825c4e European Parliament resolution of 12 September 2018 on autonomous weap; R2-300d8ec9 European Parliament resolution of 27 February 2014 on the use of armed |
| `children_vulnerable_groups` | 12 | 190 | R2-2904db2e Curbing Realistic Exploitative Electronic Pedophilic Robots Act of 201; D0815 What Pediatric Robotic Surgery Since 2000 Suggests About E; D1299 European Parliament Resolution of 16 February 2017 with recommendation |
| `criminal_liability` | 44 | 167 | R2-c6679a66 House Bill No. 4797: Drone-Free Jails Act; R2-cb3f9817 The Automated Vehicles Act 2024 (Commencement No. 1) Regulations 2025; R2-93c49f40 H.R. 1186 – Curbing Realistic Exploitative Electronic Pedophilic Robot |
| `legal_personhood_robot_rights` | 57 | 150 | D0037 Robot as Legal Person: Electronic Personhood in Robotics and Artificia; D0179 Towards Granting of Legal Personality to Autonomous Robots in the UAE; D0204 Endowed by Their Creator with Certain Inalienable Rights? On John-Stew |
| `intellectual_property` | 20 | 131 | D0553 National Legal Protection Of Artificial Intelligence And Robots In The; D1299 European Parliament Resolution of 16 February 2017 with recommendation; D0005 Robotic Technologies Law (Decree No. 340) |
| `research_ethics` | 22 | 128 | D0556 Ethical Design of a Robot Platform for Disabled Employees: Some Practi; D1466 Ethical Challenges in the Human-Robot Interaction Field; D0863 Robotics in Service and the Responsibility to Society |
| `taxation_economic_policy` | 20 | 81 | R2-193753ad Civil Aviation Safety Amendment (Unmanned Aircraft Levy Collection) Re; R2-8ef9eda8 Civil Aviation Amendment (Unmanned Aircraft Levy Collection and Paymen; D0383 Robot Taxation as a Tool for Labor Market Protection: Legal Analysis o |

## 3. Document type taxonomy

| Class | Fine type | Documents | Governance instruments | Example documents |
|---|---|---|---|---|
| communication_or_news | `blog_or_opinion` | 22 | 0 | D0861 Sex robots are here, but laws aren't keeping up with the ethical and p; D0256 Oman's National Artificial Intelligence Policy; D0806 Our pixelated selves: How AI is helping pensioners in Telangana |
| communication_or_news | `news_article` | 12 | 0 | D0306 ‘Killer robots’ hit the road – and the law has yet to catch up; D0143 Artificial Intelligence: committee will have 30 more days to vote on f; D0171 Temporary committee will establish artificial intelligence framework |
| communication_or_news | `other` | 6 | 0 | D1446 The Rape of Lucrece; D0425 Keynote Address by the Minister of Communications and Digital Technolo; D0121 Artificial Intelligence Policy |
| communication_or_news | `press_release_or_government_news` | 162 | 0 | D0150 Latin America and the Caribbean Accelerate the Adoption of Artificial ; D0434 AI: UNESCO mobilizes education ministers from around the world for a c; D0798 Strengthening Data-Based Policymaking, Government Utilizes Artificial  |
| communication_or_news | `web_page_informational` | 390 | 2 | R2-78c31b4c PennDOT - Pennsylvania Department of Transportation; D0300 SDAIA Organizational Structure: H.E. Prof. Abdullah bin Sharaf Alghamd; D0274 Artificial Intelligence | Ministry of Justice, UAE |
| governance_instrument_binding | `court_decision_or_judicial_notice` | 8 | 8 | D0093 Protocol for Contingencies of Unavailability of IT Services of the Jud; D1169 Clearview AI Inc v The Information Commissioner [2023] UKFTT 00819 (GR; D0959 Notice to the Parties and the Profession: The Use of Artificial Intell |
| governance_instrument_binding | `international_treaty_or_convention` | 2 | 2 | R2-d5631264 Council of Europe Framework Convention on Artificial Intelligence and ; R2-6e60e906 Convention on Road Traffic (Vienna, 8 November 1968) — UN Treaty Colle |
| governance_instrument_binding | `regulation_or_decree` | 567 | 567 | R2-85b49103 Commission Implementing Regulation (EU) 2025/2526 of 16 December 2025 ; R2-e38aac12 Cabinet Order on Standard Fees of Local Governments; R2-799ce2e7 Commission Decision (EU) 2018/1617 of 25 October 2018 concerning a mea |
| governance_instrument_binding | `statute_or_act` | 119 | 119 | D0697 Law on Artificial Intelligence (Law No. 134/2025/QH15); D0228 Law No. (9) of 2023 Regulating the Operation of Autonomous Vehicles in; D0942 AB-489 Health care professions: deceptive terms or letters: artificial |
| governance_instrument_binding | `technical_standard` | 9 | 9 | D0125 ABNT NBR 17225:2025 Accessibility in web content and applications — Re; R2-a476daf2 ISO 9409-1:2004 Manipulating industrial robots — Mechanical interfaces; R2-bdae7a53 ISO 13482 Robots and robotic devices – Safety requirements for persona |
| governance_instrument_soft | `consultation_or_white_paper` | 1 | 1 | D1140 White Paper on Artificial Intelligence - A European approach to excell; D0410 South Africa National Artificial Intelligence Policy Framework (Toward; D0759 Public Consultation on Artificial Intelligence and Singapore's Intelle |
| governance_instrument_soft | `ethical_framework_or_principles` | 26 | 26 | D1696 Blueprint for an AI Bill of Rights: Making Automated Systems Work for ; D0763 Responsible AI #AIFORALL Part 1 – Principles for Responsible AI; R2-7115e06c Opinion on the Integration of Autonomy into Lethal Weapon Systems |
| governance_instrument_soft | `intergovernmental_recommendation_or_resolution` | 76 | 76 | R2-d7dae4f6 Lethal autonomous weapons systems; R2-35b25790 Mobilisation of the European Globalisation Adjustment Fund: Poland - P; R2-afbe7be4 Copyright and generative artificial intelligence – opportunities and c |
| governance_instrument_soft | `national_strategy_or_action_plan` | 200 | 200 | D0046 GoJ Communication Policy; R2-90ac2b88 General Office of the State Council Notice Forwarding the Ministry of ; R2-54555e36 Notice of the General Office of the State Council on Forwarding the Ac |
| governance_instrument_soft | `parliamentary_material` | 1 | 1 | D1299 European Parliament Resolution of 16 February 2017 with recommendation; R2-9f60871f Opinion of the European Committee of the Regions – White Paper on Arti; R2-b2dc1e84 Driving Change: Technology and the Future of the Automated Vehicle |
| governance_instrument_soft | `policy_guideline_or_code_of_practice` | 245 | 245 | D0669 Guidelines on Securing AI Systems; D0335 Guidance on privacy and developing and training generative AI models; R2-bf50ddb4 Opinions of the General Office of the State Council on Promoting High- |
| governance_instrument_soft | `procurement_or_internal_policy` | 12 | 11 | D0190 Annual Plan for Promoting Employment of People with Disabilities – Isr; D0930 Driving Efficient Acquisition of Artificial Intelligence in Government; D1344 Transparency of AI use in Procurement - Information Note 02/24 |
| governance_instrument_soft | `regulation_or_decree` | 2 | 2 | R2-85b49103 Commission Implementing Regulation (EU) 2025/2526 of 16 December 2025 ; R2-e38aac12 Cabinet Order on Standard Fees of Local Governments; R2-799ce2e7 Commission Decision (EU) 2018/1617 of 25 October 2018 concerning a mea |
| governance_instrument_soft | `technical_standard` | 232 | 231 | D0125 ABNT NBR 17225:2025 Accessibility in web content and applications — Re; R2-a476daf2 ISO 9409-1:2004 Manipulating industrial robots — Mechanical interfaces; R2-bdae7a53 ISO 13482 Robots and robotic devices – Safety requirements for persona |
| governance_instrument_soft | `web_page_informational` | 1 | 0 | R2-78c31b4c PennDOT - Pennsylvania Department of Transportation; D0300 SDAIA Organizational Structure: H.E. Prof. Abdullah bin Sharaf Alghamd; D0274 Artificial Intelligence | Ministry of Justice, UAE |
| governance_proposal_or_draft | `bill_or_draft_law` | 104 | 104 | D0055 Bill No. 5938/2023 - Amends Law 12.965 of 23 April 2014 (Brazilian Int; R2-09ddb7a8 Proposal for a Regulation amending Regulation (EU) 2017/746 as regards; R2-3cdaf66c Proposal for a Regulation amending Regulations (EU) 2017/745 and (EU)  |
| governance_proposal_or_draft | `consultation_or_white_paper` | 67 | 61 | D1140 White Paper on Artificial Intelligence - A European approach to excell; D0410 South Africa National Artificial Intelligence Policy Framework (Toward; D0759 Public Consultation on Artificial Intelligence and Singapore's Intelle |
| governance_proposal_or_draft | `intergovernmental_recommendation_or_resolution` | 3 | 3 | R2-d7dae4f6 Lethal autonomous weapons systems; R2-35b25790 Mobilisation of the European Globalisation Adjustment Fund: Poland - P; R2-afbe7be4 Copyright and generative artificial intelligence – opportunities and c |
| governance_proposal_or_draft | `parliamentary_material` | 1 | 1 | D1299 European Parliament Resolution of 16 February 2017 with recommendation; R2-9f60871f Opinion of the European Committee of the Regions – White Paper on Arti; R2-b2dc1e84 Driving Change: Technology and the Future of the Automated Vehicle |
| governance_proposal_or_draft | `technical_standard` | 45 | 45 | D0125 ABNT NBR 17225:2025 Accessibility in web content and applications — Re; R2-a476daf2 ISO 9409-1:2004 Manipulating industrial robots — Mechanical interfaces; R2-bdae7a53 ISO 13482 Robots and robotic devices – Safety requirements for persona |
| government_report_or_parliamentary | `bill_or_draft_law` | 1 | 1 | D0055 Bill No. 5938/2023 - Amends Law 12.965 of 23 April 2014 (Brazilian Int; R2-09ddb7a8 Proposal for a Regulation amending Regulation (EU) 2017/746 as regards; R2-3cdaf66c Proposal for a Regulation amending Regulations (EU) 2017/745 and (EU)  |
| government_report_or_parliamentary | `consultation_or_white_paper` | 8 | 5 | D1140 White Paper on Artificial Intelligence - A European approach to excell; D0410 South Africa National Artificial Intelligence Policy Framework (Toward; D0759 Public Consultation on Artificial Intelligence and Singapore's Intelle |
| government_report_or_parliamentary | `government_report_or_review` | 183 | 6 | R2-4afed03f Report of the Special Rapporteur on extrajudicial, summary or arbitrar; R2-198920a4 Report from the Commission on the Review of Regulation (EU) 2022/1925 ; R2-c71e2c34 Report of the 2019 session of the Group of Governmental Experts on Eme |
| government_report_or_parliamentary | `intergovernmental_recommendation_or_resolution` | 1 | 1 | R2-d7dae4f6 Lethal autonomous weapons systems; R2-35b25790 Mobilisation of the European Globalisation Adjustment Fund: Poland - P; R2-afbe7be4 Copyright and generative artificial intelligence – opportunities and c |
| government_report_or_parliamentary | `national_strategy_or_action_plan` | 1 | 1 | D0046 GoJ Communication Policy; R2-90ac2b88 General Office of the State Council Notice Forwarding the Ministry of ; R2-54555e36 Notice of the General Office of the State Council on Forwarding the Ac |
| government_report_or_parliamentary | `parliamentary_material` | 66 | 5 | D1299 European Parliament Resolution of 16 February 2017 with recommendation; R2-9f60871f Opinion of the European Committee of the Regions – White Paper on Arti; R2-b2dc1e84 Driving Change: Technology and the Future of the Automated Vehicle |
| government_report_or_parliamentary | `policy_guideline_or_code_of_practice` | 1 | 1 | D0669 Guidelines on Securing AI Systems; D0335 Guidance on privacy and developing and training generative AI models; R2-bf50ddb4 Opinions of the General Office of the State Council on Promoting High- |
| grey_literature | `industry_or_ngo_report` | 52 | 0 | D0100 A Call to the State of Peru to Request Observer Status on the Council ; D0433 Comment of the Center for AI and Digital Policy (CAIDP) to the Governm; D0833 Making the Case: The Dangers of Killer Robots and the Need for a Preem |
| grey_literature | `other` | 3 | 0 | D1446 The Rape of Lucrece; D0425 Keynote Address by the Minister of Communications and Digital Technolo; D0121 Artificial Intelligence Policy |
| grey_literature | `web_page_informational` | 1 | 0 | R2-78c31b4c PennDOT - Pennsylvania Department of Transportation; D0300 SDAIA Organizational Structure: H.E. Prof. Abdullah bin Sharaf Alghamd; D0274 Artificial Intelligence | Ministry of Justice, UAE |
| research_output | `book_or_chapter` | 51 | 0 | D0490 The Role of Robotics in Ethical Surgical Practices; D1467 Ethical Challenges of Assistive Robotics in the Elderly Care: Review a; D0472 Perspective Chapter: AI in Robotic Surgical Education – Expanding Hori |
| research_output | `conference_paper` | 112 | 0 | D1525 Human-data interaction and user rights at the personal robot era; D0194 The Basis of Civil Liability for Robot Damage - a comparative study; D0461 Redefining Financial Frontiers: Ethical Imperatives and Regulatory Dyn |
| research_output | `editorial_or_commentary` | 46 | 0 | D1607 Social Robots in Nursing Homes: Field Work and Ethics; D0204 Endowed by Their Creator with Certain Inalienable Rights? On John-Stew; D0886 Ethics of Robotic Deception |
| research_output | `journal_article` | 301 | 0 | D0037 Robot as Legal Person: Electronic Personhood in Robotics and Artificia; D1571 Robot Care Ethics Between Autonomy and Vulnerability: Coupling Princip; D0539 The urgency of robot trading regulation in Indonesia: Between innovati |
| research_output | `other` | 1 | 0 | D1446 The Rape of Lucrece; D0425 Keynote Address by the Minister of Communications and Digital Technolo; D0121 Artificial Intelligence Policy |
| research_output | `preprint_or_working_paper` | 55 | 0 | D0371 Buffer or Bottleneck? Employment Exposure to Generative AI and the Dig; D0312 Using Fitts' Law to Benchmark Assisted Human-Robot Performance; D0313 Ethical Asymmetry in Human-Robot Interaction – An Empirical Test of Sp |
| research_output | `review_or_survey_article` | 22 | 0 | D1465 Ethical Aspects of the Use of Social Robots in Elderly Care -- A Syste; D0438 Legal and Ethical Implications of Data Privacy in Artificial Intellige; D1475 Ethical concerns in rescue robotics: a scoping review |
| research_output | `thesis_or_dissertation` | 15 | 0 | D0634 Embodied care, spatiality, and the ethics of robotic surgery; D0859 Can Robots go to Heaven? Artificial Intelligence & Moral Standing in C; D1473 Ethical aspects concerning the use of social robots in medication coun |
| unusable | `other` | 1 | 0 | D1446 The Rape of Lucrece; D0425 Keynote Address by the Minister of Communications and Digital Technolo; D0121 Artificial Intelligence Policy |
| unusable | `statute_or_act` | 1 | 1 | D0697 Law on Artificial Intelligence (Law No. 134/2025/QH15); D0228 Law No. (9) of 2023 Regulating the Operation of Autonomous Vehicles in; D0942 AB-489 Health care professions: deceptive terms or letters: artificial |
| unusable | `unusable` | 58 | 0 | D0577 Page Not Found; R2-01d562a9 Federal Register / eCFR bot-block page; R2-559b375a FederalRegister.gov bot-block / CAPTCHA page |
| unusable | `web_page_informational` | 2 | 0 | R2-78c31b4c PennDOT - Pennsylvania Department of Transportation; D0300 SDAIA Organizational Structure: H.E. Prof. Abdullah bin Sharaf Alghamd; D0274 Artificial Intelligence | Ministry of Justice, UAE |

## 4. Instrument lifecycle status (governance documents only)

| Status | Documents |
|---|---|
| `published_current` | 754 |
| `in_force` | 603 |
| `superseded_or_repealed` | 118 |
| `draft_or_bill_under_consideration` | 90 |
| `under_development` | 51 |
| `adopted_not_yet_in_force` | 44 |
| `consultation_open` | 35 |
| `proposal_or_concept` | 30 |
| `unknown` | 5 |
| `withdrawn_or_lapsed` | 5 |

| Binding nature | Documents |
|---|---|
| `legally_binding` | 704 |
| `voluntary_soft_law` | 617 |
| `technical_standard_voluntary` | 272 |
| `not_applicable` | 129 |
| `technical_standard_mandated` | 13 |

## 5. Principles framework

Core principles follow Jobin et al. (2019) and the OECD AI Principles; six embodied-specific extensions were added. Salience: 0 absent, 1 mentioned, 2 substantive.

| Principle | Mentioned (1) | Substantive (2) | Any |
|---|---|---|---|
| `transparency` | 928 | 417 | 1345 |
| `justice_fairness` | 778 | 325 | 1103 |
| `non_maleficence` | 1876 | 383 | 2259 |
| `responsibility_accountability` | 1194 | 680 | 1874 |
| `privacy` | 661 | 351 | 1012 |
| `beneficence` | 1474 | 286 | 1760 |
| `freedom_autonomy` | 453 | 145 | 598 |
| `trust` | 722 | 309 | 1031 |
| `sustainability` | 601 | 180 | 781 |
| `dignity` | 413 | 111 | 524 |
| `solidarity` | 618 | 65 | 683 |
| `human_oversight` | 648 | 391 | 1039 |
| `robustness_security` | 1038 | 408 | 1446 |
| `inclusive_growth` | 788 | 725 | 1513 |
| `physical_safety` | 780 | 528 | 1308 |
| `human_robot_proximity` | 454 | 252 | 706 |
| `liability_for_physical_damage` | 225 | 138 | 363 |
| `autonomy_level_control` | 595 | 257 | 852 |
| `conformity_assessment_certification` | 576 | 404 | 980 |
| `dual_use_military` | 190 | 156 | 346 |

## 6. Governance mechanisms

| Mechanism | Documents |
|---|---|
| `technical_standards_reference` | 1151 |
| `oversight_body_creation` | 886 |
| `audits_impact_assessment` | 878 |
| `international_cooperation` | 839 |
| `education_training_programs` | 806 |
| `funding_or_incentives` | 755 |
| `none` | 736 |
| `conformity_assessment_certification` | 586 |
| `licensing_registration` | 581 |
| `testing_sandboxes` | 543 |
| `transparency_disclosure_labelling` | 528 |
| `data_governance_requirements` | 402 |
| `human_oversight_requirement` | 353 |
| `risk_based_tiering` | 337 |
| `prohibitions_bans` | 320 |
| `incident_reporting` | 314 |
| `self_regulation_codes` | 261 |
| `liability_regime` | 189 |
| `insurance_requirement` | 139 |