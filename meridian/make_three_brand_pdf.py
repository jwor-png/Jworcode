import sys
sys.path.insert(0,'/tmp/claude-0/-home-user-Jworcode/bd265b20-178b-53cd-b91f-fce4cb651aef/scratchpad')
from make_meridian_pdfs import build, L, H, SUB, P, B, N, rule, callout, simple_table, S, TEAL, BLUE, NAVY, RED
from reportlab.platypus import Spacer, Paragraph, PageBreak
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm

OUT='/tmp/claude-0/-home-user-Jworcode/bd265b20-178b-53cd-b91f-fce4cb651aef/scratchpad/'
b=[]

# ---------- PAGE ONE: THE SEPARATION ----------
b+=[L('THE ONE LINE THAT DIVIDES THEM'), rule(),
 callout('<b>Ambrion governs AI. Velocity builds AI. Meridian decides.</b><br/>Three different buyers, arriving with three different questions, in three different rooms.', TEAL),
 Spacer(1,6),
 simple_table(['','MERIDIAN INTELLIGENCE','VELOCITY AI','AMBRION AI'],[
  ['<b>What it sells</b>','A decision','AI capability, built and deployed','AI governance and assurance'],
  ['<b>The buyer&rsquo;s actual question</b>','&ldquo;Should I do this, and what will it cost me if I am wrong?&rdquo;','&ldquo;How do I get AI into this business?&rdquo;','&ldquo;Are we safe, compliant and accountable on AI?&rdquo;'],
  ['<b>Is the buyer thinking about AI?</b>','<b>No.</b> They are thinking about a deal, a valuation, an investor, an audit','Yes. Already decided AI is the question','Yes, and usually because a board or a regulator made them'],
  ['<b>Who they are</b>','Owner, chair, board of a mid-market business facing one high-consequence decision','Executive team committing to an AI programme','Board, audit committee, risk function'],
  ['<b>The room</b>','The room where the decision is made','The room where the programme is built','The boardroom, after the fact'],
  ['<b>Product</b>','Written, decision-grade position. Days, not weeks','Two-phase transformation programme. Months','Frameworks, readiness, EU AI Act, board oversight'],
  ['<b>Verified pricing</b>','Indicative only, see business case','&euro;30,000 + VAT Phase One, 3 months, at &euro;10,000/month (EDelia proposal, June 2026)','UNCONFIRMED'],
  ['<b>Lead / front door</b>','John, personally','Shane','John and Shane jointly'],
  ['<b>Ownership</b>','John 70 / Shane 30','Shane 70 / John 30','UNCONFIRMED'],
  ['<b>Time to value</b>','Days','Months','Weeks to months'],
  ['<b>What it leaves behind</b>','A decision made properly, and the reasoning on file','Built systems, proof points, embedded orchestration','A governance floor that survives audit'],
 ],[30*mm,48*mm,48*mm,46*mm]),
 Spacer(1,8),
 SUB('Read across the top row again'),
 P('The single most important row is &ldquo;is the buyer thinking about AI.&rdquo; Velocity&rsquo;s and Ambrion&rsquo;s buyers are. <b>Meridian&rsquo;s buyer is not.</b>'),
 P('Anthony Hennessy was thinking about gas cylinders. John Lynch was thinking about what his business is worth. Fleming Medical&rsquo;s board was thinking about a capital event. Johnny Shanahan was thinking about a fifty thousand pound investor. United Hardware&rsquo;s ARC was thinking about whether an audit was sound. None of them wanted AI. All of them wanted an answer.'),
 callout('That is why Meridian does not compete with Velocity or Ambrion. It reaches a buyer neither of them can reach, at a moment neither of them is present for.', BLUE, HexColor('#EAF3FB')),
 PageBreak()]

