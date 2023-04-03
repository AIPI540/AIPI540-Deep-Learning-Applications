![](https://storage.googleapis.com/aipi_datasets/Duke-AIPI-Logo.png)

# Duke Compute Cluster Quickstart Guide

## Table of contents

1. [Introduction](#introduction)
2. [Recommended Workflow](#recommended-workflow)
3. [Additional Tips](#additional-tips)

## Introduction

The Duke Compute Cluster is a general purpose high performance/high-throughput installation, and it is fitted with software used for a broad array of scientific projects. With a few notable exceptions, applications on the cluster are generally Free and Open Source Software. The DCC is managed and supported by the Office of Information Technology (OIT) and Research Computing.

The Duke Compute Cluster consists of machines that the University has provided for community use and that researchers have purchased to conduct their research. The equipment is housed in enterprise-grade data centers on Duke’s West Campus. Cluster hardware is heterogenous based on installation date and current standards.

The DCC Open OnDemand portalis  focused on providing web based interactive sessions on the DCC for applications that produce visualizations of data analysis completed on the DCC. OnDemand can be used to run Jupyter Notebook environment in your browser.

## Recommended Workflow
The below steps provide a recommended workflow for one time setup of resources and running Jupyter Notebooks on DCC.

### 1. One-Time Setup - Logging into the DCC through CMD/Terminal

a). Login to the DCC using `ssh netid@dcc-login.oit.duke.edu`, (note: VPN is not required, but MFA **is required**). 

```
kk338@CDSS-5630 ~ % ssh kk338@dcc-login.oit.duke.edu
Password: 
Duo two-factor login for kk338

Enter a passcode or select one of the following options:

1. Duo Push to XXX-XXX-4007
2. Phone call to XXX-XXX-4007
3. Phone call to XXX-XXX-9784
4. SMS passcodes to XXX-XXX-4007 (next code starts with: 2)

Passcode or option (1-4): 1
Success. Logging you in...
Last login: Tue Dec 21 11:07:41 2021 from xxx
################################################################################
# MOTD                                                                         # 
# My patch window is wednesday 03:00                                           #
################################################################################
kk338@dcc-login-03  ~ $
```

b). Installing Miniconda

Students are welcome to install software in their `hpc/group/aipi540-s23/<net_id>` space.

Miniconda installation sample:
```
ln -s /hpc/group/aipi540-s23 aipi540-s23
mkdir -p /hpc/group/aipi540-s23/<netid>
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
```

and then follow the instructions. The place to give as Miniconda install location should be `/hpc/group/aipi540-s23/<netid>/miniconda3`. It will offer to update your ~/.bashrc, (init) which is what you want. Log out log back in and then you can run conda install, pip install, create environments, etc.

c). Creating a new conda environment

To create a `conda` environment, run the following command on one of the Yens:

```
conda create --name my_conda_env
```

This will make an environemnt named “my\_conda\_env”. You can also specify which python version you want:

```
conda create --name my_conda_env python=3.8
```

d). Activating your environment

First, to use your environment, you need to activate your environment:

```
conda activate my_conda_env
```

You will know your environment is activated because it will show up on your command line:

```
(my_conda_env) netid@yenX:~$ 
```

e). Installing any packages needed in that environment

Then, you can install any packages you need using `conda` or `pip`:

```
conda install numpy
pip install torch
```

If your environment is activated, `conda` keeps track of which packages are installed where. Some packages will require `pip` to install - your new `conda` environment has it’s own `pip` install.

### 2. Accessing Jupyter Lab through DCC OnDemand portal

a). Click on Interactive Apps in the top navigation menu

b). Click on Jupyter Lab

c). Select the name of your DCC group (aipi540-s23)

d). Under partition, make a selection as follows:
- If you need CPU resources, select "common"
- If you need GPU resources, select "common-gpu"
- In case you fail to get a session within 5 minutes, try "scavenger-gpu"

e). Input the number of hours you would like the server to remain active (please try to remain small, as it will continue running even if you are not using it)

f). Input the desired amount of nodes, memory, and CPUs (try to start small with only a few gigabytes of memory and cores)

g). Press the blue "Launch" button on the bottom of the page

h). After pressing the blue "launch" button, your job will be queued to start a Jupyter Lab server. You should see this automatically

i). Wait a few minutes for the Jupyter Lab server to finish launching. The status will automatically change from "Starting" to "Running" when the server is ready

j). Press the blue "Connect to Jupyter" button when the server is running to access your Jupyter Lab server

