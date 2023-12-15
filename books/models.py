from django.db import models


class Manufactures(models.Model):
    account = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=50)
    manufacture = models.ForeignKey(Manufactures, on_delete=models.CASCADE)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=50, unique=True, blank=True, null=True)
    manufacture = models.ForeignKey(Manufactures, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_url = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-created_date"]
        unique_together = (("name", "sku"),)
    

class Books(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField( blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    book_image = models.ImageField(upload_to='images/', blank=True, null=True)
    book_file = models.FileField(upload_to='files/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Posts(models.Model):
    
    chapter_name = models.CharField(max_length=100)
    chapter_content = models.TextField()
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    chapter_vorder = models.IntegerField(default=0)
    chapter_horder = models.IntegerField(default=0)
    chapter_type = models.CharField(max_length=10)
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["chapter_vorder", "chapter_horder"]
        unique_together = (("chapter_name", "book"),)

    def __str__(self):
        return self.chapter_name

class Comments(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


    
    

    
