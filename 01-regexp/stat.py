import re

composers = {}
file = open("scorelib.txt", "r", encoding="utf8")
r_composer = re.compile(r"Composer: (.*)")
for line in file:
    match = r_composer.match(line)
    if match:
        #print(match.group(1))
        sd = match.group(1).strip()
        sd = re.sub(r'\(\S+\)', '', sd).strip()
        if sd in composers:

            pocet = int(composers.get(sd))
            composers.update({sd: pocet+1})
        else:
            composers.update({sd: 1})

for key,value in composers.items():
    print("{} {}".format(key,value))

