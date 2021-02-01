from django.contrib import admin
from.models import *
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(card_categories)
admin.site.register(card)
admin.site.register(sold_card)
admin.site.register(customer_input)