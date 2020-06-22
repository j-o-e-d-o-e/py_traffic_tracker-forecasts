from django.urls import path
from planes import views

urlpatterns = [
    path('planes/predict/', views.predict_and_planes_list),
    path('planes/', views.planes_list),
]
