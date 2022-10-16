from typing import List, Dict
from daystats.day import Day


class DayStatsCalculator:
    def __init__(self) -> None:
        self.list_of_days: List[Day] = []

    def populateListofDays(self, data: List[Dict]) -> None:
        for entry in data:
            new_day = Day(**entry)
            self.list_of_days.append(new_day)

    def meanMoodScore(self) -> float:
        score_list = [day.mood_score for day in self.list_of_days]
        result: float = 0
        try:
            result = sum(score_list) / len(score_list)
        except (ZeroDivisionError):
            result = 0
        return result

    def minMoodScoreDays(self):
        min_score = min([getattr(day, "mood_score") for day in self.list_of_days])
        min_score_days = [
            day for day in self.list_of_days if day.mood_score == min_score
        ]
        return min_score_days

    def maxMoodScoreDays(self):
        max_score = max([getattr(day, "mood_score") for day in self.list_of_days])
        max_score_days = [
            day for day in self.list_of_days if day.mood_score == max_score
        ]
        return max_score_days

    def maxSequenceLowMood(self):
        """low mood is defined as mood_score of 0,1 or 2. less than 3

        step 1: sort the list_of_days by date
        step 2: loop through the list
            check mood_score if < 3 add to temp list
            else

        """
        result = []
        temp_res = []
        sorted_list_of_days = sorted(self.list_of_days, key=lambda x: x.date)

        for day in sorted_list_of_days:
            if day.mood_score < 3:
                temp_res.append(day)
            else:
                if len(temp_res) > len(result):
                    result = temp_res
                temp_res = []
        return result

    def maxSequenceHighMood(self):
        """high mood is defined as mood_score of 3, 4 or 5. greater than 2"""
        result = []
        temp_res = []
        sorted_list_of_days = sorted(self.list_of_days, key=lambda x: x.date)

        for day in sorted_list_of_days:
            if day.mood_score > 2:
                temp_res.append(day)
            else:
                if len(temp_res) > len(result):
                    result = temp_res
                temp_res = []
        return result

    def clearList(self):
        self.list_of_days = []

    def numberOfDays(self):
        return len(self.list_of_days)
