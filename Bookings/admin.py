from django.contrib import admin
from .models import Reservations, Media, Feedbacks,Category,MenuItem
# Register your models here.
admin.site.register(Reservations)
admin.site.register(Media)
admin.site.register(Feedbacks)
admin.site.register(Category)
admin.site.register(MenuItem)