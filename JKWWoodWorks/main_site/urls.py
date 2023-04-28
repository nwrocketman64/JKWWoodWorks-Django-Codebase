from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexPage.as_view(), name="index-page"),
    path("contact", views.ContactPage.as_view(), name="contact-page"),
    path("contact-submitted", views.ContactSubmitPage.as_view(), name="contact-submitted"),
    path("about", views.AboutPage.as_view(), name="about-page"),
    path("products", views.ProductList.as_view(), name="product-list"),
    path("product/<slug:slug>", views.ProductDetails.as_view(), name="product-details"),
    path("plans", views.PlanList.as_view(), name="plan-list"),
    path("plan/<slug:slug>", views.PlanDetails.as_view(), name="plan-details"),
    path("videos", views.VideoList.as_view(), name="video-list"),
]