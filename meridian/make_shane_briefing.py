import sys
sys.path.insert(0,'/tmp/claude-0/-home-user-Jworcode/bd265b20-178b-53cd-b91f-fce4cb651aef/scratchpad')
from make_meridian_pdfs import build, L, H, SUB, P, B, N, rule, callout, simple_table, S, TEAL, BLUE, NAVY, RED
from reportlab.platypus import Spacer, Paragraph, PageBreak
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm

OUT='/tmp/claude-0/-home-user-Jworcode/bd265b20-178b-53cd-b91f-fce4cb651aef/scratchpad/'
b=[]

# ---------------- 1. THE ANSWER ----------------
b+=[L('WHY THIS DOCUMENT'), rule(),
 P('Shane, you asked me four questions and told me not to come back with a launch plan until I could answer them. You were right to. I had asked you for tactics before I had given you a definition, and that was my sequencing error, not yours.'),
 P('This is the answer. It is short on ambition and long on specifics, which is the way round it should be.'),
 P('One correction to the challenge itself, offered without argument. The system has been put in front of people. Nine engagements, real businesses, real decisions, real money, all filed with their reasoning intact. What we never did was name what happened when we did it. That was the actual gap, and it was ours.'),
 L('YOUR FOUR QUESTIONS, IN FOUR SENTENCES'), rule(),
 callout('<b>What it is.</b> Meridian is an executive intelligence practice. It takes one high-consequence business decision and returns a written, decision-grade position in days, using seven senior domains run simultaneously with forty years of board judgment as the final gate.', TEAL),
 callout('<b>Who it is for.</b> Owners, chairs and boards of Irish and UK mid-market businesses facing a capital event, an expansion move, a governance question with teeth, or a proposition that needs verifying before it is backed.', TEAL),
 callout('<b>How it makes money.</b> Fixed-scope decision briefs, retained decision seats, and AI-for-equity structures. Full fee ladder at the back of this document.', TEAL),
 callout('<b>Why it is defensible.</b> A verification discipline almost nobody will match, board-level access nobody can copy, and a compounding corpus of decision precedent only Meridian holds.', TEAL),
 callout('<b>And the fifth question you did not ask out loud.</b> Ambrion makes you compliant. Velocity makes you capable. Meridian makes the call. Meridian&rsquo;s buyer is not thinking about AI at all.', BLUE, HexColor('#EAF3FB')),
 PageBreak()]

# ---------------- 2. EVIDENCE ----------------
b+=[L('THE EVIDENCE, BEFORE THE ARGUMENT'), rule(),
 P('The definition was already sitting inside the work. It had just never been written down.'),
 simple_table(['Client','The decision they faced','What was delivered'],[
  ['Stargas','Enter cylinder testing?','Deep dive, top five core supply opportunities, grant aid intelligence, branded one-pager'],
  ['United Hardware','Form a paint buying group?','Validation brief, verification pack, location addendum, formal response to Paul Candon&rsquo;s review'],
  ['United Hardware','Buy a standalone garden centre?','Recommendation against, with reasoning'],
  ['United Hardware ARC','Is the 2025 audit sound?','Audit review, Data Transformation board paper, Vendor Challenge Brief'],
  ['Arcade Trader','What is it worth, how do we build value?','Four-domain consolidated report, growth model and economics, investment and value-building analysis'],
  ['Fleming Medical','Are we ready for a capital event?','Seven-domain analysis. Corrected an earlier optimistic scoring, found value concentrated in three obscured segments, recommended 18 to 24 months of structural work first, closed with five questions the board must answer'],
  ['Barber Republic','What instrument for a &pound;50k investor?','Funding ladder, dilution modelling across rounds, two scenarios, instrument recommendation. Converged independently with your own founder documents'],
  ['Export Anatolia','How do we adopt AI?','Seven-manager briefing. <i>This one was a Velocity job and should have gone to you</i>'],
  ['UroPharma / Mike Molloy','Is this real, should John back it?','Preliminary then verified assessment. Recommended hold pending proof'],
 ],[30*mm,40*mm,102*mm]),
 SUB('The pattern nobody wrote down'),
 P('Read that table again and one thing is true of every row. <b>Not one of those clients came with an AI question.</b> Eight of the nine were not thinking about AI at all. Anthony Hennessy was thinking about gas cylinders. John Lynch was thinking about what his business is worth. Fleming Medical&rsquo;s board was thinking about a capital event. Johnny Shanahan was thinking about a fifty thousand pound investor.'),
 callout('They came with <b>a decision they could not make alone and could not afford to get wrong.</b> And every time, the same thing happened: seven domains at one decision simultaneously, a written position back in days, with a human gate at the end. That is the business. It has been the business since Arcade Trader.', TEAL),
 PageBreak()]

