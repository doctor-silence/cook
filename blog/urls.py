from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name="post_single"),
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
    path('', views.home),


]