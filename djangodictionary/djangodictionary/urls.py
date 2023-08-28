# importing the django's in-built admin url
from django.contrib import admin
# importing path and include from django's in-built urls
from django.urls import path, include
from django.contrib.staticfiles_urlpatterns()

# defining the list for urls
urlpatterns = [
    path('admin/', admin.site.urls),
    # registering dictionary app urls in project
    path('', include('dictionary.urls')),
]

urlpatterns += staticfiles_urlpatterns()