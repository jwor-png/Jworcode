import sys
sys.path.insert(0,'/tmp/claude-0/-home-user-Jworcode/bd265b20-178b-53cd-b91f-fce4cb651aef/scratchpad')
from make_meridian_pdfs import build, L, H, SUB, P, B, N, rule, callout, simple_table, S, TEAL, BLUE, NAVY, RED
from reportlab.platypus import Spacer, Paragraph, PageBreak
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm

OUT='/tmp/claude-0/-home-user-Jworcode/bd265b20-178b-53cd-b91f-fce4cb651aef/scratchpad/'
b=[]

b+=[L('CORRECTION TO THE PRICING DOCUMENT, FIRST'), rule(),
 P('The pricing paper issued earlier today recommended pricing the Decision Brief at &euro;4,950 so it would sit inside a &euro;5,000 Enterprise Ireland Innovation Voucher. <b>Two things in that were wrong and the recommendation does not stand.</b>'),
 P('<b>One. The voucher is now up to &euro;10,000, not &euro;5,000.</b> A fully funded &euro;10,000 standard voucher is available, alongside co-funded vouchers covering project costs up to &euro;20,000 where the company contributes 50 per cent.'),
 callout('<b>Two, and this is the one that matters. Meridian cannot become a registered knowledge provider.</b> Innovation Voucher knowledge providers are publicly funded research organisations: universities, institutes of technology including the seventeen Technology Gateways, and other state research bodies. The scheme exists specifically to connect private SMEs <i>to</i> public research. A private consultancy sits on the wrong side of that relationship by design.', RED, HexColor('#FBEDEF')),
 P('<b>What this does not change.</b> The Decision Brief price stands at &euro;4,950 on its own merits, because it sits inside a managing director&rsquo;s signing authority. That was always the stronger reason. The voucher was a bonus and the bonus is not available directly.'),
 P('<b>What it opens instead.</b> Meridian can work <i>with</i> a registered knowledge provider rather than as one. See route four.'),
 L('THE HARD BLOCKER, BEFORE ANY OF THIS'), rule(),
 callout('<b>Every registration on this list requires a legal entity with a CRO number, a tax clearance certificate, and in most cases professional indemnity insurance.</b> Ambrion has none of these. It therefore cannot be registered with Skillnet, with a LEO panel, with Enterprise Ireland, or with anyone else, under any circumstances, until it is incorporated.', RED, HexColor('#FBEDEF')),
 P('This is now the third separate reason incorporation is urgent, alongside the revenue flowing through Velocity at the wrong split and Pat McGrath&rsquo;s 10 per cent having nothing to attach to.'),
 SUB('Two further items to settle for Meridian at the same time'),
 B('<b>Professional indemnity insurance.</b> Meridian gives written advice that boards act on. It needs PI cover regardless of grant registration, and most panels require evidence of it before they will consider an application. This is a gap today.'),
 B('<b>Meridian&rsquo;s own legal entity and the 70/30 shareholders agreement.</b> Still undrawn.'),
 PageBreak()]