# ---------------- 3. THE THREE ----------------
b+=[L('THE THREE, SIDE BY SIDE'), rule(),
 callout('<b>Ambrion makes you compliant. Velocity makes you capable. Meridian makes the call.</b><br/>Three buyers, three questions, three rooms. Only one of them is a choice. Ambrion&rsquo;s buyer is compelled by law. Velocity&rsquo;s buyer has already decided AI is the answer. Meridian&rsquo;s buyer is standing in front of an open decision that has nothing to do with AI.', TEAL),
 Spacer(1,4),
 simple_table(['','MERIDIAN','VELOCITY','AMBRION'],[
  ['<b>What it is</b>','Executive intelligence practice','AI operator and builder','AI strategy, architecture and governance firm'],
  ['<b>What it sells</b>','A decision','AI capability, built and deployed','Done-for-you EU AI Act compliance, tiered'],
  ['<b>The buyer&rsquo;s question</b>','&ldquo;Should I do this, and what does it cost me if I am wrong?&rdquo;','&ldquo;How do I get AI into this business?&rdquo;','&ldquo;The EU AI Act applies to us now. Are we compliant?&rdquo;'],
  ['<b>Thinking about AI?</b>','<b>No.</b> Thinking about a deal, a valuation, an investor, an audit','Yes. Already decided','Yes, because the law made them'],
  ['<b>Who they are</b>','Owner, chair, board of a mid-market business facing one high-consequence decision','Executive team committing to an AI programme','Irish SME owners and boards inside EU AI Act scope'],
  ['<b>Product</b>','Written, decision-grade position. Days','Two-phase transformation programme. Months','Tiered compliance, plus executive AI training'],
  ['<b>Pricing</b>','Brief &euro;4,950, Review &euro;24,500, Transaction &euro;35,000, retained from &euro;4,500/mth','&euro;30,000 + VAT Phase One over 3 months','Tiered. Rates not yet set'],
  ['<b>Front door</b>','John, personally','Shane','Shane CEO and architect. John commercial and governance'],
  ['<b>Ownership</b>','John 70 / Shane 30','Shane 70 / John 30','Shane 60 / John 30 / Pat McGrath 10'],
  ['<b>Route to market</b>','John&rsquo;s board relationships, direct','Direct, plus site diagnostics','Smacht network c.300 SMEs, accountants and solicitors, UHL training'],
  ['<b>Time to value</b>','Days','Months','Weeks to months'],
  ['<b>What it leaves behind</b>','A decision made properly, and the reasoning on file','Built systems, proof points, embedded orchestration','A compliance position that survives scrutiny'],
 ],[27*mm,42*mm,42*mm,41*mm]),
 Spacer(1,6),
 P('<b>The row that matters is &ldquo;thinking about AI.&rdquo;</b> Velocity&rsquo;s and Ambrion&rsquo;s buyers are. Meridian&rsquo;s is not. That is why Meridian does not compete with either of you. It reaches a buyer neither of you can reach, at a moment neither of you is present for.'),
 PageBreak()]

