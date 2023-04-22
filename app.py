from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hiddenProject')
def hiddenProject():
    return render_template('hiddenProject.html')

if __name__ == '__main__':
    app.run()

@app.route("/about")
def about():
	return "HELLO about"
