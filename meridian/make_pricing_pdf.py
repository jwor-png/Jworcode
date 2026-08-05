import sys
sys.path.insert(0,'/tmp/claude-0/-home-user-Jworcode/bd265b20-178b-53cd-b91f-fce4cb651aef/scratchpad')
from make_meridian_pdfs import build, L, H, SUB, P, B, N, rule, callout, simple_table, S, TEAL, BLUE, NAVY, RED
from reportlab.platypus import Spacer, Paragraph, PageBreak
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm

OUT='/tmp/claude-0/-home-user-Jworcode/bd265b20-178b-53cd-b91f-fce4cb651aef/scratchpad/'
b=[]

b+=[L('HOW MERIDIAN IS PRICED'), rule(),
 P('<b>The fee is set by the product, not by the decision.</b> Fixed price per product, published, and held.'),
 P('An earlier draft proposed a ratio: the fee sitting roughly two orders of magnitude below the value of the decision. <b>That rule is withdrawn.</b> It was wrong in four ways and each one matters.'),
 B('<b>It hands the buyer your formula.</b> The moment you say the fee tracks the value of the decision, you have given them the lever. They are no longer negotiating your fee, they are negotiating their own estimate of what the decision is worth, and that number shrinks the instant it becomes the basis of a price.'),
 B('<b>It assumes your cost scales with their stakes.</b> It does not. The seven domains run the same way, the verification is the same, the judgment is the same, whether the decision is worth &euro;500,000 or &euro;15m.'),
 B('<b>It is degressive, which is backwards.</b> &euro;500k to &euro;5k is one per cent. &euro;5m to &euro;20k is four tenths of one per cent. The rule paid proportionately less as the stakes rose, which is precisely where the judgment is worth most.'),
 B('<b>It caps the upside.</b> On a genuinely large decision, the rule becomes the thing arguing the fee downward.'),
 SUB('What replaces it'),
 callout('<b>Decision value is a qualifier, not a calculator.</b>', TEAL),
 P('The question &ldquo;if this goes wrong, what does it cost you?&rdquo; is a strong one, because it screens the buyer and establishes the stakes in their own words. The follow-up &ldquo;therefore my fee is one per cent of that&rdquo; is a weak one, because it converts your price into an arithmetic problem they control. <b>Ask the first. Never say the second.</b>'),
 P('<b>Keep a private sense-check.</b> Does this fee look absurd against these stakes? That is a sanity test on your own list, run in your own head. It is not a pricing method and it never appears in front of a client.'),
 SUB('The comparison that carries the value argument'),
 P('A mid-tier consultancy strategic review is &euro;40,000 to &euro;100,000 and takes six to twelve weeks. Meridian delivers comparable multi-domain depth in days, because the analysis is produced by a governed engine and the senior time goes into judgment and verification rather than production. Anchor on that range before naming any Meridian figure.'),
 L('THE PRODUCT LADDER'), rule(),
 P('Five products. Four sell today. One is the long game.'),
 simple_table(['#','Product','What it answers','Scope','Turnaround','Founding','List'],[
  ['1','<b>Decision Brief</b>','One specific question','Up to 3 domains','5 working days','<b>&euro;3,950</b>','<b>&euro;4,950</b>'],
  ['2','<b>Executive Intelligence Review</b>','A whole situation, every angle','All 7 domains','10 working days','<b>&euro;18,500</b>','<b>&euro;24,500</b>'],
  ['3','<b>Transaction Intelligence</b>','Should we do this deal, on what terms','All 7, deal-grade','10 to 15 days','<b>&euro;27,500</b>','<b>&euro;35,000</b>'],
  ['4','<b>Intelligence Partner</b> (retained)','Everything, continuously','See tiers','Standing','<b>from &euro;3,500/mth</b>','<b>from &euro;4,500/mth</b>'],
  ['5','<b>AI Equity Structuring</b>','AI capability for equity','Bespoke','Bespoke','Fee + equity','Fee + equity'],
 ],[7*mm,33*mm,38*mm,23*mm,22*mm,24*mm,23*mm]),
 callout('<b>Only the Decision Brief holds its earlier level, and that is deliberate.</b> Under &euro;5,000 a managing director can say yes in the room without a board paper. It is the door into everything else. Everything above it has stopped apologising: at &euro;12,950 a full seven-domain review read as the cheap option against the mid-tier comparison, which attracts the wrong buyer and undercuts the argument that this is a different category of work.', TEAL), callout('<b>Founding rate applies to the first ten clients and ends 31 December 2026.</b> This replaces the current &ldquo;friends rate.&rdquo; Same discount, better strategy: a founding rate has a reason and an end date, so it can be withdrawn without insulting anyone. A friends rate never can, and it quietly tells the market your list price is decoration.', BLUE, HexColor('#EAF3FB')),
 PageBreak()]

