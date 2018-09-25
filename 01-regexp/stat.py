import re
import sys

#filename = sys.argv[1]
#parameter = sys.argv[2]



composers = {}
centuries = {}
file = open("scorelib.txt", "r", encoding="utf8")
r_composer = re.compile(r"Composer: (.*)")
r_century = re.compile(r"Composition Year: (.*([0-9][0-9][0-9][0-9]))")
for line in file:
    matchcomposer = r_composer.match(line)
    matchcentury = r_century.match(line)
    if matchcomposer:
        if matchcomposer is not None:
            #print(match.group(1))
            mco = matchcomposer.group(1).strip()
            mco = re.sub(r'\(\S+\)', '', mco).strip()
            if mco in composers:
                pocet = int(composers.get(mco))
                composers.update({mco: pocet+1})
            else:
                composers.update({mco: 1})
    if matchcentury:
        if matchcentury is not None:
            # mce = matchcentury.group(2).strip()
            century = int(matchcentury.group(2))//100+1

            if century in centuries:
                pocetskladeb = int(centuries.get(century))
                centuries.update({century: pocetskladeb + 1})
            else:
                centuries.update({century: 1})
print("\nPieces by composer:\n")
for key,value in composers.items():
    print("{} {}".format(key,value))
print("\nPieces in centuries:\n")
for key, value in centuries.items():
    print("{}th century - {}".format(key,value))


