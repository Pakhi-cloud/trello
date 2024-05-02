from django.urls import path
from.views import UserView, ColumnView, CardView

urlpatterns = [
    path('users/', UserView.as_view()),
    path('columns/', ColumnView.as_view()),
    path('cards/', CardView.as_view()),
    path('cards/<int:pk>/', CardView.as_view()),
]