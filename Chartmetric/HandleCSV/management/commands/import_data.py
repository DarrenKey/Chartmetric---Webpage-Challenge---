
import csv
import sys
from django.core.management.base import BaseCommand, CommandError
from HandleCSV.models import Account
import os

#Get path to sampledata
currentfolder = os.path.dirname(os.path.abspath(__file__))
csvfilepath = os.path.join(currentfolder, 'sampledata.csv')

#increase csv file limit to handle the csv data
csv.field_size_limit(sys.maxsize)

#command
class Command(BaseCommand):
    def handle(self, *args, **options):

        #open file
        with open(csvfilepath, 'r') as csvfile:
            csvdict = csv.DictReader(csvfile)


            for row in csvdict:
                account = Account()
                account.account_id = row['account_id']
                account.content = row['content']

                #handle dates   
                account.timestamp = row['timestp'] 
                account.created_at = row['created_at'] 
                account.modified_at = row['modified_at'] 
                account.save()