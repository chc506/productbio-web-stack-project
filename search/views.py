#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ahuynh
# @Date:   2015-06-08 09:58:56
# @Last Modified by:   ahuynh
# @Last Modified time: 2015-06-08 10:02:31
from django.shortcuts import render_to_response
import csv


def run_search(request):
    ''' Search through our purchases '''

    query = request.GET.get('q', None)
    value = request.GET.get('v', None)

    if query is None:
        return render_to_response('noquery.html')

    # TODO: Properly handle search query.
    my_item_set, resultSet=searchFor(query,value)
    return render_to_response('query.html',{'query':query, 'value':value, 'rSet':resultSet, 'itemSet':my_item_set})


def csvRead():
    with open(r'sample_data/San Francisco FY14-15.csv', 'r', encoding='utf-8') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        next(csvReader)
        postDate=[]
        vendor=[]
        description=[]
        quantity=[]
        invoiceAmount=[]
        item=[]
        for row in csvReader:
            postDate.append(row[0])
            vendor.append(row[1])
            description.append(row[2])
            quantity.append(row[3])
            invoiceAmount.append(row[4])
            item.append(','.join(row))
        return postDate,vendor,description,quantity,invoiceAmount,item


def searchFor(query, value):
    postDate, vendor, description, quantity, invoiceAmount,item=csvRead()
    my_item_set=[]
    resultSet=[]
    if value=='Post Date':
        counter=0
        for pDate in postDate:
            if pDate.lower().find(query.lower())!=-1:
                my_item_set.append(my_item(postDate[counter],vendor[counter],description[counter],quantity[counter],
                                           invoiceAmount[counter]))
                resultSet.append(item[counter][0:-5])
            counter+=1
        return my_item_set,resultSet
    if value=='Vendor':
        counter=0
        for ven in vendor:
            if ven.lower().find(query.lower())!=-1:
                my_item_set.append(my_item(postDate[counter], vendor[counter], description[counter], quantity[counter],
                                           invoiceAmount[counter]))
                resultSet.append(item[counter][0:-5])
            counter+=1
        return my_item_set,resultSet
    if value=='Description':
        counter=0
        for des in description:
            if des.lower().find(query.lower())!=-1:
                my_item_set.append(my_item(postDate[counter], vendor[counter], description[counter], quantity[counter],
                                           invoiceAmount[counter]))
                resultSet.append(item[counter][0:-5])
            counter+=1
        return my_item_set,resultSet
    if value=='Quantity':
        counter=0
        for quan in quantity:
            if quan.lower()==query.lower():
                my_item_set.append(my_item(postDate[counter], vendor[counter], description[counter], quantity[counter],
                                           invoiceAmount[counter]))
                resultSet.append(item[counter][0:-5])
            counter+=1
        return my_item_set,resultSet
    if value=='Invoice Amount':
        counter=0
        for inAmt in invoiceAmount:
            if inAmt.lower().find(query.lower())==3:
                my_item_set.append(my_item(postDate[counter], vendor[counter], description[counter], quantity[counter],
                                           invoiceAmount[counter]))
                resultSet.append(item[counter][0:-5])
            counter+=1
        return my_item_set,resultSet

class my_item(object):
    def __init__(self, pDate, vendor, description, quantity, invAmt):
        self.pDate = pDate
        self.vendor = vendor
        self.description=description
        self.quantity=quantity
        self.invAmt=invAmt
