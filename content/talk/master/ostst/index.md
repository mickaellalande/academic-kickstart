---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "OST/ST2019: Attenuating the ocean chaotic variability in altimetric observations: from band-pass filtering to machine learning"
event: "Ocean Surface Topography Science Team (OST/ST) Meeting"
event_url:
location:
address:
  street:
  city:
  region:
  postcode:
  country:
summary:
abstract:


# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2019-10-21
date_end:
all_day: true

# Schedule page publish date (NOT talk date).
publishDate: 2023-01-05T12:00:00+01:00

authors: ["Thierry Penduff", "admin", "Redouane Lguensat", "Sally Close", "Sabrina Speich"]
tags: ["OST/ST", "Deep Learning", "Ocean"]

# Is this a featured talk? (true/false)
featured: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

# Optional filename of your slides within your talk's folder or a URL.
url_slides: "https://hal.archives-ouvertes.fr/hal-03000767/file/22-Penduff_Variabilit%25C3%25A9_chaotique_alt_GMMC2019.pdf"

url_code: "https://github.com/mickaellalande/UNetOceanFilter"
url_pdf:
url_video:

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects:
---

The variability of sea-level anomalies (SLA) observed by satellite altimeters combines two components: a forced component paced by the atmospheric variability, and an intrinsic and chaotic component emerging from the ocean itself. This paper presents a Machine Learning algorithm, trained on ensemble simulation outputs, to estimate the forced variability from SLA observations. Our algorithm estimates the forced model variability with a 2&nbsp; cm RMS error and a temporal correlation of 0.9, a skill similar to that of a bandpass filter proposed recently, but with the additional ability to adapt its cutoff scales locally. The algorithm is applied to global altimetric observations, and shown to increase the variance of winter SLA explained by the variance of the North Atlantic Oscillation (NAO) index significantly.

https://hal.archives-ouvertes.fr/hal-03000854/
