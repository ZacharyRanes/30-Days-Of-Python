"""
The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

Sort the list and find the min and max age
Add the min age and the max age again to the list
Find the median age (one middle item or two middle items divided by two)
Find the average age (sum of all items divided by their number )
Find the range of the ages (max minus min)
Compare the value of (min - average) and (max - average), use abs() method

"""

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
ages.append(ages[-1])
ages.append(ages[0])
ages.sort()
print(ages)
ages_len = len(ages)
med_age = ((ages[ages_len // 2]) + (ages[(ages_len // 2) + (1 - ages_len % 2)]))/2
print(med_age)
avg_age = sum(ages) / len(ages)
print(avg_age)
age_range = ages[-1] - ages[0]
print(age_range)
min_avg = abs(ages[0] - avg_age)
print(min_avg)
max_avg = abs(ages[-1] - avg_age)
print(max_avg)


# Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
big1, big2, big3, *scandic_countries = countries
print(big1)
print(big2)
print(big3)
print(scandic_countries)