b+=[H('THE ROUTES, IN ORDER OF FIT'), rule(),
 L('ROUTE 1 &nbsp; LOCAL ENTERPRISE OFFICE MENTOR PANELS &nbsp;&mdash;&nbsp; BEST FIT, OPEN NOW'), rule(HexColor('#D5DDE3'),0.6),
 P('<b>What it is.</b> Each of the 31 Local Enterprise Offices maintains a panel of experienced business practitioners who deliver mentoring to small business owners in their county. Panels are procured openly and applications are generally accepted on a rolling basis through the life of a panel.'),
 P('<b>Why it fits John personally, better than anything else on this list.</b> The panels are looking for exactly what he is: decades of practical board and commercial experience, not academic credentials. A serving PLC chair and an audit and risk committee chair is an unusually strong application.'),
 callout('<b>Be clear-eyed about what it is worth.</b> LEO mentoring is heavily subsidised and pays modestly. <b>This is an acquisition channel, not a revenue line.</b> Its value is that it puts John in a room with owner-managers making exactly the decisions Meridian sells against, with the State making the introduction and vouching for him. A proportion become Decision Brief clients at full rate afterwards. That is the return, not the mentoring fee.', TEAL),
 P('<b>Which brand.</b> Meridian, for business and commercial mentoring. Ambrion once incorporated, for AI and EU AI Act mentoring, which will be in heavy demand from 2 August.'),
 P('<b>Action.</b> Apply to Meath and Louth first as home counties, then Dublin City, Fingal and Kildare. Applications are per LEO. Watch for panel calls; several run tranches with cut-off dates.'),
 L('ROUTE 2 &nbsp; ENTERPRISE IRELAND MENTOR NETWORK AND MENTOR GRANT'), rule(HexColor('#D5DDE3'),0.6),
 P('<b>What it is.</b> The same shape as the LEO panels but at Enterprise Ireland level, working with larger client companies rather than micro-enterprises. The Mentor Grant supports EI client companies to bring in external expertise.'),
 P('<b>Why it fits.</b> The client size is closer to Meridian&rsquo;s actual target of &euro;5m to &euro;100m turnover. An EI client company facing a strategic decision is a Meridian buyer in every respect.'),
 P('<b>Action.</b> Apply to join the Mentor Network. Verify current intake process directly with Enterprise Ireland.'),
 L('ROUTE 3 &nbsp; SKILLNET IRELAND &nbsp;&mdash;&nbsp; STRONGEST FIT FOR AMBRION, NOT MERIDIAN'), rule(HexColor('#D5DDE3'),0.6),
 P('<b>What it is.</b> The national workforce development agency, operating through <b>68 Skillnet Business Networks</b> nationwide. It is not a single central register. Training providers engage network by network, and each network manager sources programmes for their member companies. Funding works as joint investment: a government grant plus the company&rsquo;s own contribution.'),
 P('<b>Why it matters commercially.</b> Skillnet subsidy materially reduces what the client pays for training-shaped delivery. <b>This is a genuine revenue channel, not just acquisition</b>, and it is already in play: the Skillnet offset was live on the United Hardware programme.'),
 callout('<b>The important allocation.</b> Skillnet funds <i>training</i>. Meridian does not sell training, it sells decision briefs, so Skillnet is largely irrelevant to Meridian and should not be chased there. <b>Skillnet belongs to Ambrion</b>, and it is the natural funding mechanism for the three AI products moving across: AI in Plain English, AI Governance Readiness Assessment, AI Readiness Accelerator. Velocity&rsquo;s Migration Education tiers are also training-shaped and would qualify.', TEAL),
 P('<b>Action.</b> Target networks by relevance rather than applying blanket. Priority: the technology and digital networks, the management and leadership networks, and any network whose members are SMEs now inside EU AI Act scope. Contact network managers directly. <b>Ambrion cannot do this until it is incorporated.</b>'),
 PageBreak()]

b+=[L('ROUTE 4 &nbsp; INNOVATION VOUCHER, AS A PARTNER RATHER THAN A PROVIDER'), rule(HexColor('#D5DDE3'),0.6),
 P('<b>What it is.</b> Meridian cannot hold knowledge provider status. But a client company can take a &euro;10,000 voucher, engage a university or Technology Gateway as the registered provider, and Meridian can be involved in framing the question and applying the commercial judgment around the technical work.'),
 P('<b>Why it is worth exploring.</b> The Technology Gateways in particular are practical and industry-facing rather than purely academic. A relationship with one or two of them is a route to co-delivering work Meridian could not access alone, and a source of referrals in both directions.'),
 callout('<b>UNVERIFIED and must be checked before relying on it.</b> Whether a knowledge provider may subcontract or partner on voucher work, and on what terms. Scheme rules on this are strict and this could turn out to be closed. Do not put it in front of a client until confirmed.', RED, HexColor('#FBEDEF')),
 L('ROUTE 5 &nbsp; INTERTRADEIRELAND &nbsp;&mdash;&nbsp; WORTH CHECKING, GIVEN THE UK DIMENSION'), rule(HexColor('#D5DDE3'),0.6),
 P('<b>What it is.</b> The cross-border trade and business development body, operating consultant registers for its business support programmes.'),
 P('<b>Why it is relevant.</b> Barber Republic&rsquo;s rollout is London and Manchester. Meridian&rsquo;s stated market is Irish <i>and UK</i> mid-market. Cross-border and Ireland-to-UK expansion decisions are precisely Meridian&rsquo;s product.'),
 P('<b>Action.</b> Verify current programmes and whether consultant registration is open. Treat as second wave, after the LEO applications are in.'),
 L('ROUTE 6 &nbsp; CLIENT-SIDE GRANTS, WORTH MORE THAN PROVIDER REGISTRATION'), rule(HexColor('#D5DDE3'),0.6),
 P('The routes above register <i>you</i>. These reduce what the <i>client</i> pays, which removes the price objection at the point of sale.'),
 B('<b>LEO grants and vouchers</b>, which vary by office and by scheme, some of which can be applied to external business advice.'),
 B('<b>Enterprise Ireland Digital Transition Fund and digitalisation supports</b>, relevant to Ambrion and Velocity rather than Meridian.'),
 B('<b>Regional Skills Fora</b>, for training-shaped delivery alongside Skillnet.'),
 callout('<b>The practical point.</b> Knowing which grant a given client can draw on, and telling them so unprompted, is worth more in a sales conversation than any registration Meridian holds. It reframes the fee from a cost into a co-funded investment, and it makes Meridian look like it is on the client&rsquo;s side of the table. <b>Build a one-page internal crib sheet of what each client type can claim, and keep it current.</b>', TEAL),
 PageBreak()]

