from creepy import Crawler

taco= open('./Documents/basuritas/cosa.txt','r')
print  taco.read()
cuenta = {}

class MyCrawler(Crawler):
    def process_document(self, taco):
        if taco.status == 200:
            print '[%d] %s' % (taco.status, taco.url)
            try:
                cuenta[taco.url] += 1
            except KeyError:
                cuenta[taco.url] = 1
            except e:
                print 'Unknown exception', e
        # Do something with doc.text (the content of the page)
        else:
            pass
crawler = MyCrawler()
crawler.set_follow_mode(Crawler.F_SAME_HOST)
crawler.add_url_filter('\.(jpg|jpeg|gif|png|js|css|swf)$')
crawler.add_url_filter('/.*/.*/')
crawler.crawl('http://stackexchange.com')

print cuenta

for url, count in cuenta.items():
    print '%s \t %d' % (url, count)
