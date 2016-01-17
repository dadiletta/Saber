#!/usr/bin/env python
#
import sys

mystr = str(sys.argv[1])
#!/usr/bin/python
print "Content-Type: text/html"
print ""
print "<html>"
print "<h2>CGI Script Output</h2>"
print "<p> " + ("{}".format(mystr)) + "</p>"
print "</html>"