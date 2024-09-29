from flask_blog import create_app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


#@app.route("/about/<username>")
#def about_page(username):
 #   return f"<h1>This is the about page of {username}</h1>"