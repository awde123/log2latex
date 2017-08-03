from sys import argv

try:
    argv[1]
except IndexError:
    print("Please designate a log file with first argument")

try:
    argv[2]
except IndexError:
    print("Please designate a destination file with second argument")

with open(argv[1], "r") as f:
    sep = f.read().split("\n")
i = 0
commits = {}
while i < len(sep):
    commit = sep[i].replace("commit ", "")
    commits[commit] = {}
    i += 1
    if "Merge:" in sep[i]:
        i += 1
    commits[commit]["author"] = sep[i].replace("Author: ", "")
    i += 1
    commits[commit]["date"] = sep[i].replace("Date:   ", "")
    i += 2
    while len(sep[i]) != 0:
        commits[commit]["message"] = sep[i].replace("    ", "")
        i += 1
    i += 1

output = []
for i in commits:
    output += [("%s & %s\\\\" % (" ".join(commits[i]["date"].split(" ")[1:4]), commits[i]["message"])).replace("%", "\%")]
print(output)
with open(argv[2], "w") as f:
    f.write("\n".join(output[::-1]) + "\n")
