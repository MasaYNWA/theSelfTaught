import re

s = "Beautiful is better than ugly."

match = re.findall("Beautiful", s)

print(match)

match2 = re.findall("beautiful", s, re.IGNORECASE)

print(match2)


zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

m = re.findall("^If", zen, re.MULTILINE)
print(m)

string = "Two too"
m2 = re.findall("t[wo]o", string, re.IGNORECASE)

print(m2)

s2 = "123 hi 34 hello"
m3 = re.findall("\d", s2)

print(m3)

s3 = "__one__ __two__ __three__"
m4 = re.findall("__.*?__", s3)

for reex in m4:
    print(reex)

    import re

line = "i love $"
matching = re.findall("\\$", line, re.IGNORECASE)
print(matching)
