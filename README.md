# git-hub-hook
simple python celery task  receives git-hub event and notifies it on telegram.


### Run python worker 
celery -A demo worker --loglevel=debug --without-heartbeat --without-mingle


### Run flask server
python3 demo/api.py 
,Flask server will running on http://127.0.0.1:5000

### Run ngrok 
Download ngrok
cd ngrok
,ngrok http 5000