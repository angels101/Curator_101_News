from ssl import VERIFY_CRL_CHECK_CHAIN
import urllib.request,json
from .models import Source,Articles



api_key = None
base_url = None
articles_base_url= None
def configure_request(app):
    global api_key,base_url,articles_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['BASE_URL']
    articles_base_url= app.config['ARTICLES_BASE_URL']
    
    client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)
    verify = vonage.Verify(client)

def get_sources(category):
    '''
    function that gets the json response to our url request
    '''
    news_source_url=base_url.format(category,api_key)

    with urllib.request.urlopen(news_source_url) as url:

        source_data = url.read()
        source_response = json.loads(source_data)
        source_results= None

        if source_response['sources']:
            source_results_list = source_response['sources']
            source_results = process_results(source_results_list)

        return source_results 


def process_results(source_list):
    '''
    Function that processes the news results and transform them to a list of objects
    '''
    source_results=[]

    for news_item in source_list:

        id=news_item.get('id')
        name=news_item.get('name')
        description=news_item.get('description')
        url=news_item.get('url')
        category=news_item.get('category')
        country=news_item.get('country')

           
        source_object = Source(id,name,description,url,category,country)
        source_results.append(source_object)


    return source_results   

def get_news_articles(id):
    '''
    Function that gets json response of articles for a specific source
    '''
    get_news_url=articles_base_url.format(id,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        news_data=url.read()
        news_response=json.loads(news_data)
        news_results= None

        if news_response['articles']:
            news_results_list=news_response['articles']
            news_results=process_articles_results(news_results_list)
    return news_results


def process_articles_results(news_updates):
    '''
    This function returns a list of new articles
    '''
    news_results = []
    for news_object in news_updates:
        id=news_object.get('id')
        name = news_object.get('name')
        author =  news_object.get('author')
        title = news_object.get('title')
        description = news_object.get('description')
        url = news_object.get('url')
        urlToImage =news_object.get('urlToImage')
        publishedAt = news_object.get('publishedAt')
        content = news_object.get('content')

        new_article = Articles(id,name,author,title,description,url,urlToImage,publishedAt,content)
        news_results.append(new_article)
    return news_results

response = client.start_verification(
  number="254714796130",
  brand="Vonage",
  code_length="4")

if response["status"] == "0":
  print("Started verification request_id is %s" % (response["request_id"]))
else:
  print("Error: %s" % response["error_text"])


response = client.cancel_verification("REQUEST_ID")

if response["status"] == "0":
  print("Cancellation successful")
else:
  print("Error: %s" % response["error_text"])


request_id = "REQUEST_ID"
response = client.check_verification(request_id, code="CODE")

if response["status"] == "0":
  print("Verification successful, event_id is %s" % (response["event_id"]))
else:
  print("Error: %s" % response["error_text"])

response = VERIFY_CRL_CHECK_CHAIN.start_verification(number=RECIPIENT_NUMBER, brand="AcmeInc")

if response["status"] == "0":
    print("Started verification request_id is %s" % (response["request_id"]))
else:
    print("Error: %s" % response["error_text"])