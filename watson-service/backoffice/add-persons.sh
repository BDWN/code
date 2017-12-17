#!/bin/bash

# 1. Rembrandt van Rijn
curl --data "name=Rembrandt van Rijn&photo=rembrandt.png" "$1/api/person"

# 2. Johanness Vermeer
curl --data "name=Johannes Vermeer&photo=vermeer.png" "$1/api/person"

# 3. Carel Fabritius
curl --data "name=Carel Fabritius&photo=fabritius.png" "$1/api/person"

# 4. Paulus Potter
curl --data "name=Paulus Potter&photo=potter.pong" "$1/api/person"

# 5. Jan Brueghel
curl --data "name=Jan Brueghel&photo=brueghel.png" "$1/api/person"

# 6. Dorpskermis
curl --data "name=Jan Steen&photo=steen.png" "$1/api/person"

# 7. Hendrick Avercamp
curl --data "name=Hendrick Avercamp&photo=avercamp.png" "$1/api/person"