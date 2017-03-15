"""结合时区的日期操作"""

# 涉及到时区问题，使用pytz模块

from datetime import datetime

from pytz import timezone

d = datetime(2012, 12, 21, 9, 30, 0)
print(d)

# localize the date for Chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

#  Convert to Bangalore time
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)
