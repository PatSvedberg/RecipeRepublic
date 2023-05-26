# Recipe Republic - Recipe Maker. Project 4 by Patric Svedberg

## [Heroku Deployment](https://recipe-republic.herokuapp.com/)
<br>

# Introduction
## About Recipe Republic
Recipe Republic is a comprehensive recipe making site designed to simplify your cooking journey. We understand that the joy of cooking lies in the perfect balance of creativity, taste, and convenience.

## Target Audience
Recipe Republic caters to anyone with a love for food and a desire to discover new recipes. Whether you're a busy professional seeking quick and easy meals, a home cook looking for family-friendly recipes, or an adventurous foodie eager to explore different cuisines, we have something for everyone. Our user-friendly interface and intuitive search system make it effortless to find recipes tailored to your preferences.

# User Stories
## Account:
* As a admin I can make sure only users can create recipes so that being able to manage content easier
* As a **User ** I can create a user profile so that I can create and save recipes
## CRUD:
* As a user I can only edit or delete recipes if I'm the owner so that other users will not edit or delete them
* As a user I can view created recipes so that I can use them when cooking
* As a site admin/user I can create, read, update and delete posted recipes so that I can manage the content
## User Profile:
* As a user I can view my profile page so that to see my private recipes and edit user info
* As a user I can copy the ingredients from a recipe to a shopping list so that I easily can see what I need to buy when making the recipe
* As a user I can create my own recipes so that I can view and share them with others
## UI/UX:
* As a user I can have a placeholder image based on what recipe category i make so that the recipe will have an image even if I don't have one of my own
* As a user I can to see the recipes on the front page so that I'm presented with recipes at the start
* As a user I can view the recipe as a list so that I can see recipes submited
* As a user I can view latest uploaded recipes sorted by category (drink/food) so that I can see what is uploaded more easily
* As a user I can search recipes so that I can find what I'm looking for easier
* As a user I can view the recipes in a modal so that I can view recipes without opening a new page
* As a user I can choose to open recipes in a new page when viewing them in a modal so that view the recipes in a full screen view and have two options how to view them

# Database Design

## User:
| Type  |  Name    |  |
| ------------- |:-------------:| -----:|
| int   | UserID |
| CharField      | Username      |
| CharField | Email      |
| CharField | Password      |

## Recipe

| Type       |Name|  |
| ------------- |:-------------:| -----:|
| ForeignKey User        | Owner           |
| int     | RecipeID |
| CharField     | Title |
| CharField      | Description      |
| TextField | Instruction      |
| TextField | Ingredients      |
| ImageField | image      |
| CharField | Category      |
| CharField | Vegan      |
| CharField | Publicity      |
| DateTimeField | Post Date      |

<br>

## Profile

| Type       |Name|  |
| ------------- |:-------------:| -----:|
| ForeignKey User     | User |
| CharField      | User Image      |
| TextField | Bio     |
| CharField | First Name     |
| CharField | Last Name     |

<br>

# Database Relationships

![ERD Image](/assets/images/readme-erd.png)


# Design
## Pages
### **Index**
The front page will display a greeting text to the user, along with the four most recent food and four most recent drink recipes that have been uploaded.
### **Create Recipe**
The create recipe form is located on this page, accessible only to logged-in users. If you are not logged in and try to access this page, you will be redirected to the login page.
### **Browse Recipe**

