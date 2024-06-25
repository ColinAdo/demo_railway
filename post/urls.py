from rest_framework.routers import SimpleRouter
from .views import PostViewset

router = SimpleRouter()

router.register(r'posts', PostViewset, basename='posts')
urlpatterns = router.urls