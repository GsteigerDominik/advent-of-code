import re
from pprint import pprint

page_ord_rules = []
page_ord = []
with open('input.txt', 'r') as file:
    for line in file:
        if line.count('|') > 0:
            page_ord_rules.append(line.strip())
        elif line == '\n':
            print('EMPTY')
        else:
            page_ord.append(line.strip())
pprint(page_ord_rules)
pprint(page_ord)
count = 0
broken_pages = []
for p in page_ord:
    broken = False
    for rule in page_ord_rules:
        left, right = rule.split('|')
        x = re.search(f'(?<={right})(.*)(?={left})', p)
        if x is not None:
            broken = True
    if not broken:
        sp = p.split(',')
        count +=  int(sp[len(sp) // 2])
    else:
        broken_pages.append(p)
print('Count',count)
pprint(broken_pages)
fixed_pages=[]
for page in broken_pages:
    sp = page.split(',')
    broken = True
    while broken:
        broken = False
        for rule in page_ord_rules:
            left, right = rule.split('|')
            x = re.search(f'(?<={right})(.*)(?={left})', ",".join(sp))
            if x is not None:
                broken = True
                sp[sp.index(left)], sp[sp.index(right)] = sp[sp.index(right)], sp[sp.index(left)]
    fixed_pages.append(",".join(sp))
count = 0
print(fixed_pages)
for page in fixed_pages:
    sp = page.split(',')
    count += int(sp[len(sp) // 2])
    print(int(sp[len(sp) // 2]))
print('CountOfBroken',count)