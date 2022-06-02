from Report import Report


import Report
class ReportSet(Report):
    reports = []
    def __innit__(self,reports: Report):
        self.reports = []

    def addReport(reports,report: Report):
        reports.append(report)

    def clearReports(reports):
        reports.clear()

    def removeReport(reports,report: Report):
        reports.remove(report)

    def iterator(reports):
        for x in reports:
            print(x)