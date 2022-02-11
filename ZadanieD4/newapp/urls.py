from django.urls import path
from .views import NewList, NewDetailView, NewCreateView, NewUpdateView, NewDeleteView


urlpatterns = [
    path('', NewList.as_view()),
    path('<int:pk>/', NewDetailView.as_view(), name='news_detail'),
    path('create/', NewCreateView.as_view(), name='news_create'),
    path('create/<int:pk>', NewUpdateView.as_view(), name='news_update'),
    path('delete/<int:pk>', NewDeleteView.as_view(), name='news_delete'),
]