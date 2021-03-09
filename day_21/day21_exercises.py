class Statistics:

    def __init__(self, lst):
        self.lst = lst
        self.mn = min(self.lst)
        self.mx = max(self.lst)
        self.cnt = len(self.lst)
        self.sm = sum(self.lst)

    def count(self):
        return self.cnt

    def sum(self):
        return self.sm

    def min(self):
        return self.mn

    def max(self):
        return self.mx

    def range(self):
        return self.mx - self.mn

    def mean(self):
        return self.sm / self.cnt


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32,
        33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count())  # 25
print('Sum: ', data.sum())  # 744
print('Min: ', data.min())  # 24
print('Max: ', data.max())  # 38
print('Range: ', data.range())  # 14
print('Mean: ', data.mean())  # 30
# print('Median: ', data.median()) # 29
# print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
# print('Standard Deviation: ', data.std()) # 4.2
# print('Variance: ', data.var()) # 17.5
# print('Frequency Distribution: ', data.freq_dist())
# [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33),
# (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
