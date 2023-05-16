from django.contrib import admin
from .models import *
# Register your models here.

class PropertyGalleryInline(admin.TabularInline):
    model           = Gallery
    list_display    = ['title','image','created_date','updated_date']
    list_editable   = ('title','image')
    extra           = 1 

class PropertyAdmin(admin.ModelAdmin):
    list_display    = ['title','city','room','hall','kitchen','price','updated_at','featured','available']
    list_filter     = ['available','updated_at','featured','city']
    search_fields   = ['title','description']
    list_per_page   = 20
    inlines         = [PropertyGalleryInline]

admin.site.register(Property,PropertyAdmin) 
admin.site.register(PropertyType)
admin.site.register(Agent)
admin.site.register(Gallery)
admin.site.register(Testimonial)
admin.site.register(City)
admin.site.register(Contact)
