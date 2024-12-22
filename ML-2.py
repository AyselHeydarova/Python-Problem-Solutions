data = open("test-2.txt", "r").read().splitlines()

print("data", data)
reports = []

for i in data:
    report = list(map(int, i.split()))
    reports.append(report)

print("reports", reports)

def isIncreasing(report) -> bool:
    for i in range(0, len(report) - 1):
        if not report[i] < report[i+1]:
            return False

    return True

def isDecreasing(report) -> bool:
    for i in range(0, len(report) - 1):
        if not report[i+1] < report[i]:
            return False
                     
    return True


def checkReportSafety(report) -> bool:
     for i in range(0, len(report) - 1):
         differ = abs(report[i+1] - report[i])
         isDifferCorrect = differ >= 1 and differ <= 3

         if not isDifferCorrect:
            return False
     return True

safeCount = 0

def isSafe(report) -> bool:
    return checkReportSafety(report) and (isIncreasing(report) or isDecreasing(report))

for report in reports:
    if isSafe(report):
          safeCount+=1
    else:
      for i in range(0, len(report)):
          modifiedReport = report[:i] + report[i+1:]
          if isSafe(modifiedReport):
              safeCount+=1
              break

print("safeCount", safeCount)