from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# In-memory data structure to store user details (replace this with a database later)
users = {}

# Routes
@app.route('/')
def home():
    return redirect(url_for('index'))  # Redirect to the index page when the website is accessed

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phone_number = request.form['phone_number']
        password = request.form['password']

        if phone_number in users and users[phone_number] == password:
            # Successful login
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            # Failed login
            flash('Invalid phone number or password. Please try again.', 'error')

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        phone_number = request.form['phone_number']
        password = request.form['password']

        if phone_number in users:
            # Phone number already exists
            flash('Phone number is already registered. Please use a different phone number.', 'error')
        else:
            # Create a new user
            users[phone_number] = password
            flash('Registration successful! You can now login.', 'success')
            return redirect(url_for('login'))

    return render_template('signup.html')

# Sample EV charging stations data (you can replace this with a real data source)
charging_stations = [
    {"name": "Charging Station 1", "location": "Location 1"},
    {"name": "Charging Station 2", "location": "Location 2"},
    # Add more charging station data as needed
]

@app.route('/index')
def index():
    return render_template('index.html', charging_stations=charging_stations)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit', methods=['POST'])
def submit():
    answer = request.form['answer']
    # Process the answer or do whatever you want with it
    return f"Your answer: {answer}"

if __name__ == '__main__':
    app.run(debug=True)
