const {
  Document, Packer, Paragraph, TextRun, AlignmentType, BorderStyle
} = require('docx');
const fs = require('fs');
const NAVY = "14324f";

function h(text) {
  return new Paragraph({ spacing: { before: 200, after: 70 },
    children: [new TextRun({ text, bold: true, size: 22, color: NAVY, font: "Calibri" })] });
}
function p(text, opts = {}) {
  return new Paragraph({ spacing: { after: 90 }, alignment: AlignmentType.JUSTIFIED,
    children: [new TextRun({ text, size: 20, font: "Calibri", italics: !!opts.italics })] });
}

const doc = new Document({
  styles: { default: { document: { run: { font: "Calibri", size: 20 } } } },
  sections: [{
    properties: { page: { margin: { top: 1100, bottom: 1000, left: 1440, right: 1440 } } },
    children: [
      new Paragraph({ spacing: { after: 20 }, children: [new TextRun({ text: "MERIDIAN INTELLIGENCE", bold: true, size: 26, color: NAVY, font: "Calibri", })] }),
      new Paragraph({ spacing: { after: 160 }, border: { bottom: { color: NAVY, style: BorderStyle.SINGLE, size: 12 } },
        children: [new TextRun({ text: "Introducer Agreement", bold: true, size: 22, color: NAVY, font: "Calibri" })] }),

      p("This agreement is made between:"),
      p("(1) Meridian Intelligence, [contracting entity to be confirmed] (“Meridian”); and"),
      p("(2) ____________________________ (“the Introducer”)."),
      p("Date: ____________________"),

      h("1. Purpose"),
      p("The Introducer may introduce potential clients to Meridian. Where an introduction leads to paid work, Meridian will pay the Introducer a commission on the terms below. The relationship is non-exclusive and either party may end it on notice."),

      h("2. Introductions"),
      p("2.1  An “Introduced Client” is a person or business that the Introducer first introduces to Meridian in writing (by email or message), and which Meridian has not already engaged with or been in discussion with at the date of the introduction."),
      p("2.2  Meridian will confirm by return whether the introduction is accepted, and whether the client is already known to Meridian. Only accepted introductions qualify for commission."),
      p("2.3  An accepted introduction qualifies for commission on any engagement entered into within twelve (12) months of the date it is accepted."),

      h("3. Commission"),
      p("3.1  Meridian will pay the Introducer a commission of twenty per cent (20%) of the Net Fees actually received by Meridian from an Introduced Client."),
      p("3.2  “Net Fees” means the professional fees charged by Meridian for the engagement, excluding VAT and excluding any third-party or external costs recharged to the client."),
      p("3.3  Commission is earned only when, and to the extent that, Meridian has been paid by the client. Meridian will pay commission due within thirty (30) days of receiving the relevant client payment, against the Introducer’s invoice."),
      p("3.4  If a client payment is later refunded or recovered, any commission paid on it is repayable to, or may be offset by, Meridian."),

      h("4. The Introducer’s obligations"),
      p("4.1  The Introducer will act honestly and will not make any representation, promise, quotation or commitment on behalf of Meridian, nor hold themselves out as having authority to bind Meridian."),
      p("4.2  The Introducer will only pass on a potential client’s details where entitled to do so, and will comply with applicable data-protection law."),
      p("4.3  The Introducer is an independent contractor. Nothing in this agreement creates any employment, partnership, joint venture or agency between the parties."),

      h("5. Meridian’s discretion"),
      p("Meridian decides in its sole discretion whether to accept any introduction and whether to offer or accept any engagement. Nothing in this agreement obliges Meridian to take on any introduced client."),

      h("6. Confidentiality"),
      p("Each party will keep confidential the terms of this agreement, and any confidential information of the other party or of any client obtained through it."),

      h("7. Term and termination"),
      p("This agreement continues until ended by either party on fourteen (14) days’ written notice. Termination does not affect commission already earned, or commission on engagements entered into within the twelve-month window for introductions accepted before termination."),

      h("8. Governing law"),
      p("This agreement is governed by the laws of Ireland."),

      new Paragraph({ spacing: { before: 260, after: 120 }, children: [new TextRun({ text: "Signed for Meridian Intelligence: ______________________________", size: 20, font: "Calibri" })] }),
      new Paragraph({ spacing: { after: 200 }, children: [new TextRun({ text: "Name: John Webb O’Rourke        Date: ____________", size: 20, font: "Calibri" })] }),
      new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: "Signed by the Introducer: ______________________________", size: 20, font: "Calibri" })] }),
      new Paragraph({ spacing: { after: 240 }, children: [new TextRun({ text: "Name: ____________________        Date: ____________", size: 20, font: "Calibri" })] }),

      new Paragraph({ border: { top: { color: "808080", style: BorderStyle.SINGLE, size: 6 } },
        spacing: { before: 100 },
        children: [new TextRun({ text: "Draft for discussion. The contracting entity and the commission base (20% of Net Fees received, as drafted) to be confirmed with Shane McCarthy, and the agreement to be reviewed by Meridian’s solicitor before use.", italics: true, size: 16, color: "808080", font: "Calibri" })] }),
    ],
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync("/tmp/claude-0/-home-user-Jworcode/5d519ef4-08ff-5333-9916-fb6208cdfe63/scratchpad/Meridian_Introducer_Agreement.docx", buf);
  console.log("written");
});
