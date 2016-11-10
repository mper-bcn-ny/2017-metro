# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 15:31:25 2016

@author: walter tietze
"""

import requests
import json

"""
    Class TxtWerkClient gives access to the Txt Werk service (see http://www.txtwerk.de/ ).
"""
class TxtWerkClient:

    debug = False
    txturl = "https://api.neofonie.de/rest/txt/analyzer"
    entityColor = {"PERSON": "#FF0000", "ORGANISATION": "#0000FF", "PLACE": "#00FF00", "CONCEPT": "#FF00E9", "JOBTITLE": "#CFCFCF", "EVENT": "#CCCC00", "WORK": "#99CCFF"}

    def __init__(self):

        try :
            from txt_werk_apikey import txt_werk
            self.txt_werk = txt_werk
        except ImportError :
            raise RuntimeError("Credentials must be supplied as dict in txt_apike.py. See example_txt_apike.py or use this as a template: txt_werk=dict(apikey='apikey')")

        self.headers = {'X-Api-Key' : self.txt_werk['apikey']}


    def check_text(self, text):

        r = requests.post(self.txturl, data={'text': text, 'services' : 'entities'}, headers=self.headers)
        txt_werk_data = r.json()

        if(self.debug):
            print("Response Code: " + str(txt_werk_data) + "\n")
            self.print_entities(txt_werk_data['entities'])

        return txt_werk_data;


    def check_text_html_annotated(self, text):

        txtResponse = self.check_text(text)
        entities = txtResponse['entities']
        workText = text
        offset = 0
        for entity in entities:
            #print("Entitätarität: " + str(entity))
            modifiedText = self.insert_entity(workText, entity, offset)
            offset = len(modifiedText) - len(text)
            workText = modifiedText

        return workText;


    def insert_entity(self, string, entity, offset):

        start = offset + entity.get('start')
        end = offset + entity.get('end')
        color = self.entityColor.get(entity.get('type'))
        url = entity.get('uri')
        if(url == None):
            url = '#'
            color = "#FF9933"
        return string[:start]+'<a href="' + str(url) + '" target="_blank" style="color:' + color  + ';"><strong>'+string[start:end] +'</strong></a>'+string[end:]
#        return string[:start]+'<a href="' + str(url) + '" style="color:' + self.entityColor.get(entity.get('type'))  + ';"><strong>'+string[start:end] +'</strong></a><div class="box"><iframe src="' + str(url) + '" width = "300px" height = "300px"></iframe>'+string[end:]


    def format_entities(self, entities):

        prettyFormat = ""
        for entity in entities:
            prettyFormat += "[ " + str(entity.get('type')) + ", \""  + str(entity.get('label')) + "\", \"" + str(entity.get('surface')) + "\", " + str(entity.get('uri')) + ", [" + str(entity.get('start')) + "," + str(entity.get('end')) + "], " + str(entity.get('confidence')) + " ]\n" 
        return prettyFormat


    def print_entities(self, entities):

        for entity in entities:
            print("-------------------------------------------")
            print("Uri: " + str(entity.get('uri','')))
            print("Start,Ende: [" + str(entity.get('start',''))+","+str(entity.get('end',''))+"]")
            print("Konfidenz: " + str(entity.get('confidence','')))
            print("Typ: " + str(entity.get('type','')))
            print("Oberflächenform: " + str(entity.get('surface','')))
            print("Label: " + str(entity.get('label','')))
            print("-------------------------------------------")



if __name__=='__main__' :
    text = ("Angela Merkel wurde am 17. Juli 1954 in Hamburg als Angela Dorothea Kasner geboren.")
    txt_werk = TxtWerkClient()
    txtResponse = txt_werk.check_text(text)
    print("\nTxt Werk response:\n\n" + str(txtResponse) + "\n")
    annotatedText = txt_werk.check_text_html_annotated(text)
    print("\nMit HTML annotierter Text:\n\n" + annotatedText + "\n")



