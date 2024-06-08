from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

# HTML template for the web page
html_template = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Greeting App</title>
</head>
<body>
    <h1>Greeting App</h1>
    <form method="post" action="/">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="birthdate">Enter your birthdate (YYYY-MM-DD):</label>
        <input type="date" id="birthdate" name="birthdate" required><br><br>

        <button type="submit">Submit</button>
    </form>
    {% if name and day_of_week %}
        <h2>Hello, {{ name }}! You were born on a {{ day_of_week }}.</h2>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    name = None
    day_of_week = None
    if request.method == 'POST':
        name = request.form['name']
        birthdate = request.form['birthdate']
        try:
            # Correct date format but introduce a critical bug
            birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
            # Introduce a critical bug by dividing by zero, causing a ZeroDivisionError
            day_of_week = 1 / 0  # This will cause a ZeroDivisionError
        except ValueError:
            day_of_week = "Invalid date format. Please enter the date in YYYY-MM-DD format."
    return render_template_string(html_template, name=name, day_of_week=day_of_week)

if __name__ == '__main__':
    app.run(debug=True)
