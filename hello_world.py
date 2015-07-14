from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
@app.route("/hi")
def say_hi():
	return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
	html = """
		<h1>
			Hello {}!
		</h1>
		<p>
			Here's a picture of a kitten. Awww....
		</p>
		<img src="http://placekitten.com/g/200/300">
	"""
	return html.format(name.title())

@app.route("/hello/<first>/<last>")
def jedi(first, last):
	html = """
		<h1>
			Hello my young padawan {}!
		</h1>
		<h2>
			Your first name is {} and your last name is {} but you shall forever be known as {}
		</h2>
		<p> May the Force be with you! </p>
		<img src="http://nerdreactor.com/wp-content/uploads/2014/05/19c0uzmi9bmv1jpg.jpg">
	"""
	jedi = first[0] + first[1] + first[2] + last[0] + last[1]
	return html.format(jedi, first, last, jedi)

if __name__ == "__main__":
	app.run()