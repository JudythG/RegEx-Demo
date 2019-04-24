import re

def classDemo():
    # pull out both names
    line = "Jack and Jill"
    p = re.compile(' and ')
    m = p.search(line)
    if m:
        print (line[:m.start()])	# Jack
        print (line[m.end():])		# Jill

    # pull out both names using group
    # [a-zA-Z] is a pattern that matches either a lower or uppercase character
    # [a-zA-Z]+ matches one or more lower or uppercase characters
    p = re.compile('([a-zA-Z]+)( and )([a-zA-Z]+)')
    m = p.search(line)
    if m:
        print (m.group(1))	# Jack
        print (m.group(3))	# Jill

    # use group but ' and ' not in a group
    p = re.compile('([a-zA-Z]+) and ([a-zA-Z]+)')
    m = p.search(line)
    if m:
        print (m.group(1))	# Jack
        print (m.group(2))	# Jill

    # replace ' ' with '\s' - more general whitespace
    pattern = '([a-zA-Z]+)\sand\s([a-zA-Z]+)'
    p = re.compile(pattern)
    m = p.search(line)
    if m:
        print (m.group(1))	# Jack
        print (m.group(2))	# Jill

    # show that pattern works for names other than Jack and Jill
    line2 = "Thelma and Louise"
    p = re.compile(pattern)
    m = p.search(line2)
    if m:
        print(m.group(1))
        print(m.group(2))
    else:
        print ('why no thelma and louise?')

    # now lets use spearators other than 'and'
    pattern = '([a-zA-Z]+)\s[a-zA-Z]+\s([a-zA-Z]+)'

    line2 = "Thelma and Louise"
    p = re.compile(pattern)
    m = p.search(line2)
    if m:
        print(m.group(1))
        print(m.group(2))
    else:
        print ('why no thelma and louise?')

    line2 = "Darcy or Fitzwilliam"
    p = re.compile(pattern)
    m = p.search(line2)
    if m:
        print(m.group(1))
        print(m.group(2))
    else:
        print ('why no Darcy or Fitzwilliam?')

    # phone number (###) ###-####
    phone_pattern = '\(\d\d\d\) \d\d\d-\d\d\d\d'
    p = re.compile(phone_pattern)
    line = ' (202) 456-1111 The White House Phone'
    m = p.search (line)
    if m:
        print (line[m.start():m.end()])
    else:
        print ('no phone match')

    print ()

# main

classDemo()
