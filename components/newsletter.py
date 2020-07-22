import jinja2
import re
import os
import inspect

from nlgen.mixin.template_mixin import TemplateMixin

class Newsletter(TemplateMixin):

    def __init__(self, page_title, newsletter_title, period_text, sections, newsletter_items):

        self.template = self.load_template("newsletter.tmpl")

        self.page_title = page_title
        self.newsletter_title = newsletter_title
        self.period_text = period_text
        self.sections = sections
        self.newsletter_items = newsletter_items.sort(key=lambda x: int(x.section))
    
    def render(self):
        print('rendering newsletter.....')
        self.newsletter_str = self.render_object(
            template=self.template,
            page_title=self.page_title,
            newsletter_title=self.newsletter_title,
            period_text=self.period_text,
            sections=self.sections,
            newsletter_items=self.newsletter_items)

        return self
        
    def export(self, file_name="newsletter.mjml"):
        print('exporting newsletter...')
        with open(file_name, "w", encoding="utf-8") as nl:
            nl.write(self.newsletter_str)
            print('export done!')
