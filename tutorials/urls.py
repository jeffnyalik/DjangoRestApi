from django.urls import path
from . import views

urlpatterns = [
    path('api/v1', views.get_all_tutorials, name="home_page"),
    path('api/v1', views.get_tutorial_by_title, name='title'),
    path('api/v1/published', views.tutorials_published, name='published'),
    path('api/v1/publishedFalse', views.tutorials_published_false, name='false'),
    path('api/v1/<int:pk>', views.get_tutorial_details, name='details'),
]
