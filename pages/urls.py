from django.urls import path
from .views import ContactPageView,  AboutPageView, HomePageView, PortfolioPageView,  successView

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("about/", AboutPageView.as_view(), name="about"),
    path("portfolio/", PortfolioPageView.as_view(), name='portfolio'),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("success/", successView, name='success'),
]