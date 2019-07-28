import datetime

days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(n):
	if n % 100 == 0:
		if n % 16 == 0:
			return True
		else:
			return False
	elif n % 4 == 0:
		return True

num_of_sundays = 0

day = 0
year = 1901

start = True

while year <= 2000:
	if is_leap_year(year):
		months[1] = 29
	else:
		months[1] = 28

	for num_days in months:
		day += num_days
		day = day % 7

		if day == 6:
			num_of_sundays += 1

	year += 1

print num_of_sundays

''' Used datetime module to check result.
def how_many_sundays(year):
	num_of_sundays = 0
	months = range(1, 13)
	for month in months:
		date = datetime.datetime(year, month, 1, 0, 0, 0)
		day = date.weekday()
		if day == 6:
			print date
			num_of_sundays += 1
	return num_of_sundays

n = 1901
num_of_sundays_check= 0
while n <= 2000:
	num_of_sundays_check += how_many_sundays(n)
	n += 1
print num_of_sundays_check
'''




	