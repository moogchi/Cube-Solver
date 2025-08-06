from django.urls import path
from . import views

app_name = 'cube_solver'
urlpatterns = [
    path('', views.index, name='index'),
    path('solve/', views.solve_cube_api, name='solve_cube_api'),
    path('solution/', views.solution_steps, name='solution_steps'),
]