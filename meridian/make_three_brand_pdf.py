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
 callout('<b>Ambrion makes you compliant. Velocity makes you capable. Meridian makes the call.</b><br/>Three different buyers, three different questions, three different rooms. Only one of them is a choice. Ambrion&rsquo;s buyer is compelled by law. Velocity&rsquo;s buyer has already decided AI is the answer. Meridian&rsquo;s buyer is standing in front of an open decision that has nothing to do with AI.', TEAL),
 Spacer(1,6),
 simple_table(['','MERIDIAN INTELLIGENCE','VELOCITY AI','AMBRION AI'],[
  ['<b>What it is</b>','Executive intelligence practice','AI operator and builder','AI strategy, architecture and governance firm'],
  ['<b>What it sells</b>','A decision','AI capability, built and deployed','Done-for-you EU AI Act compliance, tiered'],
  ['<b>The buyer&rsquo;s actual question</b>','&ldquo;Should I do this, and what will it cost me if I am wrong?&rdquo;','&ldquo;How do I get AI into this business?&rdquo;','&ldquo;The EU AI Act applies to us now. Are we compliant?&rdquo;'],
  ['<b>Is the buyer thinking about AI?</b>','<b>No.</b> They are thinking about a deal, a valuation, an investor, an audit','Yes. Already decided AI is the question','Yes, and usually because the law made them'],
  ['<b>Who they are</b>','Owner, chair, board of a mid-market business facing one high-consequence decision','Executive team committing to an AI programme','Irish SME owners and boards inside EU AI Act scope'],
  ['<b>The room</b>','The room where the decision is made','The room where the programme is built','The compliance and board oversight conversation'],
  ['<b>Product</b>','Written, decision-grade position. Days, not weeks','Two-phase transformation programme. Months','Tiered done-for-you compliance, plus executive AI training'],
  ['<b>Verified pricing</b>','Indicative only, see business case','&euro;30,000 + VAT Phase One, 3 months, at &euro;10,000/month (EDelia, June 2026)','Tiered. Rates not yet on record'],
  ['<b>Lead / front door</b>','John, personally','Shane','Shane CEO and architect. John commercial and governance lead'],
  ['<b>Ownership</b>','John 70 / Shane 30','Shane 70 / John 30','Shane 60 / John 30 / Pat McGrath 10'],
  ['<b>Legal entity</b>','To be formalised','Mainly Velocity Limited, t/a Velocity AI','Incorporation in progress'],
  ['<b>Generating income?</b>','Fee income from delivered briefs','Yes','Not yet. Compliance campaign now live'],
  ['<b>Route to market</b>','John&rsquo;s board relationships, direct','Direct, plus site diagnostics','Smacht network, c.300 Irish SMEs via Padraic O&rsquo;Maille. Accountants and solicitors as referral partners. UHL training'],
  ['<b>Time to value</b>','Days','Months','Weeks to months'],
  ['<b>Portfolio priority</b>','John-led. Fee revenue in days, and the upstream feeder to both others','Shane-led build arm','Statutory timing. The EU AI Act makes now its moment'],
  ['<b>What it leaves behind</b>','A decision made properly, and the reasoning on file','Built systems, proof points, embedded orchestration','A compliance position that survives regulatory scrutiny'],
 ],[30*mm,48*mm,48*mm,46*mm]),
 Spacer(1,8),
 SUB('Read across the top row again'),
 P('The single most important row is &ldquo;is the buyer thinking about AI.&rdquo; Velocity&rsquo;s and Ambrion&rsquo;s buyers are. <b>Meridian&rsquo;s buyer is not.</b>'),
 P('Anthony Hennessy was thinking about gas cylinders. John Lynch was thinking about what his business is worth. Fleming Medical&rsquo;s board was thinking about a capital event. Johnny Shanahan was thinking about a fifty thousand pound investor. United Hardware&rsquo;s ARC was thinking about whether an audit was sound. None of them wanted AI. All of them wanted an answer.'),
 callout('That is why Meridian does not compete with Velocity or Ambrion. It reaches a buyer neither of them can reach, at a moment neither of them is present for.', BLUE, HexColor('#EAF3FB')),
 PageBreak()]

