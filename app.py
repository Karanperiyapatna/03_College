from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static_site')

# Route for the homepage
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Route for other static HTML pages
@app.route('/<path:path>')
def static_file(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    app.run(debug=True)
