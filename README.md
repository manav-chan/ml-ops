# ML Operations

## Getting Started
- Setting up the virtual environment
```console
conda create -p /path/to/virtual-environment python=3.11 -y
conda activate /path/to/venv
```
- Creating a gitignore file for python using the github template.
- Creating a setup.py file so that the application can be packaged to be used with other projects or deploy to PyPI.
- Directories which have '__init__.py' will be treated as packages. For example, 'src' directory.
- Make a requirements.txt file to store the packages that need to be installed ending with '-e .', which will trigger setup.py whenever the packages from the requirements.txt are installed.
- Run the following command, a new package (directory) will be created, which can be used or deployed to PyPI
```console
pip install -r requirements.txt
```
- src directory contains components directory which contains various modules to be used in our project.


## Project Structure
```terminal
.
├── .gitignore
├── README.md
├── requirements.txt
├── setup.py
├── logs
├── notebook
├── venv
├── templates
├── app.py
└── src
    ├── __init__.py
    ├── components
    │   ├── __init__.py
    │   ├── data_ingestion.py
    │   ├── data_transformation.py
    │   └── model_trainer.py
    ├── exception.py
    ├── logger.py
    ├── pipeline
    │   ├── __init__.py
    │   ├── predict_pipeline.py
    │   └── train_pipeline.py
    └── utils.py
```

- **.gitignore**
Conatins files and directories that are to be ignored by git while commiting and pushing to the main repository.

- **requirements.txt**
Contains the names of all the libraries required for the project. Serves as en entry point and calls the setup.py file because of the '-e' for packaging of the application.

- **setup.py**
Builds the package of our application, will also create a package of the directories having __init_.py file in them.

- **logs**
Stores the logs when exceptions are encountered.

- **notebook**
Stores the Jupyter notebook file used for exploratory data analysis, contains the code that needs to be converted to modules and pipelines to be used for our application.

- **venv**
Created using conda virtual environment.

- **exception.py**
Contains the code for handling custom exceptions in our aplication.

- **logger.py**
Contains the code for logging, the format associated with it and stores the logs in the 'logs' directory.

- **utils.py**
Extra utilities that can be used by other components in our application.


## Converting code to modular code
- Put the required code into various components as defined above in the project structure.
- Create the prediction pipeline for predicting the data given as input in the Flask app.

## Making a web app
- Flask has been used as the web server.
- 'templates' contain various html files to be rendered.

## Deploying to AWS Beanstalk
- Create python.config file in .ebextensions directory with the elastic beanstalk configuration.
- Creating EC2 instacne profile for beanstalk.
    - Open IAM Console. In the navigation pane of the console, choose Roles and then create role
    - Under Trusted entity type, choose AWS service. Under Use case, choose EC2, Choose Next
    - Attach- AWSElasticBeanstalkWebTier, AWSElasticBeanstalkWorkerTier, AWSElasticBeanstalkMulticontainerDocker. Choose Next
    - Enter a name for the role - aws-elasticbeanstalk-ec2-role. Choose Create role.
- Create web app using Elastic Beanstalk service on AWS using Python as platform and selecting 'sample application' under application code.
- Creating pipeline using AWS Codepipeline service.
    - Select GitHub in Source Provider and enter required repository details.
    - Select AWS Elastic Beanstalk under Deploy provider and enter required application information.

## Deploying to AWS using EC2 intance with Docker
- Create Dockerfile at the root level of the application and build the image.
- Set up GitHub actions by creating .github directory with main.yaml specifying the workflow for CI/CD.
- AWS ECR is used for storing the private docker images created in our application.
- Create IAM user with the following permissions policies:
    - AmazonEC2ContainerRegistryFullAccess
    - AmazonEC2FullAccess
- Create access key for CLI for the IAM user created. 
- Create private ECR repository.
