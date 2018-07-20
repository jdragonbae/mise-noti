from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from schedule import views

#router = DefaultRouter()
#router.register(r'v1/auth/', views.ScheduleApiView)

#schema_view = get_swagger_view(title='Snippets API')

urlpatterns = [
    # url('^$', schema_view),
    url(r'v1/auth/', views.ScheduleApiView.as_view()),
  #  url(r'^', include(router.urls)),
  #   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
