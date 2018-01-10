import datetime

birthday = "21-Aug-80"
date_format = "%d-%b-%y"

parsed_date = datetime.datetime.strptime(birthday, date_format)

print parsed_date.strftime("%-m/%d/%y") # 8/21/80