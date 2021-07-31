## 📚 Learning Outcomes
* Create a simple Flask application with multiple routes
* Scrape and parse data from a single web page
* Store and manipulate data within a DataFrame
* Print a DataFrame object to a webpage

## 💻 Program Specifications
Follow along with the Lab 12 demonstration. The demo program is a collaborative effort between Garth Johnson and Emily Marasco, and is used with permission.
Before submitting your files, you must complete the following tasks:
* Change "STUDENT NAME" to your own name in the code.
* Follow the "/hello/<name>" route by entering your own name. Take a screenshot of the display. 
* Modify the book table to display a new column with the sale price (reduced by 25%). Submit a screenshot of the modified table being displayed.
* Create a new route "/learn" that displays one thing that you learned in ENSF 592. Submit a screenshot of your answer being displayed.
* Your submitted code must match your provided screenshots.

To run your web application:
MAC/Linux
* Make sure you are working in the correct directory
* `export FLASK_ENV=development`
* `export FLASK_APP=web_data_app.py`
* `flask run`

Windows
* Make sure you are working in the correct directory
* `set FLASK_ENV=development`
* `set FLASK_APP=web_data_app.py`
* `flask run`

Exporting the `FLASK_ENV` as `development` enables some nice features that you can explore later on (see Visual Studio's [Run the App Debugger](https://code.visualstudio.com/docs/python/tutorial-flask#_run-the-app-in-the-debugger) page for more info on how to setup/use it from within VS), and disables some anoying reminders to NOT use this in 'production' without a proper WSGI (or similar interface).

Once the application is running, browse the local system on port `5000` (typically http://localhost:5000/).  When you do, you should see the friendly message "Hello World!" in your browser and the following in the terminal where the application is running:
    ❯ flask run
    * Serving Flask app "web_data_app.py" (lazy loading)
    * Environment: development
    * Debug mode: on
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 290-425-530
    127.0.0.1 - - [25/Apr/2021 12:04:00] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [25/Apr/2021 12:04:01] "GET /favicon.ico HTTP/1.1" 404 -

If you followed the ENSF 592 installation guidelines, you should have all the necessary modules ready to go.
If you encounter issues, run the requirements file using `pip install -r requirements.txt` to ensure you have the correct versions necessary.
Make sure you are in your assignment working directory and your ENSF 592 virtual environment.

## 📚 Developer Comments
First off, much of this is inspired by [RealPython](https://realpython.com/flask-by-example-part-1-project-setup/) and various other sites, pages, and people encountered through the teaching and learning process.
This is a basic 'quick n simple' Python-Flask application tutorial written for general usage of Python/Flask. This will help a new (but probably not noob) Pythonista learn how to set up a basic web server application in Python with Flask running on a local server, and assumes that the the developer is using Visual Studio Code as their IDE of choice.
Flask is a Model-View-Controller (MVC) framework (see [this page](https://www.guru99.com/mvc-vs-mvvm.html) for some insight to what MVC is and isn't, and also Real Python's [MVC Explained](https://realpython.com/the-model-view-controller-mvc-paradigm-summarized-with-legos/) page for more details.
If you'd like to try scraping more websites, take a look at http://toscrape.com/
If you'd like to expand on the book catalog example (without Flask), take a look at this link: https://towardsdatascience.com/a-really-gentle-introduction-to-web-scraping-in-python-83cb9e536db8
