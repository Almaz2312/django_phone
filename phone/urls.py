from . import views
from django.urls import path


urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('create/', views.create_phone_view, name='create'),
    path('detail/<int:pk>/', views.DetailPhoneView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.DeletePhoneView.as_view(), name='delete'),
    path('update/<int:pk>/', views.UpdatePhoneView.as_view(), name='update'),
]
