# Sample API project

## What is an API and what does it do?

API stands for Application Programming Interface. It allows one application to get or send data from
one application to another and can define actions to take when it is called.

In this case, the API is a simple web app that returns historical weather information from a local data folder, for a small group of weather stations in the EU.

### Set up

Prerequisite: Ensure you have Python 3.10 or newer installed on your system

1. Download clone the project to a local directory

2. Open your terminal and navigate to that directory

3. Set up a virtual environment for this project to avoid bloating your system install of Python
   "python 3.10 -m venv venv"

4. Run the activation script for your venv from the venv/scripts folder
   Windows example: "/<yourdirectory>/venv/Scripts/activate.ps1"
   Your command prompt should now show the name of your virtual environment at the beginning of
   the prompt in your terminal window.

5. Using the terminal with your activated command prompt, install the requirements for this project
   "pip install -r requirements.txt"
   This will install the flask and pandas libraries that the project needs to run

6. Once that is done, you should be able to run the weather.py file which will run the service on your local machine at the default ip and port of http://127.0.0.1:5000

7. Open that in your browser of choice and you should see the home page for this API
