from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<color>')
@app.route('/<color>/<int:x>')
@app.route('/<color>/<int:x>/<int:y>')
def checkerboard(color = "red", x=8, y=8):
    return render_template("index.html", color=color, x=x, y=y)

if __name__ == "__main__":
    app.run(debug=True)