b+=[L('1 &nbsp; DECISION BRIEF &nbsp;&mdash;&nbsp; &euro;3,950 FOUNDING / &euro;4,950 LIST'), rule(),
 callout('<i>One decision. Five days. A written position you can take to your board.</i>', TEAL),
 P('<b>What it answers.</b> A single, specific, high-consequence question with a yes or no at the end of it.'),
 P('<b>Already delivered in this shape:</b> Should United Hardware buy a standalone garden centre? Should Stargas enter cylinder testing? What instrument should Barber Republic take Ed Lawton&rsquo;s &pound;50,000 on?'),
 SUB('What the client gets'),
 B('A structured written brief, typically 8 to 15 pages, branded and print-ready'),
 B('A clear recommendation with the reasoning attached'),
 B('The three to five risks that would change the answer'),
 B('Every claim labelled verified, estimated or unverified'),
 B('The questions the client should be able to answer before committing'),
 B('A 45-minute call to walk it through'),
 P('<b>Scope boundary.</b> One decision. Up to three of the seven domains. One round of clarification. Additional domains at &euro;1,250 each.'),
 callout('<b>Why it is priced here.</b> At under &euro;5,000 it sits inside a managing director&rsquo;s own signing authority, which means it does not need a board paper to buy. That is deliberate, and it is the single most important commercial property of this product.', TEAL),
]

b+=[L('2 &nbsp; EXECUTIVE INTELLIGENCE REVIEW &nbsp;&mdash;&nbsp; &euro;18,500 FOUNDING / &euro;24,500 LIST'), rule(),
 callout('<i>Your whole situation, interrogated from seven senior angles at once, in ten days.</i>', TEAL),
 P('<b>What it answers.</b> Not one question but a position. Where is this business exposed, where is value being left on the table, and what should the board do about it.'),
 P('<b>Already delivered in this shape:</b> the Arcade Trader four-domain consolidated report with growth model and value-building analysis. The Fleming Medical seven-domain investigative analysis, which corrected an earlier optimistic scoring, found value concentrated in three obscured segments, and closed with the five questions the board had to answer before any capital event.'),
 SUB('What the client gets'),
 B('All seven domains interrogated, eight to ten specific questions each'),
 B('A consolidated executive intelligence brief with a synthesised position'),
 B('The five key risks, ranked'),
 B('A programme of recommended actions with sequencing'),
 B('The human gate: the questions the board must be able to answer before committing'),
 B('A 90-minute presentation to the client&rsquo;s board or leadership team'),
 P('<b>Scope boundary.</b> One business or one division. Ten working days from full information. Follow-on work quoted separately.'),
 callout('<b>Why it is priced here.</b> This is the flagship and the reference product. At &euro;24,500 list it still sits below the bottom of the &euro;40,000 to &euro;100,000 mid-tier range, delivered in roughly a sixth of the time, while no longer signalling that it is the budget option.', TEAL),
 PageBreak()]

