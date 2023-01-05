---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "SnowHydro2022: Adaptation of a snow cover scheme for complex topography areas"
event: "3rd International Conference on Snow Hydrology"
event_url: "https://snowhydro2022.sciencesconf.org/"
location: "Online event ! | 1-4 Feb 2022 Grenoble (France)"
address:
  street:
  city:
  region:
  postcode:
  country:
summary:
abstract: "
Snow cover strongly modulates the energy fluxes between the atmosphere and the Earth's surface. Indeed, snow has generally a much higher albedo compared to other surfaces and therefore reduces the amount of solar radiation absorbed by the surface. Moreover, because of its low conductivity, snow isolates the ground from the atmosphere, impacting soil surface temperatures and energy balance (Zhang 2005). In general circulation models (GCMs) the snow cover fraction (SCF) is usually a diagnostic variable derived from other snow quantities, as for instance, the snow water equivalent (SWE) or the snow depth (SD). The relationship between SWE and SCF varies from simple linear relationships to more advanced parameterizations taking into account the snow density allowing to represent the hysteresis effect between the accumulation phase and the more disparate melting phase (e.g., Niu and Yang 2007). Swenson and Lawrence (2012) highlighted strong differences of snow cover extents between plains and mountainous areas, which may be explained by the persistence of snow on the summits whereas a faster melting occurs in the valleys. However, the dependency of SCF on the topography is considered only in a reduced number of GCMs, whereas mountainous areas represent nearly 1/5 of the world's surface area (Huddlestone et al., 2003). In this study, we designed three new snow parameterizations that include the impact of the sub-grid topography on the SCF in the ORCHIDEE land surface model (LSM) coupled to the LMDZ atmospheric model (part of the French GCM of IPSL). This model shows a strong cold bias and an excess of SCF over the High Mountains of Asia (HMA) (Lalande et al., 2021). The new SCF parameterizations are based on the following existing ones: Swenson and Lawrence (2012; hereafter SL12), Roesch et al. (2001; hereafter R01), and a modified version of Niu and Yang (2007; hereafter NY07). These new parameterizations were calibrated over HMA using a high-resolution snow reanalysis (Liu et al., 2021), and compared to a deep learning model trained on the reanalysis dataset. The calibrated parameterizations SL12, R01, and the modified version of NY07 were then tested in coupled ORCHIDEE/LMDZ simulations. Preliminary results show improvements in simulated snow cover in HMA but slight deterioration in other areas. They suggest also that calibration should be extended to other snow covered areas and should include other parameters such as the type of vegetation in particular.
"


# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2022-02-02T09:00:00+02:00
date_end: 2022-02-02T10:30:00+02:00
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: 2022-02-01T14:00:00+02:00

authors: ["admin", "Martin Ménégoz", "Gerhard Krinner", "Catherine Ottlé"]
tags: ["SnowHydro", "Snow", "Parameterization", "High Mountain Asia", "LMDZ", "ORCHIDEE", "GCM"]

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
url_slides: "talk/phd/snowhydro/2022-scf-param/SnowHydro2022_LALANDE.pdf"

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

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vT2UJg050QeNun44bNnQVZnv0gLPSgXocMn27U2Tin10oSAJFsveeZhWZ7cFMbkrK-kdJdMJdHeDaCU/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
