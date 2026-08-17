#let resume(
  name: "",
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
  set page(
    paper: "a4",
    margin: (x: 1.4cm, top: 1.2cm, bottom: 1.2cm),
  )
  set text(
    font: ("PingFang SC", "Heiti SC", "Arial"),
    size: 9.2pt,
    lang: "zh",
    fill: rgb("#1f2328")
  )
  set par(justify: true, leading: 0.52em)

  // Header
  align(center)[
    #text(size: 17pt, weight: "bold", fill: rgb("#0969da"))[#name] \
    #v(3pt)
    #text(size: 10.5pt, weight: "medium", fill: rgb("#424a53"))[#title] \
    #v(3pt)
    #text(size: 8.8pt, fill: rgb("#57606a"))[
      #if phone != "" [#phone #h(6pt)|#h(6pt)]
      #if email != "" [#link("mailto:" + email)[#email] #h(6pt)|#h(6pt)]
      #if location != "" [#location #h(6pt)|#h(6pt)]
      #if github != "" [#link(github)[GitHub] #h(6pt)|#h(6pt)]
      #if blog != "" [#link(blog)[Blog]]
    ]
  ]
  v(3pt)
  line(length: 100%, stroke: 0.8pt + rgb("#0969da"))
  v(1pt)

  // Section Header Helper
  let section_heading(t) = {
    v(5pt)
    text(size: 10.5pt, weight: "bold", fill: rgb("#0969da"))[#t]
    v(-3pt)
    line(length: 100%, stroke: 0.5pt + rgb("#d0d7de"))
    v(2pt)
  }

  // 1. 教育背景
  section_heading("教育背景")
  for edu in education {
    grid(
      columns: (1fr, auto),
      [*#edu.school* · #edu.degree],
      [#text(fill: rgb("#57606a"))[#edu.period]]
    )
    v(-3pt)
    text(size: 8.5pt, fill: rgb("#424a53"))[
      #if "gpa" in edu [GPA: #edu.gpa #h(8pt)]
      #if "advisor" in edu [导师: #edu.advisor #h(8pt)]
      #if "honors" in edu [荣誉: #edu.honors.join("、")]
    ]
    v(2pt)
  }

  // 2. 专业技能
  section_heading("专业技能")
  for sk in skills {
    [- *#sk.title*：#sk.description]
  }

  // 3. 核心项目与科研
  section_heading("核心项目与科研经历")
  for proj in projects {
    grid(
      columns: (1fr, auto),
      [*#proj.name* #if "tag" in proj [ | #text(fill: rgb("#0969da"), weight: "medium")[#proj.tag]]],
      [#text(fill: rgb("#57606a"))[#proj.period]]
    )
    v(-3pt)
    text(size: 8.5pt, fill: rgb("#57606a"))[#proj.role #h(8pt) 技术栈: #proj.tags.join(", ")]
    v(1pt)
    for pt in proj.points {
      [- #pt]
    }
    v(2pt)
  }

  // 4. 竞赛荣誉与论文发表
  section_heading("竞赛荣誉与学术成果")
  if awards.len() > 0 {
    [- *竞赛荣誉*：#awards.join("； ")。]
  }
  if papers.len() > 0 {
    [- *学术成果*：#papers.join("； ")。]
  }
}
