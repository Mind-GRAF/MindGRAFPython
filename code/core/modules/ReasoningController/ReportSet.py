from Report import Report


import Report
class ReportSet(Report):
    reports = []
    def __innit__(self):
        pass

    def addReport(reports,report):
        reports.append(report)

    def clearReports(reports):
        reports.clear()

    def removeReport(reports,report):
        reports.remove(report)

    def iterator(reports):
        for x in reports:
            print(x)