# ---------- MERIDIAN ----------
b+=[L('MERIDIAN INTELLIGENCE &nbsp;&mdash;&nbsp; THE DEFINITION'), rule(),
 P('<b>What it is.</b> An <b>executive intelligence practice</b>. Its product is the decision brief. It takes one high-consequence business decision and returns a written, decision-grade position in days, using seven senior domains run simultaneously over the same question, with forty years of board-level judgment as the final gate.'),
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
 P('<i>Verified from the Ambrion AI Briefing Note prepared for this session, 5 August 2026.</i>'),
 P('<b>What it is.</b> An Irish intelligence and advisory firm specialising in AI strategy, architecture and governance. Founded by Shane McCarthy (CEO, Founder, AI Architect, Systems Builder) and John Webb O&rsquo;Rourke (commercial and governance lead). Ambrion helps organisations integrate AI into their foundational operating models rather than treating it as a superficial add-on.'),
 SUB('Three core beliefs'),
 B('<b>Built-in, not bolt-on.</b> AI must be designed into an organisation&rsquo;s core data pipelines, decision rights and workflows, not added as an extra software tool.'),
 B('<b>Governance as an enabler.</b> Proper governance provides the safety rails and accountability required to scale AI safely without risking client trust or data integrity.'),
 B('<b>Human judgment.</b> Systems propose options and patterns. Humans retain final decision-making authority.'),
 Spacer(1,4),
 P('<b>Current commercial focus.</b> A <b>tiered, done-for-you EU AI Act compliance offering for Irish SMEs</b>, positioned deliberately against software-only compliance platforms. The EU AI Act applies in full from 2 August 2026, which makes this immediately live and time-critical.'),
 P('<b>Route to market.</b> The Smacht network, roughly 300 Irish SMEs, via Padraic O&rsquo;Maille. Professional referral partners, specifically accountants and solicitors. The United Hardware senior executive AI training programme, with a second course being scheduled for August 2026.'),
 P('<b>Live opportunity.</b> Oifig IS na hEireann, the AI Office of Ireland, launched this week as Ireland&rsquo;s independent central coordinating authority for EU AI Act implementation, led by CEO Paul Byrne alongside Ministers Peter Burke and Niamh Smyth. The Office has explicitly flagged stakeholder engagement as a priority. This is a genuine opening for Ambrion as a practitioner voice rather than a cold approach. John and Shane are exploring LinkedIn engagement followed by a direct introduction.'),
 callout('<b>Status.</b> The 2 August 2026 anchor is <b>now active</b>, not passed: it was the compliance campaign launch date. Live outreach in progress, including Glennon Brothers.', TEAL),
 P('<i>Note on a superseded line. The Ambrion briefing describes Ambrion as John&rsquo;s primary revenue vehicle for the next three years. <b>John has confirmed that reference predates Meridian&rsquo;s conception and no longer holds.</b> It is recorded here for accuracy and should not be read as the current portfolio position. There is no single primary vehicle. There are three complementary businesses reaching three different buyers.</i>'),
 P('<b>Where it sits against Meridian.</b> Ambrion answers &ldquo;the law now applies to us, are we compliant.&rdquo; Meridian answers &ldquo;should we do this.&rdquo; Ambrion&rsquo;s buyer is compelled by regulation. Meridian&rsquo;s buyer is choosing. Ambrion sells a programme with a statutory driver behind it. Meridian sells a single answer to a single question.'),
 SUB('Ownership and structure, confirmed by John, 5 August 2026'),
 P('<b>Ownership: Shane McCarthy 60, John Webb O&rsquo;Rourke 30, Pat McGrath 10.</b>'),
 P('<b>Ambrion will have its own company shortly, and the United Hardware arrangement changes with it.</b> The Velocity routing on that training was a practical bridge because there was nothing else to contract through at the time, not a settled arrangement.'),
 callout('The only thing worth carrying forward is a single instruction for the incorporation itself: <b>record the 60/30/10 in the constitution and the share register at formation.</b> Splits agreed verbally between people who trust each other are the ones remembered differently three years later, and Pat McGrath&rsquo;s 10 per cent in particular needs a documented home. That is housekeeping, not a warning.', TEAL),
 P('There is a second reason the timing matters, and it is practical rather than governance-related: <b>no grant agency will register Ambrion without a CRO number and tax clearance.</b> Skillnet, the LEO panels and Enterprise Ireland are all closed to it until the company exists. Given the compliance campaign is live now and Skillnet is Ambrion&rsquo;s genuine revenue channel, incorporation is on the critical path to funding, not just to tidiness.'),
 P('<b>What this does not change.</b> The strategic separation stands, and arguably strengthens. Ambrion has the statutory driver, the campaign, the channel and the moment. The EU AI Act coming into full application on 2 August is exactly the event that turns it from governance work into income. The point is simply that the vehicle needs to exist before the money starts arriving, not after.'),
 PageBreak()]

