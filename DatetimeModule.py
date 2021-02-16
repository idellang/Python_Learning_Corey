import datetime

# naive dates dont have enough information like timezones
# aware do have enough information

d = datetime.date(2016, 7, 24)
print(d)

tday = datetime.date.today()
print(tday)

# grab year
# print(tday.year())
print(tday.isoweekday())

# time deltas are difference between times
# useful for operations

tdel = datetime.timedelta(days=7)
print(tday + tdel)

bday = datetime.date(2021, 12, 5)
till_bday = bday - tday

print(till_bday.total_seconds())

t = datetime.time(9, 30, 45, 10000)
print(t.hour)

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt)
print(dt.time())
print(dt.date())
print(dt.year)

# compute for date 12 hours into the future
tdelta = datetime.timedelta(hours=12)
print(dt + tdelta)

# alternative constructors
dt_today = datetime.datetime.today()  # local datetime with no timezone
dt_now = datetime.datetime.now()
dt_utc_now = datetime.datetime.utcnow()  # current utc time but tz is set to none

print(dt_today)
print(dt_now)
print(dt_utc_now)

# create timezone aware datetime
import pytz

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

# easier to read
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utc_now)

# convert to different timezone

dt_mtn = dt_now.astimezone(pytz.timezone("Hongkong"))
print(dt_mtn)

# for tz in pytz.all_timezones:
#     print(tz)

# datetime to timezone aware
dt_mtn = datetime.datetime.now()
dt_east = dt_mtn.astimezone(pytz.timezone("US/Eastern"))
print(dt_mtn)
print(dt_east)


# save datetime using isoformat
print(dt_mtn.isoformat())

# other formats
print(dt_mtn.strftime("%B %d, %Y"))

# string to datetime
dt_str = "February 16, 2021"

dt = datetime.datetime.strptime(dt_str, "%B %d, %Y")
print(dt)

lambda x: x + 1

l1 = [1, 2, 3, 4, 5]
print(list(map(lambda x: x + 1, l1)))
