import jinja2

class TemplateMixin():

    def load_template(self, file_name):

        templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
        templateEnv = jinja2.Environment(loader=templateLoader)
        TEMPLATE_FILE = file_name
        
        return templateEnv.get_template(TEMPLATE_FILE)

    def render_object(self, template, **kwargs):
        return template.render(**kwargs)