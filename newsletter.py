import jinja2
from template_mixin import TemplateMixin

class Newsletter(TemplateMixin):

    def __init__(self, page_title, newsletter_title, period_text, sections, newsletter_items):
        super().__init__("newsletter.tmpl")
        self.page_title = page_title
        self.newsletter_title = newsletter_title
        self.period_text = period_text
        self.sections = sections
        self.newsletter_items = newsletter_items
    
    def render_object(self):
        
        return super().render_object(
            page_title=self.page_title,
            newsletter_title=self.newsletter_title,
            period_text=self.period_text,
            sections=self.sections,
            newsletter_items=self.newsletter_items)