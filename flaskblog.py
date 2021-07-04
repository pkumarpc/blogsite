from flask import Flask, render_template, url_for
app = Flask(__name__)

blogs = [
	{
		'author' : 'Prem Kumar', 
		'title' : 'Blog Post 1',
		'content' : 'First post content',
		'date_posted' : 'July 2nd, 2021'
	},
	{
		'author' : 'Sadhika Bagga', 
		'title' : 'Blog Post 2',
		'content' : 'Second post content',
		'date_posted' : 'July 2nd, 2021'
	
	}
]


@app.route("/")
@app.route("/home")
def hello():
	return render_template('home.html', posts=blogs)

@app.route("/about")
def about(title="about"):
	return render_template('about.html', title="About")

if __name__ == "__main__":
	app.run(debug=True)

