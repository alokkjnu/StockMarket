from django.contrib import admin
from .models import Stock_Name, Form_Query
import csv
import datetime
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe


# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = ['issuer_name', 'slug']
    prepopulated_fields = {'slug': ('issuer_name',)}


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \ filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response

export_to_csv.short_description = 'Export to CSV'


class StockAdminDetail(admin.ModelAdmin):
    list_display = ['id']
    #inlines = [StockAdmin]
    actions = [export_to_csv]


admin.site.register(Stock_Name, StockAdmin)
admin.site.register(Form_Query,StockAdminDetail)
