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
 P('You brief it in plain language. It works out every domain the question genuinely touches, runs them <b>in parallel rather than one after another</b>, has the work independently checked, and hands back one consolidated answer. Its four jobs: <b>Classify</b> the question, <b>Route</b> it, <b>Consolidate</b> the work, <b>Return</b> it with a status and a record of how it was checked.'),
 P('<b>The seven domains.</b> Commercial and Deal. Legal and Governance, Irish law throughout, the heaviest specialist. Finance and Restructuring. Property and Development. AI Strategy and Adoption. Business Transformation and Growth. AI Equity and Investment. <b>Four of the seven carry a mandatory human gate</b>: nothing in Legal, Finance, Property or AI Equity is acted on without a person signing it off.'),
 SUB('One job, traced end to end'),
 P('<i>The brief:</i> &ldquo;A family builders&rsquo; merchant in Galway, turnover about four million, second generation coming in, cash is tight. Where do I start?&rdquo; Meridian routes it to <b>Finance</b>, <b>Business Transformation</b> and <b>Legal</b> at once. The independent critic re-reads the numbers against source before anything moves. One answer comes back: the true cash position, the two fastest value wins, the directors&rsquo; duties flag while the company is under strain, and the succession conversation that is coming whether or not anyone has raised it. <b>One brief in. Three domains. One checked, labelled answer out.</b>'),
 L('THE FLOOR UNDER EVERY ANSWER &nbsp;&mdash;&nbsp; THE PART THAT MATTERS'), rule(),
 B('<b>The grounding rule.</b> No statute, case, figure, title fact or valuation reaches a client unless it was pulled from its primary source and the passage supports it. Anything from memory is never fact. Every hard fact is tagged VERIFIED, REPORTED or UNVERIFIED, and a citation that will not resolve is held, not shipped.'),
 B('<b>The independent critic.</b> Whatever a skill produces is re-read by a separate agent, on a stronger model, against the original source. The one who makes the work and the one who checks it are never the same, so they do not share a blind spot.'),
 B('<b>A status on everything.</b> DRAFT, IN REVIEW or DECISION-READY. Only the last can be relied on, and if a piece is not there yet the system says exactly what is missing.'),
 B('<b>Fail closed.</b> Near a legal, financial or regulatory line, or below 80 per cent confidence, it stops and pulls a person in rather than guess. It cannot quietly grade its own work down to avoid that.'),
 B('<b>The audit record.</b> Who produced what, from which sources, what the critic found, at what confidence. Every answer can show its own lineage.'),
 B('<b>The boundary.</b> Meridian informs. It never represents. Anything binding, anything to be signed, filed or relied on, goes to a qualified professional first.'),
 callout('<b>Why this is the asset.</b> A tool that gives an answer is common. A tool that gives an answer <b>and can show exactly how it reached it, and where it refused to guess</b>, is rare. The floor is not overhead. The floor is the product.', TEAL),
 PageBreak()]

b+=[L('WHAT CHANGED THIS WEEK'), rule(),
 P('The engine was documented in full for the first time, and then extended. It has gone from <b>50 skills to 59</b>.'),
 simple_table(['New capability','Where it sits','What it does'],[
  ['<b>Read-this-for-me</b>','Legal','A contract, lease or term sheet dropped in. Returns what matters, what bites, what to push back on.'],
  ['<b>Obligations and deadlines</b>','Legal','Every date, statutory clock and filing in a matter, into one schedule with the liability flags on it.'],
  ['<b>Portfolio conflict check</b>','Legal','Tests a proposed action against existing board seats, shareholdings and mandates, and names any conflict before it arises.'],
  ['<b>Meeting-prep brief</b>','Commercial','One grounded page before any room: who is being met, their likely position, where the leverage sits, what could go wrong.'],
  ['<b>What-else scan</b>','Transformation','At the close of any matter, the adjacent work the client now needs next.'],
  ['<b>Support and grant scan</b>','Transformation','The State supports and funding offsets a client can actually draw on, eligibility checked to source.'],
  ['<b>Argue-the-other-side</b>','<i>Every answer</i>','Red-teams the recommendation, makes the strongest case against it, names where it would break. Runs unprompted on anything high-stakes.'],
  ['<b>Say-it-to-the-client</b>','<i>Every answer</i>','Renders any technical output as a clean plain-English page, accuracy intact, sources kept.'],
  ['<b>Prior-decision recall</b>','<i>Every answer</i>','Checks what was already concluded on a related matter and says so. A silent reversal is treated as a failure.'],
 ],[40*mm,26*mm,106*mm]),
 P('The last three sit under no single domain. They apply to <b>every</b> answer, because a skill wanted everywhere would otherwise only fire when its domain happened to be involved, which is exactly when it is least needed.'),
 callout('<b>Prior-decision recall is the significant one.</b> It turns a body of past work from an archive into an asset. Every engagement now adds a decision precedent the system can retrieve and must reconcile against.', TEAL),
 L('HOW IT GETS BETTER FROM HERE'), rule(),
 P('The engine is extended in plain English, not in code. Adding a capability is a one-line job and it is live immediately, with no rebuild.'),
 P('<b>1.</b> Say what you want in one plain sentence. &nbsp; <b>2.</b> Decide which domain already thinks that way. &nbsp; <b>3.</b> Match the shape of what is already there. &nbsp; <b>4.</b> Write the line and save. &nbsp; <b>5.</b> It is live at once. &nbsp; <b>6.</b> Prove it: point a question at it. &nbsp; <b>7.</b> Commit it, so it is on the record.'),
 P('Only the first two steps require judgment. Everything after is mechanical. A new capability <b>inherits the grounding rule, the independent critic, the status label and the human gate automatically</b>, simply by living inside the system. The discipline is never re-implemented and never degrades as the engine grows.'),
 callout('<b>The working rule: when the same thing has been done by hand twice, that is the next capability.</b> Both additions made this week came from exactly that. Grant intelligence had appeared unprompted in three separate pieces of client work before anyone thought to make it a skill.', BLUE, HexColor('#EAF3FB')),
 Spacer(1,6), rule(HexColor('#D5DDE3'),0.6),
 Paragraph('Meridian Intelligence &middot; 7 August 2026 &middot; Private and confidential. Seven managers, 56 domain skills, 3 cross-cutting. AI driven, human led.', S['foot']),
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
