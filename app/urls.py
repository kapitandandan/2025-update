from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/edit', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),


# Citizens URL 

    path('citizen/', CitizenListView.as_view(), name='citizen'),
    path('citizen/<int:pk>', CitizenDetailView.as_view(), name='citizen_detail'),
    path('citizen/create', CitizenCreateView.as_view(), name='citizen_create'),
    path('citizen/<int:pk>/edit', CitizenUpdateView.as_view(), name='citizen_update'),
    path('citizen/<int:pk>/delete', CitizenDeleteView.as_view(), name='citizen_delete'),

# Service URL

    path('service/', ServiceListView.as_view(), name='service'),
    path('service/<int:pk>', ServiceDetailView.as_view(), name='service_detail'),
    path('service/create', ServiceCreateView.as_view(), name='service_create'),
    path('service/<int:pk>/edit', ServiceUpdateView.as_view(), name='service_update'),
    path('service/<int:pk>/delete', ServiceDeleteView.as_view(), name='service_delete'),

# Complaint URL

    path('complaint/', ComplaintListView.as_view(), name='complaint'),
    path('complaint/<int:pk>', ComplaintDetailView.as_view(), name='complaint_detail'),
    path('complaint/create', ComplaintCreateView.as_view(), name='complaint_create'),
    path('complaint/<int:pk>/edit', ComplaintUpdateView.as_view(), name='complaint_update'),
    path('complaint/<int:pk>/delete', ComplaintDeleteView.as_view(), name='complaint_delete'),

# Feedback URL

    path('feedback/', FeedbackListView.as_view(), name='feedback'),
    path('feedback/<int:pk>', FeedbackDetailView.as_view(), name='feedback_detail'),
    path('feedback/create', FeedbackCreateView.as_view(), name='feedback_create'),
    path('feedback/<int:pk>/edit', FeedbackUpdateView.as_view(), name='feedback_update'),
    path('feedback/<int:pk>/delete', FeedbackDeleteView.as_view(), name='feedback_delete'),

]