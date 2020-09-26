from flask import render_template,request,redirect,url_for #import the render_template function from Flask
from . import main #import the app instance from flask
from ..request import get_sources,get_news_articles
 


#views 
@main.route('/')
def index():
    '''
    Root page function that returns the index page
    '''

    #Getting news sources
    various_sources=get_sources('category')
    

    title='Catch up on the latest news as and when they happen. keep i here for more information'
   

  
    return render_template('index.html',title=title, sources=various_sources)


@main.route('/articles/<id>')
def source(id):
    
    source_articles=get_news_articles(id)
    print(source_articles)
    title="Articles"

    return render_template('articles.html',title=title,id=id,articles=source_articles)




