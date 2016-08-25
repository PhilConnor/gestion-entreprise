from django.conf.urls import include
from django.conf.urls import url

from error_manager import views

urlpatterns = [
    url(
        r'^error_codes/',
        views.ErrorCodeListView.as_view(),
        name='error_codes'
    ),
]
