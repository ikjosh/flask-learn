from flask import Flask, render_template


# This is needed so that Flask knows where to look 
# for resources such as templates and static files.
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/second')
def second():
    return 'This is second page'

@app.route('/third')
def third():
    return 'This is third page'

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id of this page is {id}'

@app.route('/fifth/<int:id>')
def fifth(id):
    return f'Id of this page is {id}'

# The code you provided is a common pattern in Python 
# for running a Flask web application.
if __name__ == '__main__':
# This line checks whether the script is being run directly by 
# the Python interpreter (i.e., not imported as a module in another script). 
# This is a common pattern in Python scripts to ensure that certain code 
# is only executed when the script is run directly.

    # app.run(debug=True)
    # app.run(debug=True, port=3003)

    # This line actually runs the Flask application. It tells Flask 
    # to run the application on all available network interfaces ('0.0.0.0') 
    # and to use port 80, which is the default port for HTTP traffic. 
    # By default, Flask runs on localhost (127.0.0.1) and a randomly chosen port, 
    # but specifying host='0.0.0.0' makes it accessible from other devices on the network.
    app.run(host='0.0.0.0', port=80)
