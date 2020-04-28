**Original script and article**

 https://towardsdatascience.com/increase-your-instagram-followers-with-a-simple-python-bot-fde048dce20d

 I made a few editions so that it won't track comments. Also added arguments parsing feature, parametrization and a bit of cleaning up.

**Installation** 

 This script uses the following libraries that need to be installed beforehand:
 * pandas
 * selenium

 Just doing a `pip install package` will do.

 The following should be already there in your virtualenv installation:
 * time
 * argparse
 * sys
 * random

*Virtualenv*

 As you might know, a `virtualenv` is always a good idea, so here's how: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

**Usage**

`ig_follow.py -h` 
 
 Will output all the possible flags and arguments. 
 
 *Example run*
 
 `ig_follow.py -d path -u username -p password -n num -a hashtag(s)`
 
 This will use web browser driver in `path` to login to instagram account using `username:password`.

 Then access https://www.instagram.com/explore/tags/`hashtag` and click on the first thumbnail. If the `Follow` button is enabled, then it will click on it and like the photo. 
 
 Finally, it will carry on to the `next` one until `num` of loops is reached.
 
 If more than one `hashtag` is specified as argument, it will repeat the same behavior for each word.