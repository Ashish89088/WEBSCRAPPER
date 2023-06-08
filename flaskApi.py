from autoscraper import AutoScraper
from flask import Flask, render_template, request 
from utils import auto
import pandas as pd
import numpy as np
import webbrowser
from IPython.display import HTML


amazon_scraper = AutoScraper()
amazon_scraper.load('amazon-search')
app = Flask(__name__)

def get_amazon_result(search_query):
    url = 'https://www.amazon.in/s?k=%s' % search_query
    result = amazon_scraper.get_result_similar(url, group_by_alias=True)
    return _aggregate_result(result)

def _aggregate_result(result):
    final_result = []
    # print(list(result.values())[0])
    # print(list(result.values())[1])
    for i in range(len(list(result.values())[0])):
        try:
            final_result.append({alias: result[alias][i] for alias in result})
        except:
            pass

    print(final_result)
    # return final_result
    return convert_to_table(final_result)

def convert_to_table(final_result):
    print(type(final_result))
    table = pd.DataFrame(final_result)
    print(table)
    print(type(table))
    table_html=table.to_html()
    # table_html=table
    # return show_table(table_html)
    # return table.to_html()
    
    html = table.to_html()
  
    # write html to file
    # text_file = open("text.html", "w")
    # text_file.write(html)
    # text_file.close()
    return HTML(table.to_html(classes='table table-stripped'))
    # return webbrowser.open(table_html)

@app.route('/', methods=['GET'])
def search_api():
    query = request.args.get('q')
    # print(query)
    jsondata = dict(result=get_amazon_result(query))
    # print('jsonData')
    # print(jsondata)
    return jsondata

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')