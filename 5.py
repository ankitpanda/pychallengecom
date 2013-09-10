import pickle, urllib

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
pickled = pickle.load(urllib.urlopen(url))
for line in pickled:
    print ''.join(map(lambda pair: pair[0] * pair[1], line))
