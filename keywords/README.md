**Installation**

 The following need to be installed beforehand:
 * bs4
 * googlesearch

 `pip install package` will do.
 
 The following should be already there in your virtualenv installation:
 * urllib
 * argparse
 * sys
 * collections

*Virtualenv*

 As you might know, a `virtualenv` is always a good idea, so here's how: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

**Usage**

 `script.py -h` will output a full list of available flags.
 
*Example*

`script.py -q word(s) -d tld -l lang -n num -s start -p pause -t top`

This will use google.`tld` to query for `word(s)`. The first `num` results will be processed, from `start` to `last`. 

Then it will scrap each of them and parse all words in them, creating a list to analyse for word appearance.

Finally will show the `top` common words (aka keywords). 