# ---------------- 4. EACH IN TURN ----------------
b+=[L('MERIDIAN INTELLIGENCE'), rule(),
 P('<b>An executive intelligence practice.</b> Its product is the decision brief. One high-consequence decision, seven senior domains run simultaneously, a written position in days, John&rsquo;s judgment as the final gate.'),
 P('<b>It is not an AI company and will not be positioned as one.</b> It is a practice that operates a governed AI engine. The client buys the answer. The engine room is our business, not theirs.'),
 P('<b>Bought for four situations:</b> a capital event; a category or expansion move; a governance question with teeth; a proposition that needs verifying before it is backed. All four are evidenced in the table above.'),
 L('VELOCITY AI'), rule(),
 P('<b>The operator.</b> Builds and deploys AI at scale, in the client&rsquo;s business, alongside the client&rsquo;s team. Your words from the site: &ldquo;We are not consultants. We are operators who build and deploy AI at scale.&rdquo;'),
 P('<b>The offer, from the EDelia proposal.</b> Phase One, AI-Native Readiness, three months at &euro;10,000 per month: orchestration engines embedded, two to three branded proof points, a governance baseline, five team sessions and two CEO sessions. Phase Two costed at the end of Phase One.'),
 P('<b>Against Meridian.</b> Velocity is downstream of a decision already made. The client has decided AI is the answer and needs it built. Meridian is upstream, while the decision is still open, and usually about something else entirely.'),
 L('AMBRION AI'), rule(),
 P('<b>The AI governance and assurance brand.</b> An Irish intelligence and advisory firm in AI strategy, architecture and governance. Built-in not bolt-on; governance as an enabler; human judgment retains final authority.'),
 P('<b>Current commercial focus.</b> A tiered, done-for-you EU AI Act compliance offering for Irish SMEs, positioned against software-only compliance platforms. Full application from 2 August makes it live and time-critical.'),
 P('<b>Route to market.</b> Smacht network, roughly 300 Irish SMEs via Padraic O&rsquo;Maille. Accountants and solicitors as referral partners. The UHL senior executive training, second course scheduling for August.'),
 P('<b>Against Meridian.</b> Ambrion answers &ldquo;the law now applies to us, are we compliant.&rdquo; Meridian answers &ldquo;should we do this.&rdquo; Ambrion&rsquo;s buyer is compelled. Meridian&rsquo;s is choosing.'),
 SUB('On portfolio priority'),
 P('The Ambrion briefing describes it as John&rsquo;s primary revenue vehicle for three years. That line predates Meridian and John has confirmed it no longer holds. <b>There is no single primary vehicle.</b> Ambrion has the timing, because the EU AI Act window will not stay open indefinitely. Meridian has the margin and the speed, and the only buyer of the three whose market does not shrink when the AI conversation matures. Velocity has the depth. They reinforce rather than rank.'),
 PageBreak()]

# ---------------- 5. COLLISIONS ----------------
b+=[L('WHERE WE COLLIDE, AND THE THREE FIXES'), rule(),
 P('You said we cannot have two people talking about the same thing in the same way in different businesses. Agreed. There are exactly three places where that is currently true, and all three are fixable. <b>Each one needs your agreement, not just mine.</b>'),
 SUB('Collision one: Meridian&rsquo;s own price list sells AI'),
 P('The current Meridian sheet lists three products and all three are AI services: AI in Plain English (&euro;6,500), AI Governance Readiness Assessment (&euro;12,000), AI Readiness Accelerator (&euro;18,000).'),
 callout('<b>Fix: all three move to Ambrion.</b> Ambrion&rsquo;s live campaign is tiered EU AI Act compliance for Irish SMEs. A readiness assessment is not adjacent to that, it <i>is</i> a tier of it. AI in Plain English is the natural top-of-funnel for the Smacht network and the accountant and solicitor channel. The Accelerator is the delivery tier. Good products under the wrong brand, with a ready-built route to market waiting under the right one.', TEAL),
 SUB('Collision two: Meridian&rsquo;s Manager 5, AI Strategy and Adoption'),
 P('As written it claims AI governance frameworks, EU AI Act compliance, readiness assessments and adoption roadmaps. Every one of those is yours.'),
 callout('<b>Fix: Manager 5 stays in the engine, comes off the shopfront.</b> Meridian keeps the domain because decisions sometimes touch AI. Meridian stops selling it. Export Anatolia-shaped enquiries route to Velocity.', TEAL),
 SUB('Collision three: board governance is claimed three times'),
 P('Ambrion (Board and Executive Advisory), Meridian (Manager 2, Legal and Governance), Velocity (Board Advisory, The Governance Foundation). A single client could meet all three at the same door.'),
 callout('<b>Fix: Ambrion owns board AI governance outright.</b> It has the statutory driver, the live campaign, the named channel and a direct line forming to the AI Office of Ireland. Meridian&rsquo;s Manager 2 is scoped to governance <i>inside a decision</i>: directors&rsquo; duties on this transaction, is this audit sound, what is our exposure if we do this. <b>Velocity drops Board Advisory from its education tiers, or renames it to build-side governance.</b> This is the hardest of the three and it is the one I most need you to weigh in on.', RED, HexColor('#FBEDEF')),
 P('<b>And one on language.</b> Velocity leads on &ldquo;clarity&rdquo; and &ldquo;strategic intelligence,&rdquo; and owns that ground first. Meridian will stop reaching for it and will lead on the decision instead.'),
 PageBreak()]

