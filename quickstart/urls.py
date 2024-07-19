from django.urls import include, path
from rest_framework import routers

from quickstart import views
from quickstart.views import AuthorBlogsListView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'blogs', views.BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('authors/<int:author_id>/blogs/', AuthorBlogsListView.as_view(), name='author-blogs-list')
]
