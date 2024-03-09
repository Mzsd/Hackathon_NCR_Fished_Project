load folder into VSCODE
open 4 terminals

Terminal 1: 
npm i json-server -g
json-server --watch HSBC_atms.json --port 3001

Terminal 2
pip install Flask
python app.py


Terminal 3
docker-compose up

Terminal 4
docker exec -it <containerid> mongosh -u root -p example --authenticationDatabase admin    
                   