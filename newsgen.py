import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Read the input text file
with open('url.list', 'r') as f:
    urls = [line.strip() for line in f.readlines()[:30]]

# Generate the HTML code for each URL
news_links = []
for url in urls:
    # Fetch the HTML content of the web page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the head title of the web page
#    title = soup.find('title').text
    title_element = soup.find('title')
    if title_element is not None:
        title = title_element.text
    else:
        title = "Unknown"


    # Generate the HTML code for the link
#   news_link = f'<a href="{url}">{title}</a>'
    news_link = f'<a href="{url}" style="text-decoration:none;">{title}</a>'
    news_links.append(news_link)

# Get the current date and Lunar calendar date
now = datetime.now()
update_date = now.strftime("%Y年%m月%d日")

# Write the generated HTML code to a new output file
with open('index.html', 'w') as f:
    # Write the HTML header, including the title
    f.write('<!DOCTYPE html>\n')
    f.write('<html>\n')
    f.write('<head>\n')
    f.write('  <meta charset="UTF-8">\n')
    f.write('  <title>阿媽新聞匯</title>\n')
    f.write('  <meta http-equiv="refresh" content="300">')
    f.write('  <style>\n')
    f.write('    #title {\n')
    f.write('      display: flex;')
    f.write('      justify-content: space-between;')
    f.write('      background-color: #ffcc00;\n')
    f.write('      color: #333333;\n')
    f.write('      font-size: 24px;\n')
    f.write('      font-weight: bold;\n')
    f.write('      text-align: center;\n')
    f.write('      padding: 10px;\n')
    f.write('      margin-bottom: 20px;\n')
    f.write('    }\n')
    f.write('    a {')
    f.write('      font-size: 17px;')
    f.write('      text-decoration: none;')
    f.write('    }')
    f.write('  </style>\n')
    f.write('  <script>')
    f.write('    window.addEventListener(\'DOMContentLoaded\', function () {')
    f.write('      var dateElem = document.getElementById(\'date\');')
    f.write('      var now = new Date();')
    f.write('      var current_date = \'今日係\' + now.getFullYear() + \'年\' + (now.getMonth() + 1) + \'月\' + now.getDate() + \'日\';')
    f.write('      dateElem.innerHTML = current_date;')
    f.write('    });')
    f.write('  </script>')
    f.write('</head>\n')
    f.write('<body>\n')


    # Write the HTML code for the title banner
    f.write(f'<div id="title"><span id="date"></span>阿  媽  新  聞  匯<span>更新於{update_date}</span></div>\n')

    # Write the HTML code for the links
    for news_link in news_links:
        f.write(news_link)
        f.write('<p>\n')

    # Write the HTML footer
    f.write('</body>\n')
    f.write('</html>\n')