# ---------- MERIDIAN ----------
b+=[L('MERIDIAN INTELLIGENCE &nbsp;&mdash;&nbsp; THE DEFINITION'), rule(),
 P('<b>What it is.</b> A decision intelligence practice. It takes one high-consequence business decision and returns a written, decision-grade position in days, using seven senior domains run simultaneously over the same question, with forty years of board-level judgment as the final gate.'),
 P('<b>It is not an AI company.</b> It is an intelligence practice that operates a governed AI engine. The client buys the answer. The engine room is Meridian&rsquo;s business, not theirs. This was the settled position on 31 July and is reaffirmed here.'),
 SUB('The four situations it is bought for, all evidenced by delivered work'),
 N(1,'<b>A capital event.</b> Raising, selling, taking an investor, choosing an instrument. <i>Barber Republic, Fleming Medical, Arcade Trader.</i>'),
 N(2,'<b>A category or expansion move.</b> Should we enter this, buy this, form this. <i>Stargas cylinder testing, United Hardware paint buying group, United Hardware garden centre.</i>'),
 N(3,'<b>A governance question with teeth.</b> Audit soundness, directors&rsquo; exposure, vendor challenge. <i>United Hardware ARC, 2025 audit review.</i>'),
 N(4,'<b>A proposition that needs verifying before it is backed.</b> <i>UroPharma, Mike Molloy assessment.</i>'),
 Spacer(1,6),
 SUB('The proof, already delivered. Nine engagements, all filed with reasoning intact'),
 simple_table(['Client','Decision','Outcome'],[
  ['Stargas','Enter cylinder testing?','Deep dive, top five supply opportunities, grant aid, branded one-pager'],
  ['United Hardware','Form a paint buying group?','Validation brief, verification pack, location addendum, formal response to Candon&rsquo;s review'],
  ['United Hardware','Buy a standalone garden centre?','Recommendation against, with reasoning'],
  ['United Hardware ARC','Is the 2025 audit sound?','Audit review, Data Transformation board paper, Vendor Challenge Brief'],
  ['Arcade Trader','What is it worth, how do we build value?','Four-domain report, growth model and economics, investment and value-building, full seven-manager report'],
  ['Fleming Medical','Ready for a capital event?','Seven-domain analysis. Corrected an earlier optimistic scoring, found value concentrated in three obscured segments, recommended 18 to 24 months of structural work first, closed with five questions the board must answer'],
  ['Barber Republic','What instrument for Ed Lawton&rsquo;s &pound;50k?','Funding ladder, dilution modelling, two scenarios, rollout roadmap. Converged independently with Shane&rsquo;s own founder documents'],
  ['Export Anatolia','How do we adopt AI?','Seven-manager briefing <i>(note: this one belongs to Velocity)</i>'],
  ['UroPharma / Mike Molloy','Is this real, should John back it?','Preliminary then verified assessment. Recommended hold pending proof'],
 ],[32*mm,44*mm,96*mm]),
 P('Eight of the nine are decision briefs. One, Export Anatolia, is an AI adoption job that should have gone to Velocity. That is the only misplacement in the book, and it is instructive.'),
]

