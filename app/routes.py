# This file contains the route definitions for your Flask application.

from flask import jsonify, request
from app import app, db
from app.models import TodoItem
from app.schemas import TodoItemSchema

todo_item_schema = TodoItemSchema()
todo_items_schema = TodoItemSchema(many=True)

# Create a new todo item
@app.route('/todo', methods=['POST'])
def create_todo_item():
    data = request.json
    new_todo_item = TodoItem(title=data['title'], description=data.get('description'), due_date=data.get('due_date'))
    db.session.add(new_todo_item)
    db.session.commit()
    return todo_item_schema.jsonify(new_todo_item), 201

# Get all todo items
@app.route('/todo', methods=['GET'])
def get_all_todo_items():
    all_todo_items = TodoItem.query.all()
    result = todo_items_schema.dump(all_todo_items)
    return jsonify(result)

# Get a single todo item
@app.route('/todo/<int:id>', methods=['GET'])
def get_todo_item(id):
    todo_item = TodoItem.query.get_or_404(id)
    return todo_item_schema.jsonify(todo_item)

# Update a todo item
@app.route('/todo/<int:id>', methods=['PUT'])
def update_todo_item(id):
    todo_item = TodoItem.query.get_or_404(id)
    data = request.json
    todo_item.title = data.get('title', todo_item.title)
    todo_item.description = data.get('description', todo_item.description)
    todo_item.due_date = data.get('due_date', todo_item.due_date)
    todo_item.completed = data.get('completed', todo_item.completed)
    db.session.commit()
    return todo_item_schema.jsonify(todo_item)

# Delete a todo item
@app.route('/todo/<int:id>', methods=['DELETE'])
def delete_todo_item(id):
    todo_item = TodoItem.query.get_or_404(id)
    db.session.delete(todo_item)
    db.session.commit()
    return '', 204

# Implement login and logout routes
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Protect routes that require authentication using @login_required decorator:
@app.route('/protected')
@login_required
def protected():
    return 'This is a protected route!'
