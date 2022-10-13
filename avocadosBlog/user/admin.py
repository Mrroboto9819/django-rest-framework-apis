from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
    # fieldsets = (
    #     (None, {
    #         "fields": (
    #          'username', 'password'   
    #         ),
    #     }),
    #     ('User Information', {
    #         "fields": (
    #          'first_name', 'last_name', 'email'   
    #         ),
    #     }),
    # )
    
    # list_display = ['username', 'pk']