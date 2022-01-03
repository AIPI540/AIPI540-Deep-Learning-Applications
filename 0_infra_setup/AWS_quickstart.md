![](https://storage.googleapis.com/aipi_datasets/Duke-AIPI-Logo.png)

# Amazon Web Services Setup

## Table of contents

1. [Introduction](#introduction)
2. [Sign up for AWS](#sign-up-for-aws)
3. [Get your AWS Educate credits](#get-your-aws-educate-credits)
4. [Request an Increase in GPU Quota](#request-an-increase-in-gpu-quota)  
5. [Set Up VM Image](#set-up-vm-image)
6. [Access Your Newly created VM via command line](#access-your-newly-created-vm-via-command-line)
    1. [Transferring Files between your VM and Computer](#transferring-files-between-your-vm-and-computer)
7. [Development Options using your VM](#development-options-using-your-vm)
    1. [Work on Remote Server](#option-1-work-on-remote-server)
    2. [Work in JupyterLab](#option-2-work-in-jupyterlab)
    3. [Work locally and sync via GitHub](#option-3-work-locally-and-sync-via-github)
8. [Other Tips](#other-tips)  
9. [Further Training](#further-training)
    

## Introduction

One option for your team projects and your individual project is to use a GPU instance on Amazon Web Services (AWS).  

### AWS versus Colab

While [Colab](https://research.google.com/colaboratory/faq.html) is useful for your module projects and for the experimentation phase of your individual course project, there are a few reasons you will likely want to use AWS or another cloud platform rather than Colab for your course project:  
 1) Colab is not designed to deploy code into production.  Since you are required to develop an interface for your course project, Colab will not be able to support your production app.  Note: you may be able to train your model on Colab and deploy on something else like Heroku.  
 2) You may find that you need a dedicated GPU instance to train on large datasets for your course project, and perhaps for your module projects as well (depending on what data you are using).  Colab will disconnect after 12 hours or ~30 min of idling (and you will lose your unsaved data). A AWS VM instance will not disconnect untill you stop it (or run out of credits).  AWS also allows you to choose the type and number of GPUs to use, while Colab does not.
 3) A AWS VM instance's disk space allows you to deal with larger datasets. In Colab's case, you will have to save all your data and models to Google Drive.

## Sign Up for AWS
Follow the [instructions](https://portal.aws.amazon.com/billing/signup?#/start) to set up a new AWS account.  **Use your personal email rather than your Duke email to set up the account**.  You will also need to input a credit card for billing, although you will receive some free credits from AWS Educate which will be applied to your account and used first, before AWS charges your credit card.  Select "Personal account" rather than "Business account".  When you get to the page titled "Select a support plan", select "Basic support - free".

Next, log in to your console using the credentials you just created.  At the top right, click on your username and in the dropdown you should see your account number.  Note it down somewhere as you will need it for the next step.

## Get your AWS Educate credits
By joining AWS Educate you will receive $100 free credits to use.  First, go to the [AWS Educate page](https://aws.amazon.com/education/awseducate/) and click "Join AWS Educate".  When registering, **be sure to use your Duke email address** so they can verify you are a student.   

After submitting your request you will be contacted by email with approval of your request to join AWS Educate.  You will then be able to access a coupon code which you can apply the $100 credits to your existing AWS account.  Note: DO NOT start a new "AWS Starter Account" as the starter account does not allow access to GPU VM instances.  Instead, you want to apply your credits to your existing AWS account.

## Request an Increase in GPU Quota
By default new AWS accounts do not come with quota to use GPU.  You will have to request a quota increase before you will be able to launch a VM instance with GPU.

To request an increase, from the **Services** menu at top click on **Compute** -> **EC2**.  Then click on **Limits** in the left menu and in the search bar type "G instances".  Then, click on "Running On-Demand All G and VT instances". This will request an increase in quote t ouse G instances including G4dn, which uses NVIDIA T4 GPUs.  If you instead would like to use NVIDIA K80 GPUs, you can request an icnrease to your quota for P instances.

You can review the options [here](https://aws.amazon.com/ec2/instance-types/#Accelerated_Computing).  Pricing for each instance type is contained in the [AWS on-demand pricing guide](https://aws.amazon.com/ec2/pricing/on-demand/).  I recommend using either a G4dn (NVIDIA T4 GPUs) or a P2 (NVIDIA K80 GPUs) instance.

![](.img/aws_requestincrease1.png)

For "Primary instance type" select "All G instances" (or all P instances) and for "New limit value" select 4 vCPUs (or more).


For the "Use case description" in the request form, I recommend writing something like "Using AWS for project work in Duke University graduate AI course AIPI 540".

After you submit your request, it may take several hours or days for Amazon to process it, but when finished you will be notified and can proceed with the next steps.

## Set Up VM Image
To set up your VM, follow the steps in the [Launch an AWS Deep Learning AMI guide](https://aws.amazon.com/getting-started/hands-on/get-started-dlami/).  On step 2d in the guide you will need to choose a GPU instance type.  You can review the options [here](https://aws.amazon.com/ec2/instance-types/#Accelerated_Computing).  Pricing for each instance type is contained in the [AWS on-demand pricing guide](https://aws.amazon.com/ec2/pricing/on-demand/).  I recommend using either a G4dn (NVIDIA T4 GPUs) or a P2 (NVIDIA K80 GPUs) instance.


## Access Your Newly Created VM via command line
If connecting to your instance for the first time, follow the steps in the [Launch an AWS Deep Learning AMI guide](https://aws.amazon.com/getting-started/hands-on/get-started-dlami/).  

After you have connected for the first time via the method in the guide, you can connect going forward by starting your instance on the AWS console and then running the following:
 ```
ssh -L localhost:8888:localhost:8888 ubuntu@<your-instance-DNS>
 ```
Be sure to replace `<your-instance-DNS>` with the public DNS for your instance which can be found on the right column of the Description tab in the Instances page.

After you are connected, you can install git, pip and any needed packages that are not pre-installed in the VM.

```
sudo apt update
sudo apt install python3-pip
sudo apt -y install git
```

### Transferring Files between your VM and Computer
You can transfer local files to your VM using scp, so if you choose to do your development locally on your computer you can then transfer the code and data files to your VM to run.

```
scp -i <path-to-file-on-computer> ubuntu@<your-instance-DNS>
```

## Development Options using your VM
There are several different ways to use your new VM as part of your development workflow.  Here are a few possibilities:

### Option 1: Work on Remote Server
You can develop your code on the remote server directly if you are comfortable with Vim or Emacs.  There is a learning curve for each of them, so it's up to you if it is something you would like to invest your time in learning or not.  If you would like to work remotely on the server, here is a [getting started guide for Vim](https://opensource.com/article/19/3/getting-started-vim) and here is a similar [guide for Emacs](https://opensource.com/article/20/3/getting-started-emacs).

**If you chose to work using the VM, be aware that you will be charged credits for the time your VM is running - meaning while you are working, not just while you are training a model.** 

### Option 2: Work in JupyterLab
You can also use JupyterLab on your VM (may first need to run `pip install jupyterlab` after connecting to your VM), which provides access to run Jupyter Notebooks, a Python file editor, and terminal access.  

**If you chose to work using the VM, be aware that you will be charged credits for the time your VM is running - meaning while you are working, not just while you are training a model.**

### Option 3: Work locally and sync via GitHub
Alternatively, you can develop locally on your favorite editor, push to your repo on Github, and pull on the remote server using terminal or via JupyterLab (or copy the files to the remote server per the above instructions, but a better practice is to use GitHub for version control).

The benefit of this option is that you are not charged credits for working time (until you need to train your model), or run the risk of forgetting to turn your instance off when you step away from my computer.  The downside of this is the extra step of syncing your work via GitHub to the VM, and also that you will not be able to train your model from your local development environment and will need to switch over to your VM to train when ready (assuming it requires GPU).  You may also not be able to access your data while developing, if it resides on GCP unless you maintain a local copy as well.

## Other Tips
1) ### REMINDER: Make sure you stop your instances!
    Don't forget to stop your instance when you are done (by clicking on the stop button at the top of the page showing your instances). You can restart your instance and your saved files will still be available.


## Further Training
- [AWS Cloud Practitioner Essentials](https://www.amazon.com/dp/B09HSJ6HN8/ref=s9_acsd_al_bw_c2_x_0_t?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-11&pf_rd_r=SVREMD4A2EGWAQJA1W4H&pf_rd_t=101&pf_rd_p=5548c913-bd6e-44e8-b574-8f716ad2757c&pf_rd_i=14297978011)  
    - 6 hour introduction to cloud computing using AWS
    - Highly recommended place to start
- [Exploring the AWS ML Toolset](https://explore.skillbuilder.aws/learn/course/external/view/elearning/325/exploring-the-machine-learning-toolset?b96ab75c-93e7-4732-bcac-14a210fe9dce=)  
    - 2.5hr introduction to the tools avaiable on AWS for developing ML models
- [AWS ML Ramp-Up Guide](https://d1.awsstatic.com/training-and-certification/ramp-up_guides/Ramp-Up_Guide_Machine_Learning.pdf)  
    - Includes a recommended set of learning resources for getting started and ramping up with using AWS for ML  
    - Many of the suggested resources are free but some are paid
- [Full list of available free AWS trainings](https://www.amazon.com/b/?node=14297978011)  
    - Search the entire library of AWS free digital training sessions