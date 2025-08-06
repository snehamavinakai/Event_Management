from django.contrib import admin
from .models import Contact, Career, Card, Wedding,BirthDay, Corporate

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'address', 'email', 'phone', 'subject', 'message')
    search_fields=('address', )
    list_filter=('address', )


admin.site.register(Contact, ContactAdmin)

class WeddingAdmin(admin.ModelAdmin):
    list_display=('id', 'firstname', 'lastname','phone', 'email', 'date')
    search_fields=('firstname', )
    list_filter=('firstname', )

admin.site.register(Wedding, WeddingAdmin )

class CareerAdmin(admin.ModelAdmin):
    list_display=('id', 'name','email', 'file', 'message')
    search_fields=('email', )
    list_filter=('email', )


admin.site.register(Career,CareerAdmin)

admin.site.register(Card)
admin.site.register(BirthDay)
admin.site.register(Corporate)





