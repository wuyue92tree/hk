from django.contrib import admin

from .models import Http

# Register your models here.


class HttpAdmin(admin.ModelAdmin):
	list_display = ('sip', 'dip', 'sport', 'dport', 'method', 'platform', 'browser', 'host', 'time')
	search_fields = ('method',)
	ordering = ('-time',)


admin.site.register(Http, HttpAdmin)