# ---------------- 6. REFERRAL ----------------
b+=[L('THE OVERLAP TURNED INTO A CHANNEL'), rule(),
 P('Once the three doors are separate, each one feeds the others. This is worth money and should be formalised with an agreed fee split.'),
 B('<b>Meridian to Velocity.</b> Meridian sits with owners at the moment of a commercial decision, and that room throws off AI need constantly. Every Export Anatolia is a Velocity job introduced at zero acquisition cost.'),
 B('<b>Meridian to Ambrion.</b> Every capital event and audit engagement surfaces a governance gap. Fleming Medical&rsquo;s five board questions are an Ambrion opening.'),
 B('<b>Velocity to Meridian.</b> A client mid-programme hits a commercial, structural or investment decision. Velocity does not sell that. Meridian does.'),
 B('<b>Ambrion to Meridian.</b> A board that has just had its compliance handled trusts the same people with its next real decision. The accountant and solicitor partners are exactly the professionals who see a client&rsquo;s big decisions coming first.'),
 callout('Three brands, one ecosystem, no cannibalisation. That is the answer to the challenge.', BLUE, HexColor('#EAF3FB')),
 L('WHY IT IS DEFENSIBLE, AND WHERE THE AI EXPERTISE SITS'), rule(),
 callout('The rarity is not that Meridian knows about AI. It is that Meridian has <b>built and operates a governed multi-domain AI intelligence engine, and a serving PLC chair signs its output.</b> Almost nobody has both halves.', TEAL),
 SUB('Layer one: the parallel-domain method'),
 P('Seven domains interrogated simultaneously, then consolidated. Fleming Medical is the proof. Real advantage today, eroding over eighteen to thirty-six months as others build similar engines. Time-limited, so the case does not rest on it.'),
 SUB('Layer two, the rare one: the verification discipline'),
 P('Every AI-generated claim checked against source and labelled verified, estimated or unverified before it reaches a client. Visible in the work: Mike Molloy held pending proof rather than sold as verified; the Fleming Medical brief corrected Meridian&rsquo;s <i>own</i> earlier optimistic scoring; the Export Anatolia sector description corrected on record from castings to agricultural machinery parts.'),
 callout('The market is about to fill with confident, plausible, unverifiable AI analysis. Meridian&rsquo;s product is analysis a board can rely on and a director can sign against. <b>The discipline is the product. The AI is the engine.</b>', TEAL),
 SUB('Layer three: access that cannot be copied'),
 P('Chair of AHL PLC. Independent Non-Executive Director and Chair of the Audit and Risk Committee at United Hardware. Four decades of board relationships. A competitor can copy the method in a year. They cannot copy forty years of being trusted by the people who own the decision.'),
 SUB('Layer four, the compounding one: the corpus'),
 P('Nine engagements filed with reasoning intact, each adding a decision pattern to a body of precedent only Meridian holds. Barber Republic proved its worth: Meridian&rsquo;s analysis and your independently written founder documents converged on the same instrument, and that convergence is what gave the recommendation its authority in the room.'),
 PageBreak()]

