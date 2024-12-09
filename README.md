![](https://storage.googleapis.com/aipi_datasets/Duke-AIPI-Logo.png)

# AIPI 540: Deep Learning Applications 
Welcome to the GitHub repo for AIPI 540: Deep Learning Applications at Duke University.  This repo accompanies the Deep Learning Applications course, which is part of [Duke's AI Master of Engineering program](https://ai.meng.duke.edu).  
The course was originally designed by [Jon Reifschneider](https://ai.meng.duke.edu/faculty/jon-reifschneider) and modified by [Dr. Brinnae Bent](https://scholars.duke.edu/person/brinnae.bent). Please see the course Canvas site for the course syllabus.

This course contains three modules on the key areas of application of deep learning: computer vision, natural language processing, and recommendation systems.  Each module begins with a discussion of the theory behind the main techniques and architectures used in the application area and why they work, following by hands-on exploration of the key applications in Python.  Students complete a team project during each module as well as an individual course-long project which culminates in a prototype web app incorporating deep learning.

This repo contains notebooks with code examples which accompany the course.  The purpose of the notebooks is to demonstrate the application of many of the methods and model architectures we cover in the course.  For purposes of demonstration, most of the notebooks use small illustrative example datasets, but the approaches shown can be applied to tackle unstructured data problems at scale.

## Repo Organization
This repository contains the following directories:  
- **0_infra_setup**: contains cheat sheet instructions and code examples for setting up deep learning VMs on the major cloud platforms
- **1_intro_neuralnets**: demo examples of how to train fully connected neural networks in PyTorch  
- **2_computer_vision**: demo examples of main computer vision tasks in PyTorch  
- **3_nlp**: demo examples of main natural language processing tasks 
- **4_recommender_systems**: demo examples of recommendation systems  
- **5_deployment**: simple examples of deploying web apps on the cloud

## Getting Started
Before you can run the demo notebooks or work on your projects, you will need to get your computing environment set up.  Because most of the applications we cover will require GPU access for training, you will need to set up a cloud compute environment to run them.  You may choose to work entirely in the cloud, or develop locally and sync to your cloud environment through GitHub.

In this class you may use AWS, Azure, Google Cloud Platform, and/or Google Colab Pro.  We recommend using Colab Pro for running the demo notebooks due to its low cost, however you will also need to work on one of the other three full cloud platforms to do your projects.  Which one you select is up to you - if you do not have a strong preference we recommend using Google Cloud Platform, as it provides the maximum amount of free credits.

To get started, first set up your local environment for work by creating an environment and installing the necessary packages for this course following the [setting_up_environment quickstart guide](https://github.com/AIPI540/AIPI540-Deep-Learning-Applications/blob/main/0_infra_setup/setting_up_environment.md).

Then, go to the [0_infra_setup](https://github.com/AIPI540/AIPI540-Deep-Learning-Applications/tree/main/0_infra_setup) directory and follow the quickstart guide instructions for your choice of cloud platform to set up your cloud environment.

## Thank You
We extend a special thank you to our two course sponsors:  
- **Google** for their support of this course through the Google Cloud Education Grant, which provides free GCP credits for our students  
- **Microsoft** for their support of our course through their Azure Education Sponsorship, which allows us to provide free Azure credits for students in the course to use

## Additional References
In this course we will be building software applications, primarily using Python.  Many students have never built software before, and some may be somewhat new to programming in general.  If that is you, do not fear - it may take a bit of extra effort but you can be successful in this course.

There are a number of linked references throughout this repo which you can explore for information.  In addition, if you are new to software development here are several resources which I highly recommend reviewing early in the semester:  
- [Python PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)  
    - This course uses Python as the primary language of the course.  Understanding how to write clean, pythonic code is important for both the course and your future work in industry.
- [BASH Basics](https://towardsdatascience.com/basics-of-bash-for-beginners-92e53a4c117a)  
    - Review of the BASH commands to handle basic operations
- [Intro to Git and GitHub](https://docs.github.com/en/get-started/using-git/about-git)  
    - You should be familiar with Git/GitHub from your previous AIPI courses, but just in case...
- [Structuring your Python project](https://docs.python-guide.org/writing/structure/)  
    - Best practices in setting up your project repo
- [Python application layouts](https://realpython.com/python-application-layouts/)  
    - Reference showing recommended project structures for different types of Python projects.  See the **5_deployment** directory for a couple simple example web app layouts
- [The 12 Factor App](https://12factor.net)  
    - A popular set of guiding principles for building web apps in any language.  Keep these in mind as you build your projects