# ---------- VELOCITY ----------
b+=[L('VELOCITY AI &nbsp;&mdash;&nbsp; THE DEFINITION'), rule(),
 P('<b>What it is.</b> The operator. Shane&rsquo;s brand. Builds and deploys AI at scale, in the client&rsquo;s business, alongside the client&rsquo;s team.'),
 P('<b>Its own words, verified from velocityai.ie:</b> &ldquo;We are not consultants. We are operators who build and deploy AI at scale.&rdquo; &ldquo;We diagnose where AI will hit your business first, then we build the response.&rdquo;'),
 P('<b>The offer, verified from the EDelia proposal, June 2026.</b> Phase One, AI-Native Readiness, three months, &euro;30,000 + VAT at &euro;10,000 per month: orchestration engines embedded across the client&rsquo;s core team, two to three proprietary proof points built and branded for the client, a governance baseline, five team sessions and two CEO sessions, readiness diagnostics. Phase Two, AI-Native Build, full architecture and company-wide integration, costed at the end of Phase One.'),
 P('<b>Live front-of-site tools:</b> Strategic Clarity Diagnostic, Live Strategic Simulator, 90-Second Strategic Brief. Four tiers of Migration Education: Leadership Teams, 1-to-1 Decision Makers, Board Advisory, Senior Management.'),
 P('<b>Where it sits against Meridian.</b> Velocity is downstream of a decision already made. The client has decided AI is the answer and needs it built. Meridian is upstream, at the moment the decision itself is still open, and usually about something other than AI.'),
 P('<b>The genuine overlap, and it is narrow.</b> Velocity leads on the word &ldquo;clarity&rdquo; and on &ldquo;we diagnose.&rdquo; That brushes against Meridian. But Velocity diagnoses <i>where AI will hit the business</i>. Meridian diagnoses <i>whether to do the deal</i>. Same verb, different object.'),
]

# ---------- AMBRION ----------
b+=[L('AMBRION AI &nbsp;&mdash;&nbsp; THE DEFINITION'), rule(),
 P('<b>What it is.</b> The AI governance and assurance brand. John Founding and Managing Partner (board-level AI governance, risk, EU AI Act oversight), Shane CEO and Founder (systems and orchestration-layer design). Positioning: &ldquo;Governance at the foundation of AI.&rdquo; Governance built into the foundation of the client organisation, not bolted on as an IT add-on.'),
 P('<b>Three service pillars:</b> Foundational Governance, Board and Executive Advisory, AI Orchestration.'),
 P('<b>Delivered work on record:</b> the United Hardware leadership training programme, Session 1 delivered 25 June 2026 at Citywest, coordinated through Maya Gough, with Skillnet cost offset in play.'),
 P('<b>Where it sits against Meridian.</b> Ambrion answers &ldquo;are we safe and accountable on AI.&rdquo; Meridian answers &ldquo;should we do this.&rdquo; Ambrion&rsquo;s buyer is usually compelled, by a board, a regulator or the EU AI Act. Meridian&rsquo;s buyer is choosing.'),
 callout('<b>UNCONFIRMED and must be settled with Shane:</b> (1) ownership split, Meridian&rsquo;s and Velocity&rsquo;s are on record, Ambrion&rsquo;s is not. (2) Whether Ambrion is actively trading and selling today; the 2 August 2026 anchor has passed. (3) The four to five Ambrion products, an open loop, with the 60-day sales forecast on hold pending it. (4) Whether ambrion.ai and the current positioning still stand.', RED, HexColor('#FBEDEF')),
 PageBreak()]

# ---------- COLLISIONS ----------
b+=[L('WHERE THEY COLLIDE, AND THE FIX'), rule(),
 P('Three collisions. All three are fixable and none of them are structural.'),
 SUB('Collision one, and it is inside Meridian&rsquo;s own materials'),
 P('Meridian&rsquo;s current pricing sheet sells three products, and all three are AI services: AI in Plain English (&euro;4,875 / &euro;6,500), AI Governance Readiness Assessment (&euro;9,000 / &euro;12,000), AI Readiness Accelerator (&euro;13,500 / &euro;18,000). That is Ambrion&rsquo;s pillar one and Velocity&rsquo;s core offer, priced under Meridian&rsquo;s name, and it is the opposite of what Meridian delivered in eight of its nine engagements.'),
 callout('<b>Fix:</b> those three products move to Ambrion. Ambrion is the AI governance brand and readiness assessment is its natural product. Meridian&rsquo;s price list becomes the decision brief and the retained seat. This also fills part of Ambrion&rsquo;s missing product set.', TEAL),
 SUB('Collision two: Meridian&rsquo;s Manager 5, AI Strategy and Adoption'),
 P('As written it claims AI governance frameworks, EU AI Act compliance, readiness assessments and adoption roadmaps. Every one of those is Ambrion or Velocity.'),
 callout('<b>Fix:</b> Manager 5 stays in the engine, comes off the shopfront. Meridian keeps the domain because decisions sometimes touch AI and the analysis needs it. Meridian stops selling it. Export Anatolia-shaped enquiries route to Velocity.', TEAL),
 SUB('Collision three: board and governance advisory is claimed three times'),
 P('Ambrion (Board and Executive Advisory), Meridian (Manager 2, Legal and Governance), Velocity (Board Advisory, The Governance Foundation). A single client could meet all three at the same door.'),
 callout('<b>Fix:</b> Ambrion owns board AI governance outright. Meridian&rsquo;s Manager 2 is scoped to governance <i>inside a decision</i> (directors&rsquo; duties on this transaction, is this audit sound, what is our exposure if we do this). Velocity drops Board Advisory from its education tiers, or renames it to build-side governance. This one needs Shane&rsquo;s agreement and is the hardest of the three.', TEAL),
]

