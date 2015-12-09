from __future__ import unicode_literals

from wagtail.wagtailadmin.edit_handlers import FieldPanel

from wagtail.wagtailcore.fields import RichTextField

from django.db import models

from wagtail.wagtailcore.models import Page


class HomePage(Page):
	body = RichTextField()
	content_panels = Page.content_panels + [
		FieldPanel("body")

		]
	parent_page_types = []
