from typing import Any
from django.contrib import admin, messages
from django.http.request import HttpRequest
from blog.models import Category, Post

class AdminBlogArea(admin.AdminSite):
    site_header = "Blog Admin Area"

class AdminAreaPermissions(admin.ModelAdmin):

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(self, request: HttpRequest, obj=None):
        """
        Here we are drilling in the request and getting the groups that user belongs
        to and than on the basis of that we are asigning the permission to change the
        object wise not
        """
        if request.user.groups.filter(name="editors").exists():
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        """
        if the object is there than it is going to return true
        But in the second case where i am saying that if the obj.pk is not equal to 2 it will return true
        else it will return false
        So for the object whose pk is 2 it will not give delete permission and for others it is going
        to give delete permission"""

        if obj != None and request.POST.get('action') == "delete_selected":
            messages.add_message(request, messages.ERROR, (" I HOPE YOU ARE REALLY "
                                                           "sure about this"))

        return obj is None or obj.pk!=2


    def has_view_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return True

blogadmin_site = AdminBlogArea(name="Blog Admin")
blogadmin_site.register(Category,AdminAreaPermissions)
blogadmin_site.register(Post, AdminAreaPermissions)
