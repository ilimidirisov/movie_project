from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, GenreViewSet

router = DefaultRouter()
router.register('genres', GenreViewSet)
router.register('movies', MovieViewSet)

urlpatterns = router.urls
