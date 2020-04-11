from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('submit_info', views.submit),
    path('checkout/<str:name>/<str:student_id>/<str:lychee>/<str:rambutan>/<str:jackfruit>', views.checkout),
    # path('checkout/<str:name>/<str:lychee>/<str:rambutan>/<str:jackfruit>', views.checkout), #This line has been left purposely wrong for troubleshooting
    
]