# ---------------- 7. PRODUCTS ----------------
b+=[L('THE PRODUCTS'), rule(),
 P('Five products. Four sell today. One is the long game. Every one is a shape already delivered.'),
 SUB('1. Decision Brief'),
 P('<b>One decision. Five days. A written position they can take to their board.</b> A single specific question with a yes or no at the end of it. Should United Hardware buy a standalone garden centre. Should Stargas enter cylinder testing. What instrument for a fifty thousand pound investor. Eight to fifteen pages, a clear recommendation, the three to five risks that would change the answer, every claim labelled, and a 45-minute call to walk it through. Up to three domains.'),
 SUB('2. Executive Intelligence Review'),
 P('<b>The whole situation, seven senior angles at once, ten days.</b> Not one question but a position: where is this business exposed, where is value being left on the table, what should the board do. All seven domains, eight to ten interrogated questions each, consolidated into one brief with the five key risks ranked, a sequenced programme of actions, and the questions the board must be able to answer before committing. Closes with a 90-minute board presentation. Fleming Medical and Arcade Trader are the proof.'),
 SUB('3. Transaction Intelligence'),
 P('<b>Due-diligence-grade analysis before they sign.</b> Should we do this deal, at what value, on what instrument, and what will we regret in eighteen months. Valuation and dilution modelling across the funding or exit path, instrument analysis with the rejected alternatives, a term-by-term negotiating position, and a counterparty read: what the other side will push for and how to answer it. Standing availability through the negotiation window. Barber Republic is the proof.'),
 SUB('4. Intelligence Partner, retained'),
 P('<b>A standing seat at the board&rsquo;s decision-making, not a project.</b> United Hardware is already this in everything but name and price: paint buying group, verification pack, location addendum, a formal response to a challenge, the garden centre question, the audit review, a board paper and a vendor brief. Three tiers, from a board that wants the discipline available through to a chair who wants John personally and continuously, including board and ARC attendance.'),
 SUB('5. AI Equity Structuring'),
 P('<b>AI capability contributed for equity, structured so it survives a funding round.</b> This is Manager 7 and it is the line almost nobody else offers. The hard part is structuring it so a Series A investor accepts the arrangement rather than unwinding it as a mess on the cap table. Barber Republic is arguably the first live instance: milestone-based sweat equity for the build work, alongside an investor&rsquo;s cash on a convertible, the two deliberately kept apart.'),
 PageBreak()]

# ---------------- 8. FEES ----------------
b+=[L('THE FEE STRUCTURE'), rule(),
 P('<b>For discussion and agreement with you. Not yet set, and nothing goes near a client until it is.</b>'),
 simple_table(['Product','Scope','Turnaround','Founding rate','List rate'],[
  ['<b>Decision Brief</b>','One question, up to 3 domains','5 working days','<b>&euro;3,950</b>','<b>&euro;4,950</b>'],
  ['<b>Executive Intelligence Review</b>','One business, all 7 domains','10 working days','<b>&euro;18,500</b>','<b>&euro;24,500</b>'],
  ['<b>Transaction Intelligence</b>','One transaction, deal-grade','10 to 15 days','<b>&euro;27,500</b>','<b>&euro;35,000</b>'],
  ['<b>Board Seat</b> (retained)','1 brief per quarter, standing availability','Standing','<b>&euro;3,500/mth</b>','<b>&euro;4,500/mth</b>'],
  ['<b>Intelligence Partner</b> (retained)','1 brief per month, 1 Review per year, board attendance','Standing','<b>&euro;5,750/mth</b>','<b>&euro;7,500/mth</b>'],
  ['<b>Chair&rsquo;s Counsel</b> (retained)','Unlimited within reason, all 7 domains, board and ARC','Standing','<b>&euro;7,950/mth</b>','<b>&euro;10,000/mth</b>'],
  ['<b>AI Equity Structuring</b>','Bespoke','Bespoke','Fee plus equity','Fee plus equity'],
 ],[38*mm,45*mm,22*mm,25*mm,25*mm]),
 Spacer(1,4),
 SUB('How it is priced, and one thing we got wrong first time'),
 P('<b>The fee is set by the product, not by the decision.</b> An earlier draft proposed a ratio, the fee sitting two orders of magnitude below the value of the decision. That rule is withdrawn. It hands the buyer the formula, it assumes our cost scales with their stakes when it does not, it is degressive so it pays proportionately less exactly where the judgment is worth most, and it caps the upside.'),
 callout('<b>Decision value is a qualifier, not a calculator.</b> &ldquo;If this goes wrong, what does it cost you?&rdquo; is a strong question. &ldquo;Therefore my fee is one per cent of that&rdquo; is a weak follow-up.', TEAL),
 SUB('Three notes on the levels'),
 B('<b>Only the Decision Brief sits under &euro;5,000, and that is deliberate.</b> Below that threshold a managing director can say yes in the room without a board paper. It is the door into everything else and the one intentional underpricing on the sheet.'),
 B('<b>Everything above it has stopped apologising.</b> At &euro;12,950 a full seven-domain review read as the cheap option against a &euro;40,000 to &euro;100,000 mid-tier comparison. That attracts the wrong buyer and undercuts the argument that this is a different category of work rather than a discounted version of the same one. At &euro;24,500 it still sits below the bottom of that range, delivered in a sixth of the time.'),
 B('<b>The retained line is where the business is.</b> Three Intelligence Partner clients at list is &euro;270,000 a year before a single brief is sold. A single Transaction Intelligence engagement is worth seven Decision Briefs.'),
 SUB('The first ninety days, conservatively'),
 simple_table(['','Month 1','Month 2','Month 3'],[
  ['Decision Briefs','2','3','3'],
  ['Executive Reviews','0','1','1'],
  ['Retained clients','0','1','2'],
  ['<b>Revenue</b>','<b>&euro;7,900</b>','<b>&euro;33,850</b>','<b>&euro;37,350</b>'],
 ],[45*mm,38*mm,38*mm,38*mm]),
 P('Roughly <b>&euro;79,000 in the first quarter</b> at founding rates, with two retained clients carrying forward.'),
 PageBreak()]

