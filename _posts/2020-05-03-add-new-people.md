---
title: How to add yourself and publication to lab page
description: description on how to add yourself to the page
categories: blog
---

Here, we provide some description on how can you add new profile to the page by editing on Github  [LemasLab/LemasLab.github.io](https://lemaslab.github.io/). It's very simple.
You can follow the instruction below. If you have any problem, feel free to ask any lab members.

#### How to add yourself to lab page

You can add yourself to the page in `_people` folder just create file name `<firstname>_<lastname>.md` in the folder. We require few line of header before you start writing your page. See the following

```
---
name: Eva Dyer
position: gradStudent
avatar: Eva_Dryer.jpg
email:
joined: 2014
---

<img width="300" src="{{site.baseurl}}/images/people/{{page.avatar}}" data-action="zoom">

### Current Project
BEACH Project.
```

If you don't have information, just leave it blank. The avatar will bring photo from images/people folder and display it on people page. You can also add photo in your own personal page the same way your add photo in blog post. To make sure that your picture doesn't distort when upload to the webpage, the size requirement is length:width=1:1.618

For position, you can choose position from 4 choices including `gradstudent`, `underGradStudent`, `researchCoordinator`, or `alumni`. It will put you in section that you choose.

#### How to add new publications

All publications from the lab are located in `publications.md`. Please upload new publication on your own!