b+=[L('3 &nbsp; TRANSACTION INTELLIGENCE &nbsp;&mdash;&nbsp; &euro;27,500 FOUNDING / &euro;35,000 LIST'), rule(),
 callout('<i>Due-diligence-grade analysis before you sign, structured the way the other side&rsquo;s adviser will attack it.</i>', TEAL),
 P('<b>What it answers.</b> Should we do this deal, at what value, on what instrument, and what will we regret in eighteen months.'),
 P('<b>Already delivered in this shape:</b> the Barber Republic funding structure work. A funding ladder across bridge, pre-seed, seed and Series 1 to 3, dilution modelled across rounds, two investor scenarios, instrument recommendation and investor protections, plus a rollout funding roadmap. It converged independently with the founder&rsquo;s own separately written documents, which is what gave the recommendation its authority in the room.'),
 SUB('What the client gets'),
 B('Everything in the Executive Intelligence Review, applied to the transaction'),
 B('Valuation and dilution modelling across the funding or exit path'),
 B('Instrument analysis and recommendation, with the alternatives and why they were rejected'),
 B('Term-by-term negotiating position, including what to concede and what not to'),
 B('Counterparty read: what the other side will push for and how to answer it'),
 B('Standing availability through the negotiation window'),
 P('<b>Why it is priced here.</b> A corporate finance adviser on the same transaction charges a retainer plus a success fee running to multiples of this. Meridian is not replacing that adviser. It is making sure the client walks into the room already knowing their position.'),
 callout('<b>Optional success element.</b> On transactions above &euro;2m, consider a reduced fee plus a success element of 0.5 to 1 per cent on completion. Offer it, do not lead with it. It signals confidence and it materially raises the ceiling on this product.', BLUE, HexColor('#EAF3FB')),
]

b+=[L('4 &nbsp; INTELLIGENCE PARTNER &nbsp;&mdash;&nbsp; RETAINED'), rule(),
 callout('<i>A standing seat at your board&rsquo;s decision-making, not a project.</i>', TEAL),
 P('<b>Already delivered in this shape:</b> United Hardware. Paint buying group validation, verification pack, location addendum, a formal response to a reviewer&rsquo;s challenge, the garden centre question, the 2025 audit review, a Data Transformation board paper and a Vendor Challenge Brief. Multiple decisions, one board, standing access. <b>It has been a retained relationship in everything but name and price.</b>'),
 simple_table(['Tier','Who it is for','Included','Founding','List'],[
  ['<b>Board Seat</b>','A board wanting the discipline available','1 Decision Brief per quarter, standing availability','<b>&euro;3,500/mth</b>','<b>&euro;4,500/mth</b>'],
  ['<b>Intelligence Partner</b>','An active board or a founder in a growth phase','1 Decision Brief per month, 1 Executive Review per year, board attendance by agreement','<b>&euro;5,750/mth</b>','<b>&euro;7,500/mth</b>'],
  ['<b>Chair&rsquo;s Counsel</b>','A chair or owner who wants John personally, continuously','Unlimited briefs within reason, all seven domains, direct access, board and ARC attendance','<b>&euro;7,950/mth</b>','<b>&euro;10,000/mth</b>'],
 ],[30*mm,38*mm,52*mm,25*mm,25*mm]),
 P('<b>Minimum twelve months. Quarterly in advance. Reviewed annually.</b>'),
 callout('<b>Why this tier matters more than any other.</b> It removes the sell. Line one has to win a new client every time. A retained seat compounds, it is predictable, and it is what makes Meridian a business rather than a series of engagements. <b>Three Intelligence Partner clients at list is &euro;270,000 a year before a single brief is sold.</b> That is the number to aim at. For scale, a single Transaction Intelligence engagement is worth seven Decision Briefs.', TEAL),
 PageBreak()]

