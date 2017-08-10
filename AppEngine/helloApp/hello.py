import webapp2
import jinja2

ENV = jinja2.Environment( loader= jinja2.FileSystemLoader("Templates") )

html_page="""
<html>
<head>
    <title> Hello </title>
    <style>
    p {
    color:blue;
    }
    </style>
</head>
<body>
    <p> Hello World! </p>
<form action="/" method= "post">
    Name: <input type="text" name="field"/>
    <input type="submit" value="Submit"/>
</form>
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type']= 'text/html'
        self.response.write(html_page)

    def post(self):
        self.response.headers['Content-Type']= 'text/plain'
        #self.response.write(self.request.POST)
        if "field" not in self.request.POST:
            self.response.write('field not found')
        else:
            field = self.request.POST ['field']
            self.response.write("Hello " + field + "!")

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("All About Me")

class CountHandler(webapp2.RequestHandler):
    def get(self):
        for i in range(2, 51, 2):
            self.response.write(str(i) + "   ")

class GreetingsHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write("Hello People")
        template_values = {"name":"Bluc"}

        template = ENV.get_template('index.html')
        self.response.write(template.render(template_values))


routes = [
    ('/', MainHandler),
    ('/about', AboutHandler),
    ('/count', CountHandler),
    ('/greetings',GreetingsHandler)
]

app = webapp2.WSGIApplication(routes, debug = True)
