from django.contrib import admin
from . import models

# Register your models here.

#for better utilisation in same page
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)