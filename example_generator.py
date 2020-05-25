import jinja2
from nlgen.components.newsletter_item import NewsletterItem
from nlgen.components.newsletter_item_link import NewsletterItemLink
from nlgen.components.newsletter import Newsletter

sections = {"1": "Etkinlikler ve önemli duyurular",
            "2": "Güncel Çalışma Alanları"}

nlitem = NewsletterItem(
    header="Beyin aktivitelerini kelimelere dönüştürebilecek algoritma çalışmaları devam ediyor", 
    header_link="https://www.bbc.com/news/science-environment-52094111",
    content="""
        Beyin aktivitelerini kelimelere dönüştürmek oldukça eski bir araştırma alanı. California Üniversitesi'nden bir grup araştırmacı küçük bir kelime ve cümle grubu ile 3%% hata oranını yakayabildiler.
    """,
    links=[
        NewsletterItemLink(text="Makale", link="https://www.nature.com/articles/s41593-020-0608-8"),
        NewsletterItemLink(text="İlgili Github Repo", link="https://github.com/jgmakin/machine_learning")
        ],
    image="https://ichef.bbci.co.uk/news/660/cpsprodpb/14331/production/_111473728_f0194286-brain_neural_network_illustration.jpg",
    image_link="https://www.bbc.com/news/science-environment-52094111",
    section="2")

Newsletter(
    page_title="Teknolojik Gelişmeler",
    newsletter_title="Bülten",
    period_text="Şubat / Mart",
    sections=sections,
    newsletter_items=[nlitem])\
        .render()\
        .export()