import scholarly

# Define a list of keywords to search for
keywords = ["deep learning", "machine learning", "neural networks"]

# Loop through the keywords and print the titles of the first 5 articles for each keyword
for keyword in keywords:
    search_query = scholarly.search_pubs_query(keyword)
    print(f"Top articles for keyword: {keyword}")
    for i, article in enumerate(search_query):
        if i == 5:
            break
        print(f"{i+1}. {article.bib['title']}")
    print("\n")
