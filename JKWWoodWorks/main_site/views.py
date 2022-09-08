from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

# Import the needed classes from other files.
from .forms import RequestForm
from .models import Product, Request

# Create your views here.


class IndexPage(TemplateView):
    """ Index Page
    The class returns the index page with the latest product.
    """
    # Set the template.
    template_name = "main_site/index.html"


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get the earliest project.
        try:
            products = Product.objects.all().order_by("-last_update")
            lastest_product = products[0]
        except:
            # If failed, return blank.
            lastest_product = []
        
        # Update and return the context.
        context["title"] = "Home"
        context["path"] = "/home"
        context["product"] = lastest_product
        return context


class ContactPage(CreateView):
    """ Contact Page
    The class renders the contact view page based off of the request
    model.
    """
    # Set the template, model, form, and url redirect.
    template_name = "main_site/contact.html"
    model = Request
    form_class = RequestForm
    success_url = "/contact-submitted"


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Contact Us"
        context["path"] = "/contact"
        return context


class ContactSubmitPage(TemplateView):
    """Contact Submit Page
    The class renders the contact success submit page.
    """
    # Set the template.
    template_name = "main_site/contact-submit.html"


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Form Submitted"
        context["path"] = "/contact"
        return context


# The class delivers the about me page.
class AboutPage(TemplateView):
    # Set the template.
    template_name = "main_site/about.html"


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About Me"
        context["path"] = "/about"
        return context