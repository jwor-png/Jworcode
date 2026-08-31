import sys
sys.path.insert(0, '/home/user/Jworcode/meridian')
from make_meridian_pdfs import (build, L, H, SUB, P, B, N, rule, callout,
                                simple_table, TEAL, BLUE, NAVY, RED)
from reportlab.platypus import Spacer, PageBreak
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm

OUT = '/home/user/Jworcode/ventures/odin/Asterial_Transaction_Fee_Briefing.pdf'
b = []

b += [
    L('TRANSACTION COST BRIEFING'),
    rule(),
    P('<b>Asterial Limited &nbsp;&middot;&nbsp; &euro;20m for 20 per cent &nbsp;&middot;&nbsp; 31 August 2026</b>'),
    P('Agreed terms give a <b>&euro;100m post-money</b> and an <b>&euro;80m pre-money</b> valuation. '
      'This briefing sets out what it is likely to cost to get that transaction to completion, '
      'where the cost is controllable, and what should be settled in the term sheet rather than afterwards.'),
    callout('<b>These are estimated market ranges for budgeting and negotiation. They are not quotations.</b> '
            'No firm has been approached and no fee has been quoted. Replace every figure here with scoped '
            'estimates from named advisers as soon as the term sheet lands.', RED, HexColor('#FBEEEC')),

    H('THE HEADLINE'),
    callout('<b>&euro;400,000 to &euro;900,000 all-in without a corporate finance adviser. '
            '&euro;700,000 to &euro;1.6m with one.</b> Plan against <b>&euro;650,000</b> as the central case.', TEAL),
    P('The working rule for an Irish growth round of this size is <b>2 to 4 per cent of funds raised</b>. '
      'On &euro;20m that is &euro;400,000 to &euro;800,000. A broker or corporate finance mandate is what '
      'pushes it through the top of the band.'),
    P('<b>Almost all of it is borne by the company, not the investor</b>, and a material part is payable '
      'whether or not the deal completes.'),

    H('THE BUILD-UP'),
    P('Ranges exclude VAT at 23 per cent, which is additional and is a real cash cost to the extent it is not recoverable.'),

    SUB('Legal'),
    simple_table(['Item', 'Instructed by', 'Estimated range'], [
        ['<b>Company counsel</b> &mdash; term sheet, subscription and shareholders agreement, '
         'constitution, disclosure letter, warranties, completion', 'Asterial', '<b>&euro;125,000 &ndash; &euro;275,000</b>'],
        ['<b>Investor counsel</b> &mdash; their drafting and review, normally paid by the company under a negotiated cap',
         'Investor', '<b>&euro;75,000 &ndash; &euro;175,000</b>'],
        ['<b>Legal due diligence</b> &mdash; corporate, contracts, employment, data protection, litigation',
         'Investor', 'included above, or <b>&euro;30,000 &ndash; &euro;70,000</b>'],
        ['<b>IP diligence, assignment and licence</b>', 'Both', '<b>&euro;40,000 &ndash; &euro;120,000</b>'],
        ['<b>Company secretarial, CRO filings, share issue mechanics</b>', 'Asterial', '<b>&euro;3,000 &ndash; &euro;12,000</b>'],
    ], [74 * mm, 26 * mm, 44 * mm]),
    P('<b>Legal sub-total: roughly &euro;250,000 to &euro;600,000.</b>'),
    callout('<b>The IP line is the unusual one, and it is why that range is wide.</b> In a standard round the '
            'company already owns its intellectual property and the lawyers confirm it. Here the position has to be '
            '<i>constructed</i> rather than confirmed: assignment or exclusive licence into the company, and a defined '
            'boundary for anything that stays outside it. <b>Done in advance it sits at the bottom of the range. '
            'Discovered during diligence it sits at the top, and it delays completion.</b>', TEAL),
    PageBreak(),

    SUB('Accounting, tax and financial'),
    simple_table(['Item', 'Estimated range'], [
        ['<b>Financial due diligence</b> &mdash; investor-appointed, company usually bears', '<b>&euro;45,000 &ndash; &euro;110,000</b>'],
        ['<b>Tax due diligence and structuring</b>, including the treatment of any founder or participant instrument', '<b>&euro;30,000 &ndash; &euro;75,000</b>'],
        ['<b>Preparation of accounts and management information to diligence standard</b>', '<b>&euro;15,000 &ndash; &euro;50,000</b>'],
        ['<b>Valuation report</b>, if required for share option or revenue purposes', '<b>&euro;10,000 &ndash; &euro;25,000</b>'],
    ], [100 * mm, 44 * mm]),
    P('<b>Sub-total: roughly &euro;100,000 to &euro;260,000.</b> The accounts line depends entirely on what already '
      'exists. Where there are no audited accounts and limited management information, the finance function has to be '
      'built to a standard an institutional investor will accept. That cost is real even though it does not feel like a transaction cost.'),

    SUB('Commercial and technical diligence'),
    simple_table(['Item', 'Estimated range'], [
        ['<b>Technical and product diligence</b> &mdash; model, architecture, data provenance, reproducibility', '<b>&euro;40,000 &ndash; &euro;120,000</b>'],
        ['<b>Commercial and market diligence</b>', '<b>&euro;30,000 &ndash; &euro;90,000</b>'],
    ], [100 * mm, 44 * mm]),
    P('Usually investor-appointed. Whether the company bears it is a term sheet negotiation. '
      '<b>Expect the higher end.</b> The round is priced on expectation rather than trading history, and EU AI Act '
      'diligence now sits on top of ordinary technical diligence. Article 4 has been enforceable since 3 August 2026.'),

    SUB('Corporate finance adviser or broker, if engaged'),
    callout('<b>1 to 3 per cent of funds raised, so &euro;200,000 to &euro;600,000</b>, sometimes with a retainer of '
            '&euro;10,000 to &euro;25,000 a month against the success fee. <b>This is the single largest swing item and '
            'it can exceed the entire legal bill.</b> Establish before signature whether anybody is entitled to a success '
            'or introduction fee on this round, including on an introduction already made. That question is cheap now and '
            'expensive at completion.', BLUE, HexColor('#EAF3FB')),
    PageBreak(),

    L('SUMMARY'),
    rule(),
    simple_table(['', 'Low', 'High'], [
        ['Legal, all parties, company-borne', '&euro;250,000', '&euro;600,000'],
        ['Accounting, tax and financial', '&euro;100,000', '&euro;260,000'],
        ['Commercial and technical diligence', '&euro;70,000', '&euro;210,000'],
        ['<b>Sub-total, no adviser</b>', '<b>&euro;420,000</b>', '<b>&euro;1,070,000</b>'],
        ['Corporate finance adviser, if engaged', '&euro;200,000', '&euro;600,000'],
        ['<b>Total, with adviser</b>', '<b>&euro;620,000</b>', '<b>&euro;1,670,000</b>'],
    ], [92 * mm, 26 * mm, 26 * mm]),
    callout('On an &euro;80m pre-money, <b>&euro;650,000 of costs is 0.8 per cent of the pre-money and 3.25 per cent of '
            'the money raised. That is normal, and it is not a reason to compress the scope.</b> Compressed scope on a '
            'round of this size shows up later as a warranty claim or an unenforceable protection.', TEAL),

    H('THE FOUR THINGS THAT ACTUALLY CONTROL THE NUMBER'),
    B('<b>The investor cost cap, and it is a term sheet item.</b> The investor&rsquo;s legal fees being paid by the '
      'company is standard. The cap is negotiable and should be a hard figure in the term sheet, not '
      '&ldquo;reasonable costs&rdquo;. Uncapped, the line has no ceiling and the company has no control over how many '
      'hours the other side spends. <b>&euro;100,000 to &euro;125,000 is a fair ask on a &euro;20m round.</b>'),
    B('<b>Broken deal costs.</b> If the transaction does not complete, most of the legal, accounting and diligence '
      'spend is already incurred and still payable. <b>The term sheet should say who bears costs if the investor '
      'walks</b>, and that exposure goes live the moment advisers are instructed.'),
    B('<b>Whether the intellectual property work is done before or during diligence.</b> Same work, materially '
      'different price, and a much stronger negotiating position. This is the cheapest single saving available.'),
    B('<b>Whether the company&rsquo;s records are diligence-ready.</b> Statutory registers, board minutes, contracts, '
      'employment documentation, data protection records. Every gap is fixed later at senior solicitor rates under '
      'time pressure. This costs days now and money later.'),
    PageBreak(),

    L('FOUR COSTS THAT ARE NOT IN THE TABLE'),
    rule(),
    B('<b>Independent advice for individual participants.</b> Where any individual takes or is promised a personal '
      'interest, their advice is a separate cost and <b>the company should not pay it</b>. If it does, the '
      'adviser&rsquo;s independence is compromised and the point sits on the file for the investor to find. Order of '
      '&euro;5,000 to &euro;20,000 plus tax advice.'),
    B('<b>Directors and officers insurance.</b> Likely a completion requirement in any event, and it should name every '
      'officer including the company secretary. Order of &euro;5,000 to &euro;25,000 a year depending on limits.'),
    B('<b>The ongoing cost of the investor relationship.</b> Board reporting, an investor director, management accounts '
      'to an agreed standard, and probably an audit requirement. <b>Budget &euro;50,000 to &euro;100,000 a year of '
      'additional finance and governance cost from completion.</b> This is the line most often forgotten.'),
    B('<b>Management time.</b> Not a fee, but the largest real cost. A round of this size absorbs a substantial share '
      'of founder attention for three to six months, at exactly the point the valuation is being justified by growth.'),

    H('WHAT WE RECOMMEND'),
    P('<b>1.</b> Get the investor legal cost cap into the term sheet as a hard figure. Not &ldquo;reasonable&rdquo;. A number.'),
    P('<b>2.</b> Establish now whether any success or introduction fee is claimable by anyone, before it is asserted at completion.'),
    P('<b>3.</b> Complete the intellectual property assignment and define the boundary of anything staying outside the '
      'company <b>before</b> diligence starts.'),
    P('<b>4.</b> Bring the statutory records to diligence standard now. This takes days rather than money.'),
    P('<b>5.</b> Agree who bears broken deal costs.'),
    P('<b>6.</b> Ask two Irish firms with genuine venture and growth-round experience for <b>scoped fee estimates per '
      'workstream</b>, fixed or capped where possible, rather than hourly rates.'),

    H('EVIDENCE POSITION'),
    B('<b>Every figure in this briefing is an estimated market range and is unverified.</b> No adviser has been '
      'approached and no fee has been quoted.'),
    B('The &euro;20m for 20 per cent terms are confirmed as agreed. All other transaction facts are as reported and are not independently verified.'),
    B('Meridian has not seen the term sheet, the diligence request list, the accounts, the statutory registers, or any engagement letter.'),
    B('<b>Meridian is not a solicitor, is not a tax adviser, and is not quoting for work.</b> These are budget ranges '
      'to plan against and to test real quotations with. Meridian informs. It never represents.'),
    Spacer(1, 6),
    rule(NAVY, 0.7),
    N('Meridian Intelligence &nbsp;&middot;&nbsp; Transaction cost briefing &nbsp;&middot;&nbsp; 31 August 2026 &nbsp;&middot;&nbsp; '
      'Private and confidential. Status: in review. Routed to Finance and Restructuring, Legal and Governance, '
      'Commercial and Deal, and AI Equity and Investment. Prepared as commercial intelligence for budgeting purposes '
      'only and not as legal, tax or financial advice. Confirm all figures with qualified advisers before planning against them.'),
]

build(OUT, b, title='Transaction cost briefing',
      footer='Meridian Intelligence  ·  Asterial transaction costs  ·  Private and confidential')
print('written', OUT)
