class LogSystem(object):
    def __init__(self):
        self.logs = []

    def put(self, tid, timestamp):
        self.logs.append((tid, timestamp))

    def retrieve(self, s, e, gra):
        index = {'Year': 5, 'Month': 8, 'Day': 11,
                 'Hour': 14, 'Minute': 17, 'Second': 20}[gra]
        start = s[:index]
        end = e[:index]
        result = []
        # for tid, timestamp in self.logs:
        #     if start <= timestamp[:index] <= end:
        #         result.append(tid)
        #         # print(str(tid) + "," + str(timestamp))

        # sorted(result)
        # print(result)
        return sorted(tid for tid, timestamp in self.logs
                      if start <= timestamp[:index] <= end)

sln = LogSystem()
sln.put(1, "2017:01:01:23:59:59")
sln.put(2, "2017:01:01:22:59:59")
sln.put(3, "2016:01:01:00:00:00")
print(sln.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"))
# sln.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour")
