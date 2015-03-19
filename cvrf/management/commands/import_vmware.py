from django.core.management.base import BaseCommand, CommandError
from cvrf.libs.vmware import *

class Command(BaseCommand):
    help = 'Import VMware HTML as CVRF'

    def handle(self, *args, **options):
		try:
			importVmwareHtml()
		except:
			raise CommandError('importVmwareHtml failed')
		
		self.stdout.write('Successfully imported VMware HTML as CVRF')