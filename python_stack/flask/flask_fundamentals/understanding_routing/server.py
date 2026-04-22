from flask import Flask
app = Flask(__name__)

# 1. Root route
@app.route('/')
def hello_world():
    return "Hello World!"

# 2. Champion route
@app.route('/champion')
def champion():
    return "Champion!"

# 3. Say route with name variable
@app.route('/say/<name>')
def say_name(name):
    return f"Hi {name}!"

# 4. Repeat route with Ninja Bonus (using int converter)
@app.route('/repeat/<int:num>/<word>')
def repeat_word(num, word):
    return (word + " ") * num

# Sensei Bonus: Handle undefined routes
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)