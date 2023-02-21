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

As part of your project you are required to evaluate at least two approaches to modeling your data:
1) A non deep learning approach using classical ML techniques
2) A NN-based deep learning approach  

For your final deliverable you may choose whichever of the above approaches works better for you, although you must include the code for both somewhere in your repo.  There are rare situations where there may not be a viable non deep learning approach.  If this is the case, you must write a paragraph explaining why no approach other than a neural network presents a viable solution to your problem, and defend your claim by discussing the theory behind your rationale.  You must include this writeup somewhere in your repo.

Your code must be written in Python, and you are free to use any libraries you wish.  Although we will use PyTorch in class, you are welcome to use Tensorflow/Keras for the project.  Although you may use Jupyter Notebooks for the exploration phase of your project, your final submission must be in the form of Python scripts, organized as described below.  

For the individual project, you must also create a working, interactive proof-of-concept application, which must be publicly accessible via internet until 48 hours after the last day of final exams.  You may use any frameworks you wish to create your front-end, such as Flask, Streamlit, or Dash.  Your application must be deployed on GCP, Azure, or AWS.

## Project Proposal
Your project proposal will be a written document (2 page max) describing what you plan to work on for your final project.  It should focus on the following:  
- What problem you are going to work on  
- Brief description of relevant previous efforts (research papers and/or commercial products)  
- The data sources you plan to use  
- How your proposed approach will differ from previous approaches - what do you intend for your unique contribution to be in solving this problem?  
- Your project plan - include gantt chart and major milestones  
- What will be the final deliverable from your project (web app, mobile app etc) and what will it do

## Final Project Deliverables
The final deliverables for the individual project include:  
1) 15-minute maximum presentation (there is a hard stop!) including the following:  
    - Problem you are addressing  
    - Data source(s)
    - Review of relevant previous efforts and literature (if existing dataset)
    - Your model evaluation process & metric selection
    - Your modeling approach
        - Data processing pipeline  
        - Models evaluated and model selected (must include at least 1 non deep learning model and 1 deep learning model - see details above)
    - Brief demo of your project  
    - Results and conclusions
2) Submitted link to a public or private GitHub repo containing your code.  Code should be organized in the below structure.  Be sure to include a requirements.txt file and a README.md describing the project and how to run it.
3) Submitted link to a working, publicly accessible web or mobile interface of your application deployed on a cloud platform (GCP, AWS, Azure)

### Project repo structure
Your project repo should be organized similar to the below structure.  You may choose to deviate from the below (e.g. you may have more or less script files or data directories), but make sure each main component is included somewhere.  You may also add additional files/directories if needed, e.g. dockerfile, database or html/css).

Notes:  
- There should be no jupyter notebooks anywhere other than the 'notebooks' directory
- If you use code that you did not write yourself, you MUST provide attribution at top of the script file to the original author and a link to their repo 
- All code should be organized in classes and functions.  There should be NO loose code lines in any of the repo files 
- Code should be clear and commented.  Use descriptive variable names and docstrings for all classes and functions.  Include code comments where needed

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
Beginning Week 6, each week you are required to submit a 1-3 minute video progress update.  You must describe the progress you've made during the week and SHOW progress - either by displaying what your code does that you have written during the week, or (in the later stages) showing early prototypes of your app.  **The weekly progress updates count for 5% of your total course grade.**  For each update that you do not submit on time, you will lose -0.5%.  Weekly updates will be submitted via Ed Discussions.  You must create a new thread for your project, and each week you will post your weekly update video link as a response/comment on your thread.  Weekly updates are due BEFORE the start of class the following week (e.g. Week 6 update is due before start of Week 7 class).

## "Demo Day" Final Presentation
The course project will culminate in a virtual "Demo Day" (a la TechStars) via Zoom at the end of the semester.  You are also welcome to invite your family and friends to tune in live to watch your presentation/demo!  It should be a fun event.

## Final Project Grading
Your individual project deliverables (25% of course grade) will be graded on the following criteria.  Note that there are no specific numeric performance targets that are used in grading the projects - you model's performance is related to the problem and data and so will differ widely across teams/projects.

- **60% project presentation**
    - Well-defined problem and motivation - what problem are you solving and why?
    - Clear description of your data, data pipeline, modeling approach (mention both non-DL and DL), and model evaluation approach
    - Brief description of previous approaches to solving the problem and what is new and novel about your approach
    - Analysis of your performance and ability to solve the problem relative to previous approaches (unless dataset is new)
    - Key user experience decisions made and rationale
    - Understandable, descriptive demo of your application
- **25% proof-of-concept application**  
    - Application proof-of-concept acheives stated project objective
    - Interface is intuitive, interactive, and communicates model results/uncertainty well
- **15% project code submission**  
    - Code organization - well organized and includes all necessary files
    - Code documentation - code is well commented and readable, and project contains descriptive readme file

Have fun, and good luck!