# ---------- COLLISIONS ----------
b+=[L('WHERE THEY COLLIDE, AND THE FIX'), rule(),
 P('Three collisions. All three are fixable and none of them are structural.'),
 SUB('Collision one, and it is inside Meridian&rsquo;s own materials'),
 P('Meridian&rsquo;s current pricing sheet sells three products, and all three are AI services: AI in Plain English (&euro;4,875 / &euro;6,500), AI Governance Readiness Assessment (&euro;9,000 / &euro;12,000), AI Readiness Accelerator (&euro;13,500 / &euro;18,000). That is Ambrion&rsquo;s pillar one and Velocity&rsquo;s core offer, priced under Meridian&rsquo;s name, and it is the opposite of what Meridian delivered in eight of its nine engagements.'),
 callout('<b>Fix: those three products move to Ambrion, and the Ambrion briefing settles it beyond argument.</b> Ambrion&rsquo;s live campaign is a tiered done-for-you EU AI Act compliance offering for Irish SMEs. An AI Governance Readiness Assessment is not merely adjacent to that, it <i>is</i> a tier of it. AI in Plain English is the natural top-of-funnel for the Smacht network and the accountant and solicitor channel. The AI Readiness Accelerator is the delivery tier. Three products sitting under the wrong brand, with a ready-built route to market waiting for them under the right one.', TEAL),
 SUB('Collision two: Meridian&rsquo;s Manager 5, AI Strategy and Adoption'),
 P('As written it claims AI governance frameworks, EU AI Act compliance, readiness assessments and adoption roadmaps. Every one of those is Ambrion or Velocity.'),
 callout('<b>Fix:</b> Manager 5 stays in the engine, comes off the shopfront. Meridian keeps the domain because decisions sometimes touch AI and the analysis needs it. Meridian stops selling it. Export Anatolia-shaped enquiries route to Velocity.', TEAL),
 SUB('Collision three: board and governance advisory is claimed three times'),
 P('Ambrion (Board and Executive Advisory), Meridian (Manager 2, Legal and Governance), Velocity (Board Advisory, The Governance Foundation). A single client could meet all three at the same door.'),
 callout('<b>Fix: Ambrion owns board AI governance outright, and the briefing makes this the obvious answer.</b> Ambrion is the EU AI Act vehicle with a statutory driver, a live campaign, a named channel and a direct line forming to the AI Office of Ireland. Nothing else in the portfolio should reach for that ground. Meridian&rsquo;s Manager 2 is scoped to governance <i>inside a decision</i> (directors&rsquo; duties on this transaction, is this audit sound, what is our exposure if we do this). Velocity drops Board Advisory from its education tiers, or renames it to build-side governance. This one needs Shane&rsquo;s agreement and is the hardest of the three.', TEAL),
]

