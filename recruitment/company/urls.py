from django.urls import path
from . import views


urlpatterns =[
    path('add_company/',views.add_company,name="add_company"),
    path('home/', views.home, name="company-home"),
    path('view_company/',views.view_company,name="view_company"),
    path('company_view',views.company_view,name="company_view"),
    path('user_company_view/<int:user_id>/',views.user_company_view,name="user_company_view"),
    path('generate_agreement/',views.generate_agreement,name="generate_agreement"),
    ]