b+=[L('THE REFERRAL FLOW &nbsp;&mdash;&nbsp; THE OVERLAP TURNED INTO A CHANNEL'), rule(),
 P('Once the three doors are separate, each one feeds the others. This is worth money and should be formalised with an agreed fee split.'),
 B('<b>Meridian to Velocity.</b> Meridian sits with owners at the moment of a commercial decision. That room throws off AI need constantly. Every Export Anatolia is a Velocity job introduced at zero acquisition cost.'),
 B('<b>Meridian to Ambrion.</b> Every capital event and audit engagement surfaces a governance gap. Fleming Medical&rsquo;s five board questions are an Ambrion opening.'),
 B('<b>Velocity to Meridian.</b> A client mid-AI-programme hits a commercial, structural or investment decision. Velocity does not sell that. Meridian does.'),
 B('<b>Ambrion to Meridian.</b> A board that has just had its AI governance assessed is a board that trusts the same people with its next real decision.'),
 callout('Three brands, one ecosystem, no cannibalisation. That is the answer to Shane&rsquo;s &ldquo;two people talking about the same thing.&rdquo;', BLUE, HexColor('#EAF3FB')),
 PageBreak()]

# ---------- BUSINESS CASE ----------
b+=[H('THE MERIDIAN BUSINESS CASE'), P('<i>Expanded against Shane&rsquo;s four questions.</i>'), rule(),
 L('1 &nbsp; WHAT IT IS'), rule(HexColor('#D5DDE3'),0.6),
 P('Meridian takes one high-consequence business decision and returns a written, decision-grade position in days, using seven senior domains run simultaneously with forty years of board judgment as the final gate. Not a report. Not a slide deck. A position, with the reasoning attached and the unknowns named.'),
 L('2 &nbsp; WHO IT IS FOR'), rule(HexColor('#D5DDE3'),0.6),
 P('Owners, chairs and boards of Irish and UK mid-market businesses, roughly &euro;5m to &euro;100m turnover, facing a decision worth at least two orders of magnitude more than the fee, in one of the four situations above.'),
 callout('The qualifying question is a single sentence: <i>is there a decision on your desk right now that is too expensive to get wrong and too broad for any one adviser?</i>', BLUE, HexColor('#EAF3FB')),
 L('3 &nbsp; HOW IT MAKES MONEY'), rule(HexColor('#D5DDE3'),0.6),
 P('<b>Line one, the decision brief.</b> Proven nine times. One decision, defined scope, written deliverable, days not weeks. It prices as a unit because it has a boundary. Indicative &euro;3,000 to &euro;15,000 depending on domains engaged and stakes. <i>Indicative only, to be set by John.</i>'),
 P('<b>Line two, the retained decision seat.</b> United Hardware is already this shape without being named as such: multiple decisions across a year, one board, standing access. This is where the durable revenue is because it removes the sell each time. Indicative &euro;4,000 to &euro;8,000 per month covering an agreed brief count plus standing availability. <i>Indicative only.</i>'),
 P('<b>Line three, AI equity and investment (Manager 7).</b> AI capability contributed for equity. Genuinely differentiated, already written into the manager set, and the line that turns Meridian from a fee business into an asset business. Slowest to convert, hardest to sell cold. Treat as line three, not line one.'),
 P('<b>Funding offsets already identified:</b> Skillnet Ireland, Enterprise Ireland Innovation Vouchers up to &euro;5,000.'),
]

