---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "How to Create an Academic/Wowchemy/Hugo Blox GitHub Page With Hugo?"
subtitle: ""
summary: " "
authors: ["admin"]
tags: ["Website", "GitHub"]
categories: ["Tutorial"]
date: 2020-05-19T11:38:58+02:00
lastmod: 2020-05-19T11:38:58+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: ["Tutorials"]
---

{{% alert warning %}}
Be aware that Academic theme seems to have become ~~Wowchemy~~ [Hugo Blox](https://hugoblox.com/) (definitely it keeps changing...), hence this tutorial might be outdated. Nevertheless, it can be used as a basis, but please refer to the Wowchemy documentation first. I updated all the links below to refer to their new websites.
{{% /alert %}}

I guess you are wondering how to make an academic website on your GitHub with the address *.github.io*. There are, of course, the solutions proposed directly by [GitHub page](https://pages.github.com/), however, it looks a bit *"old school"* in my opinion. Another option is to make the site by yourself in markdown, but it seemed quite long and tedious. I finally came across ~~Wowchemy~~ [Hugo Blox](https://hugoblox.com/)[^1] for [Hugo](https://gohugo.io/)^2 which suits my needs and is the purpose of this tutorial! Feel free to leave a comment if you have any questions and/or additional information.

{{% alert note %}}
You need to be a bit familiar with the basics of GitHub, but you don't need any knowledge of html/css.
{{% /alert %}}

## 1. Make a GitHub page

You can directly follow the instructions on their page: https://pages.github.com/.

The important is to create the repository `your-name.github.io`, and then we will update the content of this repository automatically with a ~~Wowchemy~~ [Hugo Blox](https://hugoblox.com/) Academic template.

## 2. Install Academic Theme and Hugo

Again you'll find the steps on their website: https://docs.hugoblox.com/reference/deployment/#github-pages

{{% alert note %}}
There are different ways to install the Academic theme. The recommended installation will automatically deploy it on a free server, and I didn't find a way to link it to the GitHub page later, so I recommend following the Git installation from the link above.
{{% /alert %}}

### Install Hugo

I had some trouble with installing [**Hugo with Homebrew on Linux**](https://gohugo.io/getting-started/installing/#quick-install)**.** If you do have the same problem, I advise you to try to install it with the [**snap version**](https://gohugo.io/getting-started/installing/#snap-package) (don't install it with **apt-get** because the version is not updated: see this [issue](https://github.com/gcushen/hugo-academic/issues/703)). All this Academic theme is based on the [Hugo Framework](https://gohugo.io/) so it is necessary to install it.

### [Fork](https://github.com/HugoBlox/theme-academic-cv#fork-destination-box) the *Academic Kickstart* repository

{{% alert warning %}}
The new repository name is: ~~`wowchemy/starter-hugo-academic`~~ `HugoBlox/theme-academic-cv`, so replace `academic-kickstart` by ~~`starter-hugo-academic`~~ `theme-academic-cv` in the following paragraph.
{{% /alert %}}

{{< figure src="academic.jpg" title="" lightbox="true" >}}

It will automatically create a new repository `academic-kickstart` in your GitHub account. This repository will allow you to manage your website, and then publish it into the previously created repository `your-name.github.io``. Finally, you just need to clone and initialize the theme on your computer:

```bash
git clone https://github.com/your-name/academic-kickstart.git
cd academic-kickstart
git submodule update --init --recursive
```



## 3. Deploy your website on your GitHub page

We need now to add `your-name.github.io` repository as a submodule inside the **public** folder of the `academic-kickstart` repository as explained in this [documentation](https://wowchemy.com/docs/hugo-tutorials/deployment/#github-pages).

{{% alert warning %}}
The method below seems outdated, so follow the link above.
{{% /alert %}}

```bash
git submodule add -f -b master https://github.com/your-name/your-name.github.io.git public
```

Then you need to generate the website with the `hugo` command. First, you can commit and push your changes from the `academic-kickstart` repository on GitHub and then do the same for the `your-name.github.io` submodule and your website will be available online!

```bash
git add .
git commit -m "Initial commit"
git push -u origin master

hugo # Generate the website inside the public directory
cd public
git add .
git commit -m "Build website"
git push origin master
cd ..
```

You can easily make this automatic with a bash script for the future, for example: [update.sh](https://github.com/mickaellalande/academic-kickstart/blob/master/update.sh), and then you only have to write: `sh update.sh your_commit_message`.

## 4. Update your content and customize your page

You can then follow the documentation *[Getting Started With the Page Builder](https://wowchemy.com/docs/getting-started/page-builder/)* and *[Customization](https://wowchemy.com/docs/getting-started/customization/)*, where you'll find all the information! Before to start updating, launch the **hugo server** from your local `academic-kickstart` folder with the command:

```bash
hugo server
```

you will be able to have an instant preview in your browser before uploading it to GitHub. If you don't know any editing software, I can advise you [Atom](https://atom.io/) in combination with [typora](https://www.typora.io/) which is convenient for directly editing the content with markdown.



[^1]: Source Themes Academic 4.8.0
[^2]: Hugo Static Site Generator v0.70.0/extended linux/amd64 BuildDate: 2020-05-13T17:30:34Z
