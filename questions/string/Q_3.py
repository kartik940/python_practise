# pragoramm to greet Good Morning, Good After noon and Good evening.
import time
t = time.strftime('%H:%M')
hour = int(time.strftime('%H'))
print(hour)

if hour<12:
    print("Good Mornig")
elif hour>12<17:
    print("good Evening")
elif hour>17>23:
    print("good Night, Have a nice dream")