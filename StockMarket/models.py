from django.db import models
from django.urls import reverse


# Create your models here.

class Stock_Name(models.Model):
    security_code = models.CharField(max_length=15)
    issuer_name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    security_id = models.CharField(max_length=50)
    security_name = models.CharField(max_length=250, db_index=True)
    status = models.BooleanField(default=True)
    group = models.CharField(max_length=5)
    face_value = models.IntegerField(default=0)
    isin_no = models.CharField(max_length=20)
    industry = models.CharField(max_length=100)
    instrument = models.CharField(max_length=15, default='Equity')
    video = models.FileField(upload_to="media/%Y", null=True)

    class Meta:
        ordering = ('security_code',)

    def __str__(self):
        return self.issuer_name

    def get_absolute_url(self):
        return reverse('StockMarket:stock_detail', args=[self.id, self.slug])


class Form_Query(models.Model):
    #Stock_Name = models.ForeignKey(Stock_Name, related_name='stock_name', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    enquery = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('user_name',)
    def __str__(self):
        return self.user_name


    def get_absolute_url(self):
        return reverse('StockMarket:index', args=[self.id])
