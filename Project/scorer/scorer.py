class Scorer:

    def __init__(self):

        self.weights = {

            "skills":0.40,

            "embedding":0.25,

            "experience":0.15,

            "behaviour":0.10,

            "location":0.05,

            "company":0.05
        }

    def score(self, features):

        total = 0

        for key,value in features.items():

            total += value * self.weights[key]

        return total