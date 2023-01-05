---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "How to Install Jupyter Notebook on a Server?"
subtitle: ""
summary: ""
authors: ["admin"]
tags: ["Python", "Server", "Linux"]
categories: ["Tutorial"]
date: 2021-04-22T10:00:36+02:00
lastmod: 2021-04-22T10:00:36+02:00
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

First of all, I recommend you to look at what your server proposes as a method to launch Jupyter Notebooks. If however their method does not suit your needs and you want to install your own environment, here is the method I use (it works from a Linux workstation, you have to adapt if you are under another OS). This method is not official, nor generic, if you have other tips/methods don't hesitate to share them in the comments below.

## 1. Connect to your server

```bash
ssh -XY -o ServerAliveInterval=60 login@server
```
Think to add the options `-XY` otherwise you won't be able to open Jupyter Notebooks in your browser. `ServerAliveInterval=60` is optional, but it allows you not to get disconnected if you don't have any activity for a while (it depends on servers).

{{% alert note %}}
You can directly make an `alias` in your `bashrc`, so you only have to type the alias in your terminal.
{{% /alert %}}

For example:

```bash
gvim ~/.bashrc

# And add this line at the end or in an alias section if you already have one
alias server='ssh -XY -o ServerAliveInterval=60 login@server'
```

## 2. Install Miniconda

