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

class crawler:
    
    def __init__(self):
        self.client=py.MongoClient(port=27017) 
        self.db_lists=self.client.list_database_names()
        self.exceptions=requests.exceptions.MissingSchema,\
        requests.exceptions.ConnectionError, requests.exceptions.InvalidURL,\
        requests.exceptions.InvalidSchema
        self.urls_unfinished=deque([domain])
        self.urls_finished=set()
        self.urls_internal=set()
        self.urls_external=set()
        self.urls_failed=set()
        self.document=dict()
        self.document_str=str
        self.counter=0
        self.url=str

        if self.check_db()==True:
            self.connect_to_db()
        else:
            self.create_db()

    def check_db(self):
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

    def insert_to_db(self):
        self.col_instance.insert_one(self.document)

    def create_document(self):
        self.document={'number':self.counter,'url':self.url}
        self.counter = self.counter + 1

    def crawle(self,domain):
        try:
            while len(self.urls_unfinished):
                url=self.urls_unfinished.popleft()
                self.urls_finished.add(url)
                print("----------->> %s" %url)
                
                try:
                    response=requests.head(url)
                except self.exceptions:
                    self.urls_failed.add(url)
                    continue

                if 'content-type' in response.headers:
                    content_type=response.headers["content-type"]
                    if not 'text/html' in content_type:
                        continue

                try:
                    response=requests.get(url)
                except self.exceptions:
                    self.failed_urls.add(url)
                    continue

                parts=urlsplit(url)
                base="{0.netloc}".format(parts)
                strip_base=base.replace("www.", "")
                base_url="{0.scheme}://{0.netloc}".format(parts)
                path=url[:url.rfind('/')+1] if '/' in parts.path else url
                soup=BeautifulSoup(response.text, "lxml")
                self.url=url

                for link in soup.find_all('a'):
                     temp_base = link.attrs["href"] if "href" in link.attrs else ''

                     if temp_base.startswith('/'):
                         local_link = base_url + temp_base
                         self.urls_internal.add(local_link)

                     elif strip_base in temp_base:
                         self.urls_internal.add(temp_base)

                     elif not temp_base.startswith('http'):
                         local_link = path + temp_base
                         self.urls_internal.add(local_link)

                     else:
                         self.urls_external.add(temp_base)

                for i in self.urls_internal:
                    if not i in self.urls_unfinished and not i in self.urls_finished:
                        self.urls_unfinished.append(i)

                self.create_document()
                self.insert_to_db()
                self.document.clear()

        except KeyboardInterrupt:
            sys.exit
        
domain=input("Enter the domain that you want to extract all \
the internal urls in it:\n")
init=crawler()
init.crawle(domain)
