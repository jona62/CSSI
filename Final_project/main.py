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
    section = ndb.StringProperty()

class FormHandler(webapp2.RequestHandler):
    def get(self):
        comments = comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.1.html')
        self.response.write(template.render(template_values))

    def post(self):
        form_title = self.request.get('title')
        form_content = self.request.get('text_field')
        filters = ['bitch', 'clit', 'cock', 'cum', 'cunt', 'dick', 'fag', 'faggot', 'fuck', 'hoe', 'jizz', 'negro', 'nigga', 'nigger', 'penis', 'pussy', 'quee', 'shit', 'whore']
        for word in filters:
            form_content = form_content.replace(word, '*' * len(word))
        form_section = self.request.get('section')

        #new_comment = Comment( parent = ndb.Key(Comment, 'dummy'), title = form_title, text_field = form_content, section = form_section)
        new_comment = Comment(title = form_title, text_field = form_content, section = form_section)
        new_comment.put()

        # comments = Comment.query(ancestor = ndb.Key(Comment, 'dummy')).order(-Comment.created_at).fetch()
        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.1.html')
        self.response.write(template.render(template_values))

class FormHandler2(webapp2.RequestHandler):
    def get(self):
        comments = comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.2.html')
        self.response.write(template.render(template_values))

    def post(self):
        form_title = self.request.get('title')
        form_content = self.request.get('text_field')
        filters = ['bitch', 'clit', 'cock', 'cum', 'cunt', 'dick', 'fag', 'faggot', 'fuck', 'hoe', 'jizz', 'negro', 'nigga', 'nigger', 'penis', 'pussy', 'quee', 'shit', 'whore']
        for word in filters:
            form_content = form_content.replace(word, '*' * len(word))
        form_section = self.request.get('section')

        new_comment = Comment(title = form_title, text_field = form_content, section= form_section)
        new_comment.put()

        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.2.html')
        self.response.write(template.render(template_values))

class FormHandler3(webapp2.RequestHandler):
    def get(self):
        comments = comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.3.html')
        self.response.write(template.render(template_values))

    def post(self):
        form_title = self.request.get('title')
        form_content = self.request.get('text_field')
        filters = ['bitch', 'clit', 'cock', 'cum', 'cunt', 'dick', 'fag', 'faggot', 'fuck', 'hoe', 'jizz', 'negro', 'nigga', 'nigger', 'penis', 'pussy', 'quee', 'shit', 'whore']
        for word in filters:
            form_content = form_content.replace(word, '*' * len(word))
        form_section = self.request.get('section')

        new_comment = Comment(title = form_title, text_field = form_content, section= form_section)
        new_comment.put()

        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.3.html')
        self.response.write(template.render(template_values))

class FormHandler4(webapp2.RequestHandler):
    def get(self):
        comments = comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.4.html')
        self.response.write(template.render(template_values))

    def post(self):
        form_title = self.request.get('title')
        form_content = self.request.get('text_field')
        filters = ['bitch', 'clit', 'cock', 'cum', 'cunt', 'dick', 'fag', 'faggot', 'fuck', 'hoe', 'jizz', 'negro', 'nigga', 'nigger', 'penis', 'pussy', 'quee', 'shit', 'whore']
        for word in filters:
            form_content = form_content.replace(word, '*' * len(word))
        form_section = self.request.get('section')

        new_comment = Comment(title = form_title, text_field = form_content, section= form_section)
        new_comment.put()

        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.4.html')
        self.response.write(template.render(template_values))

class FormHandler5(webapp2.RequestHandler):
    def get(self):
        comments = comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.5.html')
        self.response.write(template.render(template_values))

    def post(self):
        form_title = self.request.get('title')
        form_content = self.request.get('text_field')
        filters = ['bitch', 'clit', 'cock', 'cum', 'cunt', 'dick', 'fag', 'faggot', 'fuck', 'hoe', 'jizz', 'negro', 'nigga', 'nigger', 'penis', 'pussy', 'quee', 'shit', 'whore']
        for word in filters:
            form_content = form_content.replace(word, '*' * len(word))
        form_section = self.request.get('section')

        new_comment = Comment(title = form_title, text_field = form_content, section= form_section)
        new_comment.put()

        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.5.html')
        self.response.write(template.render(template_values))