# ---------------- 9. OPEN / ASK ----------------
b+=[L('WHAT IS NOT DONE YET &nbsp;&mdash;&nbsp; STATED PLAINLY'), rule(),
 P('You will find these faster than I could hide them, so here they are.'),
 B('<b>Meridian has no legal entity and the 70/30 shareholders agreement is undrawn.</b>'),
 B('<b>No professional indemnity insurance.</b> Boards act on written advice John signs. It is needed regardless, and most State mentor panels require evidence of cover before they will consider an application.'),
 B('<b>The website is in design, not live.</b>'),
 B('<b>No client has been asked for permission to be named as a reference.</b> Stargas, Arcade Trader and Fleming Medical are the three to ask. United Hardware needs care given the board position.'),
 B('<b>The fee ladder has never been tested on a live client.</b> It is reasoned, not proven.'),
 B('<b>Ambrion is not yet incorporated</b>, which means it cannot register with Skillnet, the LEO panels or Enterprise Ireland. Skillnet is its genuine revenue channel, so the CRO number is effectively the date that channel opens.'),
 L('WHAT I NEED FROM YOU'), rule(),
 N(1,'<b>Agree the three fixes.</b> The AI products move to Ambrion. Manager 5 off Meridian&rsquo;s shopfront. Ambrion owns board AI governance, and Velocity drops or renames Board Advisory. The third one is yours as much as mine.'),
 N(2,'<b>Agree the fee ladder</b>, or tell me where it is wrong.'),
 N(3,'<b>Formalise the three-way referral with a fee split.</b>'),
 N(4,'<b>Settle the paperwork:</b> Ambrion incorporated with the 60/30/10 recorded at formation, and the Meridian 70/30 drawn.'),
 L('AND THEN THE THING I ASKED YOU FOR ORIGINALLY'), rule(),
 callout('Once these are agreed, I am definitive and clear, and I would like the launch plan. <b>Your invaluable and priceless, defensible and verified professional experience and know-how of many years, pointed at this properly.</b> That was your phrase, and it is the right one.', TEAL),
 P('One thing I will concede in advance. The idea of staged analyses of unnamed businesses posted on LinkedIn was wrong and I am parking it. Your instinct was right and there is a second reason you did not name: it publishes the method for free, in the exact territory where the boundary between the three brands had not been drawn.'),
 P('<b>When we do launch, we launch on the nine.</b> Real anonymised engagements, not staged samples. &ldquo;A gas distributor asked whether to enter cylinder testing. Here is how the question was answered in six days.&rdquo; That is the proof you asked for, it is already owned, and nobody who has not done the work can fake it.'),
 Spacer(1,10), rule(HexColor('#D5DDE3'),0.6),
 Paragraph('Meridian Intelligence &middot; Briefing for Shane McCarthy &middot; 5 August 2026 &middot; Private and confidential. Every Meridian claim is drawn from delivered work filed in the Meridian repository. Velocity positioning verified from velocityai.ie and the EDelia proposal, June 2026. Ambrion verified from the Ambrion AI Briefing Note, 5 August 2026. Fee levels are a basis for discussion and are not set.', S['foot']),
]

build(OUT+'Meridian_Briefing_for_Shane.pdf','Meridian Intelligence',
      'Definition, Positioning and Fee Structure',
      ['A briefing for Shane McCarthy, answering the challenge of 4 August 2026',
       'Meridian &middot; Ambrion &middot; Velocity, side by side'],
      'PRIVATE AND CONFIDENTIAL', b, 'Briefing for Shane McCarthy')
print('DONE')
