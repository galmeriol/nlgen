import jinja2
from mixin.template_mixin import TemplateMixin

class NewsletterItemLink(TemplateMixin):

    def __init__(self, text, link):
        self.template = self.load_template("newsletter_item_link.tmpl")

        self.text = text
        self.link = link
    
    def render(self):
        
        return self.render_object(
            template=self.template, 
            text=self.text,
            link=self.link)
        