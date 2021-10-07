# creator: A NOOB programmer
__authur__="MES"

from urllib.parse import urlsplit
from urllib.parse import urlparse
from collections import deque
from bs4 import BeautifulSoup
import requests
import requests.exceptions
import sys
import os
import pymongo as py

class cralwe:
    
    def __init__(self,domain):
        self.client=py.MongoClient(port=27017) 
        self.db_instance=self.client["urls"]
        self.col_instance=self.db_instance["urls_information"]
        self.db_lists=self.client.list_database_names()
        self.exceptions=requests.exceptions.MissingSchema,\
        requests.exceptions.ConnectionError, requests.exceptions.InvalidURL,\
        requests.exceptions.InvalidSchema
        self.urls_unfinished=deque([domain])
        self.urls_finished=set()
        self.urls_internal=set()
        self.urls_external=set()
        self.urls_failed=set()
        self.document=list()
        self.counter=0

    def chech_db(self):
        if "urls" in self.db_lists:
            return True
        else:
            return False

    def connect_to_db(self):
        self.db_instance=self.client.urls
        self.col_instance=self.db_instance.urls_information

    def create_db(self):
        self.db_instance=self.client["urls"]
        self.col_instance=self.db_instance["urls_information"]

    def insert_to_db(self,document):
        self.col_instance.insert_one(self.document)





        
domain="www.google.com"
init=cralwe(domain)
