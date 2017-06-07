from lxml import html
import requests

page = requests.get('https://twitter.com/search?q=i%20wish%20there%20was%20app&src=typd')
html_text = str(page.content)
html_text = html_text.replace('<strong>', '')
html_text = html_text.replace('</strong>', '')
tree = html.fromstring(html_text)

tweets = tree.xpath('//div[@class="js-tweet-text-container"]/p/text()')

print(tweets)