b+=[L('5 &nbsp; AI EQUITY STRUCTURING &nbsp;&mdash;&nbsp; BESPOKE, FEE PLUS EQUITY'), rule(),
 callout('<i>AI capability contributed for equity, structured so it survives a funding round.</i>', TEAL),
 P('<b>What it answers.</b> How do we contribute AI capability into a business in exchange for a shareholding, and how do we structure it so a Series A investor accepts it rather than unwinding it.'),
 P('<b>This is Manager 7 and it is the line almost nobody else is offering.</b> Barber Republic is arguably the first live instance: milestone-based sweat equity for build work, alongside an investor&rsquo;s cash on a convertible, with the two carefully kept distinct.'),
 P('<b>Commercial shape.</b> A structuring fee at Transaction Intelligence rates, plus an equity participation negotiated case by case. Slowest to convert and hardest to sell cold, which is why it is line five and not line one. But it is the line that turns Meridian from a fee business into an asset business, and every engagement in it compounds.'),
]

b+=[L('FUNDING OFFSETS &nbsp;&mdash;&nbsp; THE ENTRY ROUTE WORTH BUILDING'), rule(),
 P('<i>Corrected 5 August 2026 after verification. See the separate Grant Agency Registration Plan for the full position.</i>'),
 callout('<b>The Enterprise Ireland Innovation Voucher route is not available to Meridian directly.</b> Voucher knowledge providers are publicly funded research organisations: universities, institutes of technology including the seventeen Technology Gateways, and other state research bodies. A private consultancy cannot register. The scheme exists to connect private SMEs <i>to</i> public research, so Meridian sits on the wrong side of it by design. The voucher is also now up to &euro;10,000, not &euro;5,000.', RED, HexColor('#FBEDEF')),
 P('<b>The Decision Brief price of &euro;4,950 stands unchanged</b>, on the stronger of its two original reasons: it sits inside a managing director&rsquo;s own signing authority. The voucher was a bonus, and the bonus is not there. Meridian may still be able to work alongside a registered knowledge provider on voucher-funded work, which is worth exploring with a Technology Gateway, but that is unverified and must not be offered to a client until confirmed.'),
 P('<b>Skillnet Ireland.</b> Funds training, through 68 Skillnet Business Networks nationwide, on a joint-investment model. Meridian does not sell training, so this is not a Meridian route. <b>It belongs to Ambrion</b>, and it is the natural funding mechanism for the three AI products moving across.'),
 callout('<b>The routes open to Meridian are acquisition routes, not revenue routes.</b> Local Enterprise Office mentor panels and the Enterprise Ireland Mentor Network both put John in front of owner-managers with the State making the introduction. They pay modestly. Their value is the room they get him into, not the fee. <b>Meridian should not be built on an assumption of grant-subsidised fees.</b>', TEAL),
 L('WHAT COMES OFF THE MERIDIAN PRICE LIST'), rule(),
 P('The current sheet sells three products, all of them AI services: AI in Plain English (&euro;6,500), AI Governance Readiness Assessment (&euro;12,000), AI Readiness Accelerator (&euro;18,000).'),
 P('<b>All three move to Ambrion.</b> Ambrion&rsquo;s live campaign is tiered done-for-you EU AI Act compliance for Irish SMEs. A readiness assessment is not adjacent to that, it is a tier of it. AI in Plain English is the natural top-of-funnel for the Smacht network of roughly 300 SMEs and for the accountant and solicitor referral channel. The Accelerator is the delivery tier. They are good products sitting under the wrong brand, with a ready-built route to market waiting for them under the right one.'),
 P('Meridian keeps the AI domain in the engine, where a decision touches it. <b>Meridian stops selling AI.</b>'),
 PageBreak()]

