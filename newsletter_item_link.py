import jinja2
from template_mixin import TemplateMixin

class NewsletterItemLink(TemplateMixin):

    def __init__(self, text, link):
        super().__init__("newsletter_item_link.tmpl")
        self.text = text
        self.link = link
    
    def render_object(self):
        
        return super().render_object(text=self.text,
        link=self.link)