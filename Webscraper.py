#Importing required libraries.
import requests, random, datetime
from bs4 import BeautifulSoup

def get_content(url):
    '''
    Helper function (1):
    This function is used to get the content from the url and handle any exceptions.
    '''
    try:
        #Random user agent header using a random number.
        random_number = random.randint(1,99999)
        headers = {'user-agent': f'{random_number}'}

        #Get the content from the url.
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content: {e}")
        return None

def format_date(date_string):
    '''
    Helper function (2):
    This function gives the date time in a required format while handling exceptions.
    '''
    try:
        return datetime.datetime.fromisoformat(date_string).strftime("%B %d, %Y")
    except ValueError:
        print(f"Error parsing date: {date_string}")
        return None

def print_blogs_date_title(blogs):
    '''
    Helper function (3):
    This function does the scraping task and gets all the tags required in our case.
    '''
    for blog in blogs:
        title = blog.find('a', class_="entry-title-link").get_text()
        blog_datetime_string = blog.find('time', class_="entry-time").get('datetime')
        blog_datetime = format_date(blog_datetime_string)

        if blog_datetime:
            print(blog_datetime, ":", title)


def main():
    '''
    Main function:
    This is the main function which calls all the helper functions to complete the task of web scraping.
    '''
    #Using the content, parse it using a html parser.
    url = "https://pixelford.com/blog/"
    html = get_content(url)
    soup = BeautifulSoup(html, 'html.parser')

    #Find all articles on the webpage.
    blogs = soup.find_all('article', class_ = "type-post")

    print_blogs_date_title(blogs)

if __name__ == "__main__":
    main()