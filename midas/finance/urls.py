from django.urls import include, path
from rest_framework import routers

from .views import BoardViewset, EntryViewset, TagViewset

router = routers.DefaultRouter()

router.register('board', BoardViewset, base_name='board')
router.register('entry', EntryViewset, base_name='entry')
router.register('tag', TagViewset, base_name='tag')

urlpatterns = [
    path('', include(router.urls)),
]
