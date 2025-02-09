

#Creating a simple basic app

# Import the module
from flask import Flask

# Define the app application

app =      Flask(__name__)  #Creating the app instance

# Define the route
@app.route('/')
def home():
    return '<h1  style="color:Blue;">MUSIIMENTA AGNES</h1>'

