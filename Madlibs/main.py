import jinja2
import webapp2

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('main.html')
        self.response.out.write(main_template.render())
    def post(self):
        results_template = env.get_template('result.html')
        template_variables = {
            'noun':self.request.get("noun"),
            'pnoun':self.request.get("pnoun"),
            'noun':self.request.get("noun"),
            'pronoun':self.request.get("pronoun"),
            'adjective':self.request.get("adjective"),
            'verb':self.request.get("verb"),
        }
        self.response.out.write(results_template.render(template_variables))
app = webapp2.WSGIApplication(
[
    ('/', MainHandler),
        ],
     debug=True)
