#!/usr/bin/env python
# encoding: utf-8

"""
Module that gets stuff from snipplr and posts it into github gist

Edit credentials and run it from the command line: python main.py

#  ps: very quick and dirty hack! 

"""


from gisty import *
from SnipplrPy import *



GHUB_USER = "username"
GHUB_PSW = "password"

SNIPPLR_ID = "23497239472937492734"



# http://stackoverflow.com/questions/2077283/substitute-special-characters-with-html-entities-in-python

from xml.sax.saxutils import escape, unescape
# escape() and unescape() takes care of &, < and >.
html_escape_table = {
    '"': "&quot;",
    "'": "&apos;"
}
html_unescape_table = {v:k for k, v in html_escape_table.items()}

def html_escape(text):
    return escape(text, html_escape_table)

def html_unescape(text):
    return unescape(text, html_unescape_table)





def create_gist_from_snipplr(sn):
    """
    From a snippet dictionary creates the gist dict to be posted

    Note: add more languages as needed...

    """

    try:
        if sn.get("language") and sn.get("language") == 'Python':
            extension = "py"
        elif sn.get("language") and sn.get("language") == 'Django':
            extension = "py"
        elif sn.get("language") and sn.get("language") == 'Bash':
            extension = "bash"
        elif sn.get("language") and sn.get("language") == 'XML':
            extension = "xml"
        elif sn.get("language") and sn.get("language") == 'JavaScript':
            extension = "js"
        elif sn.get("language") and sn.get("language") == 'Scheme':
            extension = "scm"
        else:
            extension = "txt"
        filename = "Snipplr-%s.%s" % (str(sn.get("id")), extension)


        description = sn.get("title", "") or sn.get("comment", "")
        if sn.get("language") and sn.get("language") == 'Python':
            description = "Python: %s" % description
        if sn.get("language") and sn.get("language") == 'Django':
            description = "Django: %s" % description
        if sn.get("language") and sn.get("language") == 'Bash':
            description = "Bash: %s" % description
        if sn.get("language") and sn.get("language") == 'XML':
            description = "XML: %s" % description
        if sn.get("language") and sn.get("language") == 'JavaScript':
            description = "JavaScript: %s" % description
        if sn.get("language") and sn.get("language") == 'Scheme':
            description = "Scheme: %s" % description

        source = html_unescape(sn.get("source", ""))

        gist_post_console(filename, description, source, True, GHUB_USER, GHUB_PSW)

    except:
        print "ERROR! NOT SAVED"




# main app


c = SnipplrPy()
c.setup(SNIPPLR_ID)

snippets = [x for x in c.list()]

# {'updated': {'timezone': '+10:00 EST', 'datetime': <DateTime '20100517T06:41:47' at 10b9df710>}, 'favorite': False, 'id': '34616', 'private': False, 'title': "'Dictionary Comprehensions'"}
# {'updated': {'timezone': '+10:00 EST', 'datetime': <DateTime '20110828T06:35:36' at 10b9df758>}, 'favorite': False, 'id': '54284', 'private': False, 'title': 'Adding custom django package to WSGI settings'}

for s in snippets:
    sn = c.get(s['id'])
    if sn:
        try:
            print "Snippet --%s--" % sn.get("title", "")
        except:
            print "Snippet --%s--" % str(sn.get("id", ""))
        create_gist_from_snipplr(sn)


# Example of Snippet:
# {'username': 'magicrebirth', 'comment': '', 'updated': '2012-10-01 21:45:08', 'user_id': '15738', 'language': 'Python', 'title': 'Ways to Move up and Down the dir structure in Python', 'created': '2011-05-09 23:10:03', 'source': "#Moving up/down dir structure\nprint os.listdir('.') # current level\nprint os.listdir('..') # one level up\nprint os.listdir('../..') # two levels up\n\n\n\n# more complex example:\n# This will walk the file system beginning in the directory the script is run from. It \n# deletes the empty directories at each level\n\nfor root, dirs, files in os.walk(os.getcwd()):\n    for name in dirs:\n        try:\n            os.rmdir(os.path.join(root, name))\n        except WindowsError:\n            print 'Skipping', os.path.join(root, name)", 'snipplr_url': 'http://snipplr.com/view/53250/ways-to-move-up-and-down-the-dir-structure-in-python', 'id': '53250', 'tags': 'file dir os walk '}





