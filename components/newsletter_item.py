import jinja2

from nlgen.mixin.template_mixin import TemplateMixin
from requests import get
from io import BytesIO
from PIL import Image

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

        self.image_width, self.image_height = self.__get_image_size()
    
    def render(self):
        
        return self.render_object(
            template=self.template,
            header=self.header, 
            header_link=self.header_link,
            content=self.content, 
            links=self.links,
            image=self.image,
            image_width=self.image_width,
            image_height=self.image_height,
            image_link=self.image_link,
            section=self.section)

    def __get_image_size(self):
        print("Checking image size for url: " + self.image)

        try:
            image_raw = get(self.image, verify=False)
            image = Image.open(BytesIO(image_raw.content))
            width, height = image.size
        except Exception:
            raise ValueError("Haber görseli boyutları belirlenemedi. Lütfen başka görsel belirleyiniz.")

        return 100, height * (100 / width)