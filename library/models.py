from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.CASCADE, default=1)  # 假设 1 是一个有效的 Publisher ID
    published_date = models.DateField()

    def __str__(self):
        return self.title