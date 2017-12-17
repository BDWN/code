# Code Repository
This repository contains the latest version of our code:

__watson-app__: contains our frontend application, made using VueJs and Framework7 (JavaScript).

__watson-service__: contains our backend application, made using Flask (Python).

## IBM Bluemix/Watson

__Data Science Experience__: we tried to deploy our ML model on Bluemix, but DSX didn't support our model (scikit-surprise). Please see our [notebook](https://github.com/watson1718-group08/code/blob/master/watson-service/models/fact-prediction.ipynb).

__Machine Learning__: because of the above, we decided to deploy our ML model as part of the Python backend. Please see [/watson-service/src/services/models](https://github.com/watson1718-group08/code/tree/master/watson-service/src/services/models). 

__Visual Recognition__: this API is called from Python code. Please see [PaintingClassifier](https://github.com/watson1718-group08/code/tree/master/watson-service/src/services/watson).

__Other__: other Bluemix related code is located in [/watson-service/src/services/bluemix](https://github.com/watson1718-group08/code/tree/master/watson-service/src/services/bluemix).

## Demo

We've prepared the application for two demo scenarios, of which we have made screencasts:

https://www.youtube.com/playlist?list=PLhzYISG2-swDXPTi-FqXSjPITckDmJp3V

As you will see the personas have different preference profiles and get different facts (this is __NOT__ hardcoded):

#### Persona 1
Preference profile: __Clothings__, __People__, __Animals__, __Locations__

For Self-Portrait this persona gets as fact (related to __People__):

_"The details in this painting suggest that this is Rembrandt's last self portrait. The painter looks somewhat older, his double chin has sagged even more, the cheeks are more sunken, and the gray hair longer. The face is older but it does not show signs of mental decline as some earlier authors have suggested."_

For The Goldfinch this persona gets as fact (related to __Animals__):

_"Goldfinches are native to Europe, Northern Africa and Southwest Asia. They can be found near woodland areas, in urban gardens and car parks. A rather ordinary little bird in other words. Both the male and female goldfinch sing. They also look almost identical. But the male has a more distinct sound and more variation in his song."_

#### Persona 2
Preference profile: __Value__, __Date__, __Technique__, __Date__

For Self-Portrait this persona gets as fact (related to __Technique__):

_"The way he painted the face with strong brushstrokes is remarkable. With thick layers of paint that are almost modelled, Rembrandt suggests a man of flesh and blood. This is a true masterpiece."_

For The Goldfinch this persona gets as fact (related to __Technique__):

_"Carel Fabritius saw it: the beauty of the black, yellow and red in front of the white wall. The light and shade. A single glistening beady eye. The shadow on the wall. He painted the bird – a goldfinch – with loose, visible brushstrokes. Not too much colour or detail. A little bird on a chain, in front of a rather battered wall. That is all. Not much, but just enough. The work was painted without major corrections, with only minor ones to the contours of the bird. Most of the painting is set up with large brush strokes, but details such as the chain are painted with more precision. Fabritius showed off his skill by painting the bird's head foreshortened."_

### Instructions
If you want to try for yourself, follow these instructions:

1. Navigate to http://watson-app-dev.eu-gb.mybluemix.net
2. Login with the 'Persona 1' or 'Persona 2' account (see Final Report for login credentials).
3. The preference profile setup will open (this is read-only), click save at the bottom to close. 
4. Navigate to the 'Capture' tab
5. Upload one of the paintings below using the 'Add photo' button.
6. Optionally add a description.
7. Click 'Save' to save the post.
8. Navigate to 'Posts' and hit the 'Refresh' button.
9. Note that the name of the recognized painting is added as a hashtag.
10. Click on 'Comments' of the new post to see the comments (facts).
11. The fact will correspond to the preference profile of the user.

### Paintings
For use with the demo:

__The Goldfinsh__

![The Goldfinch](https://raw.githubusercontent.com/watson1718-group08/code/master/watson-app/src/assets/img/paintings/goldfinch.png)

__Self-Portrait__

![Self-Portrait](https://raw.githubusercontent.com/watson1718-group08/code/master/watson-app/src/assets/img/paintings/portrait.png)
