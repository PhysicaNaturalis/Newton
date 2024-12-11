from flask import Flask, render_template

app = Flask(__name__)

# Example Python function
def get_blog_content():
    return "This is the dynamic content fetched from the server."

# Route for the homepage
@app.route('/')
def home():
    content = get_blog_content()  # Calling the Python function
    return render_template('index.html', content=content)

if __name__ == '__main__':
    app.run(debug=True)
