from googlesearch import search

def search_google(Query, num_results=10):
    SearthResults = search(Query, num_results=num_results)
    
    return SearthResults


