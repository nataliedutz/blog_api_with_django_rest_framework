# django_project/urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Admin site URL
    path("admin/", admin.site.urls),

    # Include URLs from the 'posts' app under the 'api/v1/' prefix
    path("api/v1/", include("posts.urls")),

    # Include default authentication URLs provided by Django REST Framework
    path("api-auth/", include("rest_framework.urls")),

    # Include URLs for authentication provided by dj-rest-auth app
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),

    # Include URLs for registration provided by dj-rest-auth app
    path("api/v1/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls"))
]
