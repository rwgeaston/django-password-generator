from rest_framework.routers import DefaultRouter

from .views import WordViewSet
from .views import WordsetViewSet

router = DefaultRouter()
router.register(r'words', WordViewSet)
router.register(r'wordsets', WordsetViewSet)
router.register(r'languages', WordsetViewSet)
urlpatterns = router.urls
