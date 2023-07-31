

![](https://concept-stories.s3.ap-south-1.amazonaws.com/test/Stories%20-%20Images_story_77297/image_2019-08-08%2013%3A54%3A12.963547%2B00%3A00)


#      **Basic Bank Server**

## _this is a Django server application created to communicate with a React frontend_

### this project includes
* Python
* Django
* sqlite



![](./src/main/resources/squintreadmepic.jpg)



### Synopsis
Basic bank is an application created to mirror how the typicall bank website works.
it has most of the typical features one would come to expect from a bank. Personally
I bank with Wells Fargo, and I abosolutely LOVE how their website looks. Beacause of
this a lot of how my main page and the sign up page looks is inspired by their themes.


### how to use it
when you first open the application, there will be a button to test me. if you
push the button you will be taken to a random acccount that you can use to test
drive the application and see how the features work.If you want to create an 
account you can also do that, just bear in mind that the database is ephemeral
and will not save once you close the application. enjoy!!



### Challenges
the main challenge that I encountered with this project was the security issue.
You see with Django if you do not use the built in template system, then you 
have to create your own way of accessing the csrf token, which I only vagueley
knew about. howevery I soon learned that if you go cross platform(like in this 
case using React with Django), you must create a routes specifically to generate
a csrf token before each request to the server. Lots of headaches at first, but
now I am very grateful that I learned it. On to the next challenge we go!!!


### Code Review
this project is a Django server that connects to a React front end. the code is
straightforward and setup with the typical urls.py and views.py for the routes,
nothing out of the ordinary. I used sqlite as the database as it comes built
in and is very convenient because of its ease of use and flexibility being a
single file.




### final thought
#### this project was designed as a test and a simple project. Some parts of a django server are more convenient than say express, however Django is very opinionated, and does not leave as much room for creativity as I would like. either way its still cool. Thanks for reading and happy coding!!!


### for more projects by CyberStizz visit: [Charleslambjr.com](https://www.charleslambjr.com/)