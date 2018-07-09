from django.conf.urls import url, include
# from posts import views

urlpatterns = [
    # path('', views.index),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]