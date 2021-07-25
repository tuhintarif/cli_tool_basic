import csv
import os
import click

class FormatingExcel(object):
    def __init__(self, string):
        self.string = string

    def format_excel(self):
        BASE_DIR = os.path.dirname(os.path.dirname(__file__)) # This is Base Directory
        file = click.open_file(os.path.join(BASE_DIR, 'result.csv'), 'w')
        writer = csv.writer(file)
        split_string = ','.join(self.string)
        writer.writerow([split_string]) #this line of code is suggested to print to the root directory
        # writer.writerow([item for item in ''.join(self.string)])  #This line of code create each row for each letter.
        click.secho('CSV created!', fg='green')

    def __str__(self) -> str:
        return self.string