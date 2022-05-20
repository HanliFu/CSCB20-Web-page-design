
from flask import Flask, render_template
#import re
app = Flask(__name__)


@app.route('/<string:name>', methods=['GET'])
def generateResponse(name):
    newName = covertString(name)
    return f'<html><body >Welcome, {newName}, to my CSCB20 website!</body></html>!'


#dave

def covertString(name):
    res = ''

    containsDigits = False
    for char in name:
        if char.isdigit():
            containsDigits=True

    if(containsDigits):
        for char in name:
            if char.isalpha():
                res += char
    else:
        for char in name:
            if char.isalpha():
                if char.islower():
                    res += char.upper()
                elif char.isupper():
                    res += char.lower()
    return res




if __name__ == '__main__':
    # app.config['TEMPLATES_AUTO_RELOAD']=True
    app.run(debug=True, use_reloader=True)

