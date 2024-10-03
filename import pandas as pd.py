import pandas as pd
chunk_size = 10000
goodReads = pd.read_csv("Goodreads_books_with_genres.csv")
print(goodReads.head(4))