class FormHandler6(webapp2.RequestHandler):
    def get(self):
        comments = comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.6.html')
        self.response.write(template.render(template_values))

    def post(self):
        form_title = self.request.get('title')
        form_content = self.request.get('text_field')
        filters = ['bitch', 'clit', 'cock', 'cum', 'cunt', 'dick', 'fag', 'faggot', 'fuck', 'hoe', 'jizz', 'negro', 'nigga', 'nigger', 'penis', 'pussy', 'quee', 'shit', 'whore']
        for word in filters:
            form_content = form_content.replace(word, '*' * len(word))
        form_section = self.request.get('section')

        new_comment = Comment(title = form_title, text_field = form_content, section= form_section)
        new_comment.put()

        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.6.html')
        self.response.write(template.render(template_values))

class FormHandler7(webapp2.RequestHandler):
    def get(self):
        comments = comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.7.html')
        self.response.write(template.render(template_values))

    def post(self):
        form_title = self.request.get('title')
        form_content = self.request.get('text_field')
        filters = ['bitch', 'clit', 'cock', 'cum', 'cunt', 'dick', 'fag', 'faggot', 'fuck', 'hoe', 'jizz', 'negro', 'nigga', 'nigger', 'penis', 'pussy', 'quee', 'shit', 'whore']
        for word in filters:
            form_content = form_content.replace(word, '*' * len(word))
        form_section = self.request.get('section')

        new_comment = Comment(title = form_title, text_field = form_content, section= form_section)
        new_comment.put()

        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.7.html')
        self.response.write(template.render(template_values))

class FormHandler8(webapp2.RequestHandler):
    def get(self):
        comments = comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.8.html')
        self.response.write(template.render(template_values))

    def post(self):
        form_title = self.request.get('title')
        form_content = self.request.get('text_field')
        filters = ['bitch', 'clit', 'cock', 'cum', 'cunt', 'dick', 'fag', 'faggot', 'fuck', 'hoe', 'jizz', 'negro', 'nigga', 'nigger', 'penis', 'pussy', 'quee', 'shit', 'whore']
        for word in filters:
            form_content = form_content.replace(word, '*' * len(word))
        form_section = self.request.get('section')

        new_comment = Comment(title = form_title, text_field = form_content, section= form_section)
        new_comment.put()

        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.8.html')
        self.response.write(template.render(template_values))

class FormHandler9(webapp2.RequestHandler):
    def get(self):
        comments = comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.9.html')
        self.response.write(template.render(template_values))

    def post(self):
        form_title = self.request.get('title')
        form_content = self.request.get('text_field')
        filters = ['bitch', 'clit', 'cock', 'cum', 'cunt', 'dick', 'fag', 'faggot', 'fuck', 'hoe', 'jizz', 'negro', 'nigga', 'nigger', 'penis', 'pussy', 'quee', 'shit', 'whore']
        for word in filters:
            form_content = form_content.replace(word, '*' * len(word))
        form_section = self.request.get('section')

        new_comment = Comment(title = form_title, text_field = form_content, section= form_section)
        new_comment.put()

        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.9.html')
        self.response.write(template.render(template_values))

class FormHandler10(webapp2.RequestHandler):
    def get(self):
        comments = comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.10.html')
        self.response.write(template.render(template_values))

    def post(self):
        form_title = self.request.get('title')
        form_content = self.request.get('text_field')
        filters = ['bitch', 'clit', 'cock', 'cum', 'cunt', 'dick', 'fag', 'faggot', 'fuck', 'hoe', 'jizz', 'negro', 'nigga', 'nigger', 'penis', 'pussy', 'quee', 'shit', 'whore']
        for word in filters:
            form_content = form_content.replace(word, '*' * len(word))
        form_section = self.request.get('section')

        new_comment = Comment(title = form_title, text_field = form_content, section= form_section)
        new_comment.put()

        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.10.html')
        self.response.write(template.render(template_values))

