from lxml import html
import requests

scrape_search = input('Phrase to search: ')
scrape_string = scrape_search.replace(' ', '%20')

page = requests.get('https://twitter.com/search?q=' + scrape_string)

html_text = str(page.content)
html_text = html_text.replace('<strong>', '')
html_text = html_text.replace('</strong>', '')

tree = html.fromstring(html_text)

tweets = tree.xpath('//div[@class="js-tweet-text-container"]/p/text()')

with open('savedtweets.txt', 'w') as my_file:
    for tweet in tweets:
        print(tweet)
        want_save = input('Save?')

        if len(want_save) > 0:
            my_file.write(tweet + '\n')
