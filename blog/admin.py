from django.contrib import admin
from .models import Post, Category
from django_summernote.admin import SummernoteModelAdmin
# import django.apps

# models = django.apps.apps.get_models()
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

# admin.site.unregister("django.contrib.sessions.models.Session")


# =>
class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Admin Area"
    login_template = "blog/admin/login.html"

blog_site = BlogAdminArea(name="BlogAdmin")

class SummernoteAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"


blog_site.register(Post, SummernoteAdmin)
blog_site.register(Category, SummernoteAdmin)
admin.site.register(Post, SummernoteAdmin)
admin.site.register(Category, SummernoteAdmin)


# admin.site.register(Post)
# admin.site.register(Category)


# =>

# TEXT = "THIS IS SOME TEXT TO INCLUDE"

# @admin.register(Post)
# class UpdatedAdmin(admin.ModelAdmin):
#     # fields = ["title", ("author", "slug")]
#     fieldsets = (
#         ("SECTION 1", {
#             'fields':("title", "author",),
#             'description':f"{TEXT}"
#         }),
#         ("SECTION 2", {
#             "fields": ("excerpt", "content",),
#             "classes":("collapse",),
#         }),
#     )

"""
Let's work on custom forms
"""

# from django import forms

# class PostForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         self.fields["title"].help_text = "This is a help text"

#         class Meta:
#             model = Post
#             exclude = ("",)

# class PostFormAdmin(admin.ModelAdmin):
#     form = PostForm

# admin.site.register(Post, PostFormAdmin)



