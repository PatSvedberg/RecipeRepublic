# Recipe Republic - Recipe Maker. Project 4 by Patric Svedberg

## [Heroku Deployment](https://recipe-republic.herokuapp.com/)
<br>

# Introduction
Recipe Republic is a site for those who loves to make recipes or just interested in finding something new to cook.

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

| Recipe       |           |  |
| ------------- |:-------------:| -----:|
| type        | name           |
| ------------- |-------------|
| ForeignKey User     | user |
| CharField     | title |
| CharField      | description      |
| RichTextField | instructions      |
| RichTextField | ingredients      |
| ResizedImageField | image      |
| CharField | image_alt      |
| CharField | publicity      |
| DateTimeField | post_date      |

<br>

| Profile       |           |  |
| ------------- |:-------------:| -----:|
| type        | name           |
| ------------- |-------------|
| ForeignKey User     | user |
| CharField      | image      |
| RichTextField | bio      |

<br>

# Database Relationships


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

## Known bugs

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
* [Figma]()
* [Gitpod](https://gitpod.io/)

## Frameworks and packages
* [Django]()
* [Bootstrap 5]()
* [Cloudinary]()
* [Crispy Forms]()
* [Django-richtextfield]()

# Content
## Helpful souces
* [W3schools](https://www.w3schools.com/python/)
* [Stack Overflow](https://stackoverflow.com/)
* [Reddit r/Python](https://www.reddit.com/r/Python/)
* [Code Institute](https://learn.codeinstitute.net/dashboard)
* [Youtube](https://www.youtube.com/)

## Media
* Hero image from [pexels.com](https://www.pexels.com/)

    # Deployment:

    ## Deployment

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
    <br>
    <br>