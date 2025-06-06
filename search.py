from googlesearch import search

def search_google(Query, num_results=10):
    SearthResults = search(Query, num=num_results, start=0, stop=num_results)
    
    return SearthResults


