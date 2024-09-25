import datetime

begaining = datetime.date(2024, 8, 23)
current_date = datetime.date.today()
totald = 495
daypassed = current_date - begaining
totalchapter = 75
chapter = int(input("How many chapters have you finished? "))

daypassed_p = (daypassed.days / totald) * 100
completed_chap = (chapter / totalchapter) * 100

print(f"{daypassed_p:.2f}% of the Days have passed")
print(f"{completed_chap:.2f}% of the Chapters have been compleled")

if daypassed_p > completed_chap:
    print(
        """Failure...
        *visible disappointment*
        """
        )
elif completed_chap == 100 and daypassed.days < 100:
    print("Proud to call you my son")    
else:
    print("Keepup the good work.")
