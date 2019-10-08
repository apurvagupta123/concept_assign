from django.urls import path
from . import views
urlpatterns = [
    path('', views.fib_input_view),
    path('output',views.output)
]