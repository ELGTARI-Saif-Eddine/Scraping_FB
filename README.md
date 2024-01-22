# _Facebook - Public Pages Scraper_

![alt text](https://github.com/ELGTARI-Saif-Eddine/Scraping_FB/blob/main/screenshots/im_1.png)


## A simple demonstration with video, uploaded on YouTube :

[<img src="https://github.com/ELGTARI-Saif-Eddine/Scraping_FB/blob/main/screenshots/2.jpg" width="50%">](https://www.youtube.com/watch?v=rqkmqTb7Goc)


## Below, you will find a demonstration through screenshots :

- 1 - First, create an image with Docker-Compose.
- 2 - Launch the container.
- 3 - Access your browser at : ```http://127.0.0.1:8000/```
- 4 - On the displayed page, add the ID of the chosen public Facebook page.
- 5 - Add the number of posts you want to scrape.
- 6 - Click on the "Start Scraping" button.
- 7 - Wait (a few seconds or minutes) depending on the number of posts to scrape.
- 8 - The code will scrape the specified number of posts and insert them into a NoSQL MongoDB database.
- 9 - The scraped data will be saved in DataFrame format under the "dataScrapped" directory with the name "DataFrame_scrapped_FB_Page.csv" in the container.

# Screenshots to Display Code Results and Explain the Steps :
FastApi and MongoDB Images on Docker :
![alt text](https://github.com/ELGTARI-Saif-Eddine/Scraping_FB/blob/main/screenshots/im_3.png)

Containers on Docker:
![alt text](https://github.com/ELGTARI-Saif-Eddine/Scraping_FB/blob/main/screenshots/im_4.png)

Access to the Page:  ```http://127.0.0.1:8000/```
![alt text](https://github.com/ELGTARI-Saif-Eddine/Scraping_FB/blob/main/screenshots/im_1.png)

Scraping Status (Successful State):
![alt text](https://github.com/ELGTARI-Saif-Eddine/Scraping_FB/blob/main/screenshots/6.jpg)
Scraping Results:
![alt text](https://github.com/ELGTARI-Saif-Eddine/Scraping_FB/blob/main/screenshots/5.jpg)


**So, we used Docker-compose to create two images :**
One image for the FastAPI service and the other for the database (MongoDB).
--->>  ```docker-compose build``` : Build or rebuild the specified Docker images in the docker-compose.yml file.

**Containers :**
--->>  ```docker-compose up``` :  Create and start containers based on the images specified in the docker-compose.yml file.
 
**The scraped data from the posts includes the following details:**
id,name,shares,likes,loves,wow,cares,sad,angry,haha,reactions_count,comments,content,posted_on,video,image,post_url

**Graph API :**
To scrap Data from Facebook Pulic Pages :
Facebook's Graph API is the recommended and legitimate way to access data from Facebook Pages programmatically, but it requires proper authentication and adherence to Facebook's policies.
     we need to get a page_access_token.
     Use the obtained page access token to make API requests to the Graph API endpoint for the information we need.

## Note: 
**(Web Interface Improvement)** Enhancements to the outputs can be achieved by incorporating progress bars on the HTML page or by adding alerts and messages to display logs on the web page. All of this can be accomplished through the integration of websockets with FastAPI.
