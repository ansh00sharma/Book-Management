from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse, HttpResponse , HttpResponseServerError
from django.core import serializers
from django.conf import settings
import string
import os
import hashlib
from django.views.generic.edit import CreateView
from django.views.decorators.http import require_POST
import requests
import os.path
from django.views.decorators.csrf import csrf_exempt
from myapp.services.usertable_connection import DataBase
from myapp.models import user_table
from myapp.models import book_table
import json
import bcrypt



