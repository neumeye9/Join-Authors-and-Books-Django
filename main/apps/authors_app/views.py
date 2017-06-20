# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import Authors
from models import Books

# Create your views here.

def index(request):
    Authors.objects.create(first_name="Theodore", last_name="Seuss")
    Authors.objects.create(first_name="Jane", last_name="Austen")
    authors = Authors.objects.all()
    print authors 
    for author in authors:
        print author.first_name, author.last_name, author.id
    

    Books.objects.create(title="The Cat in the Hat", published_date="1957-03-12", category="Children's Literature", in_print=True, author_id=1)
    Books.objects.create(title="Green Eggs and Ham", published_date="1960-08-12", category="Children's Literature", in_print=True, author_id=1)
    Books.objects.create(title="Pride and Prejudice",published_date="1813-01-28", category="Novel", in_print=True, author_id=2)

    books = Books.objects.all()
    print books

    for book in books:
        print book.title, book.author.id

    return render(request, 'authors_app/index.html')