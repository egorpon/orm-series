from django.core.management.base import BaseCommand

class Command(BaseCommand):

    help = 'This script created to greet a user'

    def add_arguments(self, parser):
        
        parser.add_argument('name', type=str,)
        parser.add_argument('--age', nargs='?', type=int, help='Age of user')

    def handle(self, *args, **options):
        
        name = options['name']
        age = options.get('age')
        if age:
            self.stdout.write(f'Welcome {name}. Your age is {age}.')
        else:
            self.stdout.write(f'Welcome {name}. I dont know your age, though.')