# web_data_app.py
# Garth Johnson, Emily Marasco
# June 15, 2021
# Modified by: Melissa Liao
#
# An simple program for demonstrating web applications using Flask and web scraping of data using Beautiful Soup.
# Detailed specifications are provided via the Assignment 6 git repository.


import pandas as pd     # needed for data manipulation

from flask import Flask, render_template    # needed for web app

from bs4 import BeautifulSoup               # needed for web scraping
import requests

from datetime import datetime               # needed for time/regular expressions
import re


###
# Initialize our FLASK application object from the Flask class like so:
app = Flask(__name__)

@app.route("/")
def index():
    """
    Our first (topmost) route (aka 'view').  Routes are like URLs, 
    which we can access from a browser. The line immediately below is known as a 
    'decorator' and implements some boilerplate code for us without much work on 
    our end.  Basically it creates a 'view' to our app and data to show the user.
    This one merely shows a static message.  Easy-peasy.
    """
    return "Hello World!"


@app.route("/hello/<name>")
def hello_there(name):
    """
    This route shows a bit more of what we can do, including some 'REST'full user 
    interaction.  If a user specifies a name in the url like so: http://localhost:5000/hello/supercoder
    the response will include the value 'supercoder' in the `name` variable, and 
    can then be validated with the RE `match_object` output.  If an invalid value is specified
    for `name` the validator code will simply assign 'friend' value to the `clean_name`
    instead.  If no value is specified, it will error out and present a 404 error to the browser.
    """
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    # Output the semi-static text with the time and supplied name (if any)
    content = "Hello there, " + clean_name + "! Welcome to Assignment 6. It's " + formatted_now
    return content


@app.route("/data")
def book_data():
    """
    Now let's take what we learned about Pandas and scrap some data from the internet!
    """

    # Web scraping can be against the Terms of Use. 
    # Always check to make sure that you are web scraping legally and ethically.
    # The following site was specifically created to practice web scraping.
    source = requests.get("http://books.toscrape.com/")
    soup = BeautifulSoup(source.content, 'html.parser')     # Use BeautifulSoup to parse the website html code
    book_results = soup.find_all(attrs={'class':'product_pod'})  # By inspecting the site, we know books = product_pod class

    titles = []
    prices = []

    # For each book listed on the page, get the title and the price from inside in the html data
    for book in book_results:
        titles.append(book.h3.a.get('title'))
        prices.append(float(book.find('p', class_="price_color").text[1:]))

    # Create a DataFrame using the two lists
    book_data = pd.DataFrame(list(zip(titles, prices)), columns=['Titles','Prices'])
    book_data['Sale Price'] = round(book_data['Prices'] * 0.75, 2)    
    print(book_data)        # Print to the terminal as confirmation - only we can see this

    # Format and print the DataFrame using the html template provided in the templates subdirectory
    return render_template('template.html',  tables=[book_data.to_html(classes='data')], titles=book_data.columns.values)

@app.route("/learn")
def learn():
    # Return a string the describes one thing you learned in ENSF 592.
    lesson = "This course went by so fast but I learned a ton! Almost everything was new for me :D"
    return lesson

