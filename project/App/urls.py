from django.urls import path
from .views import *

urlpatterns = [
    path('user/',employe_view ,name='empd'),
    path('view/',view_emp, name='vemp'),
    path('pro/',store_view, name='pro_tab'),
    path('book/',book_view, name='book'),
    path('movie/',movie_view, name='movie'),
    path('student/',student_view, name='student'),
    path('movie/delete/<int:mov_id>/',movie_delete, name='movie_delete'),
    path('movie/edit/<int:mov_id>/', movie_edit, name='movie_edit'),


    
]
