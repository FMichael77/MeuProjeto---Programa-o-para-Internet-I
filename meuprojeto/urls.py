from django.contrib import admin
from django.urls import path
from enquetes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bemvindo/', views.bemvindo),
    path('enquete/<int:enquete_id>', views.enquete),
]