b+=[L('WHO REGISTERS WHERE'), rule(),
 simple_table(['Body','Meridian','Ambrion','Velocity','Value'],[
  ['<b>LEO mentor panels</b>','<b>Yes, priority one</b>','Yes, once incorporated','Low priority','Acquisition'],
  ['<b>EI Mentor Network</b>','<b>Yes</b>','Possibly','No','Acquisition'],
  ['<b>Skillnet networks</b>','No, wrong product','<b>Yes, priority one</b>','Yes','<b>Revenue</b>'],
  ['<b>Innovation Voucher</b>','Partner only, not provider','Partner only','Partner only','Co-delivery'],
  ['<b>InterTradeIreland</b>','Yes, verify first','No','No','Acquisition'],
  ['<b>EI Digital Transition</b>','No','<b>Yes</b>','<b>Yes</b>','Revenue'],
  ['<b>Regional Skills Fora</b>','No','Yes','Yes','Revenue'],
 ],[38*mm,36*mm,36*mm,30*mm,28*mm]),
 Spacer(1,6),
 SUB('Read the pattern'),
 P('Meridian&rsquo;s routes are <b>acquisition</b> routes. They put John in front of the right people with the State&rsquo;s endorsement, and the money comes afterwards at full rate. Ambrion&rsquo;s and Velocity&rsquo;s routes are <b>revenue</b> routes, because they sell training and training is what these agencies actually fund.'),
 callout('That is not a weakness in Meridian. It is a consequence of selling judgment rather than programmes, and judgment is not a fundable category. It does mean <b>Meridian should not be built on an assumption of grant-subsidised fees.</b>', BLUE, HexColor('#EAF3FB')),
 L('THE ACTIONS, IN ORDER'), rule(),
 N(1,'<b>Incorporate Ambrion.</b> Nothing on Ambrion&rsquo;s side of this plan can start until it exists. It is the gate.'),
 N(2,'<b>Put professional indemnity insurance in place for Meridian.</b> Required for most panels, and needed anyway.'),
 N(3,'<b>Apply to LEO mentor panels</b>, Meath and Louth first, then Dublin City, Fingal, Kildare.'),
 N(4,'<b>Apply to the Enterprise Ireland Mentor Network.</b> Verify the current intake route directly.'),
 N(5,'<b>Approach Skillnet network managers for Ambrion</b>, targeted by relevance, once incorporated. The United Hardware programme is the reference.'),
 N(6,'<b>Ask one or two Technology Gateways</b> whether partnering on Innovation Voucher work is permitted.'),
 N(7,'<b>Build the client-side grant crib sheet.</b> Cheapest action here and probably the highest return.'),
 N(8,'<b>Verify InterTradeIreland</b> consultant registration as a second wave.'),
 Spacer(1,10), rule(HexColor('#D5DDE3'),0.6),
 Paragraph('Meridian Intelligence &middot; Grant agency registration plan &middot; 5 August 2026 &middot; Private and confidential. Innovation Voucher value, eligibility and knowledge provider restrictions verified from Enterprise Ireland and Technology Gateway sources, August 2026. Skillnet structure of 68 Business Networks and joint-investment model verified from Skillnet Ireland. LEO mentor panel open-application model verified from Local Enterprise Office sources. InterTradeIreland and Technology Gateway partnering rules are UNVERIFIED and flagged as such.', S['foot']),
]

build(OUT+'Meridian_Grant_Agency_Registration_Plan.pdf','Grant Agency Registration Plan',
      'Meridian Intelligence &middot; Ambrion AI &middot; Velocity AI',
      ['Scheme rules verified against source, August 2026',
       'Where a route is closed or uncertain, it is stated plainly'],
      'PRIVATE AND CONFIDENTIAL', b, 'Grant Agency Registration')
print('DONE')
