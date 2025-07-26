import pandas as pd

class BookRecommender:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)
    
    def recommend(self, genre=None, min_rating=None, author=None):
        result = self.data
        if genre:
            result = result[result['genre'].str.lower() == genre.lower()]
        if min_rating:
            result = result[result['rating'] >= float(min_rating)]
        if author:
            result = result[result['author'].str.lower().str.contains(author.lower())]
        return result['title'].tolist()
