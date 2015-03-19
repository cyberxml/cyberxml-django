from django.core.management.base import BaseCommand, CommandError
from cvrf.imports import *

class Command(BaseCommand):
    help = 'Imports Red Hat CVRF'

    def handle(self, *args, **options):
		try:
			import_redhat_cvrf()
		except:
			raise CommandError('import_redhat_cvrf failed')
		
		self.stdout.write('Successfully imported Red Hat CVRF')