![](https://storage.googleapis.com/aipi_datasets/Duke-AIPI-Logo.png)

# Individual Project Description

## Project Topic
For your project topic you may select a topic related to any of the below six themes.  The specific topic that you select, and what type of deep learning models you utilize (computer vision / NLP / recommendation systems / etc) are fully up to you.  **Note that you CANNOT select a topic for your course project that you are already working on for a previous course, research or work.**

### Themes:
1)	Health, wellness and fitness
2)	Physical infrastructure – energy, water, transportation, buildings
3)	Entertainment and the arts
4)	Social media and news
5)	Education and knowledge management
6)	Agriculture and food

## Project Requirements
The objective of the individual course project is to develop a functioning "proof of concept" application which uses a deep learning model to generate predictions or perform analysis on real-world data.  You may focus on any type of deep learning application (computer vision / NLP / recommendation systems / graph neural network / etc).  The dataset you use may either be new (you create it) or existing.  If the dataset is existing, your project needs to go beyond the prior attempts and you must describe how it is new and novel relative to the previous efforts.

Your code must be written in Python, and you are free to use any libraries you wish.  Although we will use PyTorch in class, you are welcome to use Tensorflow/Keras for the project.  Although you may use Jupyter Notebooks for the exploration phase of your project, your final submission must be in the form of Python scripts, organized as described below.  

For the individual project, you must also create a working, interactive proof-of-concept application, which must be publicly accessible via internet until 48 hours after the last day of final exams.  You may use any frameworks you wish to create your front-end, such as Flask, Streamlit, or Dash.  

## Final Project Deliverables
The final deliverables for the individual project include:  
1) 10-minute maximum presentation including the following:  
    - Problem you are addressing  
    - Data source(s)
    - Review of relevant previous efforts and literature (if existing dataset)
    - Your model evaluation process & metric selection
    - Your modeling approach
        - Data processing pipeline  
        - Models evaluated and model selected
    - Brief demo of your project  
    - Results and conclusions
2) Submitted link to a public or private GitHub repo containing your code.  Code should be organized in the below structure.  Be sure to include a requirements.txt file and a README.md describing the project and how to run it.
3) Submitted link to a working, publicly accessible web or mobile interface of your application deployed on a cloud platform (e.g. GCP, AWS, Azure, Heroku, Render etc)

### Project repo structure
Your project repo should be organized similar to the below structure.  You may choose to deviate slightly from the below, but make sure each main component below is included somewhere.  You may also add additional files/directories if needed, e.g. dockerfile, database or html/css).

```
├── README.md               <- description of project and how to set up and run it
├── requirements.txt        <- requirements file to document dependencies
├── Makefile [OPTIONAL]     <- setup and run project from command line
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

## Weekly Progress Updates
Beginning Week 5, each week you are required to submit a 1-3 minute video progress update.  You must describe the progress you've made during the week and SHOW progress - either by displaying what your code does that you have written during the week, or (in the later stages) showing early prototypes of your app.  **The weekly progress updates count for 5% of your total course grade.**  For each update that you do not submit on time, you will lose -0.5%.  Weekly updates will be submitted via Ed Discussions.  You must create a new thread for your project, and each week you will post your weekly update video link as a response/comment on your thread.  Weekly updates are due BEFORE the start of class the following week (e.g. Week 5 update is due before start of Week 6 class).

## Final Project Grading
Your individual project deliverables (25% of course grade) will be graded on the following criteria.  Note that there are no specific numeric performance targets that are used in grading the projects - you model's performance is related to the problem and data and so will differ widely across teams/projects.

- **60% project presentation**
    - Well-defined problem and motivation
    - Clear description of your data, data pipeline, modeling approach, and model evaluation approach
    - Clear explanation of previous approaches (if existing dataset) and what is new and novel about your approach
    - Analysis of your performance relative to previous approaches (unless dataset is new)
    - Key user experience decisions made and rationale
    - Understandable, descriptive demo of your application
- **25% proof-of-concept application**  
    - Application proof-of-concept acheives stated project objective
    - Interface is intuitive, interactive, and communicates model results/uncertainty well
- **15% project code submission**  
    - Code organization - well organized and includes all necessary files
    - Code documentation - code is well commented and readable, and project contains descriptive readme file

Have fun, and good luck!