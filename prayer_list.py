from flask import Flask, render_template

app = Flask(__name__)

# Function to read prayer requests from a file or database
def get_prayer_requests():
    # Replace this with your actual data retrieval logic
    prayer_requests = ["Prayer request 1", "Prayer request 2"]
    return prayer_requests

@app.route('/')
def index():
    prayer_requests = get_prayer_requests()
    return render_template('index.html', prayer_requests=prayer_requests)

if __name__ == '__main__':
    app.run(debug=True)