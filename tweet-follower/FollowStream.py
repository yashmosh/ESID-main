#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function

import MySQLdb
import json
from StreamThread import StreamThread

from my_settings import *
import time

if __name__ == '__main__':
    print("Hello")
    Threads = []
    while True:
        db = MySQLdb.connect(host, username, password, database, charset='utf8')
        cursor = db.cursor()
        sql_del = "SELECT * FROM social_media_collector.KeyWords where Following=2" #Schedulled to be deleted
        cursor.execute(sql_del)
        results = cursor.fetchall()
        for res in results:
            keywordToDelete = res[1]
            for Th in Threads:
                if Th.keyword == keywordToDelete:
                    Th.stop()
                    Threads.remove(Th)
                    sql2 = "Update social_media_collector.KeyWords set Following=3 where KeyWord='" + res[1] + "'" # deleted
                    cursor.execute(sql2)
                    db.commit()
        sql = "SELECT * FROM social_media_collector.KeyWords where Following=0"
        cursor.execute(sql)
        results = cursor.fetchall()

        for res in results:
            st = StreamThread(res[1])
            st.start()
            Threads.append(st)
            sql2 = "Update social_media_collector.KeyWords set Following=1 where KeyWord='"+res[1]+"'"
            cursor.execute(sql2)
            db.commit()
        time.sleep(60)
        cursor.close()
        db.close()
