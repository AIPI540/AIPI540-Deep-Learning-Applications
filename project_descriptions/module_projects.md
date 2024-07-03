![](https://storage.googleapis.com/aipi_datasets/Duke-AIPI-Logo.png)

# Module Projects Description


## Project Topic
Each module of the course will include an individual module project.  Each student will be able to select which of the below six themes they will focus on for their module project.  You must then select a problem within the general area of your theme to work on for your project.

### Themes:
1)	Health, wellness and fitness
2)	Physical infrastructure – energy, water, transportation, buildings
3)	Entertainment and the arts
4)	Social media and news
5)	Education and learning
6)	Agriculture and food

## Project Requirements
The module project must align with the topics covered within the module in class, but may extend beyond that to include other approaches or technologies.  The choice of specific topic and data used is up to you.  The objective of the project is to develop a model to predict or analyze real-world data.  As part of your project you are required to evaluate at least two approaches:
1) A non deep learning approach using classical ML techniques
2) A NN-based deep learning approach  

For your final deliverable you may choose whichever of the above approaches works better for you, although you must include the code for both somewhere in your repo.  There are rare situations where there may not be a viable non deep learning approach.  If this is the case, you must write a detailed paragraph explaining why no approach other than a neural network presents a viable solution to your problem, and defend your claim by discussing the theory behind your rationale (you will lose points if your rationale is not complete or correct).  You must include this writeup somewhere in your repo.

Additionally, you must compare your approach to a naive approach (i.e. a mean model). This comparison should be included in your presentation.

Your project deliverables also include a visual interface to interact with your ML system.   You may use any frameworks you wish to create your front-end, such as Streamlit, Flask/HTML, NextJS, Dash, Gradio etc.  For the module projects you are not required to deploy your demo on the cloud (you may run locally), although for practice I encourage you to do so.

### Options for approaching project
Your goal with the project is to create a new, unique contribution to solving the problem which goes above and beyond anything which has been done previously.  There are two options on how to approach this for the project:  
1)	You may choose to work on a dataset or problem for which there are no identifiable previous modeling approaches (and therefore, your project will be entirely novel), e.g. if you create a new dataset for the project or no one has previously attempted to model the dataset.
    - For example, suppose you create a new text dataset about chemistry by gathering text from many articles about areas of chemistry, and train a new NLP topic model to extract the key topics of each article
    - Or perhaps you gather hundreds of images of different types of birds and then train an image classification system to recognize bird species  

2)	Alternatively, you may choose to work on an existing dataset or problem which others have worked on (e.g. you find a dataset on Kaggle).  If you do work on an existing problem, you must explain and show what is new and novel about your approach relative to previous approaches.  You should also make sure to reference the previous approaches you reviewed.  Your approach should either result in state-of-the-art (SOTA) performance or close to it, OR provide greater insight into the problem (e.g. better explainability) as compared to previous approaches.
    - For example, suppose you find an open source dataset of medical chest xray images and several references of disease classification models using the data.  You take a different approach to modeling it by using a computer vision model to extract certain features from the images and then feeding those into a decision tree model.

Your code must be written in Python, and you are free to use any libraries you wish.  Although we will use PyTorch in class, you are welcome to use Tensorflow/Keras for the project.  Although you may use Jupyter Notebooks for the exploration phase of your project, **your final submission must be in the form of Python scripts, NOT Jupyter Notebooks**, organized as described below.  

## Project Deliverables
The final deliverables for each module project include:  
1) 15 minute maximum presentation including the following:  
    - Problem you are addressing  
    - Data source(s)
    - Review of relevant previous efforts and literature (if existing dataset)
    - Your model evaluation process & metric selection
    - Your modeling approach
        - Data processing pipeline  
        - Models evaluated and model selected (must include at least 1 non deep learning model and 1 deep learning model - see details above)
        - Comparison to naive approach
    - Demo of your project's visual interface (Streamlit, HTML, Dash, Gradio etc)  
    - Results and conclusions
2) Submitted link to a public or private GitHub repo containing your code.  Code should be organized in a structure similar to the below.  Be sure to include a requirements.txt file and a README describing the project and how to run it.  You must either include the data in your repo if it is small enough or provide a link to it along with the original source. Each member of the team should have made at least one PR into the repository and there should be PR reviews from other team members for each PR. 

### Project repo structure
Your project repo should be organized similar to the below structure.  You may deviate from the below structure if you wish, but make sure you have at least the main components (README, requirements.txt, main.py, helper scripts, model(s), data).  You may also add additional files/directories if needed, e.g. dockerfile, database or html/css.

Notes:  
- If you use Colab Pro for your project, your main file can be a notebook file (`main.ipynb` instead of `main.py`) which accesses your data, imports modules and runs your project.  If you use a notebook as your main file, it should NOT include any code other than importing your scripts and running them.  Be sure not to accidentally include any secrets in this file.  
- If you use code that you did not write yourself, you MUST provide attribution at top of the script file to the original author and a link to their repo 
- All code should be organized in classes and functions.  There should be NO loose code lines in any of the repo files 
- Code should be clear and commented.  Use descriptive variable names and docstrings for all classes and functions.  Include code comments where needed

```
├── README.md               <- description of project and how to set up and run it
├── requirements.txt        <- requirements file to document dependencies
├── Makefile [OPTIONAL]     <- setup and run project from command line
├── setup.py                <- script to set up project (get data, build features, train model)
├── main.py [or main.ipynb] <- main script/notebook to run project / user interface
├── scripts                 <- directory for pipeline scripts or utility scripts
    ├── make_dataset.py     <- script to get data [OPTIONAL]
    ├── build_features.py   <- script to run pipeline to generate features [OPTIONAL]
    ├── model.py            <- script to train model and predict [OPTIONAL]
├── models                  <- directory for trained models
├── data                    <- directory for project data
    ├── raw                 <- directory for raw data or script to download
    ├── processed           <- directory to store processed data
    ├── outputs             <- directory to store any output data
├── notebooks               <- directory to store any exploration notebooks used
├── .gitignore              <- git ignore file
```

### Git Best Practices
Your project repo should follow git best practices. Branches should be utilized. PRs should be made by each team member and good PR reviews should be made on each PR by other team members prior to merging code into the main branch. 
Review best practices for PRs (here)[https://github.com/mawrkus/pull-request-review-guide] and (here)[https://www.alexandra-hill.com/2018/06/25/the-art-of-giving-and-receiving-code-reviews/].

## Grading
Your project will be graded on the following criteria.  Note that there are no specific numeric performance targets that are used in grading the projects - you model's performance is related to the problem and data and so will differ widely across projects.

- **65% project presentation**
    - Well-defined problem
    - Clear description of your data, data pipeline, modeling approach, and model evaluation approach
    - Clear explanation of previous approaches (if existing dataset) and what is new and novel about your approach
    - Analysis of your performance relative to previous approaches  
    - Discussion of deep learning approach vs. non deep learning approach
    - Comparison to naive approach
    - Understandable, descriptive demo or visualizations of outputs/performance  
- **25% project code submission**  
    - Code organization - well organized and includes all necessary files to run the project
    - Code documentation - code is well commented and readable, and project contains descriptive readme file
- **10% git best practices followed**
    - Git best practices used including branches
    - PRs by each team member
    - Good PR reviews for each PR by other team members


Have fun, and good luck!