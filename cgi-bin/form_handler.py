import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
try:
    email = form.getvalue("email", "error")
    password = form.getvalue("password", "error")
    season = form.getvalue("season", "error")
    fruit = form.getlist("fruit")
except (NameError, KeyError) as e:
    message = e


print("Content-Type: text/html")
print()
html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Result</title>
</head>
<body>
    <p>Data from form:</p>
    <ul>
        <li><strong>Email:</strong> {email}</li>
        <li><strong>Password:</strong> {password}</li>
        <li><strong>Season:</strong> {season}</li>
        <li><strong>Fruits:</strong> {fruit}</li>
    </ul>
</body>
</html>
"""
print(html.format(email=email, password=password, season=season, fruit=', '.join(fruit)))