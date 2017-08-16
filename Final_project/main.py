import webapp2
import jinja2
import os
from google.appengine.ext import ndb
import logging

ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Comment(ndb.Model):
    title = ndb.StringProperty()
    text_field = ndb.TextProperty()
    created_at = ndb.DateTimeProperty( auto_now_add=True )

class FormHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Refresh'] = '0;url="/"'
        comments = comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.1.html')
        self.response.write(template.render(template_values))

    def post(self):
        form_title = self.request.get('title')
        form_content = self.request.get('text_field')

        new_comment = Comment( parent = ndb.Key(Comment, 'dummy'), title = form_title, text_field = form_content)
        new_comment.put()

        comments = Comment.query(ancestor = ndb.Key(Comment, 'dummy')).order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.1.html')
        self.response.write(template.render(template_values))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main= ENV.get_template("/templates/final_project.html")
        self.response.write(main.render())

class topicHandler(webapp2.RequestHandler):
    def get(self):
        topic= ENV.get_template("/templates/topic.html")
        self.response.write(topic.render())

class no1Handler(webapp2.RequestHandler):
    def get(self):
        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.1.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.write("NO SOUP FOR YOU")
        # comments = Comment.query().order(-Comment.created_at).fetch()
        # name = self.request.get("name")
        # text_field = self.request.get("text_field")
        # template = ENV.get_template("/templates/no.1.html")
        # template_values = {'name': name, 'text_field' : text_field}
        # self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/topic', topicHandler),
    ('/no1', no1Handler),
    ('/processform', FormHandler),
], debug=True)
