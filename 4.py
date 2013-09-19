import urllib, re, time

def chain(url,k=1):
    origin = urllib.urlopen(url).read()
    while True:
        destno = ''.join(re.findall('\d+$',origin))
        originno = ''.join(re.findall('\d+$',url))
        if destno == '':
            break
        i = url.find(originno)
        newurl = url[:i] + destno
        origin = urllib.urlopen(newurl).read()
        print "Iteration " + str(k) +":", urllib.urlopen(newurl).read()
        k += 1
        
if __name__ == '__main__':
	print 'This program is being run by itself'
        start = time.time()
        print '### First Iteration Cycle ###'
        chain('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
        print '### Second Iteration Cycle ###'
        chain('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022')
        print 'Program took', time.time()-start, 'seconds to yield solution.'
else:
	print 'I am being imported from another module'

