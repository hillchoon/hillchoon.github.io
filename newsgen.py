import requests
from bs4 import BeautifulSoup

# Read the input text file
with open('url.list', 'r') as f:
    urls = f.read().splitlines()

# Generate the HTML code for each URL
news_links = []
for url in urls:
    # Fetch the HTML content of the web page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the head title of the web page
    title = soup.find('title').text

    # Generate the HTML code for the link
    news_link = f'<a href="{url}">{title}</a>'
    news_links.append(news_link)

# Write the generated HTML code to a new output file
with open('index.html', 'w') as f:
    # Write the HTML header, including the title
    f.write('<!DOCTYPE html>\n')
    f.write('<html>\n')
    f.write('<head>\n')
    f.write('<title>阿媽新聞匯</title>\n')
    f.write('</head>\n')
    f.write('<body>\n')

    # Write the HTML code for the links
    for news_link in news_links:
        f.write(news_link + '<br>\n')

    # Write the HTML footer
    f.write('</body>\n')
    f.write('</html>\n')