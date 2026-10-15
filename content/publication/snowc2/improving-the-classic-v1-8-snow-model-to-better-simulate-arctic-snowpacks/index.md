---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Improving the CLASSIC (v1.8) snow model to better simulate Arctic snowpacks"
authors: [Mickaël Lalande, Alexandre Roy, Libo Wang, Diana Verseghy, Vincent Vionnet, Florent Dominé, Christophe Kinnard]
date: 2026-10-12T00:00:00+05:00
doi: "https://doi.org/10.5194/gmd-19-9581-2026"

# Schedule page publish date (NOT publication's date).
publishDate: 2026-10-12T00:00:00+05:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "Geoscientific Model Development"
publication_short: "GMD"

abstract: "This study enhances the snow model of the Canadian Land Surface Scheme including Biogeochemical Cycles (CLASSIC), with a particular focus on Arctic environments. Key snow model physics improvements include adjustments to the thermal conductivity at the top of the first soil layer, a revised computation of the temperature at the snow–soil interface (hereafter, bottom snow temperature), and the addition of a windless exchange coefficient in sensible heat flux calculations. Arctic-specific adaptations include blowing-snow sublimation losses, a new snow compaction scheme, and snow thermal conductivity parameterization. Evaluations at seven mid-latitude and alpine sites (SnowMIP sites) and three Arctic sites (Bylot Island, Umiujaq, and Trail Valley Creek) show that these enhancements improve the overall simulated snowpack characteristics and soil temperatures across both SnowMIP and Arctic sites. The revised bottom snow temperature yields better agreement between simulated and observed snow and bottom snow temperatures. The new windless exchange coefficient reduced the surface temperature RMSE from 3.50 to 1.93 °C on average across all sites. The improved snow compaction scheme reduces the snow depth biases from 12.0 to 0.1 cm on average across the Arctic sites and improves the simulated snow densities while not degrading the overall model performance at the SnowMIP sites. Blowing-snow sublimation had a negligible effect at most sites, except at the wind-exposed sites of Umiujaq, Trail Valley Creek, and Senator Beck, decreasing snow depth on average by 2–4 cm. Adding a new snow thermal conductivity parameterization – combined with all previous developments – reduces the RMSE of the simulated soil temperatures from 5.3 to 3.0 °C on average at all Arctic sites. Our new developments demonstrate the ability of a single-layer snow model to reasonably reproduce Arctic bulk snowpack characteristics, while maintaining good performance at the SnowMIP sites. Inherent uncertainties remain in the forcing datasets, especially due to the harsh Arctic environment characterized by strong winds, snow redistribution, frost, and polar night. Future model developments will focus on spatial-scale simulations across the whole Arctic, with particular attention to snow cover fraction parameterizations to better capture sub-grid-scale spatial heterogeneity in Arctic environments."

# Summary. An optional shortened abstract.
summary: "This study enhances a snow model for Arctic environments by improving the heat exchanges within the snowpack and at its interfaces, revising the compaction scheme, and adding consideration of blowing snow sublimation losses. Simulations at ten Arctic, mid-latitude, and Alpine sites show significant reductions in simulated soil and snow temperature biases and improved simulated snow depth and density, which are key features to improve simulated energy, water, and carbon budgets in the Arctic."

tags: ["Snow", "Model", "CLASSIC", "Arctic", "Parameterization", "LSM", "SWE", "Snow Compaction", "Blowing Snow", "Thermal Conductivity"]
categories: []
featured: true

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf: "https://gmd.copernicus.org/articles/19/9581/2026/gmd-19-9581-2026.pdf"
url_code: "https://github.com/mickaellalande/SnowC2"
url_dataset:
url_poster:
url_project: "https://climate.esa.int/en/about-us-new/fellowships/esa-cci-research-fellowship-Mickael-Lalande/"
url_slides:
url_source:
url_video:

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: ["SnowC2"]

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---

**Read the full article:** [Lalande et al. (2026) – Geoscientific Model Development](https://doi.org/10.5194/gmd-19-9581-2026)

**Additional resources:**
- [Supplementary material (PDF)](https://doi.org/10.5194/gmd-19-9581-2026-supplement)
- [CLASSIC model code (GitHub)](https://github.com/mickaellalande/SnowC2-CLASSIC-1D-model)
- [Analysis and figure scripts (GitHub)](https://github.com/mickaellalande/SnowC2-CLASSIC-1D-analysis)

---

### Publication announcement

<iframe src="https://www.linkedin.com/embed/feed/update/urn:li:share:7515895128264347650" width="100%" height="1911" style="max-width: 504px; border: 0;" loading="lazy" title="LinkedIn publication announcement"></iframe>
