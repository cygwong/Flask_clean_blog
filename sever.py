from flask import Flask, render_template, request
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/52d4bbc652a10f84d851"
blog_json = requests.get(blog_url).json()

@app.route("/")
def home_page():
    return render_template('index.html', blogs_json = blog_json)

@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route("/contact", methods=['POST','GET']
def contact_page():
    if request.method == 'POST':
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['phone'])
        print(request.form['message'])
        return render_template('contact.html', mess_sent = True)
    return render_template('contact.html', mess_sent = False)


@app.route("/post/<int:index>")
def post_page(index):
    requested_post = None
    for blog in blog_json:
        if blog['id'] == index:
            requested_post = blog
    return render_template('post.html', blog_content = requested_post)


if __name__ == '__main__':
    app.run(debug=True)