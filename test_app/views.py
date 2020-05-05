import os

from django.shortcuts import render
from django.http import HttpResponse
from faker import Faker
import random
import string
import sqlite3


fake = Faker()

# Create your views here.
def hello(request):
    result = []
    for _ in range(100):
        name = fake.name()
        email = fake.email()
        result.append({'name': name, 'email': email})
#    print(request.GET)
    return HttpResponse(result)

def gen_password(request):
    def_length = 10
    if 'length' not in request.GET:
        return HttpResponse(("length", 400))
    length = int(request.arg.get['length'])
    digits = int(request.arg.get('digits', 0))
    specials = int(request.arg.get('special', 0))
    generation_symbols = string.ascii_lowercase
    if digits == 1:
        generation_symbols += string.digits
    if specials == 1:
        generation_symbols += '!@#$!%^&*()'
    """ /gen-password?length=5 Передаем значение от клиента """
    # length = int(request.args.get('length', def_length)
    """ Возвращаем строку как результат генерации списка """
    print(request.GET)
    return HttpResponse(''.join([random.choice(generation_symbols) for _ in range(length)]))


def get_customers(request):
    city = request.GET('state', '')
    query = 'SELECT FirstName, LastName  FROM customers WHERE Cit'
    records = execute_query(query, city)
    result = '<br>'.join([str(record) for record in records])
    return HttpResponse(result)

def get_price():
    query = f'SELECT sum(UnitPrice * Quantity) FROM invoice_items'
    records = execute_query(query)
    result = str(records[0][0])
    return HttpResponse(result)


def execute_query(query, *args):
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(query, args)
    record = cur.fetchall()
    return HttpResponse(record)


