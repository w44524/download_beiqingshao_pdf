
import urllib 
import urllib2 
import requests

print "downloading with urllib" 

url_base='https://www-k6.thinkcentral.com/content/hsp/reading/journeys/na/grk/Online_journeys_leveled_readers_9780547356860_/lr'
url_list=[]
url_list.append('bl')
url_list.append('ell')
url_list.append('ol')
url_list.append('al')

i=0
for url_sub in url_list:
    i+=1
    url_sub_this=url_base+'/'+url_sub+'/'
    for j in range(31):
        url='%slesson%s/lesson%s.pdf' %(url_sub_this, j, j)
        filename_local='%s_%s_lesson%s.pdf' %(i, url_sub, j)
        print  'downloading %s  as  %s' %(url, filename_local)
        urllib.urlretrieve(url, filename_local)
        
    

#url = 'https://www-k6.thinkcentral.com/content/hsp/reading/journeys/na/grk/Online_journeys_leveled_readers_9780547356860_/lr/bl/lesson30/lesson30.pdf'  
#print "downloading with urllib"
#urllib.urlretrieve(url, "1.pdf")
