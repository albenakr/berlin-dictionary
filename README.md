 # The Berlin Dictionary

This project was created for educational purposes as part of the CodeInstitute Fullstack development bootcamp with the goal to showcast my understanding and skills with databases and CRUD.

The Berlin Dictionary aims to provide a platform to create and share the Berlin experience. More specifically, it aims to provide a fun and easy community-created dictionary, which documents and satirizes what it's like to live in Berlin. 

The primary prupose of the Berlin Dictionary is to provide entertainment. Any content on it, whether it's a new addition or browsing through old postings, should be approached with humour, sarcasm and self-reflection.

## UX

### Goals
From a site owner's perstective:
* The goal of the website is to collect a substantial amount of definitions in order to publish a book of humourous content as well as build online presence and a brand around the website.
* It is targetted primarily at younger audiences, active on social media, who are looking for fun content to engage with and share.

From a user's perspective:
* Being able to find, create and share definitions.

Some of the main considerations with the UX design were to make the website friendly, intuitive, quick and easy to use. The design is visually quite minimalist in order to emphasize the functionality and options behind it. Explanations and guidance are provided only in limited occasions, where the way the application works was considered less obvious or intuitive (e.g. Use '/' in between comments to add multiple.) or in cases of notifying users of the rules and process (e.g. if they edit a word, the score would be reset to 0.)

A lot of thought and consideration was put into the flow from one functionality to the other to create a seamless experience and accomodate different approaches to the website - whether a user is clicking through the navigation menu or just following the flow of browsing through words organically. An example of that would be the 'Add Word' option - this could be accessed through the Navigation Bar, but it also appears if a user looks for a word, that doesn't exist in the dictionary. 

*User stories:*
- As a user, I want to be able to find the existing definitions, so that I can read through them.
- As a user, I want to be able to always see a word's definition, examples provided, author and score, so that I can compare words across the same parameters.
- As a user, I want to be able to filter through the existing definitions, in order to see them in an alphabetical order.
- As a user, I want to be able to filter through the existing definitions, in order to see them ranked by score.
- As a user, I want to be able to filter through the existing definitions, so that I only see the ones upvoted multiple times.
- As a user, I want to be able to search for a specific word, in order to see all definitions available for it. 
- As a user, I want to be able to edit a definition, so that I can fix errors or provide a better definition.
- As a user, I want to be able to add a definition, in order to interact with the website and add my own contribution.
- As a user, I want to be able to upvote a definition, in order to express my approval.
- As a user, I want to be able to delete a definition, so that any erroneous or bad definitions can be removed.
- As a user, I want to be able to copy the link of an individual definition, in order to share it with others through chat or social media. 

Wireframes used in the design process are added in a folder 'wireframes' within this project. While the general structure of the wireframes was followed, several changes were made throughout the development process. They were a result of intacting with the website and realizing there were more intuitive and user-friendly ways to present certain aspects.
Some examples: originally there was no 'Browse Definitions' option in the navigation menu, since the Berlin Dictionary logo was meant to be used as a way to get back to the home page. After interacting with the page, I realized that while it's helpful for logo to redirect to the Home/Browse Definitions page, it is still nicer to have a more obvious option. 

Due to the minimalist nature of the design, the same wireframes were considered appropriate and used for both web and mobile. Throughout the testing, this proved to be the case as all pages were working well across different screen sizes. The only adjustment needed was for the section, displaying the filter options, which is the only one with a significantly different layout on mobile.


## Features

The main features of the website include the posibility to search for a word/definitions, browse existing definitions, add a definition, and manage existing definitions - covering the possibility to Edit, Delete, Upvote and/or Share. 

### Existing Features

#### Primary Features
The python backend code for all functionality is within the app.py file. All HTML template files extend on the base.html file. Templates corresponding to the main functionality are specified below:
- Browse through all current submissions in the dictionary - all definitions appear in a card form, displaying all completed fields, including word, definition, examples (if any) and author (words.html).
- Add a word to the dictionary - possibility to add a new word. The word and definition fields are required, while the examples and author are not. There is the possibility to add multiple examples. Author is automatically set to Anonymous, if not added by the user. Each new word's score is 0 until upvoted (addword.html).
- Edit an already existing word - all fields of the word are editable, except score, with word and definition still the only required ones. Once a word is edited, the score automatically resets to 0. (editword.html)
- Delete a word - the option is within the 'manageword.html' template, and it redirects to a landing page once executed.
- Search the dictionary for an existing word. - available through both 'words.html' and 'managewordspage.html'
- Upvote a word - each definition has a starting score of 0 and get 1 additional vote anytime the 'Upvote' button is clicked. Available on the 'manageword.html' page.

#### Secondary and Smaller Features 
- Share a word - option to automatically copy the link of a word, in order to be shared with others.
- Filter words - possibility to change the way the words appear in the Browse Words section - they can be shown alphabetically (from A to Z), arranged by score from highest to lowest, and an additional 'Popular Words' filter shows only words with a score of 5 or above.

### Features Left to Implement
- Currently the Upvote functionality is only available on the 'Manage Word' page for each individual word. The reasoning for that was that it currently uses a <form> to collect the input, which refreshes the page - if a user upvotes a word further down a longer list of words, upvoting will refresh the page and send them back to the top, which is not a great user experience. In order to get the upvote function to display the new score without refreshing required implementing AJAX, but there was not enough time within the timeframe of this project. 
- Currently any site visitor can edit, delete, upvote words etc, regardless of whether they were the ones creating the original word or not. Further development should limit these options in some form, providing the option for users to register, and allowing only registered users to add, edit and delete words.
- Currently, when editing a word the score automatically resets to 0. This happens when the 'Update Word' button is clicked, regardless of whether the user actually made any changes. Future updates of the website to check if any changes were made before resetting the score.

## Technologies Used

* HTML
    * HTML was used for template structure
* CSS
    * CSS was used for custom styling
* JQuery
    * JQuery was used to access the DOM
* Materialize 
    * Materialize was used for most of the page elements and basic styling, including the navbar, words cards, input forms, buttons, icons etc.
* Javascript
    * JS was used with some of the materialize elements, as well as for EventListeners.
* Git
    * Git was used for version control.
* Github
    * Github was used as storage and way of sharing the source code.
* Python
    * Most of the backend functionality was build in Python.
* Flask 
    * Flask was used to build routes and render pages.
* Flask-PyMongo
    * Flask-Pymongo was used as a convenient way to use Flask and MongoDB and easily implement CRUD functionality.
* MongoDB Atlas
    * Database storage.

## Testing

The page was tested primarily manually to ensure both the functionality is working as intended, but also it works across all screen sizes.

The page was tested continuously throughout the development process, as well as multiple times after completion. 

For Browser compatibility, it was tested on Chrome and Microsoft Edge.

For responsiveness it was tested through the Dev Tools on the available sizes - browser view, Galaxy S5, Pixel 2, Pixel 2 XL, iPhone 5, 6, 7, 8, 8Plus, X, iPad, iPad Pro. It was additionally tested on one mobile device.

Details on the testing can be seen in the 'tests.txt' file within the 'tests' folder of this project.


## Deployment

### Running the code locally 
Project was developed on Gitpod, using Git and Github for version control. Pip and Python are required.
1. Copy the project file from [the Github repository]('https://github.com/albenakr/berlin-dictionary') 
4. Create a file named env.py in the root directory of the project to use to define the environment variables.
5. Create a file named .gitignore in the root directory of the project.
6. In the .gitignore file add the following text to it: `env.py` 
7. In the env.py file, import os so that you can set the environment variables in the operating system and assign the environment variables, in this case Mongo URI: 
```
import os

os.environ["MONGO_URI"] = "mongodb+srv://<username>:<password>@<cluster_name>-z5lfd.mongodb.net/<database_name>?retryWrites=true&w=majority"

```
8. Then use the following code to import this new env.py file in the app.py file. Add this under your other imports at the top of the file. 
```
from os import path
if path.exists("env.py"):
  import env
```
The if statement here is so that the env.py file is only pulled when working on your code in your workspace, not when it is deployed on heroku. For deployment you can set your environment variables in the heroku dashboard in settings > config vars.
9. Now that your environment variables have been set in your env.py file, and the file has been imported into your project, you can use them as needed using the following syntax: 
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
10. Make sure you save all your files before testing if it works.


### Heroku Deployment
1. Install Heroku with the following command: `npm install -g heroku`
2. Login to Heroku by using the following command: `heroku login`
3. Associate the Heroku application as our master branch, or remote master branch. Command: `Heroku git:remote {name of the app on heroku}`
4. Create a requirements.txt file. Command: `pip3 freeze --local > requirements.txt`
5. Create a Procfile: `echo web python3 {app.py or name of python file} > Procfile`
6. Add and commit to Git.
7. Push to Heroku. Command: `git push heroku master`
8. Set up Configuration variables in Heroku:
    - IP: 0.0.0.0
    - PORT: 8080
    - MONGO_URI: mongodb+srv://<username>:<password>@<cluster_name>-z5lfd.mongodb.net/<database_name>?retryWrites=true&w=majority

9. You can see the live app here: https://berlin-dictionary.herokuapp.com/


## Credits

### Content
- All content was custom created for this app.
- Some of the content of the deployment write-up was taken from the lectures or Slack channel support, as those were the instructions I followed.

### Acknowledgements

- Back to Top button was taken from this W3Schools example: https://www.w3schools.com/howto/howto_js_scroll_to_top.asp

- The structure and approach to CRUD functionality with MongoDB was inspired from the CodeInstitute mini-project examples.

- Research into websites such as https://www.urbandictionary.com/ was used in defining the concept and approach to the webpage.
