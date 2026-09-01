import sys
sys.path.insert(0, '/home/user/Jworcode/meridian')
from make_meridian_pdfs import (build, L, H, SUB, P, B, N, rule, callout,
                                simple_table, TEAL, BLUE, NAVY, RED, S)
from reportlab.platypus import Spacer
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm

# One page only: tighten every style for this document.
for k, size, lead in (('P', 8.0, 10.4), ('B', 8.0, 10.4), ('CO', 8.0, 10.4),
                      ('TD', 7.2, 8.9), ('TH', 7.2, 8.9), ('N', 6.1, 7.6)):
    S[k].fontSize = size
    S[k].leading = lead
S['P'].spaceAfter = 2.5
S['B'].spaceAfter = 1.6
S['H'].fontSize = 10
S['H'].spaceBefore = 6
S['H'].spaceAfter = 2
S['L'].fontSize = 13.5
S['CO'].fontSize = 7.7
S['CO'].leading = 9.9

OUT = '/home/user/Jworcode/ventures/odin/Asterial_Cost_Schedule_ONE_PAGER_DRAFT.pdf'
b = []

b += [
    L('TRANSACTION COST SCHEDULE &nbsp;&mdash;&nbsp; EVERY LINE'),
    rule(),
    P('<b>Asterial Limited &nbsp;&middot;&nbsp; &euro;20m for 20 per cent &nbsp;&middot;&nbsp; DRAFT for discussion, 31 August 2026.</b> '
      'So that no cost of this transaction is discovered after it has been committed to. Estimated market ranges for '
      'budgeting; none is a quotation and no adviser has been approached.'),

    simple_table(['#', 'Cost item', 'Borne by', 'Low', 'High'], [
        ['1', '<b>Investor arrangement or administration fee</b> &mdash; up to 2% of funds advanced, '
              'charged by the funder to cover its own costs. <b>Not yet confirmed.</b>', 'Company', '&euro;0', '<b>&euro;400,000</b>'],
        ['2', '<b>Investor legal costs contribution</b> &mdash; standard practice, must be capped at a hard figure', 'Company', '&euro;75,000', '&euro;125,000'],
        ['3', '<b>Origination / success fee</b> &mdash; 2% for sourcing and closing the terms, part deferred', 'Company', '&euro;300,000', '&euro;400,000'],
        ['4', '<b>Company legal</b> &mdash; term sheet, subscription and shareholders agreement, new constitution, disclosure letter, warranties, completion', 'Company', '&euro;125,000', '&euro;250,000'],
        ['5', '<b>IP assignment, licence and boundary definition</b>', 'Company', '&euro;40,000', '&euro;120,000'],
        ['6', '<b>Tax structuring and tax due diligence</b>, including the founder allocation', 'Company', '&euro;30,000', '&euro;75,000'],
        ['7', '<b>Financial due diligence</b> &mdash; investor-appointed', 'Company', '&euro;45,000', '&euro;110,000'],
        ['8', '<b>Technical, product and EU AI Act diligence</b>', 'Company', '&euro;40,000', '&euro;120,000'],
        ['9', '<b>Commercial and market diligence</b>, if required', 'Company', '&euro;0', '&euro;90,000'],
        ['10', '<b>Accounts and management information to diligence standard</b>', 'Company', '&euro;15,000', '&euro;50,000'],
        ['11', '<b>Valuation report</b>, if required for share option or tax purposes', 'Company', '&euro;0', '&euro;25,000'],
        ['12', '<b>CRO filings, company secretarial, share issue mechanics</b>', 'Company', '&euro;3,000', '&euro;12,000'],
        ['13', '<b>Directors and officers insurance</b>, first year', 'Company', '&euro;5,000', '&euro;25,000'],
        ['14', '<b>Corporate finance adviser</b> &mdash; <b>EXCLUDED.</b> The investor is sourced and the price is agreed; '
               'diligence and process are managed internally', '&mdash;', '<b>NIL</b>', '<b>NIL</b>'],
        ['', '<b>Sub-total</b>', '', '<b>&euro;678,000</b>', '<b>&euro;1,802,000</b>'],
        ['15', '<b>Irrecoverable VAT at 23%</b> on professional fees. Arrangement fee and insurance are typically exempt. '
               'Recoverable only against taxable supplies &mdash; <b>confirm with accountants</b>', 'Company', '&euro;154,790', '&euro;316,710'],
        ['', '<b>TOTAL COST OF THE TRANSACTION</b>', '', '<b>&euro;832,790</b>', '<b>&euro;2,118,710</b>'],
    ], [7 * mm, 86 * mm, 17 * mm, 22 * mm, 24 * mm], pad=1.7),

    H('WHAT IS LEFT'),
    simple_table(['', 'Low cost case', 'Central', 'High cost case'], [
        ['Funds raised', '&euro;20,000,000', '&euro;20,000,000', '&euro;20,000,000'],
        ['<i>less</i> founder allocation', '(&euro;2,200,000)', '(&euro;2,200,000)', '(&euro;2,200,000)'],
        ['<i>less</i> total transaction costs', '(&euro;832,790)', '(&euro;1,450,000)', '(&euro;2,118,710)'],
        ['<b>Available to deploy</b>', '<b>&euro;16,967,210</b>', '<b>&euro;16,350,000</b>', '<b>&euro;15,681,290</b>'],
    ], [50 * mm, 35 * mm, 35 * mm, 36 * mm], pad=1.7),

    callout('<b>The &euro;16.0m to &euro;16.5m working assumption holds in the central case. It does not hold in the '
            'high case.</b> The line that breaks it is item 1. If the funder charges a 2 per cent arrangement fee '
            '<i>and</i> a 2 per cent origination fee is paid, that is <b>&euro;800,000 of fee on the same &euro;20m, '
            'or 4 per cent, before a single lawyer has been instructed.</b> Establish whether an arrangement fee is '
            'being charged, and at what rate, before the term sheet is agreed.', RED, HexColor('#FBEEEC')),

    H('THE FIVE THINGS THAT MUST BE SETTLED IN THE TERM SHEET, NOT AFTER IT'),
    B('<b>The arrangement fee.</b> Charged or not, at what rate, and deducted at drawdown or invoiced? Deducted at '
      'source, the company receives less than &euro;20m while issuing shares for &euro;20m.'),
    B('<b>A hard cap on the investor&rsquo;s legal costs.</b> A number, not &ldquo;reasonable costs&rdquo;. '
      '&euro;100,000 to &euro;125,000 is fair here. Uncapped, the line has no ceiling.'),
    B('<b>Who bears costs if it does not complete.</b> Most of the spend is incurred before completion and stays payable either way.'),
    B('<b>The founder allocation and how it is structured.</b> A secondary share sale is a capital disposal; paid out '
      'of the company it is likely income. On &euro;2.2m that is roughly &euro;400,000 of tax. An agreed term, not an assumption.'),
    B('<b>Whether every cost is properly the company&rsquo;s.</b> Fees referable to the founder&rsquo;s personal share '
      'sale sit personally. Straightforward now, uncomfortable at completion.'),

    H('WHAT WE HAVE DELIBERATELY NOT INCLUDED'),
    B('<b>Recruitment and search fees</b> for the technical team. A separate mandate, separately priced and papered, '
      'and an <b>operating cost out of the deployed funds</b>, not a transaction cost. 20 to 25 per cent of first-year '
      'package on contingency, 25 to 30 per cent retained. <b>Never bundle it into a success fee.</b>'),
    B('<b>Ongoing cost of the investor relationship</b> &mdash; board reporting, investor director, management accounts, '
      'probable audit. <b>&euro;50,000 to &euro;100,000 a year, permanently.</b>'),

    rule(NAVY, 0.7),
    N('<b>DRAFT for discussion. Not for onward circulation.</b> &nbsp;Meridian Intelligence &middot; 31 August 2026 &middot; '
      'Private and confidential. All fee figures are estimated market ranges and are UNVERIFIED; no adviser has been approached '
      'and no fee quoted. Irish tax rates are headline rates; reliefs may apply. For budgeting and discussion only, not advice.'),
]

build(OUT, b, title='Cost schedule — DRAFT',
      footer='Meridian Intelligence  ·  Asterial transaction cost schedule  ·  DRAFT  ·  Private and confidential',
      watermark='DRAFT', top=18, bottom=13)
print('written', OUT)
