"""visualrecognition.py"""
from json import dumps
from watson_developer_cloud import VisualRecognitionV3

class PaintingClassifier:
    """PaintingClassifier definition"""

    def __init__(self, api_key):
        self.visual_recognition = VisualRecognitionV3('2016-05-20', api_key=api_key)

    def classify(self, photo_url):
        """Recognizes a painting from the provided photo."""
        response = self.visual_recognition.classify(parameters=dumps({
            'url': photo_url,
            'classifier_ids': ['Mauritshuispaintings_1819876186']
        }))
        print(dumps(response))

        try:
            classes = response['images'][0]['classifiers'][0]['classes']
            classes = sorted(classes, key=lambda x: x['score'], reverse=True)
            
            return classes[0]['class']
        except IndexError:
            return None
