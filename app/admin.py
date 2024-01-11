from django.contrib import admin

# Register your models here.
from app.models import *


class customezeWebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url']
    list_display_links=['name']
    list_editable=['url']
    list_filter=['topic_name']
    list_per_page=3
    list_search=['name']




admin.site.register(Topic)


admin.site.register(Webpage,customezeWebpage)


admin.site.register(AccessRecord)




