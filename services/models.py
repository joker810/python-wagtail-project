from django.db import models
from django.core.exceptions import ValidationError

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class ServiceListingPage(Page):
    parent_page_types = ["home.HomePage"]
    subpage_types=["services.ServicePage"]
    max_count=1


    template = "services/service_listing_page.html"
    subtitle = models.TextField(
        blank=True,
        max_length=500,
    )
    content_panels= Page.content_panels+[
        FieldPanel('subtitle'),
    ]
    def get_context(self, request, *args, **kwargs):
        context =  super().get_context(request, *args, **kwargs)
        context['services']=ServicePage.objects.live().public()
        
        return context

class ServicePage(Page):
    parent_page_types = ["services.ServiceListingPage"]
    subpage_types=[]
    template = "services/service_page.html"
    description = models.TextField(
        blank=True,
        max_length=500,
    ) 
    internal_page = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='select an internal wagtail page',
        on_delete=models.SET_NULL,
    )

    external_page= models.URLField(blank=True)
    button_text=models.CharField(blank=True,max_length=50)
    service_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='the image will on the service listing page. 570x370px',
        on_delete=models.SET_NULL,
    ) 

    content_panels = Page.content_panels+[
        FieldPanel('description'),
        PageChooserPanel('internal_page'),
        FieldPanel('external_page'),
        FieldPanel('button_text'),
        ImageChooserPanel('service_image')
    ]

    def clean(self):
        super().clean()

        if self.external_page and self.internal_page:
            raise ValidationError({'internal_page':ValidationError("Please select a page or enter external url"),
            'external_page':ValidationError("Please select a page or enter external url")
            })

        if not self.external_page and not self.internal_page:
            raise ValidationError({'internal_page':ValidationError("Please select a page or enter external url"),
            'external_page':ValidationError("Please select a page or enter external url")
            })

    