b+=[L('4 &nbsp; WHAT IS DEFENSIBLE, AND WHERE THE AI EXPERTISE ACTUALLY SITS'), rule(HexColor('#D5DDE3'),0.6),
 callout('The rarity is not that Meridian knows about AI. It is that Meridian has <b>built and operates a governed multi-domain AI intelligence engine, and a serving PLC chair signs its output.</b> Almost nobody has both halves.', TEAL),
 SUB('Layer one: the parallel-domain method'),
 P('Seven senior domains interrogated simultaneously over the same question, then consolidated into one position. Fleming Medical is the proof: seven domains, eight to ten interrogated questions each, consolidated into an executive brief with five risks, a four-programme recommendation and a human gate. A traditional firm takes weeks and charges multiples. Real advantage today, eroding over eighteen to thirty-six months as others build similar engines. Time-limited, so do not build the whole case on it.'),
 SUB('Layer two, and this is the rare one: the verification discipline'),
 P('Every AI-generated claim is checked against source and labelled verified, estimated or unverified before it reaches a client. Nothing unsourced. Nothing presented as fact that is not. This is already the standing rule and it is visible in the work: the Mike Molloy assessment was held pending proof rather than sold as verified; the Fleming Medical brief corrected Meridian&rsquo;s <i>own</i> earlier optimistic scoring; the Export Anatolia sector description was corrected on record from castings to agricultural machinery parts.'),
 callout('The market is about to be flooded with confident, plausible, unverifiable AI analysis. Meridian&rsquo;s product is analysis a board can rely on and a director can sign against. <b>The discipline is the product. The AI is the engine.</b>', TEAL),
 P('Very few will have this because it is expensive and unglamorous. It requires someone who knows what a board will not accept, and who is willing to slow the machine down and mark a claim unverified when it would read better as fact. That is a governance instinct, not a technical one, and it comes from forty years of sitting where the liability lands.'),
 SUB('Layer three: access that cannot be copied'),
 P('John chairs AHL PLC. He is Independent Non-Executive Director and Chair of the Audit and Risk Committee at United Hardware. Four decades of board relationships across commercial, property, healthcare, governance and capital. This is why Meridian is in the room where the decision is made, not the room where a report is received. A competitor can copy the method in a year. They cannot copy forty years of being trusted by the people who own the decision.'),
 SUB('Layer four, the compounding one: the corpus'),
 P('Nine engagements are filed with their reasoning intact, and every new one adds a decision pattern to a body of Irish and UK mid-market precedent that only Meridian holds. Barber Republic proved its worth directly: Meridian&rsquo;s analysis and Shane&rsquo;s independently written founder documents converged on the same instrument, and that convergence is what gave the recommendation its authority. In three years this corpus is the asset, and it is what makes Meridian saleable rather than merely billable.'),
]

