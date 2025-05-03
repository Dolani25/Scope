from django.contrib import admin

# Register your models here.

from core.models import Blockchain, Task, Notification, FollowerProfile, ScopeUser, Airdrop,Event


# In your app's admin.py file

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class ScopeUserInline(admin.StackedInline):
    model = ScopeUser
    can_delete = False
    verbose_name_plural = 'Scope User'

class UserAdmin(BaseUserAdmin):
    inlines = (ScopeUserInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)    
       

admin.site.register(Airdrop)
admin.site.register(Blockchain)
admin.site.register(Task)
admin.site.register(Event)