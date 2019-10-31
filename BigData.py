#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:25:34 2019

@author: cristiancepeda
"""


# Dear friend... 
# When I wrote this code, just God and me knew how this works
# Now... Only god knows

import pandas as pd
import numpy as np
from pyspark.sql import SparkSession
#spark=SparkSession.builder.getOrCreate()
#from pyspark import SparkConf, SparkContext
#sc=SparkContext()


df=pd.read_csv("Tweets.csv")
selectedcolumns=df.loc[:,["text","tweet_created"]]
hashtags=selectedcolumns["text"].str.findall(r'#.*?(?=\s|$)')
Eachhashtag=[]
for allhashtags in hashtags.values:
    if len(allhashtags)>0:
        for hashtag in allhashtags:
            Eachhashtag.append(hashtag)
HashtagsDF=pd.DataFrame(data=Eachhashtag,columns=["Hashtag"])
counts=HashtagsDF["Hashtag"].value_counts()
datab=np.column_stack((counts.index,list(counts)))
Result=pd.DataFrame(data=datab,columns=["Hashtag","Frequency"])
TenMoreUsed=Result.head(11)
FilterTenMoreUsed=TenMoreUsed.drop(0)
