from django.urls import path
from . import views
urlpatterns = [
    path('create_candidate/', views.create_candidate.as_view(template_name="candidate/create_candidate.html"),name="candidate-create"),
    path('candidate_view/<int:pk>',views.candidate_view,name='candidate-view'),




]