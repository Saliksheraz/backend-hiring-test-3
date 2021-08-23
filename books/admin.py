from django.contrib import admin
from .models import Volume, Review, ReadingPos, Bookshelf

admin.site.register(Volume)
admin.site.register(Review)
admin.site.register(ReadingPos)
admin.site.register(Bookshelf)
