from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from music import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'albums', views.AlbumViewSet)
router.register(r'tracks', views.TrackViewSet)
router.register(r'artists', views.ArtistViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]
