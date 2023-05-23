from django.core.management.base import BaseCommand, CommandError, CommandParser
from shop.models import Product
from faker import Factory
import time

faker = Factory.create()

class Command(BaseCommand):
    help = "Delete all products"
    
    def handle(self, *args, **options):
        Product.objects.all().delete()        
        self.stdout.write(self.style.SUCCESS("Successfully deleted all products"))