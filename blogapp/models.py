#from django.db import models

from mongoengine import *
from cocobongo.settings import DBNAME

connect(DBNAME)

class Post(Document):
	title = StringField(max_length=120, required=True)
	content = StringField(max_length=500, required=True)
	last_updated = DateTimeField(required=False)

# Create your models here.
