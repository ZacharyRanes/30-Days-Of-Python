from datetime import datetime, date

# Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
print(now)

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
t = now.strftime('%m/%d/%Y, %H:%M:%S')
print(t)

# Today is 5 December, 2019. Change this time string to time.
t = now.strftime('%d %B, %Y.')
print("Today is", t)

# Calculate the time difference between now and new year.
today = date(year=now.year, month=now.month, day=now.day)
new_year = date(year=now.year + 1, month=1, day=1)
time_left_for_newyear = new_year - today
print(time_left_for_newyear.days, "days left to new years.")

# Calculate the time difference between 1 January 1970 and now.
today = date(year=now.year, month=now.month, day=now.day)
start_of_time = date(year=1970, month=1, day=1)
time_that_has_passed = today - start_of_time
print(time_that_has_passed.days, "days have past since the start of time.")
