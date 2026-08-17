// Elite Stanford & Awesome-CV Inspired Typst Template for Tech & Research (Single Page Optimized)
#let resume(
  name: "",
  english_name: "",
  title: "",
  phone: "",
  email: "",
  github: "",
  blog: "",
  location: "",
  education: (),
  skills: (),
  projects: (),
  awards: (),
  papers: (),
  body
) = {
  set document(title: name + " - 个人简历", author: name)
  
  // A4 Page Setup with Precise Single-Page Margins
  set page(
    paper: "a4",
    margin: (x: 1.3cm, top: 1.0cm, bottom: 1.0cm),
  )

  // Typography Palette & Hierarchy (Classic Executive Navy & Slate)
  let brand-color = rgb("#0f2942")      // Deep Oxford Navy
  let accent-color = rgb("#1e40af")     // Royal Blue
  let text-primary = rgb("#1e293b")     // Slate 800
  let text-secondary = rgb("#334155")   // Slate 700
  let text-muted = rgb("#64748b")       // Slate 500
  let line-color = rgb("#94a3b8")       // Slate 400

  set text(
    font: ("PingFang SC", "Heiti SC", "Arial"),
    size: 8.8pt,
    lang: "zh",
    fill: text-primary
  )
  set par(justify: true, leading: 0.48em)

  // ---------------- HEADER ----------------
  align(center)[
    #text(size: 16.5pt, weight: "bold", tracking: 0.08em, fill: brand-color)[#name]
    #if english_name != "" [
      #h(4pt) #text(size: 10pt, weight: "medium", fill: text-muted)[(#english_name)]
    ]
    #v(2.5pt)
    #text(size: 9.5pt, weight: "bold", fill: accent-color)[#title]
    #v(3pt)
    #text(size: 8.5pt, fill: text-secondary)[
      #if phone != "" [#phone]
      #if email != "" [ #h(6pt)•#h(6pt) #link("mailto:" + email)[#email] ]
      #if location != "" [ #h(6pt)•#h(6pt) #location ]
      #if github != "" [ #h(6pt)•#h(6pt) #link(github)[GitHub: insistgang] ]
      #if blog != "" [ #h(6pt)•#h(6pt) #link(blog)[Blog: insistgang.top] ]
    ]
  ]
  v(1pt)

  // Section Header Helper
  let section_heading(t) = {
    v(4.5pt)
    text(size: 10pt, weight: "bold", fill: brand-color, tracking: 0.05em)[#t]
    v(-4pt)
    line(length: 100%, stroke: 0.7pt + brand-color)
    v(2pt)
  }

  // ---------------- 1. 教育背景 ----------------
  section_heading("教育背景")
  for edu in education {
    grid(
      columns: (1fr, auto),
      [
        #text(weight: "bold", size: 9.2pt)[#edu.school]
        #h(8pt)
        #text(fill: text-secondary, weight: "medium")[#edu.degree]
      ],
      [
        #text(fill: text-muted, size: 8.5pt)[#edu.period]
      ]
    )
    v(-3.5pt)
    text(size: 8.2pt, fill: text-secondary)[
      #if "gpa" in edu and edu.gpa != "" [GPA: #edu.gpa #h(8pt)]
      #if "advisor" in edu and edu.advisor != "" [导师: #edu.advisor #h(8pt)]
      #if "honors" in edu and edu.honors.len() > 0 [荣誉: #edu.honors.join("、")]
    ]
    v(2.5pt)
  }

  // ---------------- 2. 专业技能 ----------------
  section_heading("专业技能")
  for sk in skills {
    [
      #text(weight: "bold", fill: brand-color)[• #sk.title]：#text(fill: text-secondary)[#sk.description] \
    ]
    v(1.2pt)
  }

  // ---------------- 3. 核心项目与科研经历 ----------------
  section_heading("核心项目与科研经历")
  for proj in projects {
    grid(
      columns: (1fr, auto),
      [
        #text(weight: "bold", size: 9.2pt)[#proj.name]
        #if "tag" in proj and proj.tag != "" [
          #h(6pt) | #h(6pt) #text(fill: accent-color, weight: "bold", size: 8.5pt)[#proj.tag]
        ]
      ],
      [
        #text(fill: text-muted, size: 8.5pt)[#proj.period]
      ]
    )
    v(-3.5pt)
    text(size: 8.2pt, fill: text-muted)[
      #proj.role #h(8pt) [技术栈: #proj.tags.join(" / ")]
    ]
    v(1.5pt)
    for pt in proj.points {
      [• #pt \ ]
    }
    v(2.5pt)
  }

  // ---------------- 4. 竞赛荣誉与学术成果 ----------------
  section_heading("竞赛荣誉与学术成果")
  if awards.len() > 0 {
    [
      #text(weight: "bold", fill: brand-color)[竞赛荣誉]：#awards.join("； ")。 \
    ]
    v(1.5pt)
  }
  if papers.len() > 0 {
    [
      #text(weight: "bold", fill: brand-color)[学术成果]：#papers.join("； ")。 \
    ]
  }
}
