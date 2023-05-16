from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='index_view'),

    path('property/', views.property_view, name='property_view'),
    path('property_detail/<int:id>', views.property_detail_view, name='property_detail_view'),

    # path('packageDetail/<int:pk>/', views.packageDetail_view, name='packageDetail_view'),

    path('category/<int:id>/', views.category_view, name='category_view'),

    path('search/', views.search_view, name='search_view'),
    path('search/<int:price>/<str:keyword>/<int:types>/<int:city>/<int:status>', views.search_price_view, name='search_price_view'),

    path('testimonial/', views.testimonial_view, name='testimonial_view'),

    path('about/', views.aboutUs_view, name='aboutUs_view'),

    path('agents/', views.agents_view, name='agents_view'),


    # path('gallery/', views.gallery_view, name='gallery_view'),

    # path('feedbacks/', views.feedback_view, name='feedback_view'),

    path('contactUs/', views.contactUs_view, name='contactUs_view'),
    path('contact/', views.contact_view, name='contact_view'),

]
