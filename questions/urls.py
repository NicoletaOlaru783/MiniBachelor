from rest_framework import routers, urlpatterns
from .views import QuestionViewSet

router = routers.DefaultRouter()
router.register('api/questions', QuestionViewSet, 'questions')

urlpatterns = router.urls
