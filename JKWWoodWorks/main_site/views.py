from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView

# Import the needed classes from other files.
from .forms import RequestForm
from .models import Product, Request, Video

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


class ProductList(ListView):
    """ Product List
    The class delivers the full list of products.
    """
    # Set the template, model, and order by last update.
    template_name = "main_site/products.html"
    model = Product
    ordering = ["-last_update"]
    context_object_name = "products"


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Full List of Products"
        context["path"] = "/products"
        return context


class ProductDetails(DetailView):
    """ Product Detail
    The class returns the details of a product.
    """
    # Set the template and the model.
    template_name = "main_site/product-details.html"
    model = Product


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Product Details"
        context["path"] = "/products"
        return context


class VideoList(ListView):
    """
    The class delivers the list of posted videos.
    """
    # Set the template, model, and order by last update.
    template_name = "main_site/videos.html"
    model = Video
    ordering = ["-date_created"]
    context_object_name = "videos"
    paginate_by = 4


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Full List of Videos"
        context["path"] = "/videos"
        return context


class AboutPage(TemplateView):
    """About Page
    The class delivers the about me page.
    """
    # Set the template.
    template_name = "main_site/about.html"


    # Add the title and path to the page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About Me"
        context["path"] = "/about"
        return context