from django.contrib import admin
from django.contrib.auth import admin as auth

from app import models as app

admin.site.register(app.Category)
admin.site.register(app.Curriculum)
admin.site.register(app.Productions)
admin.site.register(app.User)
# Register your models here.
