
from django.urls import path
from .import views

urlpatterns = [
    # path('', views.home, name='home'),
    # path('student/', views.post_Student, name='home'),
    # path('update-student/<id>/', views.update_Student, name='home'),
    # path('delete_student/<id>/', views.delete_student, name='home'),
    path('get_book/', views.get_book, name='home'),
    path('Student/', views.StudentAPI.as_view, name='home'),

]