b+=[L('5 &nbsp; CAPACITY'), rule(HexColor('#D5DDE3'),0.6),
 P('The product is a fixed-scope written brief, not open-ended advisory days. The engine does production. John does review and judgment. That is a far higher ceiling than a conventional practice, and it is raised by adding senior reviewers who pressure-test a brief, not by finding another cross-disciplinary synthesiser. Realistic today alongside existing board commitments: <b>eight to twelve briefs a month</b>. At line-one pricing that is a real business before a single retainer is signed.'),
 L('6 &nbsp; WHAT MUST CHANGE, IN ORDER'), rule(HexColor('#D5DDE3'),0.6),
 N(1,'<b>Move the three AI products to Ambrion.</b> Meridian&rsquo;s price list becomes the decision brief and the retained seat.'),
 N(2,'<b>Take Manager 5 off the shopfront.</b> Keep it in the engine.'),
 N(3,'<b>Stop leading on &ldquo;clarity&rdquo; and &ldquo;strategic intelligence.&rdquo;</b> Velocity owns that ground and owns it first. Meridian leads on the decision.'),
 N(4,'<b>Settle board governance ownership with Shane.</b> Ambrion owns it. Meridian&rsquo;s Manager 2 is scoped to governance inside a decision.'),
 N(5,'<b>Formalise the three-way referral with a fee split.</b>'),
 N(6,'<b>Draw the Meridian 70/30 shareholders agreement.</b> Still undrawn.'),
 N(7,'<b>Then launch, and launch on the nine.</b> Real anonymised engagements, not staged samples of unnamed businesses. <i>&ldquo;A gas distributor asked whether to enter cylinder testing. Here is how it was answered in six days.&rdquo;</i> That is the proof Shane asked for and it is already owned. Seek permission to name Stargas, Arcade Trader and Fleming Medical. Handle United Hardware carefully given the board position.'),
 L('7 &nbsp; TEST TARGETS OFFERED BY JOHN, 5 AUGUST 2026'), rule(HexColor('#D5DDE3'),0.6),
 P('Primeline Logistics, Vinny Leonard, DSB Accountants. All three are live-fire tests of the decision brief in front of real businesses, which is precisely what Shane asked for. Vinny is already warm through Fleming Medical. <b>Run these after the definition above is agreed, not before</b>, so each one proves the proposition rather than adding another undefined engagement to the book.'),
]

b+=[L('THE FIVE SENTENCES'), rule(),
 callout('<b>What it is.</b> Meridian takes one high-consequence business decision and returns a written, decision-grade position in days, using seven senior domains run simultaneously with forty years of board judgment as the final gate.', TEAL),
 callout('<b>Who it is for.</b> Owners, chairs and boards of Irish and UK mid-market businesses facing a capital event, an expansion move, a governance question with teeth, or a proposition that needs verifying before it is backed.', TEAL),
 callout('<b>How it makes money.</b> Fixed-scope decision briefs, retained decision seats, and AI-for-equity structures.', TEAL),
 callout('<b>Why it is defensible.</b> A verification discipline almost nobody will match, board-level access nobody can copy, and a compounding corpus of decision precedent only Meridian holds.', TEAL),
 callout('<b>How it differs.</b> Ambrion governs AI. Velocity builds AI. Meridian decides. Meridian&rsquo;s buyer is not thinking about AI at all.', BLUE, HexColor('#EAF3FB')),
 Spacer(1,10), rule(HexColor('#D5DDE3'),0.6),
 Paragraph('Meridian Intelligence &middot; Definition and business case &middot; 5 August 2026 &middot; Private and confidential. Every Meridian claim is drawn from delivered work filed in the Meridian repository. Velocity positioning verified from velocityai.ie and the EDelia proposal, June 2026. Ambrion items marked UNCONFIRMED require Shane&rsquo;s input before external use. Pricing marked indicative is not yet set.', S['foot']),
]

build(OUT+'Meridian_Velocity_Ambrion_Definition_and_Business_Case.pdf','Meridian, Velocity, Ambrion',
      'Three Businesses, Three Front Doors, One Portfolio',
      ['Answering Shane McCarthy&rsquo;s challenge of 4 August 2026',
       'Decision taken by John, 5 August 2026: Meridian is the decision brief'],
      'PRIVATE AND CONFIDENTIAL', b, 'Definition and Business Case')
print('DONE')
