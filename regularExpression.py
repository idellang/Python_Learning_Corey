import re


text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
bat
pat
"""

sentence = "Start a sentence and then bring it to an end"

emails = """
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
"""

urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

# re.compile to separate patterns to variable
# [] = character set
# [1-5] means 1 to 5
# [a-zA-z] # all letters
# [^a-zA-Z] not a letter
# ^(\w) starts with word
# group (r|s) : match r or s
pattern = re.compile(r"([89]00)[.-](\d{3})[.-](\d{4})")
pattern2 = re.compile(r"[^b](at)")
pattern3 = re.compile(r"M(\w{1,2})(\W{1,2})(\w+)")
pattern4 = re.compile(r"[a-zA-Z1-9.-]+@(.*).(\w{3})")
pattern5 = re.compile(r"(http)s?:(\W{2})(www.)?((.*).(\w{3}))")
matches = pattern5.finditer(urls)
for match in matches:
    print(match.group(4))

matches_findall = pattern4.findall(emails)
print(matches_findall)

# with open("data.txt", "r") as file:
#     file_content = file.read()
#     matches = pattern.finditer(file_content)
#     for match in matches:
#         print(match)