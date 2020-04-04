import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import pprint
from textblob import TextBlob
import os
import pprint

from twarc import Twarc

from m3inference import M3Twitter
from m3inference import get_lang

PATH = "/Users/neilyeung/Desktop/DM_Final_Proj/data/testing/"
with os.scandir(PATH) as it:
    # Get the names of the files that end with .tsv
    for entry in it:
        if entry.name.endswith(".tsv") and entry.is_file():
            df = pd.read_csv(PATH + entry.name, delimiter='\t')
            tweet_ids = list(df['tweet_id'])

            # regex to get everything up to but not including .tsv
            match = re.search(r"^.*(?=(\.tsv))", entry.name)
            print(tweet_ids)

            # outputs .txt file w/ same name as .tsv file
            with open(match.group() + ".txt", "w+") as file:
                for i in tweet_ids:
                    file.write(str(i))
                    file.write("\n")
