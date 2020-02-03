# berlin-dictionary


Share function 
- to take out comment on top of the share function
-to show the whole link rather than just the end

To build:
>search
>filters - alphabetical order prioritizes capital letters
>upvote - reloads the page when updating the score + some bug on the first word - shows a random number before the correct one
    ?commented out Upvote in manageword - do I want an upvote button there?
>styling

Back to top button:
https://www.w3schools.com/howto/howto_js_scroll_to_top.asp
A lot of the setup was taken from the CodeInstitute Lectures

https://docs.mongodb.com/manual/text-search/
https://www.youtube.com/watch?v=dTN8cBDEG_Q&feature=youtu.be


https://www.mongodb.com/blog/post/integrating-mongodb-text-search-with-a-python-app

http://zetcode.com/python/pymongo/


print(list(cars))
With the list() method, we can transform the cursor to a Python list. It loads all data into the memory.


 for result in db_results:
        if result:
            search_results.append(result)
            print(search_results) 
            print(result['author'])           
        else:
            print("Sorry, this word doesn't exist in the dictionary.")

search_result =[]
    input = request.form.get['search_query']
    search_result.append(input)
    print(search_result)