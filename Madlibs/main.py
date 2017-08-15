import jinja2
import webapp2
import os

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('main.html')
        self.response.out.write(main_template.render())
    def post(self):
        results_template = env.get_template('result.html')
        template_variables = {
            first_name = content_dict['name']
            country = content_dict['region']
    print "My name is " + first_name + " and my country is " + country
        }
        self.response.out.write(results_template.render(template_variables))
app = webapp2.WSGIApplication(
[
    ('/', MainHandler),
        ],
     debug=True)