Here, the user can browse all the recipes by utilizing the search bar or filtering the list to display all recipes, food recipes, drink recipes, or vegan recipes.
### **View Recipe**
Here, the user will be able to read all the created recipes and view all the information provided by the creators.
<br>
# Wireframe
## Front page:
![Flowchart Image](/assets/images/wireframe_home.png)
## Create Recipe Page:
![Flowchart Image](/assets/images/wireframe_create.png)
## Browse Recipe Page:
![Flowchart Image](/assets/images/wireframe_browse.png)
## Profile Page:
![Flowchart Image](/assets/images/wireframe_profile.png)
<br>
## Flowchart
## Features
## Colors
![Palette Image](/assets/images/readme_palette.png)
Created with [coolors.co](https://coolors.co/)
<br>

# Testing

## Manual Testing:

| Test       | Action           | Expected Result  | Expected Result  |
| ------------- |:-------------| :-----| :-----|
| User       | Create User | Be able to create a user   | Works as expected |
| Admin       | CRUD User | Admin is able to create, read,<br> update and delete user  | Works as expected |
| Admin       | CRUD Recipe | Admin is able to create, read,<br> update and delete recipe  | Works as expected |
| User       | Create a recipe | Only a user will be able<br> to create a recipe| Works as expected
| User   | View Recipe | Be able to view a recipe when <br> logged in and not logged in. | Works as expected
| User      | CRUD Recipe      | Only the user who created the recipe<br> will have the ability to update or delete it | Works as expected
| User | Search recipe      | Search recipes from the search bar  | Works as expected
| User | Browse Recipe category  | Browse recipe category<br> (All, Food, Drink, Vegan)  | Works as expected

## Validators:
### Python Linter
### HTML Validator
### CSS Validator
### Lighthouse
### Known bugs

# Agile Workflow
An approximation of the agile workflow was implemented in the development of this project. The key ideas adopted were:

* **Prioritize essential features:** I focused on the implementation of fundamental features that were the most important for the project's core functionality.

* **Work in small Iterations:** The project was divided into manageable iterations, lasting one week. Each iteration was to deliver a functional portion of the project.

* **Add Additional Features When Possible:** After completing the most important features, I focused on adding more functions and a better user experience.

# Content
## Helpful souces
* [W3schools](https://www.w3schools.com/python/)
* [Stack Overflow](https://stackoverflow.com/)
* [Reddit r/Python](https://www.reddit.com/r/Python/)
* [Code Institute](https://learn.codeinstitute.net/dashboard)
* [Youtube](https://www.youtube.com/)

# Credit

## Media
* [Hero Image](https://www.pexels.com/)


## Coding
* [Button Design](http://bestjquery.com/tutorial/button/demo115/)


# Deployment:

# Technologies Used
## Languages Used
* [HTML]()
* [CSS]()
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Softwares used
* [Github](https://github.com/PatSvedberg/cal-calc)
* [Heroku](https://calcalc.herokuapp.com/)
* [CI Python Linter](https://pep8ci.herokuapp.com/#)
* [Lucidchart](https://www.lucidchart.com/pages)
* [Gitpod](https://gitpod.io/)

## Frameworks, packages and other
* [Django]() - A high-level Python web framework that simplifies and accelerates the development.
* [Bootstrap 5]() - A library consisting of CSS and JavaScript components used to create responsive websites.
* [Cloudinary]() - A cloud storage service for media files, commonly used to serve static files.
* [Crispy Forms]() - A package that simplifies the process of styling Django forms automatically.
* [Django-richtextfield]() - Package that provides a rich text field for storing and rendering formatted text content within your Django application.
* [ElephantSQL]() - An online service that offers PostgreSQL server hosting as a service.
* [dj3-cloudinary-storage]() - Provides the functionality to utilize Cloudinary storage for serving static files and media in Django.
* [dj-database-url]() - Enables the usage of Database URLs within your Django application..

## GitHub

The project was deployed to GitHub Pages using the following steps...
1. Log in to GitHub and locate the GitHub Repository.
2. Find the "Settings" button on the menu at the top of the repository
3. Scroll down the Settings page until you reach the "Pages" section.
4. In the "Source" section, click the dropdown labeled "None" and choose "Main Branch".
5. The page will refresh automatically.
6. Wait for the deployment process to complete.
<br>
<br>

## Forking

To create a copy of an existing GitHub repository without affecting the original, we can fork the repository using these steps:
1. Log in to your [GitHub](https://github.com/) account and navigate to the repository you want to fork.
2. Click the "Fork" button at the top right of the repository page.
3. You should now have a copy of the original repository in your GitHub account that you can view and make changes to without affecting the original.
<br>
<br>

## Clone
Here are the steps to clone a GitHub repository:
1. Log in to your [GitHub](https://github.com/) account and locate the repository you want to clone.
2. Click the "Clone" button.
3. Copy the HTTPS link shown under "Clone with HTTPS".
4. Open Git Bash or another command-line interface.
5. Navigate to the directory where you want to store the cloned repository.
6. Type git clone and paste the URL you copied in Step 3. The command should look like this: git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.
7. Press Enter to run the command.
8. Wait for the cloning process to complete. A message like the following should appear in the console:

```
    $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
    > Cloning into `CI-Clone`...
    > remote: Counting objects: 10, done.
    > remote: Compressing objects: 100% (8/8), done.
    > remove: Total 10 (delta 1), reused 10 (delta 1)
    > Unpacking objects: 100% (10/10), done.
```

## Push
1. Navigate to your local Git repository on your computer using your terminal or command prompt.
2. Make sure you are on the correct branch by running the command: `git branch`. If you're not on the correct branch, you can switch to it using: `git checkout <"branch-name">`.
3. Next, add the changes you have made to the file to the Git staging area using the command: `git add <"filename">`, or `git add .` to commit all files. This will prepare the changes for committing.
4. Commit the changes to the repository using the command: `git commit -m "Commit message"`.
5. Push the changes to the remote repository using the command: `git push`. This will update the file on the remote repository, making your changes available to others.


## Heroku Deployment

* Created a app called 'recipe-republic'.

* Add Procfile to project root directory

* Added these config vars:
    * CLOUDINARY_URL
    * DATABASE_URL
    * DISABLE_COLLECTSTATIC
    * HEROKU_POSTGRESQL_GRAY_URL
    * SECRET_KEY

* Before final deployment, the debug setting in settings.py was set from **TRUE** to **FALSE** for security.
    * Due to some Heroku problems I had to do it like this:
        * **DEBUG = 'DEVELOPMENT' in os.environ**
            * And added this inside my env.py:<br>**os.environ["DEVELOPMENT"] = "1"**<br>(And commit it out before deployment.)

* Before the final deployment, the DISABLE_COLLECTSTATIC config var in Heroku was changed from 1 to 0
* Connect to Github repository
    * Deploy from branch
    * Select GitHub branch
    * Click deploy button 

## ElephantSQL Account Setup
* Create account with Github
* Click Create New Instance
* Choose TinyTurtle Plan
* Enter project name
* Pick region
* From dashboard. Click the project
* Copy URL and paste to **env.py**
* Inside **settings.py** add this:

```
import os
import dj_database_url
if os.path.isfile('env.py'):
  import env
```
In **settings.py** add enviroment variables:
```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
 }
```
Migrate changes:
```
$ python manage.py makemigrations
$ python manage.py migrate
```

## Cloudinary Setup
* Create Cloudinary account
* From the dashboard, copy the URL
* Paste it inside the **env.py**:
```
    import os

os.environ["DATABASE_URL"] = the databse URL from ElephantSQL
os.environ["SECRET_KEY"]= a string used to generate security keys
os.environ["CLOUDINARY_URL"] = The url for Cloudinary storage
```
* Then copy the URL to the Heroku Config Vars
* Also add a temporary called DISABLE_COLLECTSTATIC and set it to "0"
* Add Cloudinary to installed app inside **settings.py**
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',

    # My Apps
    'cloudinary',
```
* Then tell Django to use Cloudinary for our static files by adding this in **settings.py**
```
STATIC_URL = '/static/'

# Cloudinary Settings
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```