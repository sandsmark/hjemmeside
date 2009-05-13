from django.contrib.syndication.feeds import Feed
from hjemmeside.blog.models import Entry

class LatestEntries(Feed):
    title = "sandsmark's blurg"
    link = "http://mts-productions.com/blog/"
    description = "updates from sandsmark's blurg"

    def items(self):
        return Entry.objects.order_by('-pubdate')[:5]
    
    def item_pubdate(self, item):
        return item.pubdate
