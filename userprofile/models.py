import datetime

from django.utils import timezone
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from embed_video.fields import EmbedVideoField

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    location = models.CharField(max_length=50, blank=True)
    verified_user = models.BooleanField(default=False)
    admin_account = models.BooleanField(default=False)
    profile_picture = models.ImageField()
    follower_count = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)
    skin_type = models.CharField(max_length=100, blank=True)

    pass

    def isVerifiedUser(self):
        return self.verified_user

    def isAdminAccount(self):
        return self.admin_account

    def __str__(self):
        return self.name

    def getPostCount(self):
        return self.post_set.count()


class Product(models.Model):
    product_name = models.CharField(max_length=300)
    product_brand = models.CharField(max_length=300)
    product_buy_url = models.CharField(max_length=500, blank=True)
    product_image = models.ImageField(blank=True)
    product_price = models.DecimalField(default=0, decimal_places=2,max_digits=5)
    pass


class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_text = models.TextField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    pub_user = models.ForeignKey(User,on_delete=models.CASCADE)
    post_video = EmbedVideoField(blank=True)
    products = models.ManyToManyField(Product)
    thumbnail = models.ImageField(blank=True)

    
    def __str__(self):
        return self.post_title

    def create(cls, title,text,date,user):
        post = cls(post_title=title, post_text=text, pub_date=date,pub_user=user)
        # do something with the book
        return post

    def getProducts(self):
        return products.all()



