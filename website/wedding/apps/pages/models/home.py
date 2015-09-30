from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from .core import FeatureItem


class HomePageFeatureItem(Orderable, FeatureItem):
    page = ParentalKey('pages.HomePage', related_name='feature_items')

class HomePageDetailItem(Orderable, FeatureItem):
    page = ParentalKey('pages.HomePage', related_name='detail_items')


class HomePage(Page):
    body = RichTextField(blank=True)

HomePage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('body'),
    InlinePanel('detail_items', label="Detail Items"),
    InlinePanel('feature_items', label="Feature Items"),
]