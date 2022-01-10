![](https://storage.googleapis.com/aipi_datasets/Duke-AIPI-Logo.png)

# Google Cloud Platform Setup

## Table of contents

1. [Introduction](#introduction)
2. [Create and Configure Your Account](#create-and-configure-your-account)
    1. [Sign Up for GCP](#sign-up-for-gcp)
    2. [Configure Your Project](#configure-your-project)
3. [Get the AIPI GCP credits](#get-the-aipi-gcp-credits)
4. [Request an Increase in GPU Quota](#request-an-increase-in-gpu-quota)  
    1. [Why don't I See Any GPU-related Quota](#why-dont-i-see-any-gpu-related-quota)
5. [Set Up Google Cloud VM Image](#set-up-google-cloud-vm-image)
    1. [Customize VM Hardware](#customize-vm-hardware)
6. [Access Your Newly created VM via command line](#access-your-newly-created-vm-via-command-line)
    1. [Install gcloud command-line Tools](#install-gcloud-command-line-tools)
    2. [Connect to VM](#connect-to-vm)
    3. [Transferring Files between your VM and Computer](#transferring-files-between-your-vm-and-computer)
7. [Development Options using your VM](#development-options-using-your-vm)
    1. [Work on Remote Server](#option-1-work-on-remote-server)
    2. [Work in JupyterLab](#option-2-work-in-jupyterlab)
    3. [Work locally and sync via GitHub](#option-3-work-locally-and-sync-via-github)
8. [Other Tips](#other-tips)
9. [Further Training](#further-training)
10. [Google Cloud Certifications](#google-cloud-certifications)
    
This tutorial includes a few portions from the GCP setup guide of [Stanford's CS231n](https://github.com/cs231n/gcloud).  However, please make sure to follow the directions here rather than the Stanford one, as they differ significantly in some parts of the workflow.

## Introduction

One option for your team projects and your individual project is to use a GPU instance on Google Cloud Platform (GCP).  One of the main advantages of GCP relative to AWS and Azure is that Google offers a significant amount of free credits to new users, which should be enough to cover your compute expenses throughout the semester.

### GCP versus Colab

While [Colab](https://research.google.com/colaboratory/faq.html) is useful for your module projects and for the experimentation phase of your individual course project, there are a few reasons you will likely want to use GCP or another cloud platform rather than Colab for your course project:  
 1) Colab is not designed to deploy code into production.  Since you are required to develop an interface for your course project, Colab will not be able to support your production app.  Note: you may be able to train your model on Colab and deploy on something else like Heroku.  
 2) You may find that you need a dedicated GPU instance to train on large datasets for your course project, and perhaps for your module projects as well (depending on what data you are using).  Colab will disconnect after 12 hours or ~30 min of idling (and you will lose your unsaved data). A GCP VM instance will not disconnect untill you stop it (or run out of credits).  GCP also allows you to choose the type and number of GPUs to use, while Colab does not.
 3) A GCP VM instance's disk space allows you to deal with larger datasets. In Colab's case, you will have to save all your data and models to Google Drive.

## Create and Configure Your Account

**You should use your personal Gmail account for GCP, not your Duke account, because Duke University managed email accounts do not support creating a new project.** 

For the class project, we offer students **$50 GCP coupons** for each student to use Google Compute Engine for developing and testing your
implementations. When you first sign up on GCP, you will have $300 free credits.

If your credits ends up not being enough, contact course staff on Piazza. We will also send out forms for extra GCP credit request form later in the quarter.
 
This tutorial lists the necessary steps of working on the projects using Google Cloud. Please take your time and go through each step in order - you may find that it can take up to an hour to complete.  If you have any questions please post them in the proper Ed Discussions channel.

When you first sign up for GCP using your Gmail address you will receive $300 free credits from Google to use for storage and compute expenses.  In order to use your credits for GPU access, note that you need to UPGRADE your account into a full account (and enter your credit card) - more on this later.  Additionally, for AIPI 540 students I am able to provide coupons for an extra **$50 GCP credits**, so you will have $350 of credits to spend during the semester before you have to pay out of your own pocket for anything.  This should be enough to get you through your work this semester, ***as long as you do not forget to stop your instances when done work***, otherwise the instance will continue to spend your credits even when you are not using it.

### Sign Up for GCP

You should receive $300 credits from Google when you first sign up with **Personal Gmail** and **also UPGRADE it into a full account**. 

1. Create a Google Cloud account by going to the [Google Cloud homepage](https://cloud.google.com/). Click on the blue **Get Started for free** button, and sign into your Gmail account
![](.img/launching-screen.png)

2. Choose **Account type** to be **Individual**. You will then fill in your name, address and credit card information.
![](.img/register-info.png)

3. Click the "Google Cloud Platform" (in red circle), and it will take you to the main project dashboard for a new project it has automatically set up for you.  You can set up multiple projects, or do your work all under one project.
![](.img/welcome-screen.png)

### Configure Your Project 

1. On the main project dashboard, you can change the name of your project by clicking **Go to project settings**. 
![](.img/dashboard-screen.png)

2. To add project collaborators (e.g. for your module projects), click **ADD PEOPLE TO THIS PROJECT**. Add their email and make their role owners. 
![](/.img/add-people.png)

3. **Upgrade your account** in order to use GPUs following these [instructions](https://cloud.google.com/free/docs/gcp-free-tier#how-to-upgrade). Otherwise [Google Cloud Free Tier](https://cloud.google.com/free/docs/gcp-free-tier#how-to-upgrade) does not allow you to spend your credits on GPU usage.
![](/.img/upgrade-1.png)
![](/.img/upgrade-2.png)

## Get the AIPI GCP credits 

NOTE: You should have created and logged in your GCP account registered with your personal gmail account by now. 

1. I will share the link with you to access the $50 AIPI credits. **It requires your Duke email to receive the credits**. (These credits can be **applied to your GCP account registered with your personal Gmail**. )
![](/.img/get-coupon.png)

2. After submission, you should receive a email from GCP with a link to confirm your email address. Click the link to verify your Duke email.
![](/.img/email-confirmation.png)

3. You will soon receive another email from GCP with a link that applies the $50 credits to your account. That link will jump to your [Billing](https://console.cloud.google.com/billing) page where you should see you have linked to your AIPI billing account with $50 free credits. 
![](/.img/accept-credits.png)
![](/.img/billing-page.png)

4. Google Cloud does not allow you to combine credits (i.e. you cannot combine the $300 credits and the $50 credits), so instead what you need to do is to use the $300 credits first that you receive upon sign-up, and then switch to the AIPI billing account to use the $50 credits.  You can see how to switch billing accounts in the [GCloud documentation](https://cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project).

## Request an Increase in GPU Quota

New GCP accounts do not come with quota to use GPUs. You have to explicitly request it in **IAM & Admin** > **Quotas**. 

**Please request the quota increase ASAP**, because they will take between a couple minutes up to a week to process!  If you don't have GPU quota, you will have to create a CPU-only VM first and create another GPU VM instance later.

You will need to change your quota for **GPU (all regions)**.  You can change your GPU quota on the [Quotas page](https://console.cloud.google.com/iam-admin/quotas).

![](.img/gcp_increasequota.png)

1. Click the **Filter** button and then select **Quota** from the drop-down menu.  Then select (or type) **GPUs (all regions)**.  If you do not see any options for GPU quotas, you may not yet have Compute Engine API Services enabled on your new project.  Click on the top left icon for the Navigation Menu dropdown, then select "Compute Engine".  If you get a "Failed to load" error, wait 5-10 minutes and then try again to view it.  If the screen now populates, go back to **IAM & Admin** > **Quotas** and check again for GPU in the filter.

2. Select the checkbox to the left of the first item in the table (Compute Engine API service, GPUs (all regions Quota), and click **EDIT QUOTAS**. Set the **New limit** to 1, and in the **Request description** put "Duke AIPI class project".  Click **Submit request**

3. Wait until GCP sends you a second email (first email is just to notify they receive the request) that looks like this. It could take couple minutes to couple days for them to approve.
![](.img/gpu-quota-approved.png) 

### Why don't I See Any GPU-related Quota

1. First, make sure you have upgraded your free tier account to a full account following these [instructions](https://cloud.google.com/free/docs/gcp-free-tier#how-to-upgrade).

2. If you just registered a Google Cloud account, it may take time for GCP to set up the Compute Engine API services (this is the service that provides GPU access, so the GPU quota won't show up before it is ready). You may also need to log out and back in.

3. For region-specific GPUs: Check that you have a default zone and region set under **Compute Engine** > **Settings** > **Region** / **Zone**. Some zones do not have certain GPU resources. Check [pricing and spec for GCP GPUs](https://cloud.google.com/compute/gpus-pricing) to find the availability of GPU resources. You can pick a region to use - I recommend using one with wide GPU type availability such as us-central1

More instructions on increasing your GPU quote can be found at the following links: [General quota instructions](https://cloud.google.com/compute/quotas#requesting_additional_quota).


## Set Up Google Cloud VM Image
Note: the below instructions cover how to set up a non-preemptible instance.  If you would instead like to set up a preemptible instance, see the section [Other Tips](#other-tips) at bottom of the document.  A preemptible instance means that Google can shut off your VM at any time if it needs to use the compute capacity for other customers.  The main advantage of a preemtible instance is that is can be much cheaper for GPU usage, although it can also be very frustrating if your VM is shut down in the middle of hours-long model training.  I recommend using a non-preemptible instance and then switching your configuration to use GPU only when you need it for model training, and not while writing code, to save credits.

### Customize VM Hardware 
To set up a PyTorch VM instance with GPU support, follow the instructions on [this page](https://cloud.google.com/deep-learning-vm/docs/pytorch_start_instance).

1. Go to [the gcloud marketplace](https://console.cloud.google.com/marketplace/product/click-to-deploy-images/deeplearning). You may be taken to a page where you have to click on "Launch", and then you should see a configuration sheet with the title "New Deep Learning VM deployment".
2. Choose a [Zone](https://cloud.google.com/compute/docs/gpus/gpu-regions-zones?hl=en_US).  You can pick any region, but I recommend using one with wide GPU type availability such as us-central1-a
2. Create a name for your instance in the `Deployment name` field.
3. In `Machine configuration` click the GPU tab
4. For `GPU type`, `NVIDIA Tesla K80` is typically enough, or you can also use `NVIDIA Tesla P4`. `P100` and `V100` are much more expensive (check the price on the right), but also faster and has larger memory. Check [pricing and spec for GCP GPUs](https://cloud.google.com/compute/gpus-pricing). For number of GPUs, 1 should be enough but for significant jobs you can also use more to parallelize (if you have requested a higher quota, and keep it mind it gets much more expensive)
    **GPU drivers and CUDA will be automatically installed _only if_ you select at least 1 GPU**.
5. In `Machine Type` choose your desired number of CPUs and memory (if you are unsure, keep the default). 
6. In `Frameworks` field, choose `PyTorch 1.10 (CUDA 11.0)` or whatever the latest PyTorch version is (unless you want to set up an instance with TensorFlow)
7. Check the box `Install NVIDIA GPU driver automatically on first startup?`.
8. Check the box `Enable access to JupyterLab via URL instead of SSH. (Beta)`.
9. Leave all other options as default.
10. Click to accept the terms and click the blue botton `Deploy` at the end of the page. After deploying, which will take a few minutes, it will **automatically start your instance**, so if you don't need to use it now, **stop it immediately**.  If you see a green check mark next to the instance, that means it is running (and charging you credits).

Wait until the deployment is finished. You should see a running VM with a green checkmark next to it on your [Compute Engine page](https://console.cloud.google.com/compute/).  Click "STOP" at top to stop the instance.

Your configuration sheet should look similar to below image. 
![](.img/setup_vm.png)


#### Change Configuration on Already Created VM Instances
1. You can always change number of CPUs, number of GPUs, CPU memory, and GPU type **after your VM has been created**. 

2. Just stop your instance, go to your VM instance's details at **Compute Engine** > **VM instances** > [click on instance name]. 

3. Click "edit" on your VM's page to modify the settings. Finally click "Save".

## Access Your Newly Created VM via command line

Now that you have created your VM, you want to be able to connect to it from your computer. This section goes over how to do that using the command line. 

### Install gcloud command-line Tools
To access [gcloud commands](https://cloud.google.com/sdk/docs/cheatsheet) in your local terminal, install the [Google Cloud SDK](https://cloud.google.com/sdk/docs) that is appropriate for your platform and follow their instructions. 

If `gcloud` command is not in your system path after installation, you can also reference it by its full path `/<DIRECTORY-WHERE-GOOGLE-CLOUD-IS-INSTALLED>/bin/gcloud`. See [this page](https://cloud.google.com/compute/docs/instances/connecting-to-instance "Title") for more detailed instructions.

Now, follow the "Initializing the Cloud SDK" section of the [Getting Started with Cloud SDK page](https://cloud.google.com/sdk/docs/quickstart).

### Connect to VM

Go to your VM instance details page by clicking on its name. Start the VM instance first. Once it has a green check mark on, click on the drop-down arrow and select `View gcloud command` instead to retrieve the terminal command. It should look like

```bash
gcloud beta compute ssh --zone "us-central1-a" "<YOUR_VM_NAME>" --project "<YOUR_PROJECT_ID>" 
```

![](.img/connect-to-vm.png)

Paste the above gcloud command into your terminal to connect to your VM.

You should now be logged into your VM and be able to run `nvidia-smi` in the terminal and see the list of attached GPUs and their usage statistics. Run `watch nvidia-smi` to monitor your GPU usage in real time.

### Transferring Files between your VM and Computer

For instance, to transfer `file.zip` from GCE instance to your local laptop. There is an [easy command](https://cloud.google.com/sdk/gcloud/reference/compute/scp) for this purpose:

```
gcloud compute scp <user>@<instance-name>:/path/to/file.zip /local/path
```

For example, to download files from our instance to the current folder:

```
gcloud compute scp tonystark@cs231n:/home/shared/file.zip .
```

The transfer works in both directions. To upload a file to your instance:

```
gcloud compute scp /my/local/file tonystark@cs231n:/home/shared/
```

If you would like to transfer an entire folder, you will need to add a resursive flag: 
```
gcloud compute scp --recursive /my/local/folder tonystark@cs231n:/home/shared/
```

## Development Options using your VM
There are several different ways to use your new VM as part of your development workflow.  Here are a few possibilities:

### Option 1: Work on Remote Server
You can develop your code on the remote server directly if you are comfortable with Vim or Emacs.  There is a learning curve for each of them, so it's up to you if it is something you would like to invest your time in learning or not.  If you would like to work remotely on the server, here is a [getting started guide for Vim](https://opensource.com/article/19/3/getting-started-vim) and here is a similar [guide for Emacs](https://opensource.com/article/20/3/getting-started-emacs).

**If you chose to work using the VM, be aware that you will be charged credits for the time your VM is running - meaning while you are working, not just while you are training a model.**  Since you don't need GPU access while writing code, you may want to remove GPU from your VM before starting it while writing code, and then re-start and add GPU when ready to train your model in order to save credits.

### Option 2: Work in JupyterLab
You can also work using your VM in JupyterLab, which provides access to run Jupyter Notebooks, a Python file editor, and terminal access.  There are two options to access JupyterLab on your VM:

1) Acces JupyterLab via command line:
    - First, start your instance on the GCP Console
    - In your terminal, run the following:
        ```
        gcloud compute ssh --project <PROJECT-NAME> \
        --zone=<ZONE> <INSTANCE-NAME> \
        -- -L 8080:localhost:8080
        ```
        Be sure to replace <PROJECT-NAME>,<ZONE> and <INSTANCE-NAME> with your project, zone and instance.
    - Then, in your browser go to https://localhost:8080/lab to open JupyterLab.  If it does not open, try restarting your browser and/or clear your cache.
    - When done, be sure to stop your instance

2) Access JupyterLab through the GCP site:  
    - Click on the three bars at the top left and then select **Vertex AI** -> **Workbench**.  You should see your VM instance listed.  Click the "Open Jupyterlab" blue link - it will start your instance and open JupyterLab. If you see a warning sign to the left of your instance name on the page, you may need to click "Register All" at the top right to register your VM instance with Vertex AI's API before you can start JupyterLab.  Make sure to stop your instance when you are done work!

        ![](.img/open_jupyter.png)

Note that Jupyter opens from the path /home/jupyter.  You may need to cd from a terminal to access files which are stored elsewhere on your disk (e.g. in another directory under /home)

**If you chose to work using the VM, be aware that you will be charged credits for the time your VM is running - meaning while you are working, not just while you are training a model.**  Since you don't need GPU access while writing code, you may want to remove GPU from your VM before starting it while writing code, and then re-start and add GPU when ready to train your model in order to save credits.

### Option 3: Work locally and sync via GitHub
Alternatively, you can develop locally on your favorite editor, push to your repo on Github, and pull on the remote server using terminal or via JupyterLab (or copy the files to the remote server per the above instructions, but a better practice is to use GitHub for version control).  Note that if you git clone them directly from the terminal (and not via JupyterLab's terminal), they will be stored in the path `/home/<git-username>`.  JupyterLab opens in the path `/home/jupyter` so you will need to cd up to find your files.  If you git clone them through JupyterLab's terminal they will copy into the `/home/jupyter` directory.

The benefit of this option is that you are not charged credits for working time (until you need to train your model), or run the risk of forgetting to turn your instance off when you step away from my computer.  The downside of this is the extra step of syncing your work via GitHub to the VM, and also that you will not be able to train your model from your local development environment and will need to switch over to your VM to train when ready (assuming it requires GPU).  You may also not be able to access your data while developing, if it resides on GCP unless you maintain a local copy as well.

## Other Tips
1) ### **REMINDER: Make sure you stop your instances!**
    **Don't forget to stop your instance when you are done (by clicking on the stop button at the top of the page showing your instances). You can restart your instance and your saved files will still be available.**

2) If you would like to open a Jupyter Notebook on your VM in your browser without going into JupyterLabs via the GCP site as per above, after starting your VM you can run the following to open Jupyter Notebooks:

    ```
    gcloud compute ssh --zone=<WRITE-ZONE> jupyter@<WRITE-VM-NAME> --project "<WRITE-PROJECT-NAME>" -- -L 8080:localhost:8080
    ```

3) If you would like to set up a preemtible VM instance to save credits, run the following in your command line

    ```
    export IMAGE_FAMILY="pytorch-latest-gpu"
    export ZONE="us-central1-a"
    export INSTANCE_NAME="<WRITE-INSTANCE-NAME-HERE>"
    export INSTANCE_TYPE="n1-highmem-8" # budget: "n1-highmem-4"

    gcloud compute instances create $INSTANCE_NAME \
            --zone=$ZONE \
            --image-family=$IMAGE_FAMILY \
            --image-project=deeplearning-platform-release \
            --maintenance-policy=TERMINATE \
            --accelerator="type=nvidia-tesla-t4,count=1" \
            --machine-type=$INSTANCE_TYPE \
            --boot-disk-size=200GB \
            --metadata="install-nvidia-driver=True" \
            --preemptible
    ```

3) The git extension for JupyterLab comes pre-installed and provides basic git functionality without going through the terminal.  On the left side of JupyterLab click the icon for "Extensions" and click "Enable".  You will then be able to use the git extension by clicking on its button on the left side.

4) Each time you try to push to GitHub from yoru VM, you will need to authenticate with your GitHub username and your [Personal Access Token]((https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).  If you don't want to have to do this every time, you can install the GitHub CLI on your VM using Conda and follow the instructions [here]((https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

5) [This article](https://medium.com/google-cloud/using-google-cloud-ai-platform-notebooks-as-a-web-based-python-ide-e729e0dc6eed) by a Google MLE contains a number of additional recommendations for using JupyterLab on GCP as your cloud-based IDE for software development.  In particular be sure to check out Steps 3 - 7.


6) You can use [Tmux](https://linuxize.com/post/getting-started-with-tmux/) to keep the training sessions running when you close your laptop. Also, if your collaborators log into the same account on the VM instance, they will see the same tmux session screen in real time. 

## Further Training
- [Introduction to Vertex AI video](https://www.youtube.com/watch?v=gT4qqHMiEpA)  
    - Brief introductory video on Vertex AI
- [Hands on with Cloud AI Workshop Video](https://www.youtube.com/watch?v=aB2OxnyfP0c)
- [Google Cloud Quest - Google Cloud Essentials](https://www.cloudskillsboost.google/quests/23)  
    - 4hr Google training course on Cloud Essentials
    - Highly recommend - covers most of the key functions we will be using in this course
- [Google Cloud Quest - Baseline: Data, ML, AI](https://www.cloudskillsboost.google/quests/34)  
    - Learn how to use Google's Vertex AI AutoML capabilities


## Google Cloud Certifications
- [Associate Cloud Engineer Certification](https://cloud.google.com/certification/cloud-engineer)  
- [Professional ML Engineer](https://cloud.google.com/certification/machine-learning-engineer)