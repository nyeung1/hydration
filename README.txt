###Quick Hydration Guide
This is a quick guide on how to hydrate tweets. Hydrate is just shorthand for getting the full json form of a tweet from a tweet id (b/c Twitter says you can only share the tweet id).

(1) Fill out the api_keys.json w/ your keys

(2) The input file for the hydration needs to be a singular .txt file w/ one tweet i.d. per line. This is a little inconvinient b/c the tweets come in .tsv files. 

Find a way to export a single column of the .tsv file to a .txt file. I just opened it in spreadsheet software and then copied the entire column lol; I'll write a script that does this later.

(3) Then, we can hydrate the tweets (make sure the keys are in the same file)
python hydrate.py -i some_data.txt -o output_file

I put some ex. files ignore them for now.

Source:
https://github.com/thepanacealab/SMMT/tree/master/data_acquisition