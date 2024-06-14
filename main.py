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
    {% if name and age is not none %}
        <h2>Hello, {{ name }}! You are {{ age }} years old.</h2>
    {% endif %}
</body>
</html>
'''


@app.route('/', methods=['GET', 'POST'])
def home():
    name = None
    age = None
    if request.method == 'POST':
        name = request.form['name']
        birthdate = request.form['birthdate']
        try:
            # Introduce a deliberate bug by using an incorrect date format
            birthdate = datetime.strptime(birthdate, '%d-%m-%Y')  # Incorrect format
            today = datetime.today()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        except ValueError:
            age = "Invalid date format. Please enter the date in YYYY-MM-DD format."
    return render_template_string(html_template, name=name, age=age)


if __name__ == '__main__':
    app.run(debug=True)
