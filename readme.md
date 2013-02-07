What this does
-----------------------------------------
You have all of your snippets on snipplr.com and want to move them over to GitHub Gist. This little script lets you do that. 


How
-----------------------------------------
Fill in your login credentials in main.py, then run it: `python main.py`



Credits
-----------------------------------------
I haven't done much. Just grabbed two useful libraries, `gisty` and `SnipplPy`, hacked them a little and make them work together. Credits to the creators of the two libraries. 




Examples
-----------------------------------------


1) export all stuff from Spipplr


	In [1]: from SnipplrPy import *

	In [2]: c = SnipplrPy()

	In [3]: c.setup("22b3asd66b77571efec")
	Out[3]: True

	In [4]: snippets = [x for x in c.list()]

	In [9]: c.get(24953)
	Out[9]: 
	{'comment': 'Generates a random number from 1 to 200 step 1.',
	 'created': '2009-12-17 10:40:46',
	 'id': '24953',
	 'language': 'Python',
	 'snipplr_url': 'http://snipplr.com/view/24953/random-number-generator-in-python',
	 'source': 'import random\nprint random.randrange(1,200,1)',
	 'tags': 'number python random generator console ',
	 'title': 'Random number generator in Python.',
	 'updated': '2012-10-01 03:13:46',
	 'user_id': '15912',
	 'username': 'louscomp'}

etc...






2) grab the useful data and post it to github gist

	In [1]: from gisty import *

	In [2]: gist_list("name", "password")
	https://gist.github.com/3808121 - [u'new_gist.py'] 'Python: take input from stdin and create a new public gist with it'
	https://gist.github.com/3807911 - [u'base.html'] 'Html: base'
	https://gist.github.com/3096854 - [u'Tractatus-rgraph.js'] 'RGraph for Tractatus visualization'
	https://gist.github.com/9c0263e2e5e07e6eddb0 - [u'Scheme load rss into Impromptu 2 ', u'Scheme: load rss into Impromptu 2 ', u'Scheme.scm'] 'Scheme: load rss into Impromptu'

	In [3]: gist_post_console("test.py", "define (x)", True, "magicrebirth", "zabiz99")
	Posting gist as magicrebirth
	Posted to https://gist.github.com/3808191
	Git pull: git://gist.github.com/3808191.git
	Git push: git@gist.github.com:3808191.git



