import click
from pyfiglet import Figlet
import os
from app.formating_excel import FormatingExcel
from termcolor import colored


f = Figlet(font='slant')
print (colored(f.renderText('iPrice'), 'green'))
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--s', prompt='Type any string' , type = str, help="*required must need valid sring")
def main(s):
    """
    This script accepts string and does the following to it:
        \n 
        - converts the string to uppercase and outputs it to stdout.
        \n
        - converts the string to alternate upper and lower case and outputs it to stdout.
        \n
        - creates a CSV file from the string by making each character a column in the CSV and then output "CSV created!" to stdout.
        
        \n
        For Instance:
        \n
            iprice --s='your string'

    """
    click.secho(_toProccesUpperCase(s), fg='green')
    click.secho(_stringAltering(s), fg='green')
    proccess_string = FormatingExcel(s)
    proccess_string.format_excel()


def _toProccesUpperCase(string):
    return string.upper()
  

def _stringAltering(string):
    if len(string) == 0:
        return string
    elif (len(string)-1) % 2 :
        return string[0].upper()+ _stringAltering(string[1:]) 
    else:
        return string[0].lower()+ _stringAltering(string[1:])