b+=[L('THE REFERRAL FLOW &nbsp;&mdash;&nbsp; THE OVERLAP TURNED INTO A CHANNEL'), rule(),
 P('Once the three doors are separate, each one feeds the others. This is worth money and should be formalised with an agreed fee split.'),
 B('<b>Meridian to Velocity.</b> Meridian sits with owners at the moment of a commercial decision. That room throws off AI need constantly. Every Export Anatolia is a Velocity job introduced at zero acquisition cost.'),
 B('<b>Meridian to Ambrion.</b> Meridian sits with owners and boards at the moment of a major decision, which is precisely the moment an EU AI Act exposure becomes visible and uncomfortable. Fleming Medical&rsquo;s five board questions are an Ambrion opening. <b>Meridian&rsquo;s highest-value output may not be its own fee. It is qualified, warm, board-level access for Ambrion at the moment the buyer is most receptive.</b>'),
 B('<b>Velocity to Meridian.</b> A client mid-AI-programme hits a commercial, structural or investment decision. Velocity does not sell that. Meridian does.'),
 B('<b>Ambrion to Meridian.</b> A board that has just had its AI compliance handled is a board that trusts the same people with its next real decision. The Smacht network alone is roughly 300 Irish SMEs, and the accountant and solicitor referral partners are exactly the professionals who see a client&rsquo;s big decisions coming before anyone else does.'),
 callout('Three brands, one ecosystem, no cannibalisation. That is the answer to Shane&rsquo;s &ldquo;two people talking about the same thing.&rdquo;', BLUE, HexColor('#EAF3FB')),
 SUB('The portfolio order'),
 P('There is no single primary vehicle. The Ambrion briefing&rsquo;s three-year primary-revenue line predates Meridian and John has confirmed it no longer holds. What that leaves is cleaner than a hierarchy: <b>three businesses, three buyers, three different clocks.</b>'),
 B('<b>Ambrion has the timing.</b> The EU AI Act came into full application on 2 August. A statutory event, a compliance campaign behind it, a named channel of roughly 300 SMEs, and a window that will not stay open indefinitely. Its moment is now and it should be run hard while the moment lasts.'),
 B('<b>Meridian has the margin and the speed.</b> Fee revenue in days rather than months, no build cost, no delivery team, a product already proven nine times. It also has the only buyer of the three who is not thinking about AI, which means it is the only one whose market does not shrink when the AI conversation matures.'),
 B('<b>Velocity has the depth.</b> Longer engagements, higher contract values, and the build capability the other two both need to point at.'),
 P('They reinforce rather than rank. Meridian&rsquo;s engagements put John in the room where EU AI Act exposure becomes visible, which feeds Ambrion. Ambrion&rsquo;s compliance clients hit commercial decisions, which feeds Meridian. Both feed Velocity when something needs building.'),
 callout('<b>The practical consequence for Meridian&rsquo;s business case: it stands on its own.</b> It does not need to be justified as a feeder for something else, and it should not be sequenced behind anything. It needs a defined offer, a price list and a front door, which is what the rest of this document sets out.', BLUE, HexColor('#EAF3FB')),
 PageBreak()]

