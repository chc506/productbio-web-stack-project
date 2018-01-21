#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ahuynh
# @Date:   2015-06-08 09:58:56
# @Last Modified by:   ahuynh
# @Last Modified time: 2015-06-08 10:02:31
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
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
			s = set(row.values())
			if len(s) == 1 and '' in s: # ignore all the trailing empty records
				print ("empty records")
				break
			valid = True
			for k, v in zip(attributes, request):
				if not v: # ignore empty search
					continue
				if not row[k]: # ignore empty records
					valid = False
					continue
				if k == 'INVOICE AMT': # compare the price (should be in range low - high)
					prices = v.split('-')
					if len(prices) == 2:
						low, high = prices[0], prices[1] # low, high, range inquiry
					else:
						low = high = prices[0] # accurate fit
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
				elif v.lower() not in row[k].lower(): # for other search keys, check if searched value is the substring of the record
					valid = False
					break
			if valid:
				row['INVOICE_AMT'] = row['INVOICE AMT']
				row.pop('INVOICE AMT')
				row['POST_DATE'] = row['POST DATE']
				row.pop('POST DATE')
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

def redirect_root(request):
	return HttpResponseRedirect('/search')
