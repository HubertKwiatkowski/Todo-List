from pprint import pprint
import os
from django.core.management.base import BaseCommand, CommandError
import datetime
from todolist.models import *
from glob import glob
from pprint import pprint
from invoice.ppbon import bon2dict, dict2xml
from pprint import pprint
import time
from django.conf import settings


class Command(BaseCommand):
    help = 'test html bonnen'

    def add_arguments(self, parser):
        pass
        #parser.add_argument('order_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        order = Order.objects.get(pk=8)
        print(order)
        print('--')
        for address in DeliveryAddress.objects.filter(invoice=order):
            print(' ', address)
            for parcel in SendcloudParcel.objects.filter(delivery_address=address):
                
                print('1  ', parcel)

            for parcel in address.sendcloudparcel_set.all():
                print('2  ', parcel)

        print('--')
        for address in order.deliveryaddress_set.all():
            print(address)
        print('--')
        

        print(order.status)
        print(Status.objects.filter(id=order.status_id))