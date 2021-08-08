from django.urls import path
from .views import home, student_add_api, student_api, student_list_api, student_list_api2


urlpatterns = [
    path('', home),
    # path('student/', manual_api),
    path('list/', student_list_api),
    path('list2/', student_list_api2),
    path('add/', student_add_api),
    path('student/', student_api),

]
