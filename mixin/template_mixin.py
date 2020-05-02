import jinja2
import re
import os

class TemplateMixin():

    def load_template(self, file_name):

        templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
        templateEnv = jinja2.Environment(loader=templateLoader)
        TEMPLATE_FILE = file_name
        
        return templateEnv.get_template(TEMPLATE_FILE)

    def render_object(self, template, **kwargs):
        template_str = template.render(**kwargs)

        return template_str