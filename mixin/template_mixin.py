import jinja2
import re
import os
from os.path import dirname, abspath

class TemplateMixin():

    def load_template(self, file_name):
        
        template_dir = dirname(dirname(abspath(__file__))).rstrip('/') + '/templates'
        print(template_dir)
        templateLoader = jinja2.FileSystemLoader(searchpath=template_dir)
        templateEnv = jinja2.Environment(loader=templateLoader)
        TEMPLATE_FILE = file_name
        
        return templateEnv.get_template(TEMPLATE_FILE)

    def render_object(self, template, **kwargs):
        template_str = template.render(**kwargs)

        return template_str
