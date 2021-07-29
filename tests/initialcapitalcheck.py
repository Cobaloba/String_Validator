# 1) String starts with a capital letter
import re 
captialregpattern = re.compile(r'^[A-Z]')

# Regex to check capital
def initialcapitalcheck(testword):
    return  bool(captialregpattern.match(testword))