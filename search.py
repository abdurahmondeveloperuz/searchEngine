from googlesearch import search

def search_google(Query, num_results=10):
    SearthResults = search(Query, start=0, stop=num_results)
    
    return SearthResults


