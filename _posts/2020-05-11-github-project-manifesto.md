---
title: The GitHub Project Manifesto
description: best practices for organizing LemasLab projects on GitHub
categories: blog
---

We use GitHub to organize LemasLab projects. If you are new to LemasLab, please familiarize yourself with GitHub [github resources post page]. Below are "best practices" for managment and organization of LemasLab informatics projects.
This is a work in progress and will be updated regularly. 

### Why do we need a Project Management Manifesto?
- Inconsistent file and variable names: Returning to a project a few days or even weeks later reveals the difficulty in remembering which files to work with. Additionally, there is often differences between variables and data frames with vague names such as df, df_new, df_new_final and (the dreaded) df_new_final2.
- Inconsistent folder structure: Projects often have common components such as a data folder, datasets with vague names in different stages between raw and clean.
- Wasted Time: Poorly organized and named files increases time to re-running older scripts in order clean my code before moving onto the next step.

What’s worse, all of these problems were compounded when I worked with other people with different file naming conventions and ideas about how to organize a project.
- 