from django.db import models
from django.utils.text import slugify

# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length=250,null=True)
    year = models.TextField(max_length=4, null=True)
    color = models.TextField(max_length=50, null=True)
   
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            
            # Verificar si el slug ya existe y agregar un sufijo para hacerlo único
            original_slug = self.slug
            counter = 1
            while Car.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)



class Publisher(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.TextField(max_length=200)
    birth_date = models.DateField()
    slug_author = models.SlugField(unique=True, blank=True, null=True)
    biography = models.TextField(max_length=500, null=True, blank=True)
    website = models.URLField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug_author:
            self.slug_author = slugify(self.name)

            counter = 1
            original_slug = self.slug_author
            while Author.objects.filter(slug_author = self.slug_author).exclude(pk=self.pk).exists():
                self.slug_author = f"{original_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)
    

    def __str__(self):
        return self.name

class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    website = models.URLField()
    biography = models.TextField(max_length=500)

class Book(models.Model):
    title = models.TextField(max_length=200)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name="authors")
    def __str__(self):
        return self.title
    
class Moto(models.Model):
    title = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title