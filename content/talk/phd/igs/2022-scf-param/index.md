---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "IGS2022: Adaptation of a snow cover scheme for complex topography areas"
event: "International Symposium on Snow 2022"
event_url: "https://www.slf.ch/en/about-the-slf/events-and-courses/international-symposium-on-snow-2022.html"
location: "Davos, September 25 - 30, 2022"
address:
  street:
  city:
  region:
  postcode:
  country:
summary:
abstract: "
Snow cover strongly modulates the energy fluxes between the atmosphere and the Earth’s surface. Indeed, snow has generally a much higher albedo compared to other surfaces and therefore reduces the amount of solar radiation absorbed by the surface. General circulation models (GCMs) usually compute the snow-cover fraction (SCF) as a diagnostic variable derived from other snow quantities, as for instance, the snow water equivalent (SWE) or the snow depth (SD). The relationship between SWE and SCF varies from simple linear relationships to more advanced parameterizations taking into account further parameters, such as snow density, ground roughness lengths, etc. However, only a few GCMs take into account the topography, while Swenson and Lawrence (2012) highlighted strong differences in snow-cover extent between plains and mountainous areas, which may be explained by the persistence of snow on the summits whereas a faster melting occurs in the valleys. In this study, we designed three new snow parameterizations that include the impact of the sub-grid topography on the SCF in the ORCHIDEE land surface model (LSM) coupled to the LMDZ atmospheric model (part of the French GCM of IPSL). This model shows a strong cold bias and an excess of SCF over the High Mountains of Asia (HMA). The new SCF parameterizations are based on the following existing ones: Swenson and Lawrence (2012; hereafter SL12), Roesch et al. (2001; hereafter R01), and a modified version of Niu and Yang (2007; hereafter NY07). These new parameterizations were calibrated over HMA using a high-resolution snow reanalysis, and compared to a deep learning model trained on the reanalysis dataset. The calibrated parameterizations SL12, R01, and the modified version of NY07 were then tested in coupled ORCHIDEE/LMDZ simulations. Preliminary results show improvements in simulated snow cover in HMA but slight deterioration in other areas depending on the model resolution. They suggest also that calibration should be extended to other snow-covered areas and should include other parameters such as the type of vegetation in particular.
"


# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2022-09-27T09:45:00+02:00
date_end: 2022-09-27T10:00:00+02:00
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: 2022-09-23T17:30:00+02:00

authors: ["admin", "Martin Ménégoz", "Gerhard Krinner", "Catherine Ottlé"]
tags: ["IGS", "Snow", "Parameterization", "High Mountain Asia", "LMDZ", "ORCHIDEE", "GCM"]

# Is this a featured talk? (true/false)
featured: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: true

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

# Optional filename of your slides within your talk's folder or a URL.
url_slides: "talk/phd/igs/2022-scf-param/igs22_91A3933_Lalande_compressed.pdf"

url_code: "https://github.com/mickaellalande/PhD/tree/master/SCF_parameterizations"
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
projects: ["PhD"]
---

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vSho0kDEx7_SqPEZSsZflTsc8BrOwijdh4xZsoTWKeivX8uIHLNQGCckvJp3KVKeNC4PAuqEZGqaFPG/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
