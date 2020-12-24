from django.urls import path
from . import views


urlpatterns =[
    path('add_company/',views.add_new_company,name="add_company"),
    path('home/', views.home, name="company-home"),
    path('view_company/',views.view_company,name="view_company"),
    path('company_view/<int:user_id>/',views.company_view,name="company_view"),
    path('user_company_view/<int:user_id>/',views.user_company_view,name="user_company_view"),
    path('generate_agreement/<int:company_id>/',views.generate_agreement,name="generate_agreement"),
    path('update/<int:pk>',views.Update_company.as_view(template_name='company/add_company.html'),name='update_company'),
    path('delete/<int:pk>',views.delete_company.as_view(),name='delete_company')
    ]
