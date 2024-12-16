# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World! Jatin, Its working.'

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server. 
    app.run(debug=True, port=3001)


# git remote add origin https://github.com/jatin-suthar-here/Test-flask-to-render.git
# git remote add origin https://github.com/jatin-suthar-here/Test-flask-to-render.git
