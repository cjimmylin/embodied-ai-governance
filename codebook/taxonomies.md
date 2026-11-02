# Taxonomies (with corpus counts)

Counts are over the 3450 annotated documents. 'Any mention' counts documents carrying the label in `embodied_categories`; 'Primary' counts documents whose single most central category it is.

## 1. Robotics and embodied-AI taxonomy

Two cross-cutting axes precede the categories: **embodiment status** (physical system vs software agent called a robot) and **AI scope** (general AI only / general AI with embodied provisions / embodied AI as a class / a specific embodied category).

| Embodiment status | Documents | Share |
|---|---|---|
| physical_embodied | 1630 | 47.2% |
| none | 1536 | 44.5% |
| mixed | 236 | 6.8% |
| software_agent_called_robot | 48 | 1.4% |

| AI scope | Documents | Share |
|---|---|---|
| embodied_ai_specific_category | 1073 | 31.1% |
| general_ai_only | 1035 | 30.0% |
| not_ai | 620 | 18.0% |
| embodied_ai_robotics_general | 392 | 11.4% |
| general_ai_with_embodied_provisions | 330 | 9.6% |

| Level 1 | Level 2 category | Definition | Any mention | Primary | Example documents |
|---|---|---|---|---|---|
| Industrial & logistics | `industrial_manipulators` | Fixed industrial arms and caged robots in manufacturing | 222 | 85 | R2-7bb2229f Regulation (EU) 2023/1230 of the European Parliament and of the Counci; R2-0c29bfda Regulation (EU) 2026/1744 amending Regulations (EU) 2024/1689, (EU) 20; R2-d864adaa Technical Safety Guideline on the Use of Industrial Robots (KOSHA GUID |
| Industrial & logistics | `collaborative_robots` | Cobots that share a workspace with humans | 118 | 46 | R2-f48a8103 Proposal for a Regulation of the European Parliament and of the Counci; R2-3b329b09 Collaborative Robot Systems – Planning of Installations with the Power; D0320 Guidelines for Safe Collaborative Robot Design and Implementation |
| Industrial & logistics | `mobile_industrial_logistics` | AMRs, AGVs, warehouse and forklift robots, industrial trucks | 119 | 33 | D0397 ISO/WD 26058-1 Safety requirements for industrial mobile robots — Part; D1383 ISO 3691-4:2023 Industrial trucks — Safety requirements and verificati; R2-885d8000 Commission Implementing Decision (EU) 2024/1329 of 13 May 2024 amendin |
| Industrial & logistics | `delivery_robots` | Sidewalk and last-mile delivery robots | 79 | 32 | R2-18be461c Personal Delivery Device Act (Arkansas HB 1767, Act 926 of 2021); R2-63dcc910 Section 4511.513 Operation of personal delivery device on sidewalks an; R2-d364d95a Intelligent Robots Development and Distribution Promotion Act |
| Service & social | `professional_service_robots` | Cleaning, security, hospitality, retail, inspection and rescue robots | 220 | 76 | D0005 Robotic Technologies Law (Decree No. 340); D0018 ISO 31101:2023 Robotics — Application services provided by service rob; D0508 Action Plan for the Innovation and Development of the Robotics Industr |
| Service & social | `domestic_household_robots` | Vacuum, lawn and home-assistant robots | 83 | 13 | R2-f0fbb04b National Standards Information Public Service Platform search result: ; R2-30f2fdb4 National Standards Information Public Service Platform – Search Result; R2-215234e6 National Standards Information Public Service Platform – Search result |
| Service & social | `social_companion_robots` | Companionship and emotional-interaction robots, robotic pets | 247 | 100 | D1465 Ethical Aspects of the Use of Social Robots in Elderly Care -- A Syste; D1607 Social Robots in Nursing Homes: Field Work and Ethics; D1481 Ethical perceptions towards real-world use of companion robots with ol |
| Service & social | `educational_robots` | Robots used in teaching and learning | 50 | 15 | R2-49c7c292 Educational Robots—Safety Requirements and Testing Methods (GB/T 33265; D0024 Ethical implications of emotional and psychologic ties on human-robot ; D0848 Promoting STEAM Education and AI/Robot Ethics in a Child-Robot Theater |
| Service & social | `care_assistive_robots` | Elder care, disability support and nursing assistance | 231 | 102 | D0185 ISO 13482:2014 Robots and robotic devices — Safety requirements for pe; R2-0855b2d9 Implementation Opinions of the Ministry of Commerce and Seven Other De; R2-082a618a Notice on Issuing the Several Measures on Cultivating Elderly Care Ser |
| Service & social | `toys_entertainment_robots` | Toys and entertainment robots | 13 | 6 | R2-492928d7 Entertainment robots—Safety requirements and testing methods (GB/T 413; R2-b83cc260 Revised: Internet-Connected Toys Could Present Privacy and Contact Con; D0838 Data protection for networked and robotic toys – a legal perspective |
| Service & social | `sex_robots` | Sexual and intimate-companion robots | 28 | 20 | R2-93c49f40 H.R. 1186 – Curbing Realistic Exploitative Electronic Pedophilic Robot; R2-2904db2e Curbing Realistic Exploitative Electronic Pedophilic Robots Act of 201; D0551 Current Issues with Sex Robots and Three Approaches to its Regulation |
| Medical & body-integrated | `surgical_medical_robots` | Surgical and clinical robots | 151 | 60 | D1013 Interplay between the Medical Devices Regulation (MDR) & In vitro Diag; R2-6a674697 The contribution of the robotics metaverse in the medical sector; R2-d3285a29 Publication of Evaluation Indicators for Next-Generation Medical Devic |
| Medical & body-integrated | `rehabilitation_exoskeleton_prosthetic` | Exoskeletons, prostheses, wearable robots, BCI-driven actuators | 72 | 20 | R2-afe1f8af Three-Year Action Plan for Expanding Capacity and Improving Quality of; R2-dcb1bb49 General specifications for motion rehabilitation training robot (GB/T ; R2-9afd6f5a De Novo Classification Order for ReWalk Powered Exoskeleton (K131798) |
| Medical & body-integrated | `biohybrid_or_cyborg` | Biohybrid systems and human augmentation | 14 | 4 | D1411 Bees, Humans and Robots: Ethical and Epistemic Implications of Biohybr; D1451 Ethical Concerns Of Surviving Via And From Robots: Cyborgs And Expiry ; R2-afe1f8af Three-Year Action Plan for Expanding Capacity and Improving Quality of |
| Humanoid & general-purpose | `humanoid_general_purpose` | Humanoids, androids, general-purpose embodied agents and embodied foundation models | 173 | 96 | D0003 Bill No. 391/2026 - Regulating the manufacture, sale, possession, use ; R3-59b89486 Beijing Action Plan for Embodied Intelligence Technological Innovation; D0460 Implementation Plan of Shanghai Municipality for the Development of th |
| Vehicles & field | `autonomous_road_vehicles` | Cars, trucks, buses and shuttles | 483 | 350 | R2-d97f5421 Automated Vehicles Act 2024; R2-b649a539 Regulations on the Management of Intelligent Connected Vehicles in the; R3-c4c110d0 Regulations on the Administration of Intelligent Connected Vehicles in |
| Vehicles & field | `drones_uas` | Aerial drones and unmanned aircraft systems | 481 | 347 | R2-ddd7d9c2 Commission Implementing Regulation (EU) 2019/947 of 24 May 2019 on the; R2-c5427e07 Part 107—Small Unmanned Aircraft Systems (14 CFR); R2-6c14c9c2 Commission Delegated Regulation (EU) 2019/945 on unmanned aircraft sys |
| Vehicles & field | `autonomous_maritime_or_rail` | Autonomous ships, vessels and trains | 53 | 23 | R2-5c2fd4c2 Interim Guidelines for MASS Trials (MSC.1/Circ.1604); R2-f326a923 Notice of the Ministry of Transport, MIIT, SASAC and SAMR on Issuing t; R2-5538d60f ISO/TS 23860:2022 Ships and marine technology — Vocabulary related to  |
| Vehicles & field | `agricultural_robots` | Field, harvesting and livestock robots | 86 | 21 | R2-6db84260 Commission Implementing Decision (EU) 2020/480 of 1 April 2020 amendin; R2-cf87cc99 Points to Note on "Public Road Driving of Robot Agricultural Machinery; R2-626a768f ISO 18497-1:2024 Agricultural machinery and tractors — Safety of parti |
| Vehicles & field | `space_or_extreme_environment` | Space, underwater, nuclear and mining robots | 45 | 6 | R2-9ff0eb01 Notice on Issuing the Guiding Opinions on Deepening Intelligent Mine C; R2-45a27a25 Earth-moving machinery and mining—Autonomous and semi-autonomous machi; D0558 Robot-First Mars Settlement: A Conceptual Framework for Technology Gov |
| Security & military | `military_autonomous_weapons` | Lethal autonomous weapons, armed drones, military robots | 199 | 116 | R2-d7dae4f6 Lethal autonomous weapons systems; R2-11825c4e European Parliament resolution of 12 September 2018 on autonomous weap; R2-300d8ec9 European Parliament resolution of 27 February 2014 on the use of armed |
| Security & military | `security_policing_robots` | Police, border and surveillance robots | 63 | 8 | D0016 Resolution 710/2024 - Creation of the Unit of Artificial Intelligence ; R2-de2c179b Law enforcement and state agencies: military equipment: funding, acqui; R2-cd4a42b1 Artificial Intelligence and Robotics for Law Enforcement |
| Other | `other_embodied` | Other physical AI systems | 44 | 38 | D1353 RAS 2020: A national strategy to capture value in a cross-sector UK RA; R2-98aa0eab Regulation (EU) 2025/14 on the approval and market surveillance of non; R2-84d1af71 Enforcement Decree of the Intelligent Robots Development and Distribut |

## 2. Document topic taxonomy

Documents carry one `primary_topic` and any number of `governance_topics`.

| Topic | Primary | Any mention | Example documents |
|---|---|---|---|
| `safety_physical_harm` | 474 | 1419 | R2-d97f5421 Automated Vehicles Act 2024; R2-b649a539 Regulations on the Management of Intelligent Connected Vehicles in the; R3-c4c110d0 Regulations on the Administration of Intelligent Connected Vehicles in |
| `industrial_policy_innovation` | 647 | 1261 | R2-06ecd7f6 Beijing Municipality Autonomous Vehicles Regulations; R2-d364d95a Intelligent Robots Development and Distribution Promotion Act; R2-62a59fe7 Unmanned Vehicles Technology Innovative Experimentation Act |
| `ethics_principles` | 399 | 1118 | R2-87907601 Framework of ethical aspects of artificial intelligence, robotics and ; D1008 Ethically Aligned Design: A Vision for Prioritizing Human Well-being w; R2-99c420d8 Robotics for Good Care |
| `standards_interoperability` | 237 | 1068 | R2-77acbca3 Commission Implementing Decision (EU) 2024/2103 of 30 July 2024 on har; R2-3e221bc0 Commission Implementing Regulation (EU) 2021/1166 of 15 July 2021 amen; R2-a476daf2 ISO 9409-1:2004 Manipulating industrial robots — Mechanical interfaces |
| `certification_conformity_assessment` | 240 | 940 | R2-6c14c9c2 Commission Delegated Regulation (EU) 2019/945 on unmanned aircraft sys; R2-b4af497c Commission Implementing Regulation (EU) 2022/425 of 14 March 2022 amen; R2-a283b42e Commission Implementing Regulation (EU) 2024/1110 amending Regulation  |
| `privacy_data_protection` | 87 | 924 | R2-4c85870b Maine Revised Statutes Title 25 §4501. Regulation of unmanned aerial v; R2-84e63b91 Searches and seizure using a drone (F.S. 934.50, Freedom from Unwarran; R2-8e251575 626.19 Use of Unmanned Aerial Vehicles (2026 Minnesota Statutes) |
| `risk_management_risk_tiers` | 161 | 834 | R2-ddd7d9c2 Commission Implementing Regulation (EU) 2019/947 of 24 May 2019 on the; D1140 White Paper on Artificial Intelligence - A European approach to excell; D0005 Robotic Technologies Law (Decree No. 340) |
| `education_training` | 70 | 768 | R2-d2567eac Civil Aviation Directive 6011 Part (I) – Unmanned Aircraft System: Rem; R2-be4e03ba Ordinance on Registered Training Institutions and Registered Renewal T; R2-31dc68e0 ISO 23665:2026 Uncrewed aircraft systems — Training for personnel invo |
| `transparency_explainability` | 36 | 761 | R3-e92e3ad7 IEEE 7001-2021 IEEE Standard for Transparency of Autonomous Systems; R2-de2c179b Law enforcement and state agencies: military equipment: funding, acqui; D1538 Is honesty the best policy for mismatched partners? Aligning multi-mod |
| `human_oversight_control` | 41 | 645 | R2-c6368219 PAS 1884:2021 Safety operators in automated vehicle testing and triall; R2-43bd35c0 Working paper on the "human element"; R2-6e817897 ISO 7856:2025 Intelligent transport systems — Remote support for low s |
| `cybersecurity` | 52 | 611 | R2-022998ee FAR Part 40—Information Security and Supply Chain Security (Subpart 40; R2-f9c66a43 Part 791—Securing the Information and Communications Technology and Se; R2-a061be42 General requirements for information security of service robots |
| `civil_liability` | 77 | 596 | D1299 European Parliament Resolution of 16 February 2017 with recommendation; R2-3f7ae081 Autonomous driving in European transport; R2-66142fe4 Automated and Electric Vehicles Act 2018 |
| `fairness_bias_discrimination` | 23 | 522 | R2-a85e7f8c Addressing Bias in Autonomous Weapons; D0850 Inclusion in Assistive Haircare Robotics: Practical and Ethical Consid; D1511 Gender Stereotyping of Robotic Systems in Eldercare: An Exploratory An |
| `labor_employment` | 83 | 502 | D0221 Industrial Robotic Systems & International Human Rights; D0523 Toward a Synthesis of Computational Power and Human Wisdom. Review of ; R2-d2d88408 Opinion of the European Economic and Social Committee on 'Artificial i |
| `trust_acceptance` | 39 | 447 | D0182 Humanoid Robots, Public Trust, and Ethical Algorithm Design: A Multidi; D0971 The Ethical Dimensions of Public Opinion on Smart Robots; D1517 How Ethical Issues Raised by Human–Robot Interaction can Impact the In |
| `human_robot_interaction_social_effects` | 65 | 439 | R2-95f8142d Guide for Effective Use of Nursing-Care Robots; R2-740db037 ISO/TR 23049:2018 Road Vehicles — Ergonomic aspects of external visual; R2-5f61e321 ISO/PAS 23735:2025 Road vehicles — Ergonomic design guidance for exter |
| `other` | 291 | 412 | R2-0322d77f The Air Navigation (Minimum Age for Operators of Small Unmanned Aircra; R2-f3b175ef Part 48—Registration and Marking Requirements for Small Unmanned Aircr; R2-d7556225 The Air Traffic Management and Unmanned Aircraft Act 2021 (Commencemen |
| `consumer_protection` | 46 | 381 | R2-5a3159c0 The Automated Vehicles (Marketing Restrictions) Regulations 2026; R2-2b73010a The Automated Vehicles Act 2024 (Commencement No. 3) Regulations 2026; R2-30f2fdb4 National Standards Information Public Service Platform – Search Result |
| `sustainability_environment` | 61 | 349 | R2-ce7af517 ISO/TS 25213:2026 Robotics — Test methods for measuring the energy con; D0216 Sustainable and Ethical AI-Driven Recognition in Robotics: Integrating; D1299 European Parliament Resolution of 16 February 2017 with recommendation |
| `human_dignity_autonomy` | 33 | 332 | D0183 Companion Robots, Digital Intimacy and the Purposes of Marriage in Isl; D1604 Social Assistive Robotics: An Ethical and Political Inquiry Through th; D1673 “Oh, Dignity too?” Said the Robot: Human Dignity as the Basis for the  |
| `military_use_ihl` | 101 | 215 | R2-d7dae4f6 Lethal autonomous weapons systems; R2-11825c4e European Parliament resolution of 12 September 2018 on autonomous weap; R2-300d8ec9 European Parliament resolution of 27 February 2014 on the use of armed |
| `children_vulnerable_groups` | 17 | 214 | R2-2904db2e Curbing Realistic Exploitative Electronic Pedophilic Robots Act of 201; D0815 What Pediatric Robotic Surgery Since 2000 Suggests About E; R2-d97f5421 Automated Vehicles Act 2024 |
| `criminal_liability` | 48 | 185 | R2-c6679a66 House Bill No. 4797: Drone-Free Jails Act; R2-cb3f9817 The Automated Vehicles Act 2024 (Commencement No. 1) Regulations 2025; R2-5e9a881e Draft Law on Automated-Driving Road Vehicles (Luxembourg) |
| `legal_personhood_robot_rights` | 57 | 151 | D0037 Robot as Legal Person: Electronic Personhood in Robotics and Artificia; D0179 Towards Granting of Legal Personality to Autonomous Robots in the UAE; D0204 Endowed by Their Creator with Certain Inalienable Rights? On John-Stew |
| `intellectual_property` | 20 | 138 | D0553 National Legal Protection Of Artificial Intelligence And Robots In The; D1299 European Parliament Resolution of 16 February 2017 with recommendation; D0005 Robotic Technologies Law (Decree No. 340) |
| `research_ethics` | 23 | 132 | D0556 Ethical Design of a Robot Platform for Disabled Employees: Some Practi; D1466 Ethical Challenges in the Human-Robot Interaction Field; D0863 Robotics in Service and the Responsibility to Society |
| `taxation_economic_policy` | 22 | 89 | R2-193753ad Civil Aviation Safety Amendment (Unmanned Aircraft Levy Collection) Re; R2-8ef9eda8 Civil Aviation Amendment (Unmanned Aircraft Levy Collection and Paymen; D0383 Robot Taxation as a Tool for Labor Market Protection: Legal Analysis o |

## 3. Document type taxonomy

| Class | Fine type | Documents | Governance instruments | Example documents |
|---|---|---|---|---|
| communication_or_news | `blog_or_opinion` | 22 | 0 | D0861 Sex robots are here, but laws aren't keeping up with the ethical and p; D0256 Oman's National Artificial Intelligence Policy; D0806 Our pixelated selves: How AI is helping pensioners in Telangana |
| communication_or_news | `news_article` | 12 | 0 | D0306 ‘Killer robots’ hit the road – and the law has yet to catch up; D0143 Artificial Intelligence: committee will have 30 more days to vote on f; D0171 Temporary committee will establish artificial intelligence framework |
| communication_or_news | `other` | 6 | 0 | D1446 The Rape of Lucrece; D0425 Keynote Address by the Minister of Communications and Digital Technolo; D0121 Artificial Intelligence Policy |
| communication_or_news | `press_release_or_government_news` | 163 | 0 | D0150 Latin America and the Caribbean Accelerate the Adoption of Artificial ; D0798 Strengthening Data-Based Policymaking, Government Utilizes Artificial ; D0434 AI: UNESCO mobilizes education ministers from around the world for a c |
| communication_or_news | `web_page_informational` | 392 | 2 | R2-dc5712a9 Pakistan Civil Aviation Authority – Announcements and News Page; D0296 Technology and Artificial Intelligence - Artificial Intelligence in th; D1377 Does Artificial Intelligence threaten decent work? |
| governance_instrument_binding | `court_decision_or_judicial_notice` | 8 | 8 | D0093 Protocol for Contingencies of Unavailability of IT Services of the Jud; D1169 Clearview AI Inc v The Information Commissioner [2023] UKFTT 00819 (GR; D0959 Notice to the Parties and the Profession: The Use of Artificial Intell |
| governance_instrument_binding | `international_treaty_or_convention` | 2 | 2 | R2-d5631264 Council of Europe Framework Convention on Artificial Intelligence and ; R2-6e60e906 Convention on Road Traffic (Vienna, 8 November 1968) — UN Treaty Colle |
| governance_instrument_binding | `regulation_or_decree` | 621 | 621 | R3-002e5473 Regulations of the People's Republic of China on Nature Reserves; R2-94b85e9d The Medical Devices (Coronavirus Test Device Approvals) (Amendment) Re; R2-4eb557ff The Valuation for Rating (Plant and Machinery) (Wales) (Amendment) Reg |
| governance_instrument_binding | `statute_or_act` | 178 | 178 | R2-d97f5421 Automated Vehicles Act 2024; R2-b649a539 Regulations on the Management of Intelligent Connected Vehicles in the; R3-c4c110d0 Regulations on the Administration of Intelligent Connected Vehicles in |
| governance_instrument_binding | `technical_standard` | 9 | 9 | D0125 ABNT NBR 17225:2025 Accessibility in web content and applications — Re; R2-a476daf2 ISO 9409-1:2004 Manipulating industrial robots — Mechanical interfaces; R2-bdae7a53 ISO 13482 Robots and robotic devices – Safety requirements for persona |
| governance_instrument_soft | `consultation_or_white_paper` | 1 | 1 | D1140 White Paper on Artificial Intelligence - A European approach to excell; D0743 Artificial Intelligence in the Malaysian Financial Sector (Discussion ; D0759 Public Consultation on Artificial Intelligence and Singapore's Intelle |
| governance_instrument_soft | `ethical_framework_or_principles` | 25 | 25 | D0763 Responsible AI #AIFORALL Part 1 – Principles for Responsible AI; D1696 Blueprint for an AI Bill of Rights: Making Automated Systems Work for ; D0315 Trustworthy AI in Aotearoa New Zealand: AI Principles |
| governance_instrument_soft | `intergovernmental_recommendation_or_resolution` | 76 | 76 | R2-d7dae4f6 Lethal autonomous weapons systems; R2-35b25790 Mobilisation of the European Globalisation Adjustment Fund: Poland - P; R3-52ba85aa Recommendation of the Council on Artificial Intelligence |
| governance_instrument_soft | `national_strategy_or_action_plan` | 209 | 209 | D0046 GoJ Communication Policy; R2-54555e36 Notice of the General Office of the State Council on Forwarding the Ac; R2-90ac2b88 General Office of the State Council Notice Forwarding the Ministry of  |
| governance_instrument_soft | `parliamentary_material` | 1 | 1 | D1299 European Parliament Resolution of 16 February 2017 with recommendation; R2-9f60871f Opinion of the European Committee of the Regions – White Paper on Arti; R2-b2dc1e84 Driving Change: Technology and the Future of the Automated Vehicle |
| governance_instrument_soft | `policy_guideline_or_code_of_practice` | 267 | 267 | D0669 Guidelines on Securing AI Systems; R2-22526a8e Commission Recommendation (EU) 2026/510 of 6 March 2026 on revising th; R3-a4926e7a Opinions of the National Development and Reform Commission and the Off |
| governance_instrument_soft | `procurement_or_internal_policy` | 12 | 11 | D0190 Annual Plan for Promoting Employment of People with Disabilities – Isr; D0930 Driving Efficient Acquisition of Artificial Intelligence in Government; D1344 Transparency of AI use in Procurement - Information Note 02/24 |
| governance_instrument_soft | `regulation_or_decree` | 2 | 2 | R3-002e5473 Regulations of the People's Republic of China on Nature Reserves; R2-94b85e9d The Medical Devices (Coronavirus Test Device Approvals) (Amendment) Re; R2-4eb557ff The Valuation for Rating (Plant and Machinery) (Wales) (Amendment) Reg |
| governance_instrument_soft | `technical_standard` | 232 | 231 | D0125 ABNT NBR 17225:2025 Accessibility in web content and applications — Re; R2-a476daf2 ISO 9409-1:2004 Manipulating industrial robots — Mechanical interfaces; R2-bdae7a53 ISO 13482 Robots and robotic devices – Safety requirements for persona |
| governance_instrument_soft | `web_page_informational` | 1 | 0 | R2-dc5712a9 Pakistan Civil Aviation Authority – Announcements and News Page; D0296 Technology and Artificial Intelligence - Artificial Intelligence in th; D1377 Does Artificial Intelligence threaten decent work? |
| governance_proposal_or_draft | `bill_or_draft_law` | 110 | 110 | D0055 Bill No. 5938/2023 - Amends Law 12.965 of 23 April 2014 (Brazilian Int; R2-21a51f86 Proposal for a Directive of the European Parliament and of the Council; R2-f32bac3c Proposal for a Regulation of the European Parliament and of the Counci |
| governance_proposal_or_draft | `consultation_or_white_paper` | 68 | 62 | D1140 White Paper on Artificial Intelligence - A European approach to excell; D0743 Artificial Intelligence in the Malaysian Financial Sector (Discussion ; D0759 Public Consultation on Artificial Intelligence and Singapore's Intelle |
| governance_proposal_or_draft | `intergovernmental_recommendation_or_resolution` | 3 | 3 | R2-d7dae4f6 Lethal autonomous weapons systems; R2-35b25790 Mobilisation of the European Globalisation Adjustment Fund: Poland - P; R3-52ba85aa Recommendation of the Council on Artificial Intelligence |
| governance_proposal_or_draft | `parliamentary_material` | 1 | 1 | D1299 European Parliament Resolution of 16 February 2017 with recommendation; R2-9f60871f Opinion of the European Committee of the Regions – White Paper on Arti; R2-b2dc1e84 Driving Change: Technology and the Future of the Automated Vehicle |
| governance_proposal_or_draft | `technical_standard` | 45 | 45 | D0125 ABNT NBR 17225:2025 Accessibility in web content and applications — Re; R2-a476daf2 ISO 9409-1:2004 Manipulating industrial robots — Mechanical interfaces; R2-bdae7a53 ISO 13482 Robots and robotic devices – Safety requirements for persona |
| government_report_or_parliamentary | `bill_or_draft_law` | 1 | 1 | D0055 Bill No. 5938/2023 - Amends Law 12.965 of 23 April 2014 (Brazilian Int; R2-21a51f86 Proposal for a Directive of the European Parliament and of the Council; R2-f32bac3c Proposal for a Regulation of the European Parliament and of the Counci |
| government_report_or_parliamentary | `consultation_or_white_paper` | 8 | 5 | D1140 White Paper on Artificial Intelligence - A European approach to excell; D0743 Artificial Intelligence in the Malaysian Financial Sector (Discussion ; D0759 Public Consultation on Artificial Intelligence and Singapore's Intelle |
| government_report_or_parliamentary | `government_report_or_review` | 185 | 7 | R2-4afed03f Report of the Special Rapporteur on extrajudicial, summary or arbitrar; R2-198920a4 Report from the Commission on the Review of Regulation (EU) 2022/1925 ; R2-b480ed52 Report of the 2018 session of the Group of Governmental Experts on Eme |
| government_report_or_parliamentary | `intergovernmental_recommendation_or_resolution` | 1 | 1 | R2-d7dae4f6 Lethal autonomous weapons systems; R2-35b25790 Mobilisation of the European Globalisation Adjustment Fund: Poland - P; R3-52ba85aa Recommendation of the Council on Artificial Intelligence |
| government_report_or_parliamentary | `national_strategy_or_action_plan` | 1 | 1 | D0046 GoJ Communication Policy; R2-54555e36 Notice of the General Office of the State Council on Forwarding the Ac; R2-90ac2b88 General Office of the State Council Notice Forwarding the Ministry of  |
| government_report_or_parliamentary | `parliamentary_material` | 66 | 5 | D1299 European Parliament Resolution of 16 February 2017 with recommendation; R2-9f60871f Opinion of the European Committee of the Regions – White Paper on Arti; R2-b2dc1e84 Driving Change: Technology and the Future of the Automated Vehicle |
| government_report_or_parliamentary | `policy_guideline_or_code_of_practice` | 1 | 1 | D0669 Guidelines on Securing AI Systems; R2-22526a8e Commission Recommendation (EU) 2026/510 of 6 March 2026 on revising th; R3-a4926e7a Opinions of the National Development and Reform Commission and the Off |
| grey_literature | `industry_or_ngo_report` | 52 | 0 | D0100 A Call to the State of Peru to Request Observer Status on the Council ; D0433 Comment of the Center for AI and Digital Policy (CAIDP) to the Governm; D0833 Making the Case: The Dangers of Killer Robots and the Need for a Preem |
| grey_literature | `other` | 3 | 0 | D1446 The Rape of Lucrece; D0425 Keynote Address by the Minister of Communications and Digital Technolo; D0121 Artificial Intelligence Policy |
| grey_literature | `web_page_informational` | 1 | 0 | R2-dc5712a9 Pakistan Civil Aviation Authority – Announcements and News Page; D0296 Technology and Artificial Intelligence - Artificial Intelligence in th; D1377 Does Artificial Intelligence threaten decent work? |
| research_output | `book_or_chapter` | 51 | 0 | D0490 The Role of Robotics in Ethical Surgical Practices; D1467 Ethical Challenges of Assistive Robotics in the Elderly Care: Review a; D0472 Perspective Chapter: AI in Robotic Surgical Education – Expanding Hori |
| research_output | `conference_paper` | 112 | 0 | D1525 Human-data interaction and user rights at the personal robot era; D0194 The Basis of Civil Liability for Robot Damage - a comparative study; D0461 Redefining Financial Frontiers: Ethical Imperatives and Regulatory Dyn |
| research_output | `editorial_or_commentary` | 46 | 0 | D1607 Social Robots in Nursing Homes: Field Work and Ethics; D0204 Endowed by Their Creator with Certain Inalienable Rights? On John-Stew; D0886 Ethics of Robotic Deception |
| research_output | `journal_article` | 301 | 0 | D0037 Robot as Legal Person: Electronic Personhood in Robotics and Artificia; D1571 Robot Care Ethics Between Autonomy and Vulnerability: Coupling Princip; D0539 The urgency of robot trading regulation in Indonesia: Between innovati |
| research_output | `other` | 1 | 0 | D1446 The Rape of Lucrece; D0425 Keynote Address by the Minister of Communications and Digital Technolo; D0121 Artificial Intelligence Policy |
| research_output | `preprint_or_working_paper` | 55 | 0 | D0371 Buffer or Bottleneck? Employment Exposure to Generative AI and the Dig; D0312 Using Fitts' Law to Benchmark Assisted Human-Robot Performance; D0313 Ethical Asymmetry in Human-Robot Interaction – An Empirical Test of Sp |
| research_output | `review_or_survey_article` | 22 | 0 | D1465 Ethical Aspects of the Use of Social Robots in Elderly Care -- A Syste; D0438 Legal and Ethical Implications of Data Privacy in Artificial Intellige; D1475 Ethical concerns in rescue robotics: a scoping review |
| research_output | `thesis_or_dissertation` | 15 | 0 | D0634 Embodied care, spatiality, and the ethics of robotic surgery; D0859 Can Robots go to Heaven? Artificial Intelligence & Moral Standing in C; D1473 Ethical aspects concerning the use of social robots in medication coun |
| unusable | `other` | 1 | 0 | D1446 The Rape of Lucrece; D0425 Keynote Address by the Minister of Communications and Digital Technolo; D0121 Artificial Intelligence Policy |
| unusable | `statute_or_act` | 1 | 1 | R2-d97f5421 Automated Vehicles Act 2024; R2-b649a539 Regulations on the Management of Intelligent Connected Vehicles in the; R3-c4c110d0 Regulations on the Administration of Intelligent Connected Vehicles in |
| unusable | `unusable` | 58 | 0 | D0577 Page Not Found; R2-01d562a9 Federal Register / eCFR bot-block page; R2-559b375a FederalRegister.gov bot-block / CAPTCHA page |
| unusable | `web_page_informational` | 2 | 0 | R2-dc5712a9 Pakistan Civil Aviation Authority – Announcements and News Page; D0296 Technology and Artificial Intelligence - Artificial Intelligence in th; D1377 Does Artificial Intelligence threaten decent work? |

## 4. Instrument lifecycle status (governance documents only)

| Status | Documents |
|---|---|
| `published_current` | 783 |
| `in_force` | 699 |
| `superseded_or_repealed` | 124 |
| `draft_or_bill_under_consideration` | 96 |
| `adopted_not_yet_in_force` | 56 |
| `under_development` | 51 |
| `consultation_open` | 35 |
| `proposal_or_concept` | 32 |
| `unknown` | 5 |
| `withdrawn_or_lapsed` | 5 |

| Binding nature | Documents |
|---|---|
| `legally_binding` | 817 |
| `voluntary_soft_law` | 649 |
| `technical_standard_voluntary` | 272 |
| `not_applicable` | 135 |
| `technical_standard_mandated` | 13 |

## 5. Principles framework

Core principles follow Jobin et al. (2019) and the OECD AI Principles; six embodied-specific extensions were added. Salience: 0 absent, 1 mentioned, 2 substantive.

| Principle | Mentioned (1) | Substantive (2) | Any |
|---|---|---|---|
| `transparency` | 992 | 435 | 1427 |
| `justice_fairness` | 817 | 329 | 1146 |
| `non_maleficence` | 1969 | 410 | 2379 |
| `responsibility_accountability` | 1263 | 743 | 2006 |
| `privacy` | 709 | 379 | 1088 |
| `beneficence` | 1533 | 301 | 1834 |
| `freedom_autonomy` | 473 | 147 | 620 |
| `trust` | 738 | 314 | 1052 |
| `sustainability` | 642 | 183 | 825 |
| `dignity` | 419 | 113 | 532 |
| `solidarity` | 638 | 68 | 706 |
| `human_oversight` | 674 | 428 | 1102 |
| `robustness_security` | 1084 | 442 | 1526 |
| `inclusive_growth` | 828 | 770 | 1598 |
| `physical_safety` | 832 | 585 | 1417 |
| `human_robot_proximity` | 485 | 257 | 742 |
| `liability_for_physical_damage` | 262 | 174 | 436 |
| `autonomy_level_control` | 628 | 289 | 917 |
| `conformity_assessment_certification` | 618 | 458 | 1076 |
| `dual_use_military` | 207 | 158 | 365 |

## 6. Governance mechanisms

| Mechanism | Documents |
|---|---|
| `technical_standards_reference` | 1230 |
| `oversight_body_creation` | 983 |
| `audits_impact_assessment` | 938 |
| `international_cooperation` | 879 |
| `education_training_programs` | 853 |
| `funding_or_incentives` | 812 |
| `none` | 742 |
| `licensing_registration` | 675 |
| `conformity_assessment_certification` | 647 |
| `testing_sandboxes` | 597 |
| `transparency_disclosure_labelling` | 579 |
| `data_governance_requirements` | 452 |
| `human_oversight_requirement` | 388 |
| `incident_reporting` | 380 |
| `prohibitions_bans` | 365 |
| `risk_based_tiering` | 361 |
| `self_regulation_codes` | 277 |
| `liability_regime` | 230 |
| `insurance_requirement` | 196 |