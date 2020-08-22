[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Flemaslab%2Flemaslab.github.io)](https://hits.seeyoufarm.com)

# Lemas Lab

This is the repository for the [Lemas Lab Group](https://lemas-lab-group.github.io/). We use Jekyll to run our Github page. Feel free to fork and make your own page or submit a pull-request!

## Procedure to make change
1. Login your [Github](https://github.com/) account.
2. Fork this repository to your own account.
3. If you are using Windows and have never installed or used Git, please go to [this website](https://git-scm.com/download/win) to install Git first. Otherwise, skip this step.
4. Open command line, direct to the folder in which you want to save the source code of the website. 
5. Clone forked repository to your local machine with the following command line (replace {your account} with your account name):
```
git clone https://github.com/{your account}/lemaslab.github.io.git
```
6. Make appropriate changes to the cloned repository to update information to the webpage.
7. Test if the updated repository can run appropriately on your local machine following the procedure: `Requirements -> Step2 -> Step4` on [this guideline](https://help.github.com/en/articles/setting-up-your-github-pages-site-locally-with-jekyll). 
8. Type the following lines to update the repository:
```
git add -A
```
```
git commit -m '{describe your change}'
```
```
git push
```
9. Go to the webpage of your forked repository, Make a pull request to the original repository and wait for approval by clicking `pull request` (note: this button is beside `compare` button, it is NOT `New pull request` button).

## Add yourself

You can add yourself to the page in `_people` folder just create file name `<your_firstname>_<your_lastname>.md` in the folder. See the following for the template of the content in `<firstname>_<lastname>.md`

```
---
name: Eva Dyer
position: underGradStudent
avatar: eva.jpg
twitter:
joined: 2014
---

<img width="300" src="{{site.baseurl}}/images/people/{{page.avatar}}" data-action="zoom">

### {section_name}
(section content)


```

Detailed procedures to add yourself:
1. Prepare your photo, crop it to W:H=1:1.618.
2. Put your photo to `images/people/` folder and name it to `<your_firstname>_<your_lastname>.jpg`.
3. Open file `_people/<your_firstname>_<your_lastname>.md`, change `name` to your name, `position` to your position (you can choose position from 4 classes including `pi`, `underGradStudent`, `gradStudent`, `researchCoordinator`. Position will put you into section that you choose.), `avatar` to `<your_firstname>_<your_lastname>.jpg`, `joined` to the year you joined the lab.
4. If you have more to tell, you can modify the `{section_name}` and `(section_content)` showing in the template. An example would be:
```
---
name: Eva Dyer
position: underGradStudent
avatar: Eva_Dyer.jpg
twitter:
joined: 2014
---

<img width="300" src="{{site.baseurl}}/images/people/{{page.avatar}}" data-action="zoom">

### Current Project
My current project is about designing a spaceship to prevent alian attack.


```
5. Follow `Procedure to make change` to update the webpage.


## **note: following sections are out dated and will be updated soon**
---
---


## Add posts

It's very easy to add post. All the posts are located in `_posts` folder. It arrangement is based on
date. Each post can be written in markdown format. You just have to state headers before writing: `title`, `description` and `categories`. `description` will be shown when you share on social media like Facebook or twitter. See the following headers:

```
---
title: Summer School in Computational Sensory-Motor Neuroscience (CoSMo)
description: all links to CoSMo summer school in computational neuroscience materials
categories: scientists
---
```

We have 4 categories: `scientists`, `students`, `discussion`, `blog` you can choose and this will be rendered to different location.


## How to add posts


- **Directly edit on Github**, you can simply go to `_posts` and click `New file` then put some markdown file e.g. `2016-02-03-post-name.md` and start writing blog post. Github also allows you to preview it so it's nice for people who don't want to clone the repo. 

- **Clone the repository**, kind of the same as directly add post on Github. You just have to clone the repository. Then add new post file, commit and push to the repo.

The changes will take approximately half a minute to render. You can see the new posts or changes on [Lemas Lab Group](https://lemas-lab-group.github.io/)!

## Add new publications

All publications from the lab are located in `publications.md`. Please upload new publication on your own!
