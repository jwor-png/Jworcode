import sys
sys.path.insert(0,'/tmp/claude-0/-home-user-Jworcode/bd265b20-178b-53cd-b91f-fce4cb651aef/scratchpad')
from make_meridian_pdfs import build, L, H, SUB, P, B, N, rule, callout, simple_table, S, TEAL, BLUE, NAVY, RED
from reportlab.platypus import Spacer, Paragraph, PageBreak, Table, TableStyle, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm

OUT='/tmp/claude-0/-home-user-Jworcode/bd265b20-178b-53cd-b91f-fce4cb651aef/scratchpad/'

def slimhead():
    left=[Paragraph('MERIDIAN INTELLIGENCE',ParagraphStyle('t1',fontName='Helvetica-Bold',fontSize=16,textColor=HexColor('#FFFFFF'),leading=19)),
          Paragraph('What it is, where it stands, and how it grows',ParagraphStyle('t2',fontName='Helvetica',fontSize=9.5,textColor=HexColor('#B9C4CF'),leading=13,spaceBefore=2))]
    right=[Paragraph('7 AUGUST 2026<br/>PRIVATE AND CONFIDENTIAL',ParagraphStyle('t3',fontName='Helvetica-Bold',fontSize=7.5,textColor=TEAL,leading=11,alignment=2))]
    t=Table([[left,right]],colWidths=[122*mm,48*mm])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),NAVY),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('LEFTPADDING',(0,0),(-1,-1),14),('RIGHTPADDING',(0,0),(-1,-1),14),
        ('TOPPADDING',(0,0),(-1,-1),11),('BOTTOMPADDING',(0,0),(-1,-1),11)]))
    return t

b=[slimhead(), Spacer(1,4)]

b+=[L('WHAT MERIDIAN IS'), rule(),
 P('Meridian is an executive intelligence practice. It takes one high-consequence business decision and returns a written, decision-grade position in days, using seven senior domains run at the same time, with forty years of board-level judgment as the final gate.'),
 P('You brief it in plain language. It works out every domain the question genuinely touches, runs them <b>in parallel</b>, has the work independently checked, and returns one consolidated answer with a status and a record of how it was checked.'),
 P('<b>The seven domains.</b> Commercial and Deal &middot; Legal and Governance &middot; Finance and Restructuring &middot; Property and Development &middot; AI Strategy and Adoption &middot; Business Transformation and Growth &middot; AI Equity and Investment. <b>Four carry a mandatory human gate</b>: nothing in Legal, Finance, Property or AI Equity is acted on without a named person signing it off, and where that person disagrees with the engine, they govern and the disagreement stays in the record.'),
 L('THE FLOOR UNDER EVERY ANSWER &nbsp;&mdash;&nbsp; THE PART THAT MATTERS'), rule(),
 B('<b>The grounding rule.</b> No statute, case, figure, title fact or valuation reaches a client unless it was pulled from its primary source and the passage supports it. Anything from memory is never fact. Every hard fact is tagged VERIFIED, REPORTED or UNVERIFIED, and a citation that will not resolve is held.'),
 B('<b>Two critics.</b> A verification critic tries to <i>invalidate</i> the work against source, briefed from the original question rather than the producer&rsquo;s summary of it. A separate adversarial critic asks where a supportable recommendation could still fail. Independence is established by construction, and where it cannot be, that is stated rather than claimed.'),
 B('<b>A status on everything.</b> DRAFT, IN REVIEW or DECISION-READY. The last is a ten-point release gate, not a label, and if a piece falls short the system says which point failed.'),
 B('<b>Fail closed.</b> It holds rather than guesses where a material claim is unverified, where a contradiction could change the recommendation, where a human gate is outstanding, or where the adversarial critic can name a missing fact capable of reversing the answer.'),
 B('<b>The audit record.</b> Who produced what, from which sources, what the critics found, who gated it and when, and which version of the engine produced it. Every answer can be reconstructed later.'),
 B('<b>The boundary.</b> Meridian informs, it never represents. Anything binding, signed, filed or relied on goes to a qualified professional first. The legal capability is Irish law; where other law becomes material the system stops and requires qualified input.'),
 callout('<b>Why this is the asset.</b> A tool that gives an answer is common. A tool that gives an answer <b>and can show exactly how it reached it, and where it refused to guess</b>, is rare. The floor is not overhead. The floor is the product. <b>Which means the floor has to be testable.</b>', TEAL),
 PageBreak()]

