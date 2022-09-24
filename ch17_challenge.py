import re

line = "the ghost that says boo haunts the loo"
match = re.findall(".oo", line, re.IGNORECASE)
print(match)