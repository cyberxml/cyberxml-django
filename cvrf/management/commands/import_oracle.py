from django.core.management.base import BaseCommand, CommandError
from cvrf.imports import *

class Command(BaseCommand):
    help = 'Import Oracle CVRF'

    def handle(self, *args, **options):
		try:
			import_oracle_cvrf()
		except:
			raise CommandError('import_oracle_cvrf failed')
		
		self.stdout.write('Successfully imported Oracle CVRF')