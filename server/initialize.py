import sys
import pandas as pd
import json


def initializeDB(db):
    read_tags(db)
    read_taggings(db)
    read_shops(db)
    read_product(db)
    print('---------------------------------------------------------------------------------\n')


def read_tags(db):
    fname = '../data/products.csv'
    reader = pd.read_csv(fname, iterator=True)

    # batch read the csv file in case it is too large for the memory
    batch_size = 10000
    while True:
        try:
            batch = reader.get_chunk(batch_size)
            records = json.loads(batch.T.to_json()).values()
            db.tags.insert(records)
            sys.stdout.write('.')
        except StopIteration:
            print("\nFinish loading tags.csv!\n")
            break


def read_taggings(db):
    fname = '../data/taggings.csv'
    reader = pd.read_csv(fname, iterator=True)

    # batch read the csv file in case it is too large for the memory
    batch_size = 10000
    while True:
        try:
            batch = reader.get_chunk(batch_size)
            records = json.loads(batch.T.to_json()).values()
            db.taggings.insert(records)
            sys.stdout.write('.')
        except StopIteration:
            print("\nFinish loading taggins.csv!\n")
            break


def read_shops(db):
    fname = '../data/shops.csv'
    reader = pd.read_csv(fname, iterator=True)

    # batch read the csv file in case it is too large for the memory
    batch_size = 10000
    while True:
        try:
            batch = reader.get_chunk(batch_size)
            records = json.loads(batch.T.to_json()).values()
            db.shops.insert(records)
            sys.stdout.write('.')
        except StopIteration:
            print("\nFinish loading shops.csv!\n")
            break


def read_product(db):

    fname = '../data/products.csv'
    reader = pd.read_csv(fname, iterator=True)

    # batch read the csv file in case it is too large for the memory
    batch_size = 10000
    while True:
        try:
            batch = reader.get_chunk(batch_size)
            records = json.loads(batch.T.to_json()).values()
            db.products.insert(records)
            sys.stdout.write('.')
        except StopIteration:
            print("\nFinish loading products.csv!\n")
            break
