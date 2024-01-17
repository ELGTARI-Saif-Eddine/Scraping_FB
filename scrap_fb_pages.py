from fastapi import FastAPI, WebSocket, Query
from fastapi.responses import FileResponse
from facebook_page_scraper import Facebook_scraper
from pymongo import MongoClient
import os

app = FastAPI()

# Get MongoDB connection URI from environment variable
mongo_uri = os.environ.get('MONGO_DB_URI', 'mongodb://localhost:27017/scraping_database')
mongo_client = MongoClient(mongo_uri)

# db = mongo_client.get_default_database()

# Reference the "scraping_database" database
db = mongo_client["scraping_database"]


@app.get("/", response_class=FileResponse)
async def read_root():
    return FileResponse("templates/index.html")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        json_data = "Scraping not yet started."
        await websocket.send_text(json_data)
    except Exception as e:
        await websocket.send_text(f"Error: {str(e)}")

@app.get("/start_scraping")
async def start_scraping(page_name: str = Query("NatGeoAbuDhabi"), posts_count: int = Query(10)):
    try:
        browser = "firefox"
        proxy = "IP:PORT"
        timeout = 600
        headless = True
        data_scrapped = Facebook_scraper(page_name, posts_count, browser, proxy=proxy, timeout=timeout, headless=headless)
        
        filename = "data_file"  #file name without CSV extension,where data will be saved
        directory = "./data" #directory where CSV file will be saved
        data_scrapped.scrap_to_csv(filename, directory)
        print("Data saved successfully as a DataFrame in the data folder.")


        # Reference the "scraping_collection" in the "facebook_scraper" database
        collection = db['scraping_collection']
        # Assuming 'data' is the data you want to insert into MongoDB
        result = collection.insert_one(data_scrapped.scrap_to_json())

        # Print the MongoDB insert result
        print("Data successfully saved to MongoDB : ", result.inserted_id)

        return {"message": "Scraping completed successfully!"}
    except Exception as e:
        return {"message": f"Error: {str(e)}"}
