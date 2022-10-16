from fastapi import FastAPI
from decouple import config
from daystats.datahandler import DataHandler
import uvicorn

app = FastAPI()

@app.get("/daystats/{calendar_id}")
async def StatsCalc(calendar_id):
    url = config('API_URL') + str(calendar_id)
    dh = DataHandler(api_url = url)
    data = dh.processData()
    return data

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=3000)
