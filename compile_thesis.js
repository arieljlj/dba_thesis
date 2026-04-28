"use strict";
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, AlignmentType, HeadingLevel, BorderStyle, WidthType,
  ShadingType, PageNumber, PageBreak, LineRuleType, TabStopType,
  TabStopPosition, LevelFormat, NumberFormat, ExternalHyperlink,
  convertInchesToTwip
} = require("docx");
const fs = require("fs");
const path = require("path");

// ── UIIX FORMAT CONSTANTS ──────────────────────────────────────────────────
// A4 in DXA (1 inch = 1440 DXA; 1 cm ≈ 567 DXA)
const PAGE_W   = 11906;  // A4 width
const PAGE_H   = 16838;  // A4 height
const M_LEFT   = 2268;   // 4 cm
const M_TOP    = 1418;   // 2.5 cm
const M_BOTTOM = 1418;   // 2.5 cm
const M_RIGHT  = 1418;   // 2.5 cm
// Content width for tables = PAGE_W - M_LEFT - M_RIGHT = 11906 - 2268 - 1418 = 8220
const CONTENT_W = 8220;

const TNR = "Times New Roman";
const FONT_SIZE = 24; // 12pt in half-points
const FONT_SIZE_LG = 28; // 14pt
const FONT_SIZE_XL = 32; // 16pt
const LINE_SPACING = { line: 360, lineRule: LineRuleType.AUTO }; // 1.5
const PARA_SPACE_AFTER = 160; // ~8pt after paragraph

// ── HELPERS ───────────────────────────────────────────────────────────────

function makeStyle(opts = {}) {
  return {
    font: TNR,
    size: opts.size || FONT_SIZE,
    bold: opts.bold || false,
    italics: opts.italics || false,
    color: opts.color || "000000",
    ...opts,
  };
}

