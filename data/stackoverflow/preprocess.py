import sys
from tqdm import tqdm

source=sys.argv[1]
destination=sys.argv[2]
target_tags=['javascript', 'java', 'python', 'ruby', 'php', 'c++', 'c#', 'go', 'scala', 'swift']

with open(source, "r") as source:
    with open(destination, "w+") as destination:
        for line in tqdm(source):
            if line.count('\t')==1:
                line = line.rstrip('\n').split('\t')
                text = line[0]
                tag = list(set(line[1].split(' ')).intersection(target_tags))
                if len(tag)==1:
                    label = target_tags.index(tag[0]) + 1
                    destination.write("{} |{}\n".format(label,text.replace(":"," ").replace("|"," ")))

