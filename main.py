#import libraries
import pandas as pd
import numpy as np
import flask



#Connect to html file
app = flask.Flask(__name__, template_folder='.')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('front_page.html'))
    if flask.request.method == 'POST':
        #Retreive input from html
        hoursAlone = int(flask.request.form.get('hoursAlone'))
        stageFright = int(flask.request.form.get('stageFright'))
        events = int(flask.request.form.get('events'))
        outside = int(flask.request.form.get('outside'))
        exhausted = int(flask.request.form.get('exhausted'))
        friends = int(flask.request.form.get('friends'))
        posts = int(flask.request.form.get('posts'))

        print("hoursAlone:", hoursAlone)
        print("stageFright:", stageFright)
        print("events:", events)
        print("outside:", outside)
        print("exhausted:", exhausted)
        print("friends:", friends)
        print("posts:", posts)
        


if __name__ == '__main__':
    app.run(debug=True)