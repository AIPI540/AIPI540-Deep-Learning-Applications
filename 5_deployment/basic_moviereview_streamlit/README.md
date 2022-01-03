![](https://storage.googleapis.com/aipi_datasets/Duke-AIPI-Logo.png)

# Streamlit App Example
![](.img/streamlit_app.png)

This directory contains a simple example web app which uses [Streamlit](https://streamlit.io) for the user interface.  Streamlit is a very simple but powerful way to create interactive interfaces for web apps using scripting in Python.  You can create dynamic interfaces for apps using very little code, which makes it great for prototyping new applications.

The demo app uses a NLP model to evaluate text of a movie review which a user inputs and attempts to classify whether the sentiment of the movie review is positive or negative.  The app can be run locally (and I recommend you do this first), and can also be deployed on the Google Cloud Platform via the Google App Engine.

## Run the app locally
The first thing we want to do with this example project is to run it locally so we can ensure things are working locally before we deploy it to the cloud.  To run the app locally, first make sure that you have installed all dependencies listed in the `requirements.txt` file for this repo into a virtual environment and have activated your environment.  Then, navigate to this directory from the command line and enter `make run`.  It should start the app and you can then open your browser to [http://0.0.0.0:8080](http://0.0.0.0:8080) and you should see the interface of the app.

When we enter `make run`, it triggers the `run` section of the Makefile in the project directory.  A [Makefile](https://opensource.com/article/18/8/what-how-makefile) is a script which allows us to write short commands (e.g. `make run`) which then initiate larger commands - the benefit of using a Makefile is that we do not have to remember and type the larger commands each time.

The commands which are triggered when we execute `make run` are:
```
streamlit run app.py --server.port=8080 --server.address=0.0.0.0
```
which starts our Streamlit app and serves it so that it is avaiable to access from the browser.

### Run the app locally within a Docker container
You can also try out running the app on your computer within a Docker container.  Make sure that you have Docker installed and running on your machine.  Then, navigate to this directory from the command line and enter `make run-container`.  It should then build a new Docker container, install the needed dependencies from the `requirements.txt` file within this directory, and then run the app.  You can then navigate to [http://0.0.0.0:8080](http://0.0.0.0:8080) in your browser to view the app.

As before, when we enter `make run-container`, it triggers the commands within the `run-container` section of the Makefile.  The commands which are triggered are:
```
docker build . -t app.py
docker run -p 8080:8080 app.py
```
The first command builds the Docker container for the app, and the second command then runs the app within the Docker container and serves it so that it is accessible from our browser.

## Deploy the app on Google App Engine
After you've gotten comfortable running the app locally, let's now deploy it to the Google Cloud Platform so it is publicly accessible.  You'll first need to have created a GCP account and set up a project in GCP.  If you have not done so already, follow the instructions in the [GCP quickstart guide](https://github.com/AIPI540/AIPI540-Deep-Learning-Applications/blob/main/0_infra_setup/GCP_quickstart.md).

To deploy the app on GCP, do the following:  
1) In the Makefile, under the 'gcloud-deploy' section change the GCP project name to your own project name in the line:
    ```
    gcloud config set project <your-project-name>
    ```
    This sets the active project in the gcloud CLI so that you deploy your app to the correct GCP project.  
2) Now, enter `make gcloud-deploy` from the command line.  This will deploy your app via Google App Engine (GAE), and the process may take several minutes.  It may ask you to authenticate with GCP if you are not already authenticated.

**WARNING:** when this completes, your app will be live on GAE - meaning it will be publicly accessible and also that you will be charged credits for hosting and serving the app.  

When we run `make gcloud-deploy`, we execute the following commands via the Makefile:  
```
gcloud config set project <your-project-name>
gcloud app deploy app.yaml --stop-previous-version
```

The first command sets our GCP project.  The second command deploys our app via Google App Engine according to the 'app.yaml' file.  This process consists of the following steps:
1) A [Docker container](https://www.docker.com/resources/what-container) is created for our app, defined by the [Dockerfile](https://docs.docker.com/engine/reference/builder/) within our directory 
2) Once the Docker container is created it becomes a Docker image, which you can think of as an immutable Docker container which we can deploy anywhere and it will not change.  This is the main benefit of using a Docker container to house our app - we could deploy it on another cloud platform (or locally) and should not need to change anything except the process to deploy the container.
3) The Docker image is uploaded to the [Google Container Registry (GCR)](https://cloud.google.com/container-registry)
4) When the Docker container is available on GCR, it is then deployed to a Google App Engine instance, which is defined by the instructions in the 'app.yaml' file:
    ```
    runtime: custom
    env: flex
    ```
    Because we are using Streamlit, we need to specify a custom runtime and flexible environment for our app.

After you have completed the above steps, your app will now be live on GCP!  You can access your app at the url:
```
https://<your-project-name>.ue.r.appspot.com/
```





