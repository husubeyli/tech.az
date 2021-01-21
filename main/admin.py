from django.contrib import admin
from main.models import Account
from django.contrib.auth.models import User, Group
admin.site.unregister(User)
admin.site.unregister(Group)



@admin.register(Account)
class TechAdmin(admin.ModelAdmin):
    # list_display = ('first_name', 'image', 'is_active_class', 'is_main', 'is_sub', 'is_position')
    # list_display_links = ('first_name')
    list_filter = ('first_name',)
    search_fields = ('first_name', ) 
    save_on_top = True
    save_as = True #create new product easy way
    readonly_fields = (
        'created_at',
    )
    fieldsets = (
        ('Informations', {
            'fields': ('first_name', 'last_name', 'email', 'created_at')
        }),
        
    )

# admin.site.site_url = '/tech.az/'