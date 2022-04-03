from pprint import pprint
import os
from typing import ItemsView, List
from django.core.management.base import BaseCommand, CommandError
import datetime
from todolist.models import *
from glob import glob
from pprint import pprint
from pprint import pprint
import time
from django.conf import settings


class Command(BaseCommand):
    help = 'test html bonnen'

    def add_arguments(self, parser):
        pass
        #parser.add_argument('order_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        # tag = Tag.objects.get(pk=1)
        # print(tag)
        # print('--')

        # for task in ListItem.objects.filter(task_name=tag):
        #     print(task)

        # print('-----')


        # task = ListItem.objects.get(pk=1)
        # print(task)
        # print(task.task_start_date)

        # result = ListItem.objects.filter(task_note__contains='sa')
        # print(result)

        # print('-----')
        
        status = Status.objects.all()
        for s in status:
            print(s, s.listitem_set)

        item = ListItem.objects.select_related('task_status').get(id=1)        

        print(item.task_status.status)

        print('-----')

        status = Status.objects.prefetch_related('listitem_set').get(id=1)
        print(status)
        items = status.listitem_set.all()
        print(items)

        for item in items:
            # print(Status.objects.filter(id=order.status_id))
            # print(Status.objects.filter(id=item.status_id))
            print(item, type(item), item.task_done)
            print(item.task_start_date)

        # print('--')
        # for task in ListItem.objects.filter(taskName=task):
        #     print(task.taskStartDate)


""" import os
from django.core.management.base import BaseCommand, CommandError
import datetime
from invoice.models import DeliveryAddress, Order, Invoice, SendcloudParcel, Verzending, Orderregel, Product, Status, SendcloudShippingMethod
from glob import glob
from bs4 import BeautifulSoup
import re
from pprint import pprint
from invoice.ppbon import bon2dict, dict2xml
from pprint import pprint
import time
from django.conf import settings """


        # order = Order.objects.get(pk=8)
        # print(order)
        # print('--')
        # for address in DeliveryAddress.objects.filter(invoice=order):
        #     print(' ', address)
        #     for parcel in SendcloudParcel.objects.filter(delivery_address=address):            
        #         print('1  ', parcel)
        #     for parcel in address.sendcloudparcel_set.all():
        #         print('2  ', parcel)
        # print('--')
        # for address in order.deliveryaddress_set.all():
        #     print(address)
        # print('--')
        
        # print(order.status)
        # print(Status.objects.filter(id=order.status_id))