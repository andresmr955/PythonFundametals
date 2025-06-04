# coding: utf-8
from my_first_app.models import Book, Publisher, Author, Profile
author = Author.objects.first()
author
profile = Profile(website="https://example.com", biography="lorem ipsum", authot=author)
profile = Profile(website="https://example.com", biography="lorem ipsum", author=author)
profile.save()
Author.objects.count()
Author.objects.first()
Author.objects.last()
get_ipython().run_line_magic('pinfo2', 'Author')
Author.objects.create(name="luis martinez", birth_date="1999-01-09" )
