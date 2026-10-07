from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
<title>Registration Form</title>
</head>
<body>
<h2>Student Registration Form</h2>

<form method="POST">
<label>Name:</label>
<input type="text" name="name" required><br><br>

<label>Email:</label>
<input type="email" name="email" required><br><br>

<label>Phone:</label>
<input type="text" name="phone" required><br><br>

<label>Course:</label>
<select name="course">
<option>B.Tech</option>
<option>BCA</option>
<option>MCA</option>
</select><br><br>

<button type="submit">Register</button>
</form>

{% if message %}
<h3>{{ message }}</h3>
{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def register():
    message = ""

    if request.method == "POST":
        name = request.form["name"]
        message = f"Registration successful! Welcome, {name}."

    return render_template_string(html, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)