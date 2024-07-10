# Overview

I wrote a web app in django that allows the user to enter a task with a name, descriction, and time associated with it adn view it in a week calendar format. I run this by using
django's manage.py with the argument being runserver. This starts the page and allows access on your local computer on port 8000 (http://127.0.0.1:8000)

I made this project to fimiliarize myself with django and how things interact in this library. Specifically I built a calendar to help with a seprate project involving gamifiying a to-do list.

[Software Demo Video](https://www.youtube.com/watch?v=BbwHpyW9CtM)

# Web Pages

I created a calendar and a add task page. The calednar is a table where each date of the week is passed to the template and made for each day of the week. This creates a day of the day of the week
and the actual date of that day for their respective tasks under them. The tasks in the database are then iterated through and put in their respective day and ordered by time. This is done
by passing a dictionary to the template when loading it. the add task page uses django's built in form that is built on the page and the user can interact with it.

# Development Environment

I used VScode as my environment and IDE with github to hold my code.

I used python and django to build the app. Speciffically a django project for the server and an app for the urls and templates.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Tech With Tim Django Tutorial](https://www.youtube.com/watch?v=nGIg40xs9e4&t=103s)
* [Chat GPT](https://chatgpt.com/)
* [W3Schools Django Tutorial](https://www.w3schools.com/django/index.php)

# Future Work

* Registration For User
* More Styling for calendar
* Public Website
