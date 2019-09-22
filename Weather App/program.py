import requests
import bs4

def main():
    print_the_header()
    # get zipcode from user
    code = input('What zipcode do you want the weather for? ')


    html = get_html_from_web(code)

    get_weather_from_html(html)

# parse the html
# display the forcast


def print_the_header():
    print('---------------------')
    print('    Weather APP      ')
    print('---------------------')


def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    #print(url)
    response = requests.get(url)
    #print(response.status_code)
    #print(response.text[0:250])
    return response.text

def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    print(soup)

if __name__ == '__main__':
    main()
