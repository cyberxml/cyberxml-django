from django.core.management.base import BaseCommand, CommandError
from cvrf.libs.adobe import *

class Command(BaseCommand):
    help = 'Import Adobe HTML as CVRF'

    def handle(self, *args, **options):
		try:
			importAdobeHtml()
		except:
			raise CommandError('importAdobeHtml failed')
		
		self.stdout.write('Successfully imported Adobe HTML as CVRF')