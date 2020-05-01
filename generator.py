import jinja2
from components.newsletter_item import NewsletterItem
from components.newsletter_item_link import NewsletterItemLink
from components.newsletter import Newsletter

sections = {"1": "Etkinlikler ve önemli duyurular"}

nlitem = NewsletterItem(
    header="Apache Spark 3.0 Preview Release çıktı", 
    header_link="https://spark.apache.org/news/spark-3.0.0-preview.html",
    content="""
    Dağıtık veri işlemci kütüphanesi Apache Spark yeni majör versiyonu 3.0'ı geliştiricilerin test etmesi amacıyla yayınladı. Bu versiyonda;
          <ul>
            <li>Graph tabanlı veritabanı sorgulama dili <b>Cypher</b> desteği eklendi.</li>
            <li>Python 3'e tam geçiş bekleniyor.</li>
            <li>Scala 2.12 ve Java 11 desteği geldi.</li>
            <li>RDD üzerindeki işlemler ve UDF'ler için GPU desteği geldi.</li>
          </ul>
    """,
    links=[
        NewsletterItemLink(text="Yeni özellikler", link="https://towardsdatascience.com/glimpse-into-spark-3-0"),
        NewsletterItemLink(text="Cypher Query Language", link="https://neo4j.com/developer/cypher-query-language/")
        ],
    image="https://www.computing.co.uk/w-images/cc6f36ae-ffb1-4271-8847-725556046f5c/0/apachesparklogo-580x358.png",
    image_link="https://spark.apache.org/news/spark-3.0.0-preview.html",
    section="1")

newsletter = Newsletter(
    page_title="Big Data ve Data Science Teknolojik Gelişmeler",
    newsletter_title="Büyük Veri ve İleri Analitik Bülten",
    period_text="Şubat / Mart ",
    sections=sections,
    newsletter_items=[nlitem]).render_object()

with open("newsletter.mjml", "w") as nl:
    nl.write(newsletter)
