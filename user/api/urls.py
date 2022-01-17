from django.urls import path
from user.views import (
    registration_view,
    user_view,
    update_view,
    deposit_view,
    delete_view,
    withdraw_view,
    transfer_view,
)

''' Overview of the api urls '''

app_name = 'users'

urlpatterns = [
    path('register/', registration_view, name="register"),
    path('view/<str:pk>/', user_view, name="view"),
    path('update/<str:pk>/', update_view, name="update"),
    path('delete/<str:pk>/', delete_view, name="delete"),
    path('deposit/<str:pk>/', deposit_view, name="deposit"),
    path('withdraw/<str:pk>/', withdraw_view, name="withdraw"),
    path('transfer/<int:pk1>/<int:pk2>', transfer_view, name="transfer"),
]