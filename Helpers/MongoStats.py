#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymongo import MongoClient
import nltk
import csv

if __name__ == '__main__':
    client = MongoClient()
    db = client.ESID
    project_pagecount = {}
    project_wordcount = {}
    everything = db.projects3.find({})
    for pro in everything:
        name = pro["name"]
        if len(project_pagecount)!=0 and name in project_pagecount.keys():
            project_pagecount[name]=project_pagecount[name]+1
        else:
            project_pagecount[name]=1
        tokens = nltk.word_tokenize(pro["text"])
        if len(project_wordcount)!=0 and name in project_wordcount.keys():
            project_wordcount[name] = project_wordcount[name] + len(tokens)
        else:
            project_wordcount[name] = len(tokens)
    print "Writing files"
    with open('res_pagecount3.csv', 'wb') as csvfile:
        res1 = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for item in project_pagecount:
            res1.writerow([item.encode('utf-8').strip(),project_pagecount[item]])
    with open('res_wordcount3.csv', 'wb') as csvfile:
        res2 = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for item in project_wordcount:
            res2.writerow([item.encode('utf-8').strip(),project_wordcount[item]])
    print "Done"
