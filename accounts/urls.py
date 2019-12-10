from django.urls import path

from accounts.views import HelloView

urlpatterns = [
    path('home/', HelloView.as_view(), name='hello')
]
