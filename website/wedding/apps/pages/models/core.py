from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailcore.fields import RichTextField

class FeatureItem(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    title = models.CharField(max_length=255, blank=True)
    description = RichTextField(blank=True)
    
    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('description', classname="full"),
    ]

    class Meta:
        abstract = True