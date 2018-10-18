from datetime import datetime
print"what is the date you want to know the day, input yyyymmdd:)"

odate=raw_input()
print"The output 0 represent Monday :P and 1 mean Tuesday... you can +1 then that is the day you want to know:))"
odate = datetime.strptime(odate,'%Y%m%d' ).weekday()
print odate