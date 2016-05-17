from django.conf.urls import url, include
from svincnik import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'jedi', views.JedViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'komentarji', views.KomentarViewSet)
urlpatterns = (
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')
        )
)
