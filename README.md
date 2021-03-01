

## Step 1: Install requirements.txt

`pip install -r requirements.txt`

## Step 2: Create databases

Create the databases and the initial migrations with the following command:
`python manage.py migrate`

## Step 3: Create user

`python manage.py createsuperuser`


## Step 4: Run server

And start the server with 

`python manage.py runserver`

You should now be able to go to localhost:8000/chat/ and chat with the bot

## Step 4: Test 

Login with the user name and password created at step 3
Click the three buttons to get output from bot
Click the `Userstats` to get the button click count of all users

