#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ahuynh
# @Date:   2015-06-08 09:58:56
# @Last Modified by:   ahuynh
# @Last Modified time: 2015-06-08 10:02:31
from django.shortcuts import render_to_response


def run_search( request ):
    ''' Search through our purchases '''

    query = request.GET.get( 'q', None )

    if query is None:
        return render_to_response( 'noquery.html' )

    # TODO: Properly handle search query.
    return render_to_response( 'query.html' )
