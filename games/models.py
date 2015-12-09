from wagtail.wagtailcore.models import Page

class GameIndex(Page):
	subpage_types = ["GamePage"]

class GamePage(Page):
	subpage_types = []
	parent_page_types = ["GameIndex"]
		