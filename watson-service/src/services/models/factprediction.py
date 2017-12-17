"""factprediction.py"""
from os import path
from pandas import read_csv

class FactPrediction:
    """FactPrediction definition."""

    def train(self):
        """Trains the model."""
        from surprise import Reader, Dataset, KNNBasic
        
        directory = path.dirname(path.realpath(__file__))

        ratings = read_csv(path.join(directory, 'fact_ratings.csv'))
        ratings = Dataset.load_from_df(ratings[['userId', 'factId', 'rating']], Reader())

        trainset = ratings.build_full_trainset()
        self.model = KNNBasic()
        self.model.train(trainset)

    def predict(self, u_id, f_id):
        """Performs a prediction."""
        return self.model.predict(u_id, f_id)
