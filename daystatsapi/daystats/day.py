import datetime

class Day():
    def __init__(self,**kwargs) -> None:
        self.calendar : int
        self.date : str
        self.mood_score : int
        self.comments : str 

        for key,value in kwargs.items():
            setattr(self,key,value)

    def weekday(self):
        int_to_weekday = {
            0:'Monday',
            1:'Tuesday',
            2:'Wednesday',
            3:'Thursday',
            4:'Friday',
            5:'Saturday',
            6:'Sunday'
        }

        date_to_int = [int(_) for _ in self.date.split('-')]
        int_to_datetime = datetime.date(*date_to_int)
        "return date day of the week"
        return int_to_weekday.get(int_to_datetime.weekday())

    def asDict(self):
        to_dict = {
            "calendar":self.calendar,
            "date": self.date,
            "mood_score":self.mood_score,
            "comments":self.comments
        }
        return to_dict

    def __str__(self):
        return self.date
    def __repr__(self):
        return self.date
        