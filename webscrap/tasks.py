from .models import News

import requests
from bs4 import BeautifulSoup

def news_task():
        
        url = "https://techcrunch.com/tag/news/"

        r = requests.get(url)

        soup = BeautifulSoup(r.text,'html5lib')

        table = soup.find_all('header', attrs = {'class':'post-block__header'}) 
        # article = soup.find(class_ = "post-block post-block--image post-block--unread" )
        article = soup.find_all("div",class_='post-block')

        extracted_link = []
        extracted_title = []
        extracted_content = []
        extracted_date = []
        extracted_img = []

        # header = article.text
        data = dict()
        data = {
            "link":extracted_link,
            "title":extracted_title,
            "content":extracted_content,
            "date":extracted_date,
            "img":extracted_img,
        }
        c=0
        for x in article:
            link = x.h2.find("a")["href"]
            title = x.h2.find("a").text.strip()
            content = x.find("div",class_="post-block__content").text.strip()
            date = x.find('time').text.strip()
            img = x.figure.find("img")["src"]
            extracted_link.append(link)
            extracted_title.append(title)
            extracted_content.append(content)
            extracted_date.append(date)
            extracted_img.append(img)
            c+=1
            # print(img)

        # print(extracted_link[10])
        # data["link"].append(extracted_link)
        for i in range(c):
            print(data["title"][i]," ",data["content"][i]," ",data["date"][i],end="\n\n\n")

        News.objects.create(
                title=title,
                description=content,
                link=link,
                img=img,
                date=date,
            )


news_task()


