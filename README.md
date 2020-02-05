# berlin-dictionary




To do:
-add comments to code
-clean up code

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
https://www.w3schools.com/howto/howto_js_scroll_to_top.asp
A lot of the setup was taken from the CodeInstitute Lectures

https://docs.mongodb.com/manual/text-search/
https://www.youtube.com/watch?v=dTN8cBDEG_Q&feature=youtu.be


https://www.mongodb.com/blog/post/integrating-mongodb-text-search-with-a-python-app

http://zetcode.com/python/pymongo/


print(list(cars))
With the list() method, we can transform the cursor to a Python list. It loads all data into the memory.


 
