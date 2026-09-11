import sys
sys.path.insert(0, '/home/user/Jworcode/meridian')
from make_meridian_pdfs import (build, L, H, SUB, P, B, N, rule, callout,
                                simple_table, TEAL, BLUE, NAVY, RED, S)
from reportlab.platypus import Spacer
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm

for k, size, lead in (('P', 8.5, 11.4), ('B', 8.5, 11.4), ('CO', 8.5, 11.4), ('TD', 8.0, 10.2), ('TH', 8.0, 10.2), ('N', 6.4, 8.2)):
    S[k].fontSize = size; S[k].leading = lead
S['P'].spaceAfter = 4
S['B'].spaceAfter = 3
S['H'].fontSize = 10.5
S['H'].spaceBefore = 8
S['H'].spaceAfter = 3
S['L'].fontSize = 14.5

OUT = '/home/user/Jworcode/ventures/authority-layer/Authority_Layer_Briefing_for_Shane.pdf'
b = [
    L('THE AUTHORITY LAYER'),
    rule(),
    P('<b>A short note for Shane &nbsp;&middot;&nbsp; 11 September 2026 &nbsp;&middot;&nbsp; For discussion, nothing committed.</b>'),
    P('An idea worth twenty minutes of your time. It came out of a newspaper column asking who owns your life after you '
      'die, and who gets to tell your story when you can no longer object. <b>The law protecting a person&rsquo;s face and '
      'voice generally switches off at death</b>, at exactly the point where both became trivially easy to synthesise.'),

    H('THE IDEA IN ONE LINE'),
    callout('<b>The layer that proves who decided, that they had the right to decide, and that the buyer was entitled '
            'to rely on it.</b> Not another registry of declarations. Declarations are already free. <b>Evidence is not.</b>', TEAL),

    H('WHY THE BUYER PAYS'),
    P('The buyer is the party facing the fine, not the person facing the harm. EU AI Act transparency duties on synthetic '
      'content are live, with a further marking deadline reported for December 2026. Voiceprints and facial geometry are '
      'special category data, so the only practical lawful basis is explicit consent, and <b>proving you held it is the '
      'problem</b>. In Ireland the Protection of Voice and Image Bill 2025 has passed Second Stage and is not yet law.'),

    H('WHERE IT SHOULD LIVE, AND THIS IS THE MAIN POINT'),
    P('<b>Not as a new company.</b> Between us there is already Meridian, Ambrion, Velocity, EOLAS, Asterial and ODIN, and '
      'Tairseach. The boundary conversation we flagged in August has not happened, and this week Ambrion and Meridian are '
      'both offering EU AI Act compliance on public websites. <b>A seventh vehicle on top of an unresolved six would be '
      'wrong even if the idea were perfect.</b>'),
    B('<b>The advisory sits inside Meridian and can start now.</b> Likeness and synthetic media exposure, using existing '
      'domains, no capital, no new company, no new brand. Sellable this quarter against a hard regulatory date.'),
    B('<b>The venture waits for two gates.</b> Neither has been tested and both can be tested in a fortnight.'),
    B('<b>And one thing to check first.</b> If the Asterial term sheet carries field-of-use or IP assignment wording, '
      'this may already sit there whether we intend it or not. Worth reading before we choose.'),

    H('THE TWO GATES'),
    simple_table(['', 'The question', 'How it gets answered', 'Cost'], [
        ['<b>1</b>', '<b>Is the liability insurable?</b> The model is reliance. If it is uninsurable there is no venture, '
                     'whatever the demand.', 'One specialty broker meeting', '<b>Nil</b>'],
        ['<b>2</b>', '<b>Will a buyer pay?</b> Two or three providers, platforms or insurers saying they would query and '
                     'pay for a verified authority check.', 'Warm conversations', '<b>Nil</b>'],
    ], [9 * mm, 74 * mm, 50 * mm, 15 * mm], pad=3.5),

    H('THE INSURER ANGLE, AND IT IS THE BEST PART'),
    P('Insurers do not buy undeveloped technology. But <b>the thing an insurer actually wants here is not the registry, '
      'it is the underwriting data.</b> Synthetic media and likeness misuse is a liability line they cannot price, '
      'because there is no loss history and no way to tell whether an insured holds valid consent. A verified attestation '
      'layer is a risk-selection tool: it says which insureds can prove consent and which cannot. '
      '<b>That is a reason to fund it rather than merely buy it.</b>'),
    callout('The opening is not &ldquo;we have built a registry&rdquo;. It is: <b>you are being asked to write synthetic '
            'media liability and you have no way to price it. Here is how you would.</b>', BLUE, HexColor('#EAF3FB')),
    P('The Aviva door is worth using for the market read rather than the pitch, since media and emerging liability sit '
      'mostly in the specialty market. A specialty broker answers gate one in a single meeting.'),

    H('WHAT I SUGGEST'),
    P('<b>1.</b> Sell the advisory under Meridian now. It needs nothing from anybody and it pays for the rest.'),
    P('<b>2.</b> Run both gates in parallel over the next fortnight. Two conversations, no cost.'),
    P('<b>3.</b> Before we go further, two sentences on paper about who owns what if this becomes a venture, whatever they '
      'say, including that nothing is agreed yet. <b>Easier now than after a term sheet, and it applies to me as much as to you.</b>'),
    P('<b>4.</b> Then decide whether it is a venture at all.'),

    rule(NAVY, 0.7),
    N('Meridian Intelligence &middot; 11 September 2026 &middot; Private and confidential, for discussion. Source: Kate Durrant, '
      'Irish Country Living, 12 September 2026, verified as published. Regulatory dates and the competitive landscape are '
      'reported, not independently verified; check primary sources before either of us repeats them externally. Insurance '
      'observations are judgement, not a placement recommendation. Meridian informs. It never represents.'),
]

build(OUT, b, title='The Authority Layer',
      footer='Meridian Intelligence  ·  The Authority Layer  ·  For discussion  ·  Private and confidential',
      top=19, bottom=13)
print('written', OUT)
