from NewGurnoor import *
import re

aliases = {
    "eng": "Engineering",
    "es": "Earth Science",
    "ms": "Math Science",
    "sa": "Science A",
    "sb": "Science B",
    "ss": "Social Sciences",
    "bs": "Biological Sciences",
    "st": "Science Theaters",
    "education": "Education Classroom Block",
    "pf": "Professional Faculties",
    "ad": "Administration",
    "admin": "Administration",
    "social science": "Social Sciences",
    "ccit": "CCIT",
    "ict": "ICT",
    "ms": "Math Sciences"
}

general = [
    'CCIT',
    'Engineering',
    'Earth Science',
    'Math Sciences',
    'Science Theaters',
    'Science A',
    'Social Sciences',
    'Science B',
    'Biological Sciences',
    'Administration',
    'Professional Faculties',
    'Education Classroom Block',
    'Education Tower',
    'Scurfield Hall',
    'ICT',
    'Math Sciences'
]

def splitNumberAndChar(s):
    pre = list(filter(None, re.split(r'(\d+)', s)))
    final = []
    for i in pre:
        final.append(i.rstrip())
    return final

alternate = ["go to", "get to", "walk to"]

def directionHandler(s):
    token = None
    if ("get" in s or "go" in s) and "from" in s:
        for alt in alternate:
            if alt in s:
                token = s.split(alt)[1].split(" from ")
                break
        if not token:
            token = s.split(" from ")[1].split(" to ")
        startString = splitNumberAndChar(token[0])
        endString = splitNumberAndChar(token[1])
        start = aliases[startString[0].lower().strip()] if startString[0].lower().strip() in aliases else startString[0].lower().strip()
        end = aliases[endString[0].lower().strip()] if endString[0].lower().strip() in aliases else endString[0].lower().strip()
        print("start: '%s' | end: '%s'" % (start, end))

        startFinal = start
        endFinal = end
        if len(startString) > 1:
            floor = str("room %s, floor %s" % (startString[1], startString[1][0]))
            startFinal += " " + floor
        if len(endString) > 1:
            floor = str("room %s, floor %s" % (endString[1], endString[1][0]))
            endFinal += " " + floor
        if start not in general:
            return("Unknown start location: '%s'" % start)
        if end not in general:
            return("Unknown end location: '%s'" % end)
        else:
            path = graph.dijkstra(start.strip(), end.strip())
            if len(path) == 0:
                return("You're in luck - you can walk directly from %s to %s." % (startFinal, endFinal))
            #print(path)
            path.popleft() # ignore first thing
            response = str("First, start at %s then walk to " % (startFinal))
            previous = start
            concat = ['then', 'and']
            concatIdx = 0
            while (len(path) != 1):
                next = path.popleft()
                if concatIdx == 0:
                    response += str("%s. %s from %s, walk to " % (next, concat[concatIdx].title(), next))
                else:
                    response += str("%s, %s from %s, walk to " % (next, concat[concatIdx], next))
                concatIdx = 1 if concatIdx == 0 else 0
            last = path.popleft()
            response += str("%s which is your final destination." % endFinal)
            return(response)
