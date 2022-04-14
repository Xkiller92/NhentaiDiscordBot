from typing import Text
from bs4 import BeautifulSoup as b 
import requests 


class Doujin:
                 
    def __init__(self, number):
        page = b(requests.get("https://nhentai.net/g/{}".format(number)).content, "html.parser")
        content = page
        main = content.find(id = "info")
        self.doujin_number = number
        self.element = main
        
    def get_name(self):
        text = self.element.find("h1").get_text()
    
        return text
    
    def  get_tags(self):
        elements = self.element.find(id = "tags")
        tag_elements = b(elements.findAll("div")[2].__str__(), features= "html.parser")
        
        text =  tag_elements.find_all("span", "name")
        
        tag_structure =  b(text.__str__(), features="html.parser")
        tag_list = tag_structure.get_text() 
        
        tags = "".join(tag_list)
        
        return tags
    
    def get_artist(self):
        elements = self.element.find(id = "tags")
        tag_elements = b(elements.findAll("div")[3].__str__(), features= "html.parser")
        
        artist = tag_elements.find("span", "name").get_text() 
        
        return artist
    
    def get_languages(self):
        elements = self.element.find(id = "tags")
        tag_elements = b(elements.findAll("div")[5].__str__(), features= "html.parser")
        
        language_list = tag_elements.findAll("span", "name")
        
        languages = b(language_list.__str__(), features="html.parser").get_text()
        
        return languages
    
    def get_page_count(self):
        elements = self.element.find(id = "tags")
        tag_elements = b(elements.findAll("div")[7].__str__(), features= "html.parser").getText()
        
        page_count = tag_elements.splitlines()[1].strip() +  " " + tag_elements.splitlines()[2].strip()
        
        page_count_int = int(page_count.split(" ")[1])
        
        return page_count_int
    
    
    def  get_page_by_number(self, Page_number):
        
        while (requests.get("https://nhentai.net/g/{}/{}".format(self.doujin_number, Page_number)).status_code == 200):
            a =  requests.get("https://nhentai.net/g/{}/{}".format(self.doujin_number, Page_number)).content
    
            e = b(a, features="html.parser")
    
            image_element = e.find(id ="image-container")
    
            image_link = image_element.findAll("img")[0]["src"]
            
            return image_link