b+=[L('HOW TO PRESENT PRICE &nbsp;&mdash;&nbsp; FIVE RULES'), rule(),
 N(1,'<b>Never lead with the number. Lead with the decision.</b> &ldquo;What is the decision worth to you if you get it right, and what does it cost you if you get it wrong?&rdquo; The price answers itself after that.'),
 N(2,'<b>Give three options, not one.</b> Decision Brief, Executive Review, Intelligence Partner. Buyers given one option decide whether to buy. Buyers given three decide which to buy.'),
 N(3,'<b>Anchor high, then place.</b> Mention the mid-tier consultancy comparison of &euro;40,000 to &euro;100,000 over six to twelve weeks before naming your own figure. Every number after that sounds reasonable.'),
 N(4,'<b>Hold the price. Move the scope.</b> If a client cannot reach &euro;12,950, they do not get a discounted Review. They get a Decision Brief at &euro;4,950. Discounting the product teaches the market the price was invented. Reducing the scope teaches them it was real.'),
 N(5,'<b>Say no to the ones that are too small.</b> A client with a &euro;50,000 decision is not a Meridian client yet. Telling them so is worth more in reputation than the fee is in cash, and it is the single most credible thing a new practice can do.'),
 L('THE FIRST NINETY DAYS &nbsp;&mdash;&nbsp; A REALISTIC REVENUE PICTURE'), rule(),
 P('Deliberately conservative, founding rates, and assuming Ambrion&rsquo;s compliance campaign remains the priority claim on John&rsquo;s time.'),
 simple_table(['','Month 1','Month 2','Month 3'],[
  ['Decision Briefs','2','3','3'],
  ['Executive Reviews','0','1','1'],
  ['Intelligence Partner','0','1 (Board Seat)','2'],
  ['<b>Revenue</b>','<b>&euro;7,900</b>','<b>&euro;33,850</b>','<b>&euro;37,350</b>'],
 ],[45*mm,40*mm,42*mm,42*mm]),
 callout('Roughly <b>&euro;79,000 across the first quarter</b> at founding rates, with two retained clients carrying into the next one. A real business, built on a product set already proven nine times, and it does not require Meridian to be anyone&rsquo;s primary vehicle.', TEAL),
 L('THE SIX ACTIONS'), rule(),
 N(1,'<b>Replace the current pricing sheet.</b> The three AI products move to Ambrion. The five products above go live.'),
 N(2,'<b>Rename &ldquo;friends rate&rdquo; to &ldquo;founding client rate.&rdquo;</b> First ten clients, ends 31 December 2026. And settle these figures with Shane before the list goes near a client.'),
 N(3,'<b>Grant registrations: see the separate registration plan.</b> The Innovation Voucher route is closed to Meridian as a provider. Priority is LEO mentor panels and the EI Mentor Network for Meridian, and Skillnet for Ambrion once incorporated. Meridian needs professional indemnity insurance before most panels will consider it.'),
 N(4,'<b>Convert United Hardware to a named Intelligence Partner tier.</b> It is already this relationship. It is simply not priced as one.'),
 N(5,'<b>Run Primeline, Vinny Leonard and DSB Accountants as the first three founding-rate Decision Briefs.</b> Treat DSB as a double play: a Meridian client and an Ambrion referral partner in one conversation.'),
 N(6,'<b>Decide the success-element policy on Transaction Intelligence</b> before the first deal above &euro;2m, not during it.'),
 Spacer(1,10), rule(HexColor('#D5DDE3'),0.6),
 Paragraph('Meridian Intelligence &middot; Products and pricing &middot; 5 August 2026 &middot; Private and confidential. Every product shape is drawn from work already delivered and filed in the Meridian repository. Prices are John&rsquo;s approved basis for discussion with Shane McCarthy, not yet set. The ratio pricing rule proposed in the first draft is withdrawn. Innovation Voucher eligibility and knowledge provider restrictions verified from Enterprise Ireland and Technology Gateway sources, August 2026. Velocity comparison pricing verified from the EDelia proposal, June 2026.', S['foot']),
]

build(OUT+'Meridian_Products_and_Pricing.pdf','Products and Pricing','The Go-to-Market Set',
      ['Revised ladder, ratio pricing rule withdrawn',
       'John&rsquo;s approved basis for discussion with Shane &middot; 5 August 2026'],
      'PRIVATE AND CONFIDENTIAL', b, 'Products and Pricing')
print('DONE')
