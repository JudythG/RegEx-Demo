import re

# moving towards parsing titles and authors from the Hugo Awards site
# the exercises here are to parse each line into authors and titles
# the pattern to match titles and authors will build-up in each function
# at the end, check that the new pattern works on all the line variants

# for this exercise, parse out the title, The Stone Sky, 
# and the author, N.K. Jemisin
# 
def parse_title():
    line = 'The Stone Sky, by N.K. Jemisin'

# title and author lines start with whitespace
def start_with_whitespace():
    line = '    The Stone Sky, by N.K. Jemisin'

# add publisher after title
# parse out title, author, and publisher
# Note: may leave publisher in parentheses
# results:
#  Title:     The Stone Sky
#  Author:    N.K. Jemisin
#  Publisher: (Orbit)
# 
# Note: ( and ) are metacharacters
def add_publisher():
    line = '    The Stone Sky, by N.K. Jemisin (Orbit)'

# publishers not just one word i.e (Orbit)
# parse all variants
# results:
# parsing ' (Orbit)' should return 'Orbit' or '(Orbit)'
# parsing '(Uncanny, March/April 2017)' should return 
#    '(Uncanny, March/April 2017)' or 'Uncanny, March/April 2017'
def parse_publishers():
    orbit = ' (Orbit)'
    tor = ' (Tor.com Publishing)'
    uncanny = '(Uncanny, March/April 2017)'
    harper = '(Harper Voyager / Spectrum Literary Agency)'
    twelfth_planet = '(Twelfth Planet Press)'

# adding characters to title pattern
# parse title and author
# the title pattern has new characters: " ( ) -
# results (printed as m.group())
#    ('And Then There Were (N-One)', 'Sarah Pinsker ')
#    ('Binti: Home', 'Nnedi Okorafor ')
def update_title_format():
    line = '"And Then There Were (N-One)," by Sarah Pinsker (Uncanny, March/April 2017)'

# note the comma in the title. Ending title search at a comma won't work
# apparently need to use a negative lookahead assertion
def comma_in_title():
    line = '"Children of Thorns, Children of Water," by Aliette de Bodard (Uncanny, July-August 2017)'

# separator can be ', by' or ', edited by'
def different_separators():
    line = '    Luminescent Threads: Connections to Octavia E. Butler, edited by Alexandra Pierce, and Mimi Mondal (Twelfth Planet Press)'

# main

classDemo()
parse_title()
start_with_whitespace()
add_publisher()
parse_publishers()
update_title_format()
comma_in_title()
different_separators()