# ---------- BUSINESS CASE ----------
b+=[H('THE MERIDIAN BUSINESS CASE'), P('<i>Expanded against Shane&rsquo;s four questions.</i>'), rule(),
 L('1 &nbsp; WHAT IT IS'), rule(HexColor('#D5DDE3'),0.6),
 P('<b>Meridian is an executive intelligence practice.</b> Its product is the decision brief: one high-consequence business decision, answered with a written, decision-grade position in days, using seven senior domains run simultaneously with forty years of board judgment as the final gate. Not a report. Not a slide deck. A position, with the reasoning attached and the unknowns named.'), P('Note the shape of the sentence, because it is the whole argument. <i>Practice</i> is what it is. <i>The decision brief</i> is what it sells. AI appears in neither, and that is deliberate.'),
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
 N(6,'<b>Complete the Ambrion incorporation with the 60/30/10 recorded at formation</b>, and draw the Meridian 70/30 shareholders agreement. Both are in train. The practical driver on Ambrion is that no grant agency can register it without a CRO number, and Skillnet is its real revenue channel.'),
 N(7,'<b>Then launch, and launch on the nine.</b> Real anonymised engagements, not staged samples of unnamed businesses. <i>&ldquo;A gas distributor asked whether to enter cylinder testing. Here is how it was answered in six days.&rdquo;</i> That is the proof Shane asked for and it is already owned. Seek permission to name Stargas, Arcade Trader and Fleming Medical. Handle United Hardware carefully given the board position.'),
 L('7 &nbsp; TEST TARGETS OFFERED BY JOHN, 5 AUGUST 2026'), rule(HexColor('#D5DDE3'),0.6),
 P('Primeline Logistics, Vinny Leonard, DSB Accountants. All three are live-fire tests of the decision brief in front of real businesses, which is precisely what Shane asked for. Vinny is already warm through Fleming Medical. <b>Run these after the definition above is agreed, not before</b>, so each one proves the proposition rather than adding another undefined engagement to the book.'), P('<b>DSB Accountants is a double play and should be run deliberately as one.</b> Ambrion&rsquo;s stated referral channel is accountants and solicitors. So DSB is simultaneously a Meridian decision-brief prospect and an Ambrion referral-partner prospect. Approach it as one conversation with two doors: Meridian demonstrates the calibre of thinking on a live decision, and that same demonstration is the credential that makes DSB comfortable referring its own client base into Ambrion&rsquo;s EU AI Act offering. That is the referral flow above, proven on a single account.'),
]

b+=[L('THE FIVE SENTENCES'), rule(),
 callout('<b>What it is.</b> Meridian is an executive intelligence practice. It takes one high-consequence business decision and returns a written, decision-grade position in days, using seven senior domains run simultaneously with forty years of board judgment as the final gate.', TEAL),
 callout('<b>Who it is for.</b> Owners, chairs and boards of Irish and UK mid-market businesses facing a capital event, an expansion move, a governance question with teeth, or a proposition that needs verifying before it is backed.', TEAL),
 callout('<b>How it makes money.</b> Fixed-scope decision briefs, retained decision seats, and AI-for-equity structures.', TEAL),
 callout('<b>Why it is defensible.</b> A verification discipline almost nobody will match, board-level access nobody can copy, and a compounding corpus of decision precedent only Meridian holds.', TEAL),
 callout('<b>How it differs.</b> Ambrion makes you compliant. Velocity makes you capable. Meridian makes the call. Ambrion&rsquo;s buyer is compelled by law, Velocity&rsquo;s has already chosen AI, and Meridian&rsquo;s is not thinking about AI at all.', BLUE, HexColor('#EAF3FB')),
 Spacer(1,10), rule(HexColor('#D5DDE3'),0.6),
 Paragraph('Meridian Intelligence &middot; Definition and business case &middot; 5 August 2026 &middot; Private and confidential. Every Meridian claim is drawn from delivered work filed in the Meridian repository. Velocity positioning verified from velocityai.ie and the EDelia proposal, June 2026. Ambrion verified from the Ambrion AI Briefing Note, 5 August 2026. Ambrion ownership, trading status and absence of a legal entity confirmed by John, 5 August 2026. Meridian pricing marked indicative is not yet set.', S['foot']),
]

build(OUT+'Meridian_Velocity_Ambrion_Definition_and_Business_Case.pdf','Meridian, Velocity, Ambrion',
      'Three Businesses, Three Front Doors, One Portfolio',
      ['Answering Shane McCarthy&rsquo;s challenge of 4 August 2026',
       'Decision taken by John, 5 August 2026: Meridian is the decision brief'],
      'PRIVATE AND CONFIDENTIAL', b, 'Definition and Business Case')
print('DONE')
