// Elite Stanford & Awesome-CV Single-Page High-Density Typst Template
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
  
  // A4 Page Setup with High-Density 1-Page Margins
  set page(
    paper: "a4",
    margin: (x: 1.25cm, top: 0.9cm, bottom: 0.9cm),
  )

  // Typography Palette & Hierarchy
  let brand-color = rgb("#0a2540")      // Deep Oxford Navy
  let accent-color = rgb("#1d4ed8")     // Vibrant Cobalt Blue
  let text-primary = rgb("#0f172a")     // Slate 900
  let text-secondary = rgb("#334155")   // Slate 700
  let text-muted = rgb("#64748b")       // Slate 500

  set text(
    font: ("PingFang SC", "Heiti SC", "Arial"),
    size: 8.6pt,
    lang: "zh",
    fill: text-primary
  )
  set par(justify: true, leading: 0.44em)

  // ---------------- HEADER ----------------
  align(center)[
    #text(size: 16pt, weight: "bold", tracking: 0.08em, fill: brand-color)[#name]
    #if english_name != "" [
      #h(4pt) #text(size: 9.5pt, weight: "medium", fill: text-muted)[(#english_name)]
    ]
    #v(1.5pt)
    #text(size: 9.2pt, weight: "bold", fill: accent-color)[#title]
    #v(2pt)
    #text(size: 8.3pt, fill: text-secondary)[
      #if phone != "" [#phone]
      #if email != "" [ #h(5pt)•#h(5pt) #link("mailto:" + email)[#email] ]
      #if location != "" [ #h(5pt)•#h(5pt) #location ]
      #if github != "" [ #h(5pt)•#h(5pt) #link(github)[GitHub: insistgang] ]
      #if blog != "" [ #h(5pt)•#h(5pt) #link(blog)[Blog: insistgang.top] ]
    ]
  ]
  v(1pt)

  // Section Header Helper
  let section_heading(t) = {
    v(3.5pt)
    text(size: 9.6pt, weight: "bold", fill: brand-color, tracking: 0.04em)[#t]
    v(-4pt)
    line(length: 100%, stroke: 0.75pt + brand-color)
    v(1.5pt)
  }

  // ---------------- 1. 教育背景 ----------------
  section_heading("教育背景")
  for edu in education {
    grid(
      columns: (1fr, auto),
      [
        #text(weight: "bold", size: 9pt)[#edu.school]
        #h(6pt)
        #text(fill: text-secondary, weight: "medium")[#edu.degree]
      ],
      [
        #text(fill: text-muted, size: 8.2pt)[#edu.period]
      ]
    )
    v(-3.5pt)
    text(size: 8.0pt, fill: text-secondary)[
      #if "gpa" in edu and edu.gpa != "" [GPA: #edu.gpa #h(6pt)]
      #if "advisor" in edu and edu.advisor != "" [导师: #edu.advisor #h(6pt)]
      #if "thesis" in edu and edu.thesis != "" [论文方向: #edu.thesis #h(6pt)]
      #if "honors" in edu and edu.honors.len() > 0 [荣誉: #edu.honors.join("、")]
    ]
    v(1.5pt)
  }

  // ---------------- 2. 专业技能 ----------------
  section_heading("专业技能")
  for sk in skills {
    [
      #text(weight: "bold", fill: brand-color)[• #sk.title]：#text(fill: text-secondary)[#sk.description] \
    ]
    v(1pt)
  }

  // ---------------- 3. 核心项目与科研经历 ----------------
  section_heading("核心项目与科研经历")
  for proj in projects {
    grid(
      columns: (1fr, auto),
      [
        #text(weight: "bold", size: 8.9pt)[#proj.name]
        #if "tag" in proj and proj.tag != "" [
          #h(5pt) | #h(5pt) #text(fill: accent-color, weight: "bold", size: 8.2pt)[#proj.tag]
        ]
      ],
      [
        #text(fill: text-muted, size: 8.2pt)[#proj.period]
      ]
    )
    v(-3.5pt)
    text(size: 8.0pt, fill: text-muted)[
      #proj.role #h(8pt) [技术栈: #proj.tags.join(" / ")]
    ]
    v(1pt)
    for pt in proj.points {
      [• #pt \ ]
    }
    v(1.8pt)
  }

  // ---------------- 4. 竞赛荣誉与学术成果 ----------------
  section_heading("竞赛荣誉与学术成果")
  if awards.len() > 0 {
    for aw in awards {
      [• #aw \ ]
      v(0.8pt)
    }
  }
  if papers.len() > 0 {
    for pp in papers {
      [• #pp \ ]
    }
  }
}
