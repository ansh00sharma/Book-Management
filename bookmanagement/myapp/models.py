from django.db import models

class user_table(models.Model):
    user_email = models.CharField(max_length=100, primary_key=True)
    user_password = models.CharField(max_length=256)
    user_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) 


class book_table(models.Model):
    book_name = models.CharField(max_length=256,primary_key=True)
    author_id = models.CharField(max_length=5)
    stock = models.IntegerField()
    Added_at = models.DateTimeField(auto_now_add=True) 

    # def __str__(self):
    #     return f"{self.book_name} by {self.author_id} (Stock: {self.stock})"