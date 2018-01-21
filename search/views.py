#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ahuynh
# @Date:   2015-06-08 09:58:56
# @Last Modified by:   ahuynh
# @Last Modified time: 2015-06-08 10:02:31
from django.shortcuts import render_to_response
import csv

# Read csv file and search for corresonding attributes
def search_csv( request ):
	request = request.split(',') # the search keys for all the attributes
	attributes = ['POST DATE','VENDOR','DESCRIPTION','QTY','INVOICE AMT']
	res = {'result':[]}
	with open('sample_data/San Francisco FY14-15.csv') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',')
		for row in reader:
			row.pop('') # There is an empty key in the dict
			valid = True
			for k, v in zip(attributes, request):
				if not v: # ignore empty search
					continue
				if not row[k]: # ignore all the trailing empty records..
					valid = False
					break
				if k == 'INVOICE AMT': # compare the price (should be in range low - high)
					low, high = v.split('-') # low, high
					low, high = float(low.replace(',','')), float(high.replace(',',''))
					target = float(row[k].lstrip(' $\t').replace(',',''))
					if target < low or target > high:
						valid = False
						break
				elif k == 'QTY':
					v = v.replace(',','')
					t = row[k].replace(',','')
					if float(v) != float(t):
						valid = False
						break
				elif v not in row[k]: # for other search keys, check if searched value is the substring of the record
					valid = False
					break
			if valid:
				res['result'].append(row)
	return res


def run_search( request ):
    ''' Search through our purchases '''

    query = request.GET.get( 'q', None )
    print(query)

    if query is None:
        return render_to_response( 'noquery.html' )

    # TODO: Properly handle search query.
    m = search_csv(query)
    return render_to_response( 'query.html', m)
