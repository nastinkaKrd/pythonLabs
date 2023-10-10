import cgi
import cgitb
import http.cookies
import os
import datetime

cgitb.enable()

form = cgi.FieldStorage()

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
counter = int(cookie.get("counter", 0))

try:
    if "email" in form:
        counter += 1
        cookie["counter"] = str(counter)
        cookie["counter"]["max-age"] = 3600
    if "password" in form:
        counter += 1
        cookie["counter"] = str(counter)
        cookie["counter"]["max-age"] = 3600
    if "season" in form:
        counter += 1
        cookie["counter"] = str(counter)
        cookie["counter"]["max-age"] = 3600
    if "fruit" in form:
        counter += 1
        cookie["counter"] = str(counter)
        cookie["counter"]["max-age"] = 3600
    email = form.getvalue("email", "error (data is not found)")
    password = form.getvalue("password", "error (data is not found)")
    season = form.getvalue("season", "error (data is not found)")
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
    <p>Filled forms: {counter}</p>
    <form method="post" action="">
        <input type="submit" name="clear_cookies" value="Delete all cookies">
    </form>
</body>
</html>
"""
if "clear_cookies" in form:
    cookie["counter"] = ""
    cookie["counter"]["expires"] = str(datetime.datetime.now())

print(cookie.output())  
print()
print(html.format(email=email, password=password, season=season, fruit=', '.join(fruit), counter=counter))