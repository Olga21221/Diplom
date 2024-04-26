from django.urls import path, include
from .views import Dog_page, Home_page, Help_page


urlpatterns = [
    path('', include('heppy_pet_app.urls'),)

]