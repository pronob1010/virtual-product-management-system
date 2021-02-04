from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# from autoslug import AutoSlugField
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    TYPE=(
        ('Male','Male'),
        ('Female','Female'),
        ('Transgender','Transgender')
        )
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    Gender = models.CharField(max_length=100, choices=TYPE,default=None, blank=True)
    phone = models.CharField(max_length=15, default=None, null=True, blank=True) 
    self_bio = models.TextField(max_length=150,default=None, null=True, blank=True)

class card_categories(models.Model):
    tittle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,default=tittle)

    def slug(self):
        return slugify(self.title)

    def __str__(self):
        return self.tittle

class card(models.Model):
    card_tittle = models.CharField(max_length=150, default=None, null=True)
    # slug = AutoSlugField(max_length=100,populate_from=card_tittle, default=card_tittle)
    card_type = models.ForeignKey(card_categories, null=True,blank=True, on_delete=models.CASCADE)
    card_selling_price= models.FloatField(default=None)
    card_used = models.BooleanField(default=False, blank=True)
    card_description = models.TextField(max_length=1000, default=None, null=True, blank=True)


    def __str__(self):
        return self.card_tittle

class customer_input(models.Model):
    product = models.ForeignKey(card, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    order_time = models.DateTimeField(default=now)
    order_price = models.FloatField(null=True)

    def __str__(self):
        return self.customer.username
    