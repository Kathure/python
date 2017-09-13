import datetime


def bday():
   print "When is your birthday?"
   year = int(raw_input("Year:[YYYY]"))
   month = int(raw_input("Month:[MM]"))
   day = int(raw_input("Day:[DD]"))
   birthday = datetime.datetime(year,month,day)
   return birthday 
   
#def daysaway(dday,today):
#  date1 = dday
#  date2 = datetime.datetime(today.year,dday.month,dday.day)
#  diff = date1 -date2
#  days = int(diff.total_seconds() / 60 / 60 / 24)
#  return days


def compute(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, original_date.month, original_date.day)
    dt = date1 - date2
    days = int(dt.total_seconds() / 60 / 60 / 24)
    return days



def final(days):
  if days < 0:
     print "Your birthday is in %r days" %(-days)
  elif days < 0:
     print "You had your birthday already this year! %r days ago" %(days)
  else:
     print "Happy Birthday!"


#def main():
#   dday = bday()
#   today = datetime.datetime.now()
#   diff = compute(dday,today)
#   final(diff)


def main():
    
    btday = bday()
    now = datetime.datetime.now()
    number_of_days = compute(btday, now)
    final(number_of_days)

main()

