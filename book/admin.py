value1 = 10
value2  = 'ABC'









from django.contrib import admin
from book.models import BookInfo

admin.site.register(BookInfo)


# provide crud opearation for ur model
# provide login functionlity