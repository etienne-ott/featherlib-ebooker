#!/usr/bin/python

import cgi
import Cookie


cookie = Cookie.SimpleCookie()
cookie['session_id'] = 'daosjdniwludbniwluadwad'
cookie['session_id']['expires'] = 24 * 60 * 60

#form = cgi.FieldStorage()
#message = form.getvalue("message", "(no message)")

print cookie
print """Content-type: text/html"""
print
print """
<!DOCTYPE html>
<html>
<head>
    <title>featherlib ebooker</title>
    <meta charset="utf-8"/>
    <link rel="icon" type="image/png" href="favicon.png"/>
    <link href="styles/default-style.css" rel="stylesheet" type="text/css"/>
</head>

<body>
    <h3> featherlib ebooker </h3>

    <p>Make epub with a simple form.</p>

</body>
</html>
"""