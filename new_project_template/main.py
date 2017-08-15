#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import logging
import os

import jinja2
import webapp2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
    def post(self):
        my_day = self.request.get('day')
        picture = self.request.get('picture')
        good_day = my_day == 'good'
        images = {
            'favicon' : '/favicon.ico',
            'matt_bomer' : '/matt_bomer.jpg',
            'guy' : 'https://blackgeoscientists.files.wordpress.com/2014/06/helloworld.jpg'
        }
        messages = {
            'good' :  'Yeah it\'s a good day',
            'bad' : ' Hope you feel better',
            'meh' : ' Let\'s go to lunch'
        }
        default = "Try again"

        temp_vars = {
            'image_source': images.get(picture, '/not_cat'),
            'message': messages.get(my_day, default),
            'bad_message': 'feel better',
            'good_day': good_day,
            }
        template=jinja_environment.get_template(
            'template = Template/template.html')
        self.response.write(template.render(temp_vars))

class AnotherHandler(webapp2.RequestHandler):
      def get(self):
        template = jinja_environment.get_template(
            'html_templates/question.html')
        message = "Hello another world!"
        logging.info(message)
        self.response.write(template.render())


app = webapp2.WSGIApplication(
[
    ('/', MainHandler),
    ('/question', AnotherHandler),
    ],
     debug=False)
