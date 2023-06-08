from autoscraper import AutoScraper

url = 'https://www.amazon.in/s?k=speaker'

# We can add one or multiple candidates here.
# You can also put urls here to retrieve urls.
wanted_list = ['₹994 ','boAt Stone 180 5W Bluetooth Speaker with Upto 10 Hours Playback, 1.75" Driver, IPX7 & TWS Feature(Black)']


scraper = AutoScraper()
result = scraper.build(url, wanted_list)
# print(result)

res = scraper.get_result_similar(url,grouped=True)
# print(res)

web_key = list(res.keys())

k1, k2 = web_key[0], web_key[2]

scraper.set_rule_aliases({f'{k1}':'Price',f'{k2}':'Title'})
scraper.keep_rules([f'{k1}',f'{k2}'])
scraper.save('amazon-search')
# result = scraper.get_result_similar('https://www.amazon.in/s?k=mobiles+above+25000',group_by_alias=True)
# print("\n")
# print(len(result['Price']))
# print(len(result['Title']))


