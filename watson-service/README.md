# Watson Service

[https://watson-service.eu-gb.mybluemix.net](https://watson-service.eu-gb.mybluemix.net)

## Run the service

1. Run `pip install -r requirements.txt`
2. Run `python src/index.py`
3. Access the service at <http://localhost:5000>

## Deploy the sevice

1. Run `bluemix api https://api.eu-gb.bluemix.net`
2. Run `bluemix login -u account_name -o o.a.b.valkering@student.vu.nl -s dev`
3. Run `bluemix app push "Watson Service"`
4. Access the service at <https://watson-service.eu-gb.mybluemix.net>
