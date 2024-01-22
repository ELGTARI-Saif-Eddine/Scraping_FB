[<img src="https://i.ytimg.com/vi/rqkmqTb7Goc/maxresdefault.jpg" width="50%">](https://www.youtube.com/watch?v=rqkmqTb7Goc "Now in Android: 55")
# Scraping_FB

https://youtu.be/rqkmqTb7Goc


Vous trouvez au-dessous une démonstartion par screenshots et une autre avec une vidéo uploaded to youtube.

1 - D'abord, créer une image avec Docker-Compose
2 - Lancer le container 
3 - Accéder sur votre navigateur à l'adresse http://127.0.0.1:8000/
4 - Sur la page qui sera affichée, ajouter l'ID de la page facebook publique choisie.
5 - Ajouter le nombre des posts qu'on le veut scraper.
6 - Cliquer sur le boutton "Start Scrapping"
7 - Il faut attendre (quelques seconds ou minutes) tout dépend de nombre de posts à scraper
8 - Le code va scrapper le N nombre posts choisis et l'insiréer dans une base de données NoSQL MongoDB.  
9 - Ainsi, Les Données scrappées seront enrigistrer sous format DataFrame sous le répertoire "dataScrapped" avec le nom "DataFrame_scrapped_FB_Page.csv" dans le Contenaire

Les captures pour Montrer les resultats du Code :
Scren Sohoots : ![alt text](https://github.com/ELGTARI-Saif-Eddine/Scraping_FB/blob/main/screenshots/im_1.png)

Une simple démonstastion avec Video, Uploaded sur youtube  

Donc, On a utilisé Docker-compose pour créer deux images : 
une image pour le service FastAPI et l'autre pour la DataBase (MongoDB)  
 --->>  docker-compose build : construire ou reconstruire les images Docker spécifiées dans le fichier docker-compose.yml

Conteneurs :
 --->>  docker-compose up :  créer et démarrer les conteneurs basés sur les images spécifiées dans le fichier docker-compose.yml.

Les données scrapées dans les POSTS sont les suivantes : 
id,name,shares,likes,loves,wow,cares,sad,angry,haha,reactions_count,comments,content,posted_on,video,image,post_url

 Graph API :
 To scrap Data from Facebook Pulic Pages :
 Facebook's Graph API is the recommended and legitimate way to access data from Facebook Pages programmatically, but it requires proper authentication and adherence to Facebook's policies.
     we need to get a page_access_token.
     Use the obtained page access token to make API requests to the Graph API endpoint for the information we need.

NB : (Amélioration de l'interface web) Les sorties peuvent etre amiloirées par l'ajout de progress par sur la page HTML ou bien les alerts et les messages pour afficher les LOGS sur la page web. tout ça on peut le faire avec l'integration de websockets avec FastApi.


 
 (Ajouter les données scrappées from the posts !!!!!!)

 (????? N'oublier pas d'ajouter dictionnaire appéss JSON MongoDB ,pour test la création de la base de données sinon enlever ty.. expt ?????????????????? )
