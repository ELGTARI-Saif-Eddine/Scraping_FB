# Scraping_FB

Vous trouvez au-dessous une démonstartion par screenshots et une autre avec une vidéo uploaded to youtube.

1 - D'abord, créer une image avec Docker-Composer
2 - Lancer le container 
3 - Accéder sur votre navigateur à l'adresse http://127.0.0.1/8000
4 - Sur la page qui sera affichée, ajouter l'ID de la page facebook publique choisie.
5 - Ajouter le nombre des posts qu'on le veut scraper.
6 - Cliquer sur le boutton "Start Scrapping"
7 - Il faut attendre (quelques seconds ou minutes) tout dépend de nombre de posts à scraper
8 - Le code va scrapper le N nombre posts choisis et l'insiréer dans une base de données NoSQL MongoDB.  
9 - Ainsi, Les Données scrappées seront enrigistrer sous format DataFrame sous le répertoire "dataScrapped" avec le nom "DataFrame_scrapped_FB_Page.csv" dans le Contenaire

Les captures pour Montrer les resultats du Code :
Scren Sohoots : ![alt text](https://github.com/ELGTARI-Saif-Eddine/Scraping_FB/blob/main/screenshots/im_1.png)

Une simple démonstastion avec Video, Uploaded sur youtube  

Donc, On a utilisé Docker-composer pour créer deux images : 
une image pour le service FastAPI et l'autre pour la DataBase (MongoDB)  
 --->>  docker-compose build : construire ou reconstruire les images Docker spécifiées dans le fichier docker-compose.yml

Conteneurs :
 --->>  docker-compose up :  créer et démarrer les conteneurs basés sur les images spécifiées dans le fichier docker-compose.yml.

 Graph API !!
 (Ajouter les données scrappées from the posts !!!!!!)
