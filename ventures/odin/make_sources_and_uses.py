import sys
sys.path.insert(0, '/home/user/Jworcode/meridian')
from make_meridian_pdfs import (build, L, H, SUB, P, B, N, rule, callout,
                                simple_table, TEAL, BLUE, NAVY, RED)
from reportlab.platypus import Spacer, PageBreak
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm

OUT = '/home/user/Jworcode/ventures/odin/Asterial_Sources_and_Uses_Briefing.pdf'
b = []

b += [
    L('SOURCES AND USES &nbsp;&mdash;&nbsp; THE &euro;20m ROUND'),
    rule(),
    P('<b>Asterial Limited &nbsp;&middot;&nbsp; &euro;20m for 20 per cent &nbsp;&middot;&nbsp; 31 August 2026</b>'),
    P('What the whole process costs, what should be paid to the person who originated the transaction, '
      'and what is left to deploy once the founder allocation and all costs are met.'),
    callout('<b>Every figure is an estimated range for budgeting and negotiation. None is a quotation.</b> '
            'No adviser has been approached. The origination fee below is a market benchmark, not an offer, '
            'and it is for discussion between the parties before it is put to anyone.', RED, HexColor('#FBEEEC')),

    H('THE HEADLINE ANSWER'),
    callout('<b>The working assumption of &euro;16.0m to &euro;16.5m available for operations is sound.</b> '
            'Meridian&rsquo;s own build-up gives a range of <b>&euro;16.1m to &euro;16.9m</b>, with a central case of '
            '<b>&euro;16.45m</b>. The assumption is slightly conservative, which is the right way to be wrong.', TEAL),
    P('<b>But it only lands there because of one line that is easy to leave out.</b> See the VAT point below. '
      'Strip that out and the same model gives &euro;16.7m; leave it in and it gives &euro;16.45m. '
      'A quarter of a million turns on whether Asterial can recover VAT on professional fees.'),

    H('THE WATERFALL'),
    simple_table(['', 'Low case', '<b>Central</b>', 'High case'], [
        ['<b>Funds raised</b>', '&euro;20,000,000', '<b>&euro;20,000,000</b>', '&euro;20,000,000'],
        ['<i>less</i> founder allocation', '(&euro;2,200,000)', '<b>(&euro;2,200,000)</b>', '(&euro;2,200,000)'],
        ['<b>Into the company</b>', '<b>&euro;17,800,000</b>', '<b>&euro;17,800,000</b>', '<b>&euro;17,800,000</b>'],
        ['<i>less</i> origination / success fee', '(&euro;300,000)', '<b>(&euro;400,000)</b>', '(&euro;500,000)'],
        ['<i>less</i> legal, accounting and diligence', '(&euro;450,000)', '<b>(&euro;700,000)</b>', '(&euro;900,000)'],
        ['<i>less</i> irrecoverable VAT at 23%', '(&euro;172,500)', '<b>(&euro;253,000)</b>', '(&euro;322,000)'],
        ['<b>Available to deploy</b>', '<b>&euro;16,877,500</b>', '<b>&euro;16,447,000</b>', '<b>&euro;16,078,000</b>'],
    ], [56 * mm, 30 * mm, 30 * mm, 30 * mm]),
    P('<b>Total cost of the process: &euro;922,500 to &euro;1,722,000, central &euro;1,353,000.</b> '
      'That is 4.6 to 8.6 per cent of the money that reaches the company, and 6.8 per cent in the central case. '
      'For a first institutional round with an unusual intellectual property position, that is within normal range.'),
    PageBreak(),

    L('THE ORIGINATION FEE'),
    rule(),
    P('One person originated this transaction: found the investor, put the deal together, and brought it to agreed '
      'terms of &euro;20m for 20 per cent. That is the hardest part of any raise and it should be paid for. '
      'The question is how much, and the answer turns on <b>what is being paid for and what is not</b>.'),

    SUB('What the market pays, and for what'),
    simple_table(['Scope of the mandate', 'Typical rate', 'On &euro;20m'], [
        ['<b>Full corporate finance mandate</b> &mdash; sourcing, competitive process, price, documentation, '
         'diligence management, completion', '2.5 &ndash; 3.5%', '&euro;500,000 &ndash; &euro;700,000'],
        ['<b>Sourced, negotiated and closed the terms</b>, but does not run the diligence or the process',
         '<b>1.5 &ndash; 2.5%</b>', '<b>&euro;300,000 &ndash; &euro;500,000</b>'],
        ['<b>Introduction only</b> &mdash; made the connection, no negotiation, no process', '1 &ndash; 1.5%',
         '&euro;200,000 &ndash; &euro;300,000'],
    ], [78 * mm, 30 * mm, 38 * mm]),
    callout('<b>The middle row is this transaction.</b> The origination and the price were delivered. '
            'The diligence and the process will be managed internally. That is a materially reduced scope against a '
            'full mandate, and the fee should reflect it. <b>Meridian&rsquo;s indicative figure is 2 per cent, '
            '&euro;400,000</b>, as the point to open at and defend.', TEAL),

    SUB('How it should be structured, and this matters more than the number'),
    B('<b>Payable on completion only.</b> No success fee is earned unless the money lands. If the transaction does '
      'not complete, nothing is due.'),
    B('<b>Split the payment.</b> Three quarters on completion, one quarter deferred by six months. This is normal, it '
      'keeps the originator engaged through the closing period, and it is easier to agree at the outset than to introduce later.'),
    B('<b>Consider part in equity.</b> An element taken in shares rather than cash reduces the cash cost of the round, '
      'aligns the originator with the outcome, and is frequently welcomed by someone who believes in the business. '
      'It also has to be agreed with the incoming investor, because it affects the cap table.'),
    B('<b>Paper it before completion, not at it.</b> An unpapered origination fee becomes a dispute at exactly the '
      'moment the money is on the table and the leverage has gone. This is the single most important line on this page.'),
    B('<b>Define what it covers and what it excludes.</b> Specifically: it is a fee for this transaction. It is not a '
      'retainer, it does not attach to future rounds, and it does not cover any other service.'),

    H('AND THE SEPARATE ROLE'),
    P('A recruitment or search mandate to build the technical team is <b>a different piece of work, at a different '
      'time, on a different basis</b>, and it should be priced and papered entirely separately.'),
    B('<b>It is an operating cost, not a transaction cost.</b> It comes out of the deployed &euro;16m and belongs in '
      'the operating budget, not in this waterfall.'),
    B('<b>Market rate is 20 to 25 per cent of first-year package on contingency</b>, or 25 to 30 per cent on retained '
      'search. For a technical team of six to ten hires that is a meaningful figure and it should be budgeted for openly.'),
    B('<b>Never bundle it into the success fee.</b> Two roles paid through one number is impossible to audit, '
      'impossible to unwind if one relationship ends, and it is the kind of arrangement an investor&rsquo;s counsel '
      'asks pointed questions about.'),
    callout('<b>Where one person holds more than one role, each role gets its own agreement, its own fee and its own '
            'termination.</b> That is not a comment on any individual. It is how the arrangement stays clean when '
            'circumstances change, and it protects the person in the roles as much as the company.', BLUE, HexColor('#EAF3FB')),
    PageBreak(),

    L('THREE THINGS TO SETTLE BEFORE THE TERM SHEET'),
    rule(),
    P('These are ordered by what they cost if they are left until afterwards.'),

    H('1.  HOW THE FOUNDER ALLOCATION IS STRUCTURED'),
    P('The &euro;2.2m coming off the top is <b>the single most consequential open item in the whole structure</b>, and '
      'it is not a cost line. It is a transaction in itself, and there are two entirely different ways to do it.'),
    B('<b>As a secondary sale.</b> The investor buys &euro;2.2m of existing shares directly from the founder and '
      'subscribes &euro;17.8m of new shares into the company. <b>This is the clean route.</b> The proceeds are a '
      'capital disposal and are taxed as such.'),
    B('<b>As a payment out of the company.</b> The full &euro;20m subscribes for new shares and the founder is paid '
      '&euro;2.2m afterwards. <b>This is the route to avoid.</b> It requires a lawful basis, it is taxed as income if '
      'it is remuneration, and a shareholders agreement will almost certainly prohibit it once the investor is on the register.'),
    callout('<b>The tax difference is not marginal.</b> A capital disposal at Irish CGT of 33 per cent leaves roughly '
            '&euro;1.47m of a &euro;2.2m sum. The same amount taken as remuneration, at marginal income tax, USC and '
            'PRSI approaching 52 per cent, leaves roughly &euro;1.06m. <b>A difference of about &euro;400,000 on the '
            'same &euro;2.2m, decided entirely by structure.</b> Reliefs may be available and may change this materially. '
            'This requires a tax adviser before the term sheet, not after.', RED, HexColor('#FBEEEC')),
    P('<b>The question that has to be asked out loud:</b> is the &euro;2.2m the gross amount coming off the round, or '
      'the amount intended to be available personally after tax? <b>Those are very different numbers.</b> To net '
      '&euro;2.2m at 33 per cent, roughly &euro;3.28m of secondary is required, which is 16 per cent of the round '
      'rather than 11 per cent, and that is a different conversation with the investor.'),
    P('<b>And it must be agreed at term sheet.</b> Founder secondary in a first institutional round is common but it '
      'is never assumed. At &euro;2.2m it is 11 per cent of the round, which is at the upper end of what investors '
      'accept and is arguable on an &euro;80m pre-money for a founder who has not previously taken money off the '
      'table. <b>Arguable is not agreed. Put it in the term sheet.</b>'),

    H('2.  VAT ON PROFESSIONAL FEES'),
    P('Irish professional fees carry VAT at 23 per cent. On &euro;1.1m of fees that is roughly &euro;253,000. '
      '<b>It is recoverable only to the extent the company makes taxable supplies.</b> A company that is not yet '
      'trading, or whose supplies are not fully taxable, may not recover it, and it becomes a hard cash cost.'),
    callout('<b>This is the line most often left out of a funding budget, and here it is the difference between '
            '&euro;16.7m and &euro;16.45m.</b> Establish the VAT position with the accountants before the budget is '
            'fixed. It is a short question with a large answer.', TEAL),

    H('3.  WHO BEARS WHAT, AND WHO BEARS IT IF THE DEAL BREAKS'),
    B('<b>Transaction costs are ordinarily borne by the company</b>, which is what the waterfall assumes and is correct.'),
    B('<b>The investor&rsquo;s legal costs are also normally borne by the company, and the cap is a term sheet item.</b> '
      'A hard figure, not &ldquo;reasonable costs&rdquo;. &euro;100,000 to &euro;125,000 is a fair ask on a &euro;20m round.'),
    B('<b>Costs attributable to the founder allocation are arguably the founder&rsquo;s, not the company&rsquo;s.</b> '
      'A secondary sale is a personal transaction. The advice on it, and any part of an origination fee properly '
      'referable to it, sits personally. Settle this early; it is uncomfortable to raise at completion.'),
    B('<b>Broken deal costs.</b> Most of the spend is incurred before completion and remains payable if the '
      'transaction fails. <b>The term sheet should say who bears it if the investor walks.</b>'),
    PageBreak(),

    L('MANAGING THE PROCESS INTERNALLY'),
    rule(),
    P('The intention is to run diligence and process management internally, using the tools available, with '
      'professionals engaged where they are genuinely required. <b>Meridian&rsquo;s read is that this is the right '
      'call and it is where the real saving sits.</b>'),
    SUB('What it saves'),
    B('<b>The process-management element of a full corporate finance mandate</b>, which is the difference between a '
      '2.5 to 3.5 per cent fee and a 1.5 to 2.5 per cent one. On &euro;20m that is &euro;200,000 or more.'),
    B('<b>Preparation, assembly and coordination.</b> Data room construction, document indexing, diligence request '
      'tracking, first-pass responses, management information assembly. This is where the hours go and it is the work '
      'most amenable to being done well internally.'),
    SUB('What it does not save, and this should be understood clearly'),
    B('<b>Investor-side costs.</b> Their counsel, their financial diligence, their technical diligence. Those are '
      'their appointments, at their rates, and internal effort does not reduce them.'),
    B('<b>Drafting and negotiation of the transaction documents.</b> The subscription and shareholders agreement, the '
      'constitution, the disclosure letter and the warranties are legal work and they require a solicitor. '
      '<b>This is not a place to economise.</b>'),
    B('<b>Tax structuring.</b> See the founder allocation above. The advice costs a fraction of what getting it wrong costs.'),
    B('<b>The intellectual property work.</b> Assignment or licence into the company, and a defined boundary for '
      'anything staying outside it, is document drafting to an investor&rsquo;s satisfaction.'),
    callout('<b>Doing the intellectual property work before diligence rather than during it is the cheapest single '
            'saving available on this transaction</b>, and it is worth more than any fee negotiation. Same work, '
            'materially lower cost, materially stronger position, and no delay to completion.', TEAL),
    SUB('One thing to put in place'),
    P('<b>Where an individual takes on the management of the transaction process, that role should be defined in '
      'writing and, if appropriate, remunerated.</b> It is real work of real value over three to six months, it '
      'displaces a paid mandate, and an investor&rsquo;s counsel will expect to see who is accountable for the '
      'process. An undocumented role is harder to recognise afterwards than to define now.'),

    H('THE SHORT LIST'),
    P('<b>1.</b> Structure the founder allocation as a secondary sale, and confirm whether &euro;2.2m is the gross or the net.'),
    P('<b>2.</b> Take tax advice on it before the term sheet, not after.'),
    P('<b>3.</b> Put the founder allocation, the investor legal cost cap and broken deal costs into the term sheet as agreed terms.'),
    P('<b>4.</b> Agree and paper the origination fee before completion. Indicative 2 per cent, &euro;400,000, part deferred.'),
    P('<b>5.</b> Paper any search or recruitment mandate separately, and budget it as an operating cost.'),
    P('<b>6.</b> Establish the VAT recovery position with the accountants.'),
    P('<b>7.</b> Complete the intellectual property assignment before diligence starts.'),
    P('<b>8.</b> Get scoped fee estimates per workstream from two Irish firms with real growth-round experience.'),

    Spacer(1, 5),
    rule(NAVY, 0.7),
    N('Meridian Intelligence &nbsp;&middot;&nbsp; Sources and uses briefing &nbsp;&middot;&nbsp; 31 August 2026 &nbsp;&middot;&nbsp; '
      'Private and confidential. Status: in review. Routed to Finance and Restructuring, Legal and Governance, '
      'Commercial and Deal, and AI Equity and Investment. All fee figures are estimated market ranges and are unverified; '
      'no adviser has been approached and no fee has been quoted. Irish tax rates are stated as general headline rates '
      'and reliefs may apply; nothing here is tax advice. Prepared as commercial intelligence for budgeting and '
      'discussion only. Meridian informs. It never represents. Confirm all figures and all structuring with qualified '
      'advisers before acting on them.'),
]

build(OUT, b, title='Sources and uses',
      footer='Meridian Intelligence  ·  Asterial sources and uses  ·  Private and confidential')
print('written', OUT)
