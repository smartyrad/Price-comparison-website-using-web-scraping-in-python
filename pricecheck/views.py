# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from shopclues import *
from amazon_india import *
from amazon_global import *


data = []


# Create your views here.


def pricecheck(request):
    return render(request, 'pricecheck/index.html', {})


def search(request):
    if 'query' in request.POST:
        del extracted_data_amazon_india[:]
        del extracted_data_amazon_main[:]
        del extracted_data_shopclues[:]
        hello = str(request.POST['query'])
        data = hello.split(",")
        i = 0
        while i < len(data):
            print "Inside link no" + str(i)
            Initial_shopclues(data[i])
            initialamazon_main(data[i])
            initialamazon_India(data[i])
            i = i + 1
        print "Hello finally out"
        print extracted_data_amazon_main
        print extracted_data_shopclues
        print extracted_data_amazon_india
        datamatch=zip(extracted_data_amazon_india,extracted_data_shopclues,extracted_data_amazon_main)
        context = {'datamatch':  datamatch}
        return render(request, 'pricecheck/results.html', context)
    else:
        hi = "No query detected!!"
        return HttpResponse('<h1>' + message + '</h1>')
