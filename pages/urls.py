from django.urls import path

from . import views as pages_views

app_name = 'pages'

urlpatterns = [
    path('' , pages_views.Index.as_view() , name = 'index'),
    path('aboutme/' , pages_views.AboutMePage.as_view() , name = 'aboutme'),
    ]