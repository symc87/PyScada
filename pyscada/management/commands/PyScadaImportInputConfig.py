#!/usr/bin/python
# -*- coding: utf-8 -*- 
import os,sys
from pyscada.utils import update_input_config
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = 'filename'
    help = 'import variable config from json file'

    def handle(self, *args, **options):
        if len(args) < 1:
            self.stdout.write('usage: python manage.py  PyScadaImportInputConfig "jsonfile.json" \n', ending='')
        elif len(args) == 1:
            json_data = file(os.path.abspath(args[0]))
            update_input_config(json_data.read().decode("utf-8-sig"))
            json_data.close()
        else:
            self.stdout.write('usage: python manage.py  PyScadaExportData "outputfile.mat" 100 400\n', ending='')