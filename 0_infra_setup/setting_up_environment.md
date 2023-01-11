![](https://storage.googleapis.com/aipi_datasets/Duke-AIPI-Logo.png)

# Setting Up Your Environment Quickstart Guide

## Table of contents

1. [Introduction](#introduction)
2. [Environments Using venv](#environments-using-venv)
3. [Environments Using conda](#environments-using-conda)

## Introduction

Because data scientists tend to use a number of different python packages in their work, tracking dependencies of code files and managing compatibility of different versions of packages can become complicated, especially if you are working with many files built with different versions of different packages.  A best practice to manage dependencies of our code is to create a new virtual environment for each project.  We then install only the needed packages for the project into the project’s virtual environment.  By having a separate virtual environment for each project, we can use different versions of packages (and even different versions of python) for each project without having to worry about version conflicts or tracking what goes where.  There are two primary methods of creating and managing virtual environments for python: [venv](https://docs.python.org/3/library/venv.html) and [conda/Anaconda](https://docs.conda.io/en/latest/).

[Venv](https://docs.python.org/3/library/venv.html) is an environment manager for python which creates isolated virtual environments for python development specifically.  To install packages into an environment created with venv, we use the pip package manager.

[Conda](https://docs.conda.io/en/latest/) (included with [Anaconda](https://www.anaconda.com/products/individual)) is both a package manager and an environment manager.  We can use conda to create and manage environments, and also use it to install packages into those environments rather than pip (although we can also use pip), and can install packages not only from PyPI but also from Anaconda Repository and Anaconda Cloud.  Conda is also language-agnostic whereas venv is specific to python.

Whether you choose to use venv or conda to manage your environments is up to you.  There are subtle differences between them, but neither is better or worse than the other.

## Environments Using venv
Below is the suggested workflow to set up a new environment for your project using venv.  You will likely want to set up an environment for the materials from this course, and you may want to set up a separate one for your projects, depending on what libraries you plan to use.

1) Create a new environment using venv  
    ```
    (base) $ python3 -m venv <environment-name>
    ```

2) Activate the new environment  
    ```
    (base) $ source <environment-name>/bin/activate
    ```

3) Install packages into the environment  
    - Install packages manually  
        ```
        (env) $ pip install pandas scikit-learn matplotlib notebook
        ```  

    - Install packages from an existing **requirements.txt** file  
        ```
        (env) $ pip install -r requirements.txt
        ```

    - Show what packages are installed  
        ```
        (env) $ pip list
        ```

4) Create/update a **requirements.txt** file for your environment  
    - OPTION A: include all packages installed in the environment
        ```
        (env) $ pip freeze > requirements.txt
        ```

    - OPTION B: include only the packages actually used in your code files (.py files and notebooks)  
        ```
        (env) $ pip install pipreqsnb
        (env) $ cd <PROJECT-DIRECTORY>
        (env) $ pipreqsnb
        ```

5) Deactivate the environment  
    ```
    (env) $ deactivate
    ```

## Environments Using conda
Below is the suggested workflow to set up a new environment for your project using conda.  You will likely want to set up an environment for the materials from this course, and you may want to set up a separate one for your projects, depending on what libraries you plan to use.

1) Create a new environment
    ```
    (base) $ conda create –-name <environment-name>
    ```

2) Activate the new environment
    ```
    (base) $ conda activate <environment-name>
    ```

3) Install packages into the new environment  

    - Install packages manually using conda (can also use pip instead)  
        ```
        (env) $ conda install pandas scikit-learn matplotlib notebook
        ```

    - Install packages from an existing **requirements.txt** file
        ```
        (env) $ pip install -r requirements.txt
        ```
    
    - Install packages from an existing **environment.yml** file
        ```
        (env) $ conda env create -f environment.yml
        ```

4) Create a **environment.yml** file for your environment
    ```
    (env) $ conda env export --file environment.yml
    ```

5) Deactivate environment
    ```
    (env) $ conda deactivate
    ```