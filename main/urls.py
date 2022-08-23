from rest_framework import routers

from .views import TaskRetrieveListViewSet, TaskCreateViewSet

router = routers.SimpleRouter()
router.register('tasks', TaskRetrieveListViewSet)
router.register('create-task', TaskCreateViewSet)

urlpatterns = router.urls
