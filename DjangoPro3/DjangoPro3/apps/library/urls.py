from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from library.views import AuthorViewSet, PublisherViewSet, BookViewSet

urlpatterns = [
    # path("admin/", admin.site.urls),

]

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'books', BookViewSet)

urlpatterns += router.urls
