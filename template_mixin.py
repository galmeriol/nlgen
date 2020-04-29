import jinja2

class TemplateMixin():

    def __init__(self, file_name):

        templateLoader = jinja2.FileSystemLoader(searchpath="./")
        templateEnv = jinja2.Environment(loader=templateLoader)
        TEMPLATE_FILE = file_name
        
        self.template = templateEnv.get_template(TEMPLATE_FILE)

    def render_object(self, **kwargs):
        return self.template.render(**kwargs)