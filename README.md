# Create Landing Page
You will need to create the following files/folders:
Virtual Environment
Main Package Folder
At min 2 blueprint folders with
- templates_folder (ie auth_templates)
- routes.py
- static
- main_templates_folder (ie templates)
- __init__.py
- config.py

Create the flask environment variables 

Create a .gitignore file and place your Virtual Environment inside of that along with .vscode and __pycache__ folders. 
If you're on a Mac, add the .DS_Store file as well. 
______________________________________________________________________
# Create a User Form and User Database
Build a form for a user to input data and persist that data into a Car-Collection Database Table Called "user".

You will need to create the following:
Inside of the blueprint folder for "authentication" (assuming the name is "authentication"):
- 1 routes: One for "signup"
- 1 User Model with the basic infomation listed:
- ID
- First_name
- Last_name
- email
- password
- token
- date_created
- 1 Form with the following information:
- email
- password
- submit_button
- 1 .env file: to add your DATABASE_URL

So by the end of the homework for tonight you should have:
- A Database Called "car-collection" (Create this inside of Elephant SQL)
- A Database Table called "user"
- A form that can be placed on your HTML for signup
- Data in the user table given to your database by the user form

You will need to add the following dependencies to your virtual environment
- pip install Flask-WTF
- pip install Flask-Migrate
- pip install psycopg2
- pip install psycopg2-binary -- For those on mac machines
- pip install email-validator -- Verification of emails inside of forms
- pip install python-dotenv

__________________________________________________________________________

# Create Authentication for Email/Password - CRUD API Operations
Inside of your car collection api project create login functionality with Flask Login.

You will need the following packages for the project:
flask-login (Flask-Login==0.5.0)
secrets (import secrets)
flask-marshmallow (flask-marshmallow==0.14.0) 

You should be able to log in and log out via email/password and create CRUD API routes.
While logged in, you should also be able to access your profile page (this should be a protected route, only available for authed users)

Login and access your token, create your CRUD operations
CREATE - Car
RETRIEVE - Cars/Car (get all and single drone(s))
UPDATE - Car
DELETE - Car

Also, create at least one car 🚗(possibly two if you are using numeric as a datatype for your Car model) to verify that your API route has a token passed to it.
Once completed, send the updated code to your project's repository. 
__________________________________________________________________________

# Create CRUD Operations for API
To finish your API, you will now need to implement CRUD operations for your car collection API. 

By the end you should have:
5 Routes for: Create, Retrieve (2 routes here...GET ALL Cars, GET SINGLE Car), Update, Delete
Should be able to run your app and use Insomnia to manipulate data in your database.