In general, there is not infinite space on the servers and therefore I advise you to install the minimalist version of Anaconda : [Miniconda](https://docs.conda.io/en/latest/miniconda.html), in order to install only what you need.

So first of all, I download Miniconda on the server and install it:

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
```

{{% alert note %}}
During the installation, be careful to change the installation path to avoid installing it in your `home`, otherwise, it may saturate your space very quickly! In general, it is recommended to install it in a `data` space or another where you have more storage space.

`[/home/login/miniconda3] >>> /data/login/miniconda3`
{{% /alert %}}

At the end of the installation, I recommend that you initialize `conda` so that it automatically adds the correct path to your `bashrc` so that you can directly have the conda command available (if you prefer to put these lines somewhere else, you can adapt them).

```bash
Do you wish the installer to initialize Miniconda3
by running conda init? [yes|no]
[no] >>> yes
```

Then update your `bashrc`:

```bash
source ~/.bashrc
```
You should have a `(base)` that should appear in front of your command line.

{{% alert note %}}
If you are not happy, fucked up any step or you are scared... that happens... Just remove the folder `miniconda3` (`rm -r /data/login/miniconda3` or the path you put at the installation step) and then remove the lines that were added in your `bashrc`. Then you can start over or forget about Miniconda forever :p
{{% /alert %}}

## 3. Add [conda-forge](https://conda-forge.org/docs/user/introduction.html) and update your installation (optional but I recommend)

This step is completely optional, but it allows to facilitate the installation of future packages that would not be the basic channel of conda.

```bash
conda config --add channels conda-forge  
conda config --set channel_priority strict  
conda update -n base -c defaults conda  
```
If you want to know more, click on the link in the title.

## 4. Create an environment

I do not recommend that you use your base environment. By experience, it happened to me several times to break this environment without being able to go back and to have to finally reinstall everything. The problem is that when you are not familiar with the environment you don't necessarily make a backup and it is sometimes difficult to get back to something functional!

So here is how I work on my side, I create an environment with the name of my project and a version (for example project_v0):

```bash
conda create -n project_v0
conda activate project_v0
```

Then install all the packages you need, especially `jupyter` (+ `jupyterlab` if you prefer from basic notebooks, which is my case).

I also recommend you to install the [nb_conda_kernels](https://github.com/Anaconda-Platform/nb_conda_kernels) package in each of your environments, which will allow you to switch from one environment to another, directly from your notebooks.

```bash
conda install nb_conda_kernels
```

{{% alert note %}}
Here is an example of an environment I created for my Ph.D.: https://github.com/mickaellalande/PhD/tree/master/envs/phd
{{% /alert %}}

To save and manage your environment, see at the end of this tutorial.

For simplicity, I also recommend that you add the line `conda activate project_v0` to your `bashrc` so you don't have to activate it every time. This should replace the `(base)` with the name of your environment.

## 5. Configure Jupyter

The problem with launching Jupyter on a server is that you will have to make an `ssh` bridge between your machine and the server to open Jupyter directly on your internet browser. So you have to specify to Jupyter not to open a window on the server and to open Jupyter on a specific port (if needed).

There are two ways to do this, either you specify all this in your command when you run Jupyter, or you create a configuration file:

### Command line

Here is an example of a command line (where XXXX would be your port number), but don't run it yet, it would be for later!

```bash
jupyter lab --port XXXX --ip 0.0.0.0 --no-browser
```


### Configuration file

Alternatively, you can put this directly into a configuration file and just run the command `jupyter lab` (or `jupyter notebook`):

```bash
# Create a configuration file and edit it
jupyter notebook --generate-config
gvim ~/.jupyter/jupyter_notebook_config.py

# Uncomment these lines and modify them as follow
c.NotebookApp.allow_origin = '*'
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = XXXX
c.NotebookApp.open_browser = False
```

More informations:
- https://jupyter-notebook.readthedocs.io/en/stable/public_server.html
- https://stackoverflow.com/questions/42848130/why-i-cant-access-remote-jupyter-notebook-server


### Report errors (optionnal)
Optionally you can also send automatically report to Anaconda in case of errors:

```bash
conda config --set report_errors true
```

## 6. Launch a job

This step depends on the server you are on, so find out how to launch an interactive job. Depending on the servers and their security level, it can be more or less complicated (even more so during teleworking if you use intermediate machines!).

Think of adapting the memory you need, because very often jobs are killed if you exceed it.

## 7. Run Jupyter Notebook or Jupyter Lab

Once your job is launched you can now directly run `jupyter lab` or `jupyter notebook` if you configured Jupyter (see above) otherwise:

```bash
jupyter lab --port XXXX --ip 0.0.0.0 --no-browser
```

Then you need to make a tunnel from your own terminal (on your PC, not the server), which is usually a command as:

```bash
ssh -L XXXX:hostname:XXXX login@server
```
with possible other flags as `-fNL` (but I'm not familiar with that, so go and look what you need, ex: https://explainshell.com/explain?cmd=ssh+-L+-N+-f+-l)

Then you can open the link directly given from Jupyter on the server, which will open on your browser.

Here is an example of a script, to get automatically the `ssh` tunnel from one of the servers I use and run jupyter lab (you can inspire yourself from that and adapt it to your needs): {{% staticref "post/tutorial/how-to-install-jupyter-notebook-on-a-server/jupyterlab.sh" "newtab" %}}jupyterlab.sh{{% /staticref %}}.

## 8. Save your environment

Once you have something functional and stable enough. I advise you to save your environment and not to touch it anymore (not even to update it). If you want to update it or install new packages (which would cause version changes in your other packages), in that case I advise you to clone your current environment and do some tests then if you get something stable again, call it with the same project name and increment the version number by making a new backup. This way you can always go back to an old environment and/or rebuild it identically (at least on the machine you were on).

To save your environment here are the different methods I use:

```bash
conda list --explicit > projet_v0.txt
conda env export > projet_v0.yml
conda env export --from-history > projet_v0_fh.yml
```

The first one allows you to have the exact version of packages on the machine you are using and their dependencies, which will allow you to have exactly the same environment (however it might not work on some other machines). The second one is similar to the first one but with the yaml format. The last one allows you to only have the names of the packages you installed with their version number if specified (what I advise you to add otherwise it might not work in the future). This last one allows sharing your environment across different platforms/OS, but without a guaranty that it will work (knowing that some packages are not always available across all platforms) and even on your own machine/server if you didn't specify all version numbers, it's possible that you won't succeed to make it work in the future. Hence I recommend saving your environment under different format/version.

To get more information, go and check the conda documentation: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

I also recommend you to document your environment with a README, so you know how you set it up, what's inside, etc., here is an example from my environment: https://github.com/mickaellalande/PhD/tree/master/envs/phd.

I hope this will help you! I'm not an expert with conda myself, but this is a sharing of the experience I've gained over the past few years. Feel free to ask questions in the comments and/or fill in any points that I haven't explained well or that are missing!
