# Hangman-Project
&nbsp;

The aim of this project is implement the use of python classes to play the hangman game. 

&nbsp;


## Milestone 1 - Create the variables for the game. 
&nbsp;


The first step is to create a list which contains a string of each fruit. The __import random function__ is implemented in order to pick a random word from the list of fruits.  The next step is to implement a __while True loop__ and __if/else__ statements to ask and the player to enter a single character and keep looping looping until the player enters only one character.

&nbsp;

![Alt text](Project_Images/Milstone%201.PNG)
*Figure 1 - Milestone 1 script.

&nbsp;
## Milestone 2 - Check if the guessed character is in the word.
&nbsp;

__ask_for_input method__

&nbsp;

The code written in milestone 1 was encapsulated into the __ask_for_input method__ and returns the guessed letter in string format.
&nbsp;
__check_guess method__

The method takes in the guessed letter returned from the __ask_for_input method__ as an argument and a for if/else statements within a for loop is coded to check if the guessed letter is in the chosen word.
&nbsp;

&nbsp;


![Alt text](Project_Images/Milstone%202.PNG)
*Figure 2 - Milestone 2 script.

&nbsp;



## Milestone 3 - Create the game class

&nbsp;

In order to code a complete hangman the use of object orientated programming (OOP).
&nbsp;

__init method__

The init method is used to initialise the first instance of the hangman class. The attributes of the class are defined by the parameters. The parameters allow for a complete game loop as they serve multiple purposes such as initialising a starting letter and keeping track of the guessed letters.



&nbsp;


## Milestone 4 - Containerising the scraper

&nbsp;

__Headless mode__

After confirming the unit tests still run, the next step was to run the scraper file in headless mode without the GUI. This was done so that the script could be run correctly in docker. The correct&ensp;__options arguments__&ensp; were coded into the __init method__ to allow the headless mode to work.

![Alt text](project_images/Milstone%204%20-%20options%20arguments.PNG)
*Figure 11 - Options arguments*


&nbsp;

__Docker image__

In order to build the docker image a docker file which contains the instructions on how to build the image is first created. A docker account was also created in order to upload the image file. The desktop app was downloaded.

The docker file contains the following;

* From - The base image for the docker image(python).
* Copy - Copies everything in the docker file directory (requirements.txt, scraper folder) into the container.
* Run -  Installs the required dependencies for the script to run. 
* CMD - Specifies the instruction that is to be executed when a Docker container starts.

&nbsp;

![Alt text](project_images/Milstone%204%20-%20docker%20file.PNG)
*Figure 12 - Dockerfile*


&nbsp;


The next step is to build the image using the docker build command.

&nbsp;

__Docker container__

&nbsp;

Now that the docker image is built the next step is to run the docker container using the docker run command. The script within the container ran fine with no issues. The container is then pushed onto docker hub.

&nbsp;

## Milestone 5 - Set up a CI/CD pipeline for your docker image

&nbsp;

in order to fully automate the docker image build and container run, it was first required to set up Github actions on the repository. 

__Create repository__
&nbsp;

The first step is to go yo the actions section in the repository on github and create two GitHub secrets actions. 

The first is a secret is called DOCKER_HUB_USERNAME which containes the name of the dockerhub account created and the second is called OCKER_HUB_ACCESS_TOKEN which contained a Personal Access Token (PAT) generated on dockerhub.

__Set up the workflow__
&nbsp;

The next step is to set up the GitHub Actions workflow for building and pushing the image to Docker Hub. This is done by going to the actions section on the repo and selecting set up workflow which creates a Github actions work file contained in yaml format.

&nbsp;

__Define the workflow steps__
&nbsp;

The  last step includes setting up the build context within the yaml file. The contains all the information for docker hub to copy to files mentioned in the dockerfile then build an image and automatically push to docker hub.

The last step is to commit the changes in the repo which would automatically start workflow. In order to make sure the workflow worked the image pushed on to docker hub was downloaded and a container was created and ran to ensure the script ran correctly.  A docker compose file which contains commands to self automate running containers was also created.