class FormHandler11(webapp2.RequestHandler):
    def get(self):
        comments = comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.11.html')
        self.response.write(template.render(template_values))

    def post(self):
        form_title = self.request.get('title')
        form_content = self.request.get('text_field')
        filters = ['bitch', 'clit', 'cock', 'cum', 'cunt', 'dick', 'fag', 'faggot', 'fuck', 'hoe', 'jizz', 'negro', 'nigga', 'nigger', 'penis', 'pussy', 'quee', 'shit', 'whore']
        for word in filters:
            form_content = form_content.replace(word, '*' * len(word))
        form_section = self.request.get('section')

        new_comment = Comment(title = form_title, text_field = form_content, section= form_section)
        new_comment.put()

        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.11.html')
        self.response.write(template.render(template_values))

class FormHandler12(webapp2.RequestHandler):
    def get(self):
        comments = comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.12.html')
        self.response.write(template.render(template_values))

    def post(self):
        form_title = self.request.get('title')
        form_content = self.request.get('text_field')
        filters = ['bitch', 'clit', 'cock', 'cum', 'cunt', 'dick', 'fag', 'faggot', 'fuck', 'hoe', 'jizz', 'negro', 'nigga', 'nigger', 'penis', 'pussy', 'quee', 'shit', 'whore']
        for word in filters:
            form_content = form_content.replace(word, '*' * len(word))
        form_section = self.request.get('section')

        new_comment = Comment(title = form_title, text_field = form_content, section= form_section)
        new_comment.put()

        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.12.html')
        self.response.write(template.render(template_values))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main= ENV.get_template("/templates/final_project.html")
        self.response.write(main.render())

class topicHandler(webapp2.RequestHandler):
    def get(self):
        topic= ENV.get_template("/templates/topic.html")
        self.response.write(topic.render())

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        about= ENV.get_template("templates/about.html")
        self.response.write(about.render())

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        contact= ENV.get_template("templates/contact.html")
        self.response.write(contact.render())

class no1Handler(webapp2.RequestHandler):
    def get(self):
        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.1.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.write("NO SOUP FOR YOU")

class no2Handler(webapp2.RequestHandler):
    def get(self):
        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.2.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.write("NO SOUP FOR YOU")

class no3Handler(webapp2.RequestHandler):
    def get(self):
        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.3.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.write("NO SOUP FOR YOU")

class no4Handler(webapp2.RequestHandler):
    def get(self):
        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.4.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.write("NO SOUP FOR YOU")

class no5Handler(webapp2.RequestHandler):
    def get(self):
        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.5.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.write("NO SOUP FOR YOU")

class no6Handler(webapp2.RequestHandler):
    def get(self):
        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.6.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.write("NO SOUP FOR YOU")

class no7Handler(webapp2.RequestHandler):
    def get(self):
        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.7.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.write("NO SOUP FOR YOU")

class no8Handler(webapp2.RequestHandler):
    def get(self):
        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.8.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.write("NO SOUP FOR YOU")

class no9Handler(webapp2.RequestHandler):
    def get(self):
        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.9.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.write("NO SOUP FOR YOU")

class no10Handler(webapp2.RequestHandler):
    def get(self):
        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.10.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.write("NO SOUP FOR YOU")

class no11Handler(webapp2.RequestHandler):
    def get(self):
        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.11.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.write("NO SOUP FOR YOU")

class no12Handler(webapp2.RequestHandler):
    def get(self):
        comments = Comment.query().order(-Comment.created_at).fetch()
        template_values = {'name' : 'Anonymous', 'comments' : comments}
        template = ENV.get_template('/templates/no.12.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.write("NO SOUP FOR YOU")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/topic', topicHandler),
    ('/about', AboutHandler),
    ('/contact', ContactHandler),
    ('/no1', no1Handler),
    ('/processform', FormHandler),
    ('/no2', no2Handler),
    ('/processform2', FormHandler2),
    ('/no3', no3Handler),
    ('/processform3', FormHandler3),
    ('/no4', no4Handler),
    ('/processform4', FormHandler4),
    ('/no5', no5Handler),
    ('/processform5', FormHandler5),
    ('/no6', no6Handler),
    ('/processform6', FormHandler6),
    ('/no7', no7Handler),
    ('/processform7', FormHandler7),
    ('/no8', no8Handler),
    ('/processform8', FormHandler8),
    ('/no9', no9Handler),
    ('/processform9', FormHandler9),
    ('/no10', no10Handler),
    ('/processform10', FormHandler10),
    ('/no11', no11Handler),
    ('/processform11', FormHandler11),
    ('/no12', no12Handler),
    ('/processform12', FormHandler12),
], debug=False)
