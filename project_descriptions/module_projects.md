![](https://storage.googleapis.com/aipi_datasets/Duke-AIPI-Logo.png)

# Module Projects Description


## Project Topic
Each module of the course will include a team-based module project.  At the beginning of each module new teams will be assigned randomly, so that you have the chance to work with a different set of teammates each module.  Each team will role a dice to randomly select which of the below six themes they are assigned for their module project.  Every team has 1 opportunity for a re-roll the second week of the module if they wish to change their topic (however, when you re-roll you are committed to the new theme and cannot go back).  If you wish to re-roll, please contact the instructor via email and they will do the re-roll for you.

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

For your final deliverable you may choose whichever of the above approaches works better for you, although you must include the code for both somewhere in your repo.  There are rare situations where there may not be a viable non deep learning approach.  If this is the case, you must write a paragraph explaining why no approach other than a neural network presents a viable solution to your problem, and defend your claim by discussing the theory behind your rationale.  You must include this writeup somewhere in your repo.

### Options for approaching project
There are two options on how to approach the project:  
1)	You may choose to work on a dataset or problem for which there are no identifiable previous modeling approaches (and therefore, your project will be entirely novel), e.g. if you create a new dataset for the project or no one has previously attempted to model the dataset.
    - For example, suppose you create a new text dataset about chemistry by gathering text from many articles about areas of chemistry, and train a new NLP topic model to extract the key topics of each article
    - Or perhaps you gather hundreds of images of different types of birds and then train an image classification system to recognize bird species  

2)	Alternatively, you may choose to work on an existing dataset or problem which others have worked on (e.g. you find a dataset on Kaggle).  If you do work on an existing problem, you must explain and show what is new and novel about your approach relative to previous approaches.  You should also make sure to reference the previous approaches you reviewed.  Your approach should either result in state-of-the-art (SOTA) performance or close to it, OR provide greater insight into the problem (e.g. better explainability) as compared to previous approaches.
    - For example, suppose you find an open source dataset of medical chest xray images and several references of disease classification models using the data.  You take a different approach to modeling it by using a computer vision model to extract certain features from the images and then feeding those into a decision tree model.

Your code must be written in Python, and you are free to use any libraries you wish.  Although we will use PyTorch in class, you are welcome to use Tensorflow/Keras for the project.  Although you may use Jupyter Notebooks for the exploration phase of your project, your final submission must be in the form of Python scripts, organized as described below.  

## Project Deliverables
The final deliverables for each module project include:  
1) 10 minute maximum presentation including the following:  
    - Problem you are addressing  
    - Data source(s)
    - Review of relevant previous efforts and literature (if existing dataset)
    - Your model evaluation process & metric selection
    - Your modeling approach
        - Data processing pipeline  
        - Models evaluated and model selected (must include at least 1 non deep learning model and 1 deep learning model - see details above)
    - Either visualizations of the output (graphs) and/or a demo of your project  
    - Results and conclusions
2) Submitted link to a public or private GitHub repo containing your code.  Code should be organized in the following structure.  Be sure to include a requirements.txt file and a README describing the project and how to run it.  You must either include the data in your repo if it is small enough or provide a link to it along with the original source.

### Project repo structure
Your project repo should be organized similar to the below structure.  You may choose to deviate from the below, but make sure each main component below is included somewhere.  You may also add additional files/directories if needed, e.g. dockerfile, database or html/css).

Note: if you use Colab Pro for your project, you can include a **run.ipynb** notebook file which accesses your data, imports modules and runs your project.  Be sure not to accidentally include any secrets in this file.

```
├── README.md               <- description of project and how to set up and run it
├── requirements.txt        <- requirements file to document dependencies
├── Makefile [OPTIONAL]     <- setup and run project from command line
├── run.ipynb [OPTIONAL]    <- run project on Google Colab (only include if using Google Colab for project)
├── setup.py                <- script to set up project (get data, build features, train model)
├── app.py                  <- app to run project / user interface
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

## Grading
Your project will be graded on the following criteria.  Note that there are no specific numeric performance targets that are used in grading the projects - you model's performance is related to the problem and data and so will differ widely across teams/projects.

- **70% project presentation**
    - Well-defined problem
    - Clear description of your data, data pipeline, modeling approach, and model evaluation approach
    - Clear explanation of previous approaches (if existing dataset) and what is new and novel about your approach
    - Analysis of your performance relative to previous approaches  
    - Discussion of deep learning approach vs. non deep learning approach
    - Understandable, descriptive demo or visualizations of outputs/performance  
- **20% project code submission**  
    - Code organization - well organized and includes all necessary files
    - Code documentation - code is well commented and readable, and project contains descriptive readme file
- **10% team peer evaluation**  
    - After the project each member of the team will anonymously evaluate the contribution of each other member by selecting from two choices: 1) "member contributed equally to the project", or 2) "member did not contribute sufficiently to the project".  If ALL other team members rate your contribution to the project as "member did not contribute sufficiently to the project", you will receive a 0 on this component.  Otherwise, you will receive full credit (10% of total grade)

Have fun, and good luck!