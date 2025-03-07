from datetime import datetime
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from PIL import Image as PILImage, ImageOps
from djmoney.models.fields import MoneyField
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
from embed_video.fields import EmbedVideoField
from pytz import timezone

# Create your models here.


class Video(models.Model):
    """Video
    This class is a model for videos for the website.
    """
    video_title = models.CharField(max_length=200)
    video_source = EmbedVideoField()
    date_created = models.DateTimeField(blank=True, null=True, editable=False)

    # The function defines how each project appears in admin.
    def __str__(self):
        # Convert from UTC time to the proper timezone.
        current_zone = timezone(settings.TIME_ZONE)
        local_time = self.date_created.astimezone(current_zone)

        # Return the string of the object.
        return f"{self.video_title} - Date Posted: {local_time.strftime('%A, %b %d, %Y - %I:%M %p')}"

    # The function sets the date created.
    def save(self, *args, **kwargs):
        # Set sent time to the current time.
        self.date_created = datetime.now()

        # Save everything else.
        super().save(*args, **kwargs)


class Image(models.Model):
    """Image
    The class is a model for how the images of the projects are stored.
    """
    image_title = models.CharField(max_length=50)
    date_created = models.DateTimeField(blank=True, null=True, editable=False)
    image = models.ImageField(upload_to="images")
    priority = models.PositiveIntegerField(blank=False, default=1, null=False)

    # The function defines how each image appears in admin.
    def __str__(self):
        # Convert from UTC time to the proper timezone.
        current_zone = timezone(settings.TIME_ZONE)
        local_time = self.date_created.astimezone(current_zone)

        # Return the string of the object.
        return f"{self.image_title} - Uploaded on: {local_time.strftime('%A, %b %d, %Y - %I:%M %p')}"


    # The function creates the slug and sets the last update.
    def save(self, *args, **kwargs):
        # Set sent time to the current time.
        self.date_created = datetime.now()

        # Save everything else.
        super().save(*args, **kwargs)

        # Set the base width and height for the thumbnail of the image.
        base_width = 900
        base_height = 900

        # Grab the image that was just saved.
        img_data = PILImage.open(self.image.path)

        # Use exif_transpose to maintain image EXIF metadata.
        img = ImageOps.exif_transpose(img_data)

        # Resize the image that was just save and then save the image.
        img.thumbnail((base_width, base_height), PILImage.LANCZOS)
        img.save(self.image.path)


class Product(models.Model):
    """ Project
    The class is a model for how the projects are stored in a database.
    """
    title = models.CharField(max_length=50)
    base_price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    description = models.TextField()
    options = models.TextField()
    external_url = models.URLField(max_length=200, blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True, editable=False)
    slug = models.SlugField(default="", blank=True, editable=False,
                            null=False, db_index=True, unique=True)
    images = models.ManyToManyField(Image)


    # The function defines how each project appears in admin.
    def __str__(self):
        # Convert from UTC time to the proper timezone.
        current_zone = timezone(settings.TIME_ZONE)
        local_time = self.last_update.astimezone(current_zone)

        # Return the string of the object.
        return f"{self.title} - Last Updated: {local_time.strftime('%A, %b %d, %Y - %I:%M %p')}"


    # The function creates the slug and sets the last update.
    def save(self, *args, **kwargs):
        # Create the slug for the entry.
        self.slug = slugify(self.title)

        # Set sent time to the current time.
        self.last_update = datetime.now()

        # Save everything else.
        super().save(*args, **kwargs)


class Plan(models.Model):
    """ Project
    The class is a model for how the plans are stored in a database.
    """
    title = models.CharField(max_length=50)
    base_price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    description = models.TextField()
    external_url = models.URLField(max_length=200, blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True, editable=False)
    slug = models.SlugField(default="", blank=True, editable=False,
                            null=False, db_index=True, unique=True)
    images = models.ManyToManyField(Image)


    # The function defines how each project appears in admin.
    def __str__(self):
        # Convert from UTC time to the proper timezone.
        current_zone = timezone(settings.TIME_ZONE)
        local_time = self.last_update.astimezone(current_zone)

        # Return the string of the object.
        return f"{self.title} - Last Updated: {local_time.strftime('%A, %b %d, %Y - %I:%M %p')}"


    # The function creates the slug and sets the last update.
    def save(self, *args, **kwargs):
        # Create the slug for the entry.
        self.slug = slugify(self.title)

        # Set sent time to the current time.
        self.last_update = datetime.now()

        # Save everything else.
        super().save(*args, **kwargs)


class Request(models.Model):
    """ Request
    The class defines how request from the contact form are saved.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    comment = models.TextField()
    sent_time = models.DateTimeField(editable=False)


    # The function defines how each request appears in admin.
    def __str__(self):
        # Convert from UTC time to the proper timezone.
        current_zone = timezone(settings.TIME_ZONE)
        local_time = self.sent_time.astimezone(current_zone)

        # Return the string of the object.
        return f"{self.first_name} {self.last_name} on {local_time.strftime('%A, %b %d, %Y - %I:%M %p')}"


    # The function saves sent_time as the current time the request was
    # saved.
    def save(self, *args, **kwargs):
        # Set sent time to the current time.
        self.sent_time = datetime.now()

        # Send an email to the Owner.
        subject = f'New Request from {self.first_name} {self.last_name} at {self.email}'
        message = f'You have a new request from {self.first_name} {self.last_name}\n\nComment:\n{self.comment}\n\n{self.email}\n\nThis is an automatically generated email from your website.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER, ]
        send_mail(subject, message, email_from, recipient_list)

        # Send an email to the customer making the request.
        subject = 'Request Has Been Receive - JKW Wood Works'

        # Load and render the html message.
        html_message = loader.render_to_string(
            'main_site/submit-email.html',
            {
                'full_name': f'{self.first_name} {self.last_name}'
            }
        )
        
        recipient_list = [self.email, ]
        send_mail(subject, html_message, email_from, recipient_list, html_message=html_message)

        # Save everything else.
        super().save(*args, **kwargs)