/** Parse inline markdown (**bold**, *italic*, `code`) into TextRun array */
function parseInline(text) {
  if (!text) return [new TextRun({ text: "", font: TNR, size: FONT_SIZE })];
  const runs = [];
  // Pattern: **bold+italic** | **bold** | *italic* | `code` | plain
  const re = /(\*\*\*(.+?)\*\*\*|\*\*(.+?)\*\*|\*(.+?)\*|`(.+?)`|([^*`]+))/g;
  let m;
  while ((m = re.exec(text)) !== null) {
    if (m[2]) runs.push(new TextRun({ text: m[2], font: TNR, size: FONT_SIZE, bold: true, italics: true }));
    else if (m[3]) runs.push(new TextRun({ text: m[3], font: TNR, size: FONT_SIZE, bold: true }));
    else if (m[4]) runs.push(new TextRun({ text: m[4], font: TNR, size: FONT_SIZE, italics: true }));
    else if (m[5]) runs.push(new TextRun({ text: m[5], font: TNR, size: FONT_SIZE }));
    else if (m[6]) runs.push(new TextRun({ text: m[6], font: TNR, size: FONT_SIZE }));
  }
  if (runs.length === 0) runs.push(new TextRun({ text, font: TNR, size: FONT_SIZE }));
  return runs;
}

function normalPara(text, opts = {}) {
  return new Paragraph({
    alignment: opts.alignment || AlignmentType.JUSTIFIED,
    spacing: { ...LINE_SPACING, after: PARA_SPACE_AFTER },
    indent: opts.indent ? { left: opts.indent } : undefined,
    children: parseInline(text),
  });
}

function headingPara(text, level) {
  const levelMap = {
    1: { heading: HeadingLevel.HEADING_1, size: 32, bold: true },
    2: { heading: HeadingLevel.HEADING_2, size: 28, bold: true },
    3: { heading: HeadingLevel.HEADING_3, size: 26, bold: true },
    4: { heading: HeadingLevel.HEADING_4, size: 24, bold: true },
  };
  const cfg = levelMap[level] || levelMap[4];
  // Strip markdown formatting from heading text
  const clean = text.replace(/\*\*(.+?)\*\*/g, "$1").replace(/\*(.+?)\*/g, "$1").replace(/`(.+?)`/g, "$1");
  return new Paragraph({
    heading: cfg.heading,
    spacing: { before: level <= 2 ? 400 : 280, after: 160, ...LINE_SPACING },
    children: [new TextRun({ text: clean, font: TNR, size: cfg.size, bold: cfg.bold })],
  });
}

function pageBreakPara() {
  return new Paragraph({ children: [new PageBreak()] });
}

function emptyPara() {
  return new Paragraph({
    children: [new TextRun({ text: "", font: TNR, size: FONT_SIZE })],
    spacing: { after: 0 },
  });
}

/** Build a docx Table from a markdown table block (array of lines) */
function buildTable(lines) {
  // Filter out separator lines (---|---)
  const dataLines = lines.filter(l => !/^\|?\s*[-:]+\s*(\|[-:\s]+)*\|?\s*$/.test(l));
  if (dataLines.length === 0) return null;

  const parseRow = (line) => {
    return line
      .replace(/^\|/, "").replace(/\|$/, "")
      .split("|")
      .map(c => c.trim());
  };

  const rows = dataLines.map(parseRow);
  const colCount = Math.max(...rows.map(r => r.length));
  const colWidth = Math.floor(CONTENT_W / colCount);
  const colWidths = Array(colCount).fill(colWidth);

  const borderDef = { style: BorderStyle.SINGLE, size: 1, color: "AAAAAA" };
  const borders = { top: borderDef, bottom: borderDef, left: borderDef, right: borderDef };

  const tableRows = rows.map((row, ri) => {
    const isHeader = ri === 0;
    const cells = [];
    for (let ci = 0; ci < colCount; ci++) {
      const cellText = row[ci] || "";
      cells.push(
        new TableCell({
          borders,
          width: { size: colWidths[ci], type: WidthType.DXA },
          shading: isHeader ? { fill: "D9D9D9", type: ShadingType.CLEAR } : undefined,
          margins: { top: 60, bottom: 60, left: 100, right: 100 },
          children: [
            new Paragraph({
              spacing: { line: 276, lineRule: LineRuleType.AUTO, after: 0 },
              children: parseInline(cellText).map(r =>
                new TextRun({ ...r, bold: isHeader ? true : r.options?.bold || false, size: 20, font: TNR })
              ),
            }),
          ],
        })
      );
    }
    return new TableRow({ children: cells, tableHeader: isHeader });
  });

  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: colWidths,
    rows: tableRows,
  });
}

/** Convert a stripped markdown string to docx elements */
function mdToElements(markdown) {
  const elements = [];
  // Remove YAML frontmatter
  const cleaned = markdown.replace(/^---[\s\S]*?---\n?/, "").trim();
  const lines = cleaned.split("\n");

  let i = 0;
  while (i < lines.length) {
    const line = lines[i];

    // Heading
    const hMatch = line.match(/^(#{1,4})\s+(.+)/);
    if (hMatch) {
      const level = hMatch[1].length;
      elements.push(headingPara(hMatch[2], level));
      i++;
      continue;
    }

    // Horizontal rule / page separator → small spacing
    if (/^---+\s*$/.test(line)) {
      elements.push(emptyPara());
      i++;
      continue;
    }

    // Table: collect all table lines
    if (line.startsWith("|")) {
      const tableLines = [];
      while (i < lines.length && lines[i].startsWith("|")) {
        tableLines.push(lines[i]);
        i++;
      }
      const tbl = buildTable(tableLines);
      if (tbl) {
        elements.push(tbl);
        elements.push(emptyPara());
      }
      continue;
    }

    // Blockquote (>)
    if (line.startsWith("> ")) {
      const text = line.replace(/^>\s*/, "");
      elements.push(new Paragraph({
        alignment: AlignmentType.JUSTIFIED,
        spacing: { ...LINE_SPACING, after: PARA_SPACE_AFTER },
        indent: { left: 720, right: 720 },
        children: parseInline(text),
      }));
      i++;
      continue;
    }

    // Bullet list (- or *)
    if (/^(\s*)[-*]\s+(.+)/.test(line)) {
      const m = line.match(/^(\s*)[-*]\s+(.+)/);
      const indent = m[1].length;
      elements.push(new Paragraph({
        alignment: AlignmentType.JUSTIFIED,
        spacing: { ...LINE_SPACING, after: 80 },
        numbering: { reference: "bullets", level: Math.min(Math.floor(indent / 2), 2) },
        children: parseInline(m[2]),
      }));
      i++;
      continue;
    }

    // Numbered list (1. 2. etc.)
    if (/^\d+\.\s+(.+)/.test(line)) {
      const m = line.match(/^\d+\.\s+(.+)/);
      elements.push(new Paragraph({
        alignment: AlignmentType.JUSTIFIED,
        spacing: { ...LINE_SPACING, after: 80 },
        numbering: { reference: "numbering", level: 0 },
        children: parseInline(m[1]),
      }));
      i++;
      continue;
    }

    // Empty line
    if (line.trim() === "") {
      // skip blank lines between paragraphs
      i++;
      continue;
    }

    // Regular paragraph (possibly multi-line)
    let paraText = line;
    while (i + 1 < lines.length && lines[i + 1].trim() !== "" &&
           !lines[i + 1].startsWith("#") && !lines[i + 1].startsWith("|") &&
           !lines[i + 1].startsWith(">") && !lines[i + 1].startsWith("-") &&
           !lines[i + 1].startsWith("*") && !/^\d+\./.test(lines[i + 1]) &&
           !/^---+\s*$/.test(lines[i + 1])) {
      i++;
      paraText += " " + lines[i];
    }
    elements.push(normalPara(paraText));
    i++;
  }

  return elements;
}

// ── FILE READER ────────────────────────────────────────────────────────────
const BASE = path.join(__dirname, "docs");

function readMd(relPath) {
  const full = path.join(BASE, relPath);
  try { return fs.readFileSync(full, "utf8"); }
  catch (e) { console.warn(`⚠  File not found: ${full}`); return ""; }
}

// ── PORTADA (manual, no from md parser) ───────────────────────────────────
function buildPortada() {
  const centBold = (text, size, after = 160) =>
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after },
      children: [new TextRun({ text, font: TNR, size, bold: true })],
    });
  const centNorm = (text, size = FONT_SIZE, after = 160, italics = false) =>
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after },
      children: [new TextRun({ text, font: TNR, size, italics })],
    });

  return [
    pageBreakPara(),
    emptyPara(), emptyPara(), emptyPara(),
    centBold("UNIVERSIDAD DE INVESTIGACIÓN E INNOVACIÓN DE MÉXICO", FONT_SIZE_XL, 80),
    centNorm("UIIX", FONT_SIZE_LG, 240, true),
    centBold("DOCTORADO EN ADMINISTRACIÓN DE EMPRESAS", FONT_SIZE_LG, 480),
    centBold("TESIS DOCTORAL", FONT_SIZE_XL, 480),
    centBold(
      "Factores determinantes de la intención emprendedora en estudiantes universitarios colombianos y el rol de las políticas públicas",
      FONT_SIZE_LG, 480
    ),
    emptyPara(), emptyPara(),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 80 },
      children: [new TextRun({ text: "Candidato doctoral:", font: TNR, size: FONT_SIZE, bold: true })],
    }),
    centNorm("Jorge Ariel Loaiza Loaiza", FONT_SIZE, 240),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 80 },
      children: [new TextRun({ text: "Directora de tesis:", font: TNR, size: FONT_SIZE, bold: true })],
    }),
    centNorm("Dra. Lyzzi Coromoto Davalillo Bolívar", FONT_SIZE, 240),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 80 },
      children: [new TextRun({ text: "Institución de adscripción:", font: TNR, size: FONT_SIZE, bold: true })],
    }),
    centNorm("Corporación de Estudios Tecnológicos del Norte del Valle — COTECNOVA", FONT_SIZE, 80),
    centNorm("Cartago, Valle del Cauca, Colombia", FONT_SIZE, 480),
    emptyPara(), emptyPara(),
    centBold("México, 2026", FONT_SIZE, 240),
    centNorm("Tesis presentada como requisito para obtener el grado de Doctor en Administración de Empresas", FONT_SIZE, 0, true),
  ];
}

// ── DOCUMENT STYLES ────────────────────────────────────────────────────────
const styles = {
  default: {
    document: {
      run: { font: TNR, size: FONT_SIZE },
      paragraph: {
        spacing: { ...LINE_SPACING, after: PARA_SPACE_AFTER },
        alignment: AlignmentType.JUSTIFIED,
      },
    },
  },
  paragraphStyles: [
    {
      id: "Normal",
      name: "Normal",
      run: { font: TNR, size: FONT_SIZE },
      paragraph: {
        spacing: { ...LINE_SPACING, after: PARA_SPACE_AFTER },
        alignment: AlignmentType.JUSTIFIED,
      },
    },
    {
      id: "Heading1",
      name: "Heading 1",
      basedOn: "Normal",
      next: "Normal",
      quickFormat: true,
      run: { font: TNR, size: 32, bold: true, color: "000000" },
      paragraph: {
        spacing: { before: 480, after: 240, ...LINE_SPACING },
        outlineLevel: 0,
      },
    },
    {
      id: "Heading2",
      name: "Heading 2",
      basedOn: "Normal",
      next: "Normal",
      quickFormat: true,
      run: { font: TNR, size: 28, bold: true, color: "000000" },
      paragraph: {
        spacing: { before: 360, after: 160, ...LINE_SPACING },
        outlineLevel: 1,
      },
    },
    {
      id: "Heading3",
      name: "Heading 3",
      basedOn: "Normal",
      next: "Normal",
      quickFormat: true,
      run: { font: TNR, size: 26, bold: true, color: "000000" },
      paragraph: {
        spacing: { before: 280, after: 120, ...LINE_SPACING },
        outlineLevel: 2,
      },
    },
    {
      id: "Heading4",
      name: "Heading 4",
      basedOn: "Normal",
      next: "Normal",
      quickFormat: true,
      run: { font: TNR, size: 24, bold: true, italics: true, color: "000000" },
      paragraph: {
        spacing: { before: 200, after: 80, ...LINE_SPACING },
        outlineLevel: 3,
      },
    },
  ],
};

// ── NUMBERING ──────────────────────────────────────────────────────────────
const numbering = {
  config: [
    {
      reference: "bullets",
      levels: [
        {
          level: 0,
          format: LevelFormat.BULLET,
          text: "•",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 }, spacing: LINE_SPACING }, run: { font: TNR, size: FONT_SIZE } },
        },
        {
          level: 1,
          format: LevelFormat.BULLET,
          text: "◦",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 1080, hanging: 360 }, spacing: LINE_SPACING }, run: { font: TNR, size: FONT_SIZE } },
        },
        {
          level: 2,
          format: LevelFormat.BULLET,
          text: "-",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 1440, hanging: 360 }, spacing: LINE_SPACING }, run: { font: TNR, size: FONT_SIZE } },
        },
      ],
    },
    {
      reference: "numbering",
      levels: [
        {
          level: 0,
          format: LevelFormat.DECIMAL,
          text: "%1.",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 }, spacing: LINE_SPACING }, run: { font: TNR, size: FONT_SIZE } },
        },
      ],
    },
  ],
};

// ── PAGE HEADER (page number upper right) ─────────────────────────────────
function makeHeader() {
  return new Header({
    children: [
      new Paragraph({
        alignment: AlignmentType.RIGHT,
        spacing: { after: 0 },
        children: [new TextRun({ children: [PageNumber.CURRENT], font: TNR, size: FONT_SIZE })],
      }),
    ],
  });
}

// ── SECTION PROPERTIES ────────────────────────────────────────────────────
const pageProps = {
  page: {
    size: { width: PAGE_W, height: PAGE_H },
    margin: { top: M_TOP, right: M_RIGHT, bottom: M_BOTTOM, left: M_LEFT },
  },
};

// ── MAIN BUILD ─────────────────────────────────────────────────────────────
console.log("Leyendo archivos fuente...");

// Load all content
const portadaElements = buildPortada();

const resumenMd    = readMd("00_portada_resumen_abstract/resumen.md");
const abstractMd   = readMd("00_portada_resumen_abstract/abstract.md");
const introMd      = readMd("01_introduccion/introduccion.md");
const cap1Md       = readMd("02_cap1_proyeccion_investigacion/01_capitulo_1.md");
const cap2Md       = readMd("03_cap2_fundamentos_teoricos/02_capitulo_2.md");
const cap3Md       = readMd("04_cap3_metodologia_resultados/01_capitulo_3.md");
const cap4Md       = readMd("05_cap4_propuesta_transformacion/01_capitulo_4.md");
const conclusionesMd = readMd("06_conclusiones/conclusiones.md");
const recomendacionesMd = readMd("07_recomendaciones/recomendaciones.md");
const referenciasRaw = readMd("08_bibliografia/referencias_apa.md");
const anexosMd     = readMd("09_anexos/anexos.md");

console.log("Convirtiendo secciones a elementos DOCX...");

// Convert each section
const resumenElems = mdToElements(resumenMd);
const abstractElems = mdToElements(abstractMd);
const introElems = mdToElements(introMd);
const cap1Elems = mdToElements(cap1Md);
const cap2Elems = mdToElements(cap2Md);
const cap3Elems = mdToElements(cap3Md);
const cap4Elems = mdToElements(cap4Md);
const conclusionesElems = mdToElements(conclusionesMd);
const recomendacionesElems = mdToElements(recomendacionesMd);
const referenciasElems = mdToElements(referenciasRaw);
const anexosElems = mdToElements(anexosMd);

console.log("Ensamblando documento...");

// Assemble all children with page breaks between chapters
function withBreak(elements) {
  return [pageBreakPara(), ...elements];
}

const allChildren = [
  // Portada (sin número de página visible — en sección sin header)
  ...portadaElements,

  // Resumen
  ...withBreak(resumenElems),

  // Abstract
  ...withBreak(abstractElems),

  // Introducción
  ...withBreak(introElems),

  // Capítulo 1
  ...withBreak(cap1Elems),

  // Capítulo 2
  ...withBreak(cap2Elems),

  // Capítulo 3
  ...withBreak(cap3Elems),

  // Capítulo 4
  ...withBreak(cap4Elems),

  // Conclusiones
  ...withBreak(conclusionesElems),

  // Recomendaciones
  ...withBreak(recomendacionesElems),

  // Referencias
  ...withBreak(referenciasElems),

  // Anexos
  ...withBreak(anexosElems),
];

// Build document
const doc = new Document({
  styles,
  numbering,
  sections: [
    {
      properties: pageProps,
      headers: { default: makeHeader() },
      children: allChildren,
    },
  ],
});

// Output path
const outPath = path.join(__dirname, "Tesis_DBA_Loaiza_2026.docx");

console.log("Generando archivo DOCX...");
Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync(outPath, buffer);
  const kb = Math.round(buffer.length / 1024);
  console.log(`✅  Tesis compilada: ${outPath} (${kb} KB)`);
}).catch((err) => {
  console.error("❌  Error generando DOCX:", err);
  process.exit(1);
});
