from pprint import pprint

def check_level(report):
    increasing = report[0] > report[1]  ## When 5 10 -> False when 10 5 True
    for c in range(1, len(report)):
        if ((report[c - 1] > report[c]) != increasing) or not (0 < abs(report[c - 1] - report[c]) < 4):
            return False
    return True

def check_level_with_dampener(report):
    for x in range(0,len(report)):
        report_cp = report.copy()
        del report_cp[x]
        if check_level(report_cp):
            return True
    return False

reports = []
with open('input.txt', 'r') as file:
    for line in file:
        if len(line) > 2:
            report = [int(level.strip()) for level in line.split(" ")]
            reports.append(report)


count_safe = 0
for report in reports:
    if check_level(report):
        count_safe += 1
    elif check_level_with_dampener(report):
        count_safe += 1
print('SaveReports',count_safe)
print('UnsaveReports',len(reports)-count_safe)