import argparse
from flask import Flask
from libs.migration.migrate import Migration

argparser = argparse.ArgumentParser(description="Elefense migration CLI")
argparser.add_argument('option', help='Options: <migrate>, <runserver>')
args = argparser.parse_args()

def serve():
    import entrypoint

if args.option == 'runserver':
    serve()

if args.option == 'migrate':
    migration = Migration()
    migration.execute_all_file()