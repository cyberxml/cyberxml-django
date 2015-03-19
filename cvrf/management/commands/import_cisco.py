from django.core.management.base import BaseCommand, CommandError
from cvrf.imports import *

class Command(BaseCommand):
    help = 'Import CISCO CVRF'

    def handle(self, *args, **options):
		try:
			import_cisco_cvrf()
		except:
			raise CommandError('import_cisco_cvrf failed')
		
		self.stdout.write('Successfully imported Cisco CVRF')