from bs4 import BeautifulSoup
import requests
from tabulate import tabulate

print('Basic EspnCricInfo Data - Rankings / Articles / News ')
print('')


#-------------TEST Ranking-----------------------------

def fetch_ranking(format):
    html_text = requests.get('https://www.espncricinfo.com/rankings/content/page/211271.html').text
    soup = BeautifulSoup(html_text, 'lxml')                                    
    rank_title = soup.find_all('h3')

    for title in rank_title:
        if format in title.text:
            table = title.find_next('table', class_='StoryengineTable')
            if table:
                rows = table.find_all('tr')
                data = []
                for row in rows:
                    columns = row.find_all('td')
                    row_data = [column.get_text().strip() for column in columns]
                    data.append(row_data)
                
                print('')
                print(f"{format} Ranking")
                print(tabulate(data, headers="firstrow", tablefmt="grid"))
                print()


#-------------ODI Ranking-----------------------------

def ranking_odi(format):
    html_text = requests.get('https://www.espncricinfo.com/rankings/content/page/211271.html').text
    soup = BeautifulSoup(html_text, 'lxml')                                    
    rank_title = soup.find_all('h3')

    for title in rank_title:
        if format in title.text:
            table = title.find_next('table', class_='StoryengineTable')
            if table:
                rows = table.find_all('tr')
                data = []
                for row in rows:
                    columns = row.find_all('td')
                    row_data = [column.get_text().strip() for column in columns]
                    data.append(row_data)
                
                print('')
                print(f"{format} Ranking")
                print(tabulate(data, headers="firstrow", tablefmt="grid"))
                print()
               


#------------------Articles----------------------------

def fetch_technology_articles():
    html_text = requests.get('https://www.espncricinfo.com/cricket-news/technology-in-cricket-18').text
    soup = BeautifulSoup(html_text, 'lxml')
    cric_tech = soup.find_all('div', class_='ds-w-2/3')

    print('------------------------------------')
    print('Article Section')
    print('------------------------------------')

    for tech_article in cric_tech:
        art_date = tech_article.find('div', class_='ds-leading-[0] ds-text-typo-mid3 ds-mt-1').span.text
        if '202' in art_date :
            art_name = tech_article.find('h2', class_='ds-text-title-s').text.replace(' ', ' ')
            art_desc = tech_article.find('div', class_='').text.replace(' ',' ')

            print(f'Article_Name: {art_name.strip()}')
            print(f'Article_Description: {art_desc.strip()}')
            print()

    
#------------------News-----------------------------

def fetch_news():
    html_text = requests.get('https://www.espncricinfo.com/cricket-news').text
    soup = BeautifulSoup(html_text, 'lxml')
    cric_news = soup.find_all('div', class_='ds-w-2/3')
    
    print('------------------------------------')
    print('News Section')
    print('------------------------------------')
    
    for news in cric_news:
        published_date = news.find('div', class_='ds-leading-[0] ds-text-typo-mid3 ds-mt-1').span.text
        if '16-May-2024' in published_date:
            news_title = news.find('h2', class_='ds-text-title-s').text.replace(' ', ' ')
            news_desc = news.find('div', class_='').text.replace(' ', ' ')

            print(f'News_Title: {news_title.strip()}')
            print(f'News_Description: {news_desc.strip()}')
            print(f'News_Published_By: ESPNCricInfo Staff')


fetch_ranking('Test')
fetch_ranking('ODI')
fetch_technology_articles()
fetch_news()