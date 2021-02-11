from flask import Flask, render_template, request
from .data import session_items as sessionitems
from todo_app.flask_config import Config
import requests
import json
import os

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    allCards = requests.get('https://api.trello.com/1/boards/602410634db0296b392dc99c/cards/open?key={key}&token={token}'.format(os.environ["TRELLO_KEY"], os.environ["TRELLO_TOKEN"] )).json()
    items = {}
    for item in allcards.items():
        
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

    allCards = requests.get('https://api.trello.com/1/boards/602410634db0296b392dc99c/cards/open?key={key}&token={token}'.format(os.environ["TRELLO_KEY"], os.environ["TRELLO_TOKEN"] ))
    items = allCards.text
    return render_template('index.html', items=items)

@app.route('/complete_item', methods=['POST'])
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

    allCards = requests.get('https://api.trello.com/1/boards/602410634db0296b392dc99c/cards/open?key={key}&token={token}'.format(os.environ["TRELLO_KEY"], os.environ["TRELLO_TOKEN"] ))
    items = allCards.text
    return render_template('index.html', items=items)
    
if __name__ == '__main__':
    app.run()

#update a  card with the status change

url = "https://api.trello.com/1/cards/{id}"

headers = {
   "Accept": "application/json"
}

query = {
   'key': os.environ["TRELLO_KEY"],
   'token': os.environ["TRELLO_TOKEN"], 
   'idList': '602410634db0296b392dc99f'
}

response = requests.request(
   "PUT",
   url,
   headers=headers,
   params=query
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

# class for the item

class todoitem:
  def __init__(self, id, status, title):
    self.id = id
    self.status = status
    self.title = title