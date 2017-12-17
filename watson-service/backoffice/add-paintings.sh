#!/bin/bash

# The Anatomy Lession of Dr. Nicolaes Tulp
curl --data "name=the-anatomy-lesson&person=1&wikidata=Q661378" "$1/api/painting"

# Girl with a Pearl Earring
curl --data "name=girl-with-a-pearl-earring&person=2&wikidata=Q185372" "$1/api/painting"

# The Goldfinch
curl --data "name=the-goldfinch&person=3&wikidata=Q13726073" "$1/api/painting"

# The Young Bull
curl --data "name=the-young-bull&person=4&wikidata=Q2917717" "$1/api/painting"

# Saul and David
curl --data "name=saul-and-david&person=1&wikidata=Q9074913" "$1/api/painting"

# The Earthly Paradise 
curl --data "name=the-earthly-paradise&person=5&wikidata=Q29656879" "$1/api/painting"

# Self-portrait
curl --data "name=self-portrait&person=1&wikidata=Q17276109" "$1/api/painting"

# View of Delft
curl --data "name=view-of-delft&person=2&wikidata=Q523974" "$1/api/painting"

# Dorpskermis
curl --data "name=village-fair&person=6&wikidata=Q17276015" "$1/api/painting"

# IJsvermaak
curl --data "name=ice-skating&person=7&wikidata=Q17276074" "$1/api/painting"