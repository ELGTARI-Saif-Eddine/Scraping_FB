from fastapi import FastAPI, WebSocket, Query, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from facebook_page_scraper import Facebook_scraper
from pymongo import MongoClient
import os
import json

app = FastAPI()

# Get MongoDB connection URI from environment variable
mongo_uri = os.environ.get('MONGO_DB_URI', 'mongodb://localhost:27017/scraping_database')
mongo_client = MongoClient(mongo_uri)

# Reference the "scraping_database" database
db = mongo_client["scraping_database"]

# Configure Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    message_content = "Scraping completed successfully!"
    return templates.TemplateResponse("index.html", {"request": request, "message_content": message_content})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    json_data = "Enter the Facebook Page ID and specify the number of posts you want to scrape. Click 'Start Scraping' to initiate the scraping process."
    await websocket.send_text(json_data)

@app.get("/start_scraping")
async def start_scraping(page_name: str = Query("NatGeoAbuDhabi"), posts_count: int = Query(10)):
    try:
        browser = "firefox"
        proxy = "IP:PORT"
        timeout = 600
        headless = True
        data_scrapped = Facebook_scraper(page_name, posts_count, browser, proxy=proxy, timeout=timeout, headless=headless)

        filename = "DataFrame_scrapped_FB_Page"
        directory = "dataScrapped"

        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Directory '{directory}' created.")

        data_scrapped.scrap_to_csv(filename, directory)
        print("Data saved successfully as a DataFrame in the data folder.")

        collection = db['scraping_collection']
        json_data = data_scrapped.scrap_to_json()
        document = json.loads(json_data)
        result = collection.insert_one(document)

        print("Data successfully saved to MongoDB : ", result.inserted_id)

        return {"message": "Scraping completed successfully!"}

    except Exception as e:
        return {"message": f"Error: {str(e)}"}
