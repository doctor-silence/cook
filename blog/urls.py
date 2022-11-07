from django.urls import path
from .  import views

urlpatterns = [
    path('<slug:slug>/<slug:postslug/', views.PostDetailView.as_view(), name='post_single'),
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
    path('', views.home),


]