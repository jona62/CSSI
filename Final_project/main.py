import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        no_one= JINJA_ENVIRONMENT.get_template("templates/no.1.html")
        self.response.write(no_one.render())
    def post(self):
        name = self.request.get("name")
        text_field = self.request.get("text_field")
        output = JINJA_ENVIRONMENT.get_template("templates/no.2.html")
        collective = {'name': name, 'text_field' : text_field}
        self.response.write(output.render(collective))

app = webapp2.WSGIApplication([
    ('/', MainHandler),

], debug=True)
