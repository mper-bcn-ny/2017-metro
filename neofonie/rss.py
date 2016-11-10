# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 15:31:25 2016

@author: walter tietze
"""

import requests
import tempfile
import os
import errno
import json
from pprint import pprint
from os import listdir
from os.path import isfile, join
import feedparser
from boilerpipe.extract import Extractor


#import sys;
#reload(sys);
#sys.setdefaultencoding("utf8")

"""
    Class RSS - Loader for RSS feeds into the temp directory of the system with content extraction.
"""
class RSS:

    def __init__(self, name, rss):

        self.name = name
        self.rss = rss

        self.tmpDir = tempfile.gettempdir()
        self.baseDir = self.tmpDir + "/dpa_hackathon/"
        self.htmlDir = self.baseDir + "/html"
        self.extractDir = self.baseDir + "/extract"
        self.sourceHtml = self.htmlDir + "/" + self.name + "/"
        self.sourceExtract = self.extractDir + "/" + self.name + "/"

        self.checkCreateDir(self.sourceHtml)
        self.checkCreateDir(self.sourceExtract)

    def checkCreateDir(self, directory):

        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except OSError as exception:
                if exception.errno != errno.EEXIST:
                    raise
        return;

    def processPost(self, url):
	
        r = requests.get(url)
        self.writeToFile(url, r.text, True)
        self.updateExtract(url, r.text)
	# r.status_code, r.headers['content-type'], r.encoding, r.text, r.json()
	#    print("Url:", r.url)
	#    print("Nachricht:", r.text)
        return;

    def update(self):

        print("Fetching " + self.rss + "\n")
        d = feedparser.parse(self.rss)

        for post in d.entries:
            if(not self.alreadyProcessed(post.link)):
                print("New Post: "+post.title + "\n\t" + post.link + "\n")
                self.processPost(post.link)
            else:
                print("Skipping Post: " + post.title + "\n\t" + post.link + "\n")

        return;

    def clean(self):
        return;

    def updateExtract(self, url, html): 
        extractor = Extractor(extractor='ArticleExtractor', html=html)
        extracted_text = extractor.getText()
        try:
            #print ("Boilerpipe: ", extracted_text)
            self.writeToFile(url, extracted_text, False)
        except UnicodeEncodeError as exception:
            print("Error writing document for " + url + ":\n" + str(exception))
        return;

    def writeToFile(self, url, text, isHtml):

        filename = self.sourceHtml + "/" + url.replace('/', '_') + ".html"

        if(not isHtml): 
            filename = self.sourceExtract + "/" + url.replace('/', '_') + ".extract"

        #directory = os.path.dirname(filename)
        #print("Writing to " + filename)

        with open(filename, 'w') as fd:
            fd.write(text)
        return;

    def alreadyProcessed(self, url):

        return os.path.exists(self.sourceHtml + "/" + url.replace('/', '_') + ".html");

    def getExtracts(self, limit = -1):

        extracts = []
        extractfiles = [f for f in listdir(self.sourceExtract) if isfile(join(self.sourceExtract, f))]
        # print("Found files:" + str(extractfiles))

        for extractfile in extractfiles:
            with open(self.sourceExtract + "/" + extractfile, 'r') as f:
                extract = f.read()
                #print("Loaded extract:" + extract)
                extracts.append(extract)
                f.close()

        print("Anzahl an Extrakten: " + str(len(extracts)))
        #print("Type " + str(type(extracts)))
        if limit > 0:
            extracts = extracts[:limit]
        return extracts;


#map(lambda post: printEntry(post), d.entries)


if __name__=='__main__' :

    presseportal = RSS("presseportal", "http://www.presseportal.de/rss/presseportal.rss2")
    presseportal.update()

    spiegelTop = RSS("spiegelTop", "http://www.spiegel.de/schlagzeilen/tops/index.rss")
    spiegelTop.update()

    spiegelEil = RSS("spiegelEil", "http://www.spiegel.de/schlagzeilen/eilmeldungen/index.rss")
    spiegelEil.update()

    spiegel = RSS("spiegel", "http://www.spiegel.de/schlagzeilen/index.rss")
    spiegel.update()

    extracts = presseportal.getExtracts()

    print("Type " + str(type(extracts)))

    if extracts is not None:
        if len(extracts) > 0:
            print("Anzahl an Extrakten: " + str(len(extracts)))
            print("Le Zero: " + str(extracts[0]))
            for extract in extracts:
                print(extract)
    else:
        print("List is None")

