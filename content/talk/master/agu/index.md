---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "AGU2019: Convolutional Neural Networks for Estimating Atmospherically-forced Sea Level Variations"
event: "American Geophysical Union, Fall Meeting 2019"
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
date: 2019-12-01
date_end:
all_day: true

# Schedule page publish date (NOT talk date).
publishDate: 2023-01-05T12:00:00+01:00

authors: ["Redouane Lguensat", "admin", "Sally Close", "Thierry Penduff"]
tags: ["AGU", "Deep Learning", "Ocean"]

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
url_slides:

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

The variability of sea-level anomalies (SLA) observed by satellite altimeters combines two components: a forced component paced by the atmospheric variability, and an intrinsic and chaotic component emerging from the ocean itself.This work presents a deep convolutional neural network (ConvNet) trained to estimate the forced variability from SLA observations. The ConvNet is trained on the available OCCIPUT 50-member ensemble of global oceanic hindcasts. The use of global SLA fields to train the ConvNet being computationally impossible, representative regions of the ocean dynamics were carefully selected to allow training the ConvNet in an acceptable time.The algorithm yields an estimation of the forced model variability with a 2~cm RMS error and a temporal correlation of 0.9. We compare this performance to that of a bandpass filter proposed recently, and show that our ConvNet has the advantage to adapt its cutoff scales locally and identify larger-scale intrinsic patterns.The algorithm is applied to global altimetric observations, and shown to significantly increase the variance of winter SLA explained by the North Atlantic Oscillation (NAO) index.

https://ui.adsabs.harvard.edu/abs/2019AGUFMGC31L1373L/abstract
