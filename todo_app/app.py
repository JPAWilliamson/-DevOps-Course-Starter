from flask import Flask, render_template, request
from todo_app.flask_config import Config
import json
import os
import requests

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    allCards = requests.get('https://api.trello.com/1/boards/602410634db0296b392dc99c/cards/open?key={}&token={}'.format(os.environ["TRELLO_KEY"], os.environ["TRELLO_TOKEN"] )).json()
    items = []
    for item in allCards:
        if item['idList'] == "602410634db0296b392dc99d":
            items.append(item['name'])
    return render_template('index.html', items=items)

@app.route('/add_item', methods=['POST'])
def add():
    todoTitle = request.form.get('title')
    url = "https://api.trello.com/1/cards"

    query = {
    'key': os.environ["TRELLO_KEY"],
    'token': os.environ["TRELLO_TOKEN"], 
    'idList': '602410634db0296b392dc99d',
    'name': todoTitle
    }

    response = requests.request(
    "POST",
    url,
    params=query
    )

    allCards = requests.get('https://api.trello.com/1/boards/602410634db0296b392dc99c/cards/open?key={}&token={}'.format(os.environ["TRELLO_KEY"], os.environ["TRELLO_TOKEN"] )).json()
    items = []
    for item in allCards:
        if item['idList'] == "602410634db0296b392dc99d":
            items.append(item['name'])
    return render_template('index.html', items=items)

@app.route('/complete_item', methods=['POSt'])
def complete():
    itemId= request.form.get('itemId')
    url = "https://api.trello.com/1/cards/{}".format(itemId)

    query = {
    'key': os.environ["TRELLO_KEY"],
    'token': os.environ["TRELLO_TOKEN"], 
    'idList': '602410634db0296b392dc99f',
    }

    response = requests.request(
    "PUT",
    url,
    params=query
    )

    allCards = requests.get('https://api.trello.com/1/boards/602410634db0296b392dc99c/cards/open?key={}&token={}'.format(os.environ["TRELLO_KEY"], os.environ["TRELLO_TOKEN"] )).json()
    items = []
    for item in allCards:
        if item['idList'] == "602410634db0296b392dc99d":
            items.append(item['name'])
    return render_template('index.html', items=items)
    
if __name__ == '__main__':
    app.run()

#update a  card with the status change
# class for the item

class todoitem:
  def __init__(self, id, status, title):
    self.id = id
    self.status = status
    self.title = title