## Additional Tips

## Setting up SSH keys

Setting up SSH keys from your workstation will greatly simplify the login and file transfer process by creating a secure key based session between your workstation and the DCC instead of using your password with MFA. The steps below will guide you through the process of setting up SSH keys on your workstation.

a). Generate a new SSH key

To generate a key pair on a Macintosh or Linux machine, open terminal and run the following command:
```
ssh-keygen -t rsa -b 4096
```
b). The public key generated will be stored in the file "~/.ssh/id_rsa.pub" by default

c). Enter the following command to view the contents of your generated public key and copy its contents to your clipboard
```
cat ~/.ssh/id_rsa.pub
```

d). To enable ssh public key authentication, access the Duke Identity Manager portal [here](https://idms-web.oit.duke.edu/portal/)

e). Go to the “Advanced User Options”

f). Click on “SSH Public Keys” and paste the contents of your public key into the text box

g). Click “Add Key” and you should see your public key listed

## Accessing Cluster Computing Resources through VSCode

### 1. Connecting to the DCC cluster

a). Install the [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) extension in VSCode

b). Once the extension is installed, the bottom-left of your VS Code application will show a green box (“Open a Remote Window”). Clicking on it opens a dropdown menu (see the .gif), where you should select “Open SSH Configuration File…”

c). This will open a config file where you can specify the address of the computing cluster (HostName) as well as your username (User) and store them under a convenient name (Host). For example, if you want to connect to the DCC cluster, you can add the following lines to the config file:
```
Host dcc
    HostName dcc-login.oit.duke.edu
    User <netid>
```

d). Once the config file is updated, open a remote window by selecting “Connect to Host…” and selecting the "dcc" server from the dropdown menu

### 2. Requesting a Compute Node

So far, your connection to the computing server has been to the head node. Since the resources of the head node are shared across all users, it should not be used for any tasks that require high computing power.

To use the cluster for active development, it is necessary to request allocation of a computing node under your Duke NetID. Allocated resources are not shared across users and hence can be utilized in good conscience. To request a computing node, follow the steps below:

a). Open a terminal in VSCode by clicking on the “+” icon in the top-left corner of the VSCode window and selecting “New Terminal”

b). Enter the following Slurm command to request a node:
```
srun --account=aipi540-s23 --cpus-per-task=4 --mem-per-cpu=8G --partition=common-gpu --gres=gpu:1 --pty bash -l
```
This command will request a node with 4 CPUs, 8GB of RAM, 1 GPU, and will connect you to the node via a bash shell

c). Wait until the resources have been allocated (that can take a few seconds). You should notice a change in the name of the node that you are connected to.

For example, while the terminal read netid@dcc-login-01 ~$ after initially connecting to the DCC cluster, it will change to something else (e.g. netid@dcc-carlsonlab-gpu-16 ~$) after requesting an interactive session via the above command

At this point, you could already utilize the compute node by simply running commands from your terminal. But that would not be an enjoyable experience: among its many downsides is the inability for your VS Code session to access the environment variables. The reason for this is that while your terminal is now connected to the compute node, your VS Code session still rests on the head node of the cluster.

To fix this issue, VS Code needs to directly connect to the compute node.

### 3. Connecting to a Compute Node with VS Code

Unlike the head node of the computing cluster – to which you can connect directly via SSH – the compute nodes of the cluster don’t have a direct connection to the internet. For VS Code to connect to a computing node, it’s therefore necessary to “go through” the head node. This is done via a proxy connection.

a). Check the exact name of the compute node that you have requested. In the previous example, the name of the compute node is dcc-carlsonlab-gpu-16

b). Add a new host to the config file that you’ve set-up in step 1. Here, HostName is the name of the compute node (which may change across sessions) and ProxyJump specifies the address of the head node. Notice that I have set up a host called dcc in Section 1
```
Host dcc-carlsonlab-gpu-16
    HostName dcc-carlsonlab-gpu-16
    ProxyJump dcc
    User <netid>
```

c.) Start a new VS Code session and connect to a remote host via the Remote-SSH extension as before. Select the address of the newly specified host (in this case dcc-carlsonlab-gpu-16) and wait for the connection to establish

d.) You’re almost done! As a last step, install any VS Code extensions that you may want to utilize

You can now use VS Code to code interactively on a compute node. Of course, next time around, you won’t have to jump through all these steps again. You only have to repeat steps 2 and 3 i.e. request resources on the cluster and connect VS Code to the compute node.
