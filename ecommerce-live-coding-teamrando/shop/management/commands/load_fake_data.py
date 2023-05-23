from django.core.management.base import BaseCommand, CommandError, CommandParser
from shop.models import Product
from faker import Factory

faker = Factory.create()

class Command(BaseCommand):
    help = "create some fake products for our store"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('number', nargs='+', type=int)

    def handle(self, *args, **options):
        number = options.get('number', [1000])[0]

        for i in range(number):
            print(f'Product number {i}')
            Product.objects.create(
                name=faker.word(), 
                description=faker.text(),
                price = faker.random_number(digits=2)
                )
        self.stdout.write(self.style.SUCCESS("Successfully created some fake data..."))