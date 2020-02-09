To do:
-add comments to code
-clean up code

Cards are not responsive

>If Upvote - the back button doesn't work properly

>filters - alphabetical order prioritizes capital letters
>upvote - reloads the page when updating the score + some bug on the first word - shows a random number before the correct one
    ?commented out Upvote in manageword - do I want an upvote button there?
>Share function 
- to take out comment on top of the share function
-to show the whole link rather than just the end
>


>styling
for result in db_results:
        if result:
               
        else:
            print("Sorry, this word doesn't exist in the dictionary. - add functionality")


With AJAX:
@app.route('/upvote/<word_id>', methods=['POST'])
def upvote_word(word_id):
    words = mongo.db.words
    the_id= {"_id": ObjectId(word_id)}
    the_word = words.find_one(the_id)
    the_word['score'] = the_word['score'] + 1
    words.replace_one(the_id, the_word)
    if request.is_xhr or request.accept_mimetypes.accept_json:
        print('ajax')
        return make_response(jsonify({"score": the_word['score']}), 200)
    else:
        print('request')
        return redirect(url_for('get_words'))

Back to top button:

A lot of the setup was taken from the CodeInstitute Lectures

https://docs.mongodb.com/manual/text-search/
https://www.youtube.com/watch?v=dTN8cBDEG_Q&feature=youtu.be


https://www.mongodb.com/blog/post/integrating-mongodb-text-search-with-a-python-app

http://zetcode.com/python/pymongo/


print(list(cars))
With the list() method, we can transform the cursor to a Python list. It loads all data into the memory.


 # The Berlin Dictionary

This project was created for educational purposes as part of the CodeInstitute Fullstack development bootcamp with the goal to showcast my understanding and grasps of working with databases and CRUD.

The Berlin Dictionary aims to provide a platform to create and share the Berlin experience. More specifically, it aims to provide a fun and easy community-created dictionary, which documents and satirizes what it's like to live in Berlin. 

The primary prupose of the Berlin Dictionary is to provide entertainment. Any content on it, whether it's a new addition or browsing through old postings, should be approached with humour, sarcasm and self-reflection.

## UX

###Goals
From a site owner's perstective:
> The goal of the website is to collect a substantial amount of definitions in order to publish a book of humourous content as well as build online presence and a brand around the website.
> It is targetted primarily at younger audiences, active on social media, who are looking for fun content to share and engage with.

From a user's perspective:
> Being able to find, create and share definitions.

Some of the main considerations with the UX design were to make the website friendly, intuitive, quick and easy to use. The design is visually quite minimalist in order to emphasize the functionality and options behind it. Explanations and guidance are provided only in limited occasions, where the way the application works was considered less obvious or intuitive (e.g. Use '/' in between comments to add multiple.) or in cases of notifying users of the rules and process (e.g. if they edit a word, the score would be reset to 0.)

A lot of thought and consideration was put into the flow from one functionality to the other to create a seamless experience and accomodate different approaches to the website - whether a user is clicking through the navigation menu or just following the flow of browsing through words organically. An example of that would be the 'Add Word' option - this could be accessed through the Navigation Bar, but it also appears if a user looks for a word, that doesn't exist in the dictionary. 

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user, I want to be able to look through the existing definitions, so that I can read through them.
- As a user, I want to be able to always see a word's definition, examples provided, author and score, so that I can compare words across the same parameters.
- As a user, I want to be able to filter through the existing definitions, in order to see them in an alphabetical order.
- As a user, I want to be able to filter through the existing definitions, in order to see them ranked by score.
- As a user, I want to be able to filter through the existing definitions, so that I can see only the ones upvoted at least 5 times.
- As a user, I want to be able to search for a specific word, in order to see what definitions are available for it. 
- As a user, I want to be able to edit a definition, so that I can fix errors or provide a better definition.
- As a user, I want to be able to add a definition, in order to interact with the website and add my own contribution.
- As a user, I want to be able to upvote a definition, in order to express my approval.
- As a user, I want to be able to delete a definition, so that any erroneous or bad definitions can be removed.
- As a user, I want to be able to copy the link of an individual definition, in order to share it with others through chat or social media. 

Wireframes used in the design process are added in a folder 'wireframes' within this project. While the general structure of the wireframes was followed, several changes were made throughout the development process. They were a result of intacting with the website and realizing there were more intuitive and user-friendly ways to present certain aspects.
Some examples: originally there was no 'Brose Definitions' option in the navigation menu, since the Berlin Dictionary logo was meant to be used as a way to get back to the home page. After interacting with the page, I realized that while it's helpful for logo to redirect to the Home/Browse Definitions page, it is still nicer to have a more obvious option. Additionally, the Manage Words page doesn't display 'Edit' and 'Delete' functions for each word, but rather the option to choose a definition and be redirected to a page, which allows you to upvote, edit, delete or share.



## Features

The main features of the website include the posibility to search for a word/definitions, browse existing definitions, add a definition, and manage existing definitions - covering the possibility to Edit, Delete, Upvote and/or Share. 

### Existing Features

#### Primary Features
The python backend code for all functionality is within the app.py file. All HTML template files extend on the base.html file. Templates corresponding to the main functionality is specified below:
- Browse through all current submissions in the dictionary - all definitions appear in a card form, displaying all completed fields, including word, definition, examples (if any) and author - words.html.
- Add a word to the dictionary - possibility to add a new word. The word and definition fields are required, while the examples and author are not. There is the possibility to add multiple examples. Author is automatically set to Anonymous, if not added by the user. Each new word's score is 0 until upvoted -  addword.html.
- Edit an already existing word - all fields of the word are editable, with word and definition still the only required ones. Once a word is edited, the score automatically resets to 0. - editword.html
- Delete a word - the option is within the manageword.html template.
- Search the dictionary for an existing word. - available through both 'words.html' and 'managewordspage.html'
- Upvote a word - each definition has a starting score of 0 and get 1 additional vote anytime the 'Upvote' button is clicked.

#### Secondary and Smaller Features 
- Share a word - option to automatically copy the link of a word, in order to be shared with others.
- Filter words - possibility to change the way the words appear in the Browse Words section - they can be shown alphabetically (from A to Z), arranged by score from highest to lowest, and an additional 'Popular Words' filter shows only words with a score of 5 or above.

### Features Left to Implement
- Currently the Upvote functionality is only available on the 'ManageWord' page for each individual word. The reasoning for that was that it currently uses a <form> to collect the input, which refreshes the page - if a user upvotes a word further down a longer list of words, upvoting will refresh the page and send them back to the top, which is not a great user experience. In order to get the upvote working without refreshing required implementing AJAX, but there was not enough time within the timeframe of this project. 
- Currently any site visitor can edit, delete, upvote words etc, regardless of whether they were the ones creating the original word or not. Further development should limit these options in some forms, providing the option for users to register, and allowing only registered users to add, edit and delete words.
- Currently, when editing a word the score automatically resets to 0. This happens when the 'Update Word' button is clicked, regardless of whether the user actually made any changes. Future updates of the website to check if any changes were made before resetting the score.

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

HTML
CSS
JQuery
Materialize 
Javascript
Git
Github
Python
Flask 
Flask-PyMongo
MongoDB Atlas

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- Back to Top button was taken from this W3Schools example: https://www.w3schools.com/howto/howto_js_scroll_to_top.asp

- The structure and approach to CRUD functionality with MongoDB was taken from the CodeInstitute lectures.

- Research into websites such as https://www.urbandictionary.com/ was used in defining the concept and approach of the webpage.
