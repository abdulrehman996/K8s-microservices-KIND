from django.urls import path
from .views import SubmitDataView, DisplayDataView

urlpatterns = [
    path('submit/', SubmitDataView.as_view()),
    path('display/', DisplayDataView.as_view()),
] 