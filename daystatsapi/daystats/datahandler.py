from daystats.daystatscalculator import DayStatsCalculator
import requests

class DataHandler:
    def __init__(self,api_url:str) -> None:
        self.calculator = DayStatsCalculator()
        self.api_url = api_url

    def getDataFromAPI(self):
        response = requests.get(self.api_url)
        return response.json()

    def processData(self):
        self.calculator.populateListofDays(self.getDataFromAPI())

        if self.calculator.numberOfDays() == 0:
            return {"error":"Calendar not found"}
        processed_data = {
            "days_checked": self.calculator.numberOfDays(),
            "mean_mood_score": self.calculator.meanMoodScore(),
            "min_mood_score_days": self.calculator.minMoodScoreDays(),
            "max_mood_score_days": self.calculator.maxMoodScoreDays(),
            "max_sequence_low_mood": self.calculator.maxSequenceLowMood(),
            "max_sequence_high_mood": self.calculator.maxSequenceHighMood(),
        }
        return processed_data
