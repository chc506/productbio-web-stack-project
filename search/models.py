#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ahuynh
# @Date:   2015-06-08 09:38:58
# @Last Modified by:   ahuynh
# @Last Modified time: 2015-06-08 09:58:44
from django.db import models


class Purchase( models.Model ):
    ''' Represents a purchase order at an organization '''

    id           = models.AutoField( primary_key=True )
    date         = models.DateField( blank=True )

    # About the vendor
    vendor       = models.CharField( max_length=128, db_index=True,
                                     blank=True, null=True)

    # About the product
    name         = models.TextField(blank=True, null=True, db_index=True )
    description  = models.TextField(blank=True, null=True)
    category     = models.TextField(blank=True, null=True, db_index=True )

    # Cost/quantity
    quantity     = models.FloatField(blank=True, null=True, default=1.0 )
    cost         = models.FloatField(blank=True, null=True, default=0.0 )
