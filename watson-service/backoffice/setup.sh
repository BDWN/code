#!/bin/bash

URL='https://watson-service.eu-gb.mybluemix.net'
#URL='http://localhost:5000'

./add-persons.sh $URL
./add-paintings.sh $URL
./add-facts.sh $URL
