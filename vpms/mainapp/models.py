from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    TYPE=(
        ('Male','Male'),
        ('Female','Female'),
        ('Transgender','Transgender')
        )
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    Gender = models.CharField(max_length=100, choices=TYPE,default=None)
    phone = models.CharField(max_length=15)
    self_bio = models.TextField(max_length=150)

class card_categories(models.Model):
    tittle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,default=tittle)

    def slug(self):
        return slugify(self.title)

    def __str__(self):
        return self.tittle

class card(models.Model):
    card_tittle = models.CharField(max_length=150)
    card_type = models.ForeignKey(card_categories, null=True,blank=True, on_delete=models.CASCADE)
    card_selling_price= models.FloatField()
    card_description = models.TextField(max_length=1000)

    def slug(self):
        return slugify(self.card_tittle)

    def __str__(self):
        return self.card_tittle

class sold_card(models.Model):
    sold_card_tittle = models.CharField(max_length=150)
    sold_card_type = models.ForeignKey(card_categories, null=True,blank=True, on_delete=models.CASCADE)
    sold_card_selling_price= models.FloatField()

    def slug(self):
        return slugify(self.sold_card_tittle)

    def __str__(self):
        return self.sold_card_tittle