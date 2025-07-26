from book_recommender.book_recommender import BookRecommender

def main():
    recommender = BookRecommender("book_data/books.csv")
    print("Recommendations for genre='Fiction', min_rating=4.5:")
    print(recommender.recommend(genre='Fiction', min_rating=4.5))

if __name__ == "__main__":
    main()
