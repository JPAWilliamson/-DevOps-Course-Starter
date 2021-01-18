from flask import Flask, render_template, request
from .data import session_items as sessionitems
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    items = sessionitems.get_items()
    return render_template('index.html', items=items)

@app.route('/add_item', methods=['POST'])
def add():
    todoTitle = request.form.get('title')
    sessionitems.add_item(todoTitle)
    items = sessionitems.get_items()
    return render_template('index.html', items=items)
    
if __name__ == '__main__':
    app.run()
