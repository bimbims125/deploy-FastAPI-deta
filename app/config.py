import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
conn = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')
