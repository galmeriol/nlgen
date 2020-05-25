import jinja2

from nlgen.mixin.template_mixin import TemplateMixin

class NewsletterItem(TemplateMixin):

    def __init__(self, header, header_link, content, section, links=[], image=[], image_link=[]):

        self.template = self.load_template("newsletter_item.tmpl")

        self.header = header
        self.header_link = header_link
        self.content = ''.join(line.strip() for line in content.splitlines(True))
        self.links = links
        self.image = image
        self.image_link = image_link
        self.section = section
    
    def render(self):
        
        return self.render_object(
            template=self.template,
            header=self.header, 
            header_link=self.header_link,
            content=self.content, 
            links=self.links,
            image=self.image,
            image_link=self.image_link,
            section=self.section)