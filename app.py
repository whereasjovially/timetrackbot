'''
Created on 16 Sep 2019

@author: jwendling
'''

from bot.application import Application as BotApp
from flask import Flask, request

app = Flask(__name__)
app.debug = True
bot_app = BotApp()

# Custom Errorpage for 404 Page not found!
@app.errorhandler(404)
def webhook_error(e):
    return ("""
    <html>
    <head><title>404 - Bad Request</title></head>
    <body>Oops...We did not found the requested page!</body>
    </html>
    """)

# Default Actionplan
@app.route('/messages', methods=['GET', 'POST'])
def webhook_messages():
    if request.method == 'POST':
        return bot_app.process_webhook(request.json)
    return("Running WebEx Bot!")

@app.route("/")
def default_page():
        return "<h1>Nothing to see here!!!</h1>"