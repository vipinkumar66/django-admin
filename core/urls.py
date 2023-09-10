
from django.contrib import admin
from django.urls import path, include
from blog.admin import blog_site
from adminblog.admin import blogadmin_site
from django.conf import settings
from django.conf.urls.static import static
# from library.admin import library_admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogadmin/', blog_site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("blogadmin-area/", blogadmin_site.urls)
    # path('libraryadmin/', library_admin.urls),

] #+ static(settings.STATIC_URL, documnet_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
