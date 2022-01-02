from django.urls import path
from first import views

urlpatterns = [
    path('', views.index ,name="index"),
    path("sf/", views.student_form ,name="sf"),
    path("student_info/<int:student_id>/", views.student_info ,name="student_info"),
    path("student_update/<int:student_id>/", views.student_update ,name="student_update"),
    path("student_delete/<int:student_id>/", views.student_delete ,name="student_delete"),
]