# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 15:31:25 2016

@author: walter tietze
"""

from enum import Enum
import feedparser
import requests
from boilerpipe.extract import Extractor
import tempfile
import os
import errno
import json
from pprint import pprint
from os import listdir
from os.path import isfile, join

import urllib
from itertools import chain

"""
Class for request to the solr instance of the News-Stream poject.
"""
class NewsStreamClient:

    default_params = { 'rows': '3', 'wt': 'json', 'indent': 'on'}

    url = "https://nstr.neofonie.de/solr-dev/hackathon/select"

    def __init__(self):

        try :
            from credentials import dpa as auth
            self.auth = auth
        except ImportError :
            raise RuntimeError("Credentials must be supplied as dict in credentials.py. See example_credentials.py or use this as a template: dpa=dict(login='user',password='secret')")
        print("\nUsing as base url for News-Stream: " + self.url + "\n")
        return;

    def merge_params(self, params):

        return dict((k,v) for k,v in chain(self.default_params.items(), params.items()))

    def exec_query(self, params):

        r = requests.get(self.url, auth=(self.auth["login"],self.auth["password"]), params=self.merge_params(params))
        #print (str(r))
        solrdata = r.json()
        #print(json.dumps(solrdata, indent=4))
        return solrdata;


if __name__=='__main__' :
    newsstream = NewsStreamClient()

    res = newsstream.exec_query({ 'q': '"Hillary Clinton" AND "Donald Trump"', 'fq': 'language: en AND sourceId:neofonie', 'fl': 'title', 'sort': 'publicationDate DESC', 'rows': '10' }) 
    #res = newsstream.query( {'q': 'Hillary Clinton', 'wt': 'json', 'rows': '0'}) 
    print("--------------------------------------------------------")
    print(str(res))
    print(str(res['response']))
    [print(x) for x in res['response']['docs']]
    print("--------------------------------------------------------")

    # print(str(newsstream.merge_params({ 'q': '"Hillary Clinton" AND "Donald Trump"', 'fq': 'language: en AND sourceId:neofonie', 'wt':'xml', 'fl': 'title', 'sort': 'publicationDate DESC', 'rows': '10' })))



