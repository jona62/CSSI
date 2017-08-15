import json
import urllib
import os

import jinja2
import webapp2

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        response = urllib.urlopen("https://uinames.com/api/")
        content = response.read()
        content_dict = json.loads(content)
        
        first_name = content_dict['name']
        surname = content_dict['surname']
        gender = content_dict['gender']
        country = content_dict['region']
        main=jinja_environment.get_template("templates/main.html"))
        self.response.out.write(results_template.render(content_dict)

app = webapp2.WSGIApplication(
[
    ('/', MainHandler),
        ],
     debug=True)