b+=[L('WHAT CHANGED THIS WEEK'), rule(),
 P('The engine was documented in full for the first time, extended from <b>50 skills to 61</b>, and then put through an external review of its assurance claims. The controls below were tightened as a result.'),
 simple_table(['New capability','Where it sits','What it does'],[
  ['<b>Read-this-for-me</b>','Legal','A contract, lease or term sheet dropped in. What matters, what bites, what to push back on.'],
  ['<b>Obligations and deadlines</b>','Legal','Every date, statutory clock and filing in one schedule, with the liability flags.'],
  ['<b>Portfolio conflict check</b>','Legal','Tests an action against existing board seats, shareholdings and mandates before a conflict arises.'],
  ['<b>Meeting-prep brief</b>','Commercial','One grounded page before any room: who is being met, their position, where the leverage sits.'],
  ['<b>What-else scan</b>','Transformation','At the close of a matter, the adjacent work the client needs next.'],
  ['<b>Support and grant scan</b>','Transformation','State supports a client can actually draw on, eligibility checked to source.'],
  ['<b>Argue-the-other-side</b>','<i>Every answer</i>','Makes the strongest case against the recommendation and names where it would break. Runs unprompted on anything high-stakes.'],
  ['<b>Say-it-to-the-client</b>','<i>Every answer</i>','Renders technical output as a clean plain-English page, accuracy intact, sources kept.'],
  ['<b>Prior-decision recall</b>','<i>Every answer</i>','Checks what was already concluded, and whether it is genuinely analogous or merely similar. Silent reversal and silent repetition are both failures.'],
  ['<b>Change-the-answer test</b>','<i>Every answer</i>','The smallest set of facts or events that would materially reverse the recommendation. How robust the call is, not only what it is.'],
  ['<b>Evidence gap before advice</b>','<i>Every answer</i>','What is still not known that could affect the decision, stated before the reasoning accelerates.'],
 ],[40*mm,26*mm,106*mm]),
 callout('The last five sit under no single domain and apply to <b>every</b> answer, because a skill wanted everywhere would otherwise fire only when its domain happened to be involved, which is exactly when it is least needed. <b>Prior-decision recall is the significant one</b>: it turns past work from an archive into an asset.', TEAL),
 L('HOW IT GETS BETTER FROM HERE'), rule(),
 P('The engine is extended in plain English, not in code. <b>1.</b> Say what you want in one plain sentence. <b>2.</b> Decide which domain already thinks that way. <b>3.</b> Match the shape of what is already there. <b>4.</b> Write the line and save. <b>5.</b> Prove it against the five test cases. <b>6.</b> Commit it, so it is on the record.'),
 P('Only the first two steps require judgment. Everything after is mechanical. <b>Every capability is required to inherit the same grounding, review, status and escalation controls, and that inheritance is validated before the capability is promoted into use.</b> Each new capability is exercised against an ordinary case, an incomplete-evidence case, a contradictory-source case, a case that must reach a human, and a case it should refuse. <b>Easy to add is not the same as automatically trusted</b>, and the system does not claim otherwise.'),
 callout('<b>The working rule: when the same thing has been done by hand twice, that is the next capability.</b> Both additions made this week came from exactly that. Grant intelligence had appeared unprompted in three separate pieces of client work before anyone thought to make it a skill.', BLUE, HexColor('#EAF3FB')),
 Spacer(1,6), rule(HexColor('#D5DDE3'),0.6),
 Paragraph('Meridian Intelligence &middot; 7 August 2026 &middot; Private and confidential. Seven managers, 56 domain skills, 5 cross-cutting. AI driven, human led.', S['foot']),
]

from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame
from reportlab.lib.pagesizes import A4
from make_meridian_pdfs import GREY
def slimbuild(path, story, running):
    def deco(c,d):
        c.saveState()
        c.setStrokeColor(TEAL); c.setLineWidth(0.8); c.line(18*mm,285*mm,192*mm,285*mm)
        c.setFont('Helvetica-Bold',7); c.setFillColor(NAVY); c.drawString(18*mm,287*mm,'MERIDIAN INTELLIGENCE')
        c.setFont('Helvetica',7); c.setFillColor(GREY); c.drawRightString(192*mm,287*mm,running)
        c.setStrokeColor(HexColor('#D5DDE3')); c.setLineWidth(0.4); c.line(18*mm,13*mm,192*mm,13*mm)
        c.drawRightString(192*mm,9.5*mm,'Private and Confidential  |  Page %d of 2'%d.page)
        c.restoreState()
    doc=BaseDocTemplate(path,pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=18*mm,bottomMargin=16*mm)
    f=Frame(doc.leftMargin,doc.bottomMargin,doc.width,doc.height,id='n')
    doc.addPageTemplates([PageTemplate(id='m',frames=[f],onPage=deco)])
    doc.build(story)
    import os; print('BUILT',path,os.path.getsize(path))
slimbuild(OUT+'Meridian_What_It_Is_and_Where_It_Stands.pdf', b, 'What it is, where it stands, how it grows')
print('DONE')
