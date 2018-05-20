#-*- coding: UTF-8 -*-


import urllib 
import urllib2 
import requests
import re


def get_file_url_name(doc_type, url_html, url_rel_name_list, i):
    '''
    '''
    print 'start get %s' %(doc_type)
    url_html_base=url_html[:url_html.rfind('/')+1]
    for (url_rel, filename) in url_rel_name_list:
        url_dld=url_html_base+url_rel
        fname=filename.replace(":", "__")
        fname=fname.replace("&nbsp;", "")
        fname=fname.replace("\t", "")
        filename_local='%s_' %(i)+doc_type+'_'+fname+'.pdf'
        print  'downloading %s  as  %s' %(url_dld, filename_local)
        urllib.urlretrieve(url_dld, filename_local)

        


if __name__ == '__main__':

    url_base='https://www-k6.thinkcentral.com/content/hsp/reading/journeys/na/grk/Online_journeys_leveled_readers_9780547356860_/'

    #四类教材
    doc_type_list=[]
    doc_type_list.append('bl')
    doc_type_list.append('ell')
    doc_type_list.append('ol')
    doc_type_list.append('al')
    doc_type_list.append('vr')

    i=0
    for doc_type in doc_type_list:
        print '******************* %s: %s ***************' %(i, doc_type)
        i+=1
        
        '''
            拼接出来这种URL,存在url_sub_this:
            https://www-k6.thinkcentral.com/content/hsp/reading/journeys/na/grk/Online_journeys_leveled_readers_9780547356860_/lesson_bl.html
            https://www-k6.thinkcentral.com/content/hsp/reading/journeys/na/grk/Online_journeys_leveled_readers_9780547356860_/lesson_ell.html
            https://www-k6.thinkcentral.com/content/hsp/reading/journeys/na/grk/Online_journeys_leveled_readers_9780547356860_/lesson_ol.html
            https://www-k6.thinkcentral.com/content/hsp/reading/journeys/na/grk/Online_journeys_leveled_readers_9780547356860_/lesson_al.html
        '''
        doc_type_r=doc_type if doc_type != 'al' else 'a'
        url_sub_this=url_base+'lesson_'+doc_type_r+'.html'
        
        #获取url_sub_this的网页
        page = urllib.urlopen(url_sub_this)


        #网页内容存到字符串中
        str_page=page.read()

        reg = r'launcher\(\'(.*pdf).*>(Lesson \d+:.*)</a>'
        pdf_re = re.compile(reg)
        pdfurl_name_list = re.findall(pdf_re,str_page)
        #if(pdfurl_name_list):
        #print url_sub_this
        #print '-------------------------------------'
        #print str_page
        #print '--------------------------------------------------'
        #print pdfurl_name_list

        get_file_url_name(doc_type, url_sub_this, pdfurl_name_list, i)

            
        


    '''
    <!DOCTYPE html PUBLIC "-//W3C//DTD html 4.0 Transitional//EN">
    <html>
    <head>
    <TITLE>Leveled Readers Kindergarten</TITLE>
    <meta name="Generator" content="EditPlus">
    <meta name="Author" content="">
    <meta name="Keywords" content="">
    <meta name="Description" content="">
    <link rel="stylesheet" type="text/css" href="css/main.css">
    <script type="text/javascript" src="scripts/common.js"></script>
    </head>
    <body>
    <div id="mainContainer">

            <!-- Header Image -->
            <div id="header"><img src="image/bl_grk.jpg" width="1014" height="355" border="0" alt=""></div>
                    <!-- Header Image end -->

            <!-- Lesson  List Start -->
            <div class="lessonList">
                    <table width="90%" border="0" cellspacing="" cellpadding="0">
    <tr class="Heading">

    </tr>

    <tr class="content" >
        <td><a href="#" tabindex=1 onclick="launcher('lr/bl/lesson1/lesson1.pdf');return false;">Lesson 1: Visiting Grandma
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and Grandpa</a></td>
        <td><a href="#" tabindex=11 onclick="launcher('lr/bl/lesson11/lesson11.pdf');return false;">Lesson 11: October Days<
    /a></td>
        <td><a href="#" tabindex=21 onclick="launcher('lr/bl/lesson21/lesson21.pdf');return false;">Lesson 21: The Show</a>
    </td>
        </tr>

        <tr class="content">
        <td><a href="#" tabindex=2 onclick="launcher('lr/bl/lesson2/lesson2.pdf');return false;">Lesson 2: My Backpack</a></
    td>
        <td><a href="#" tabindex=12 onclick="launcher('lr/bl/lesson12/lesson12.pdf');return false;">Lesson 12: Winter Vacati
    on</a></td>
        <td><a href="#" tabindex=22 onclick="launcher('lr/bl/lesson22/lesson22.pdf');return false;">Lesson 22: Our Family Va
    cation</a></td>
        </tr>

    <tr class="content" >
        <td><a href="#" tabindex=3 onclick="launcher('lr/bl/lesson3/lesson3.pdf');return false;">Lesson 3: My Dog</a></td>
        <td  ><a href="#" tabindex=13 onclick="launcher('lr/bl/lesson13/lesson13.pdf');return false;">Lesson 13: The Pet Sho
    w</a></td>
        <td  ><a href="#" tabindex=23 onclick="launcher('lr/bl/lesson23/lesson23.pdf');return false;">Lesson 23: The Vegetab
    le &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Garden</a></td>
    </tr>


    <tr class="content">
    <td><a href="#" tabindex=4 onclick="launcher('lr/bl/lesson4/lesson4.pdf');return false;">Lesson 4: The Fire Fighter</a
    ></td>
        <td><a href="#" tabindex=14 onclick="launcher('lr/bl/lesson14/lesson14.pdf');return false;">Lesson 14: At the Pond</
    a></td>
        <td><a href="#" tabindex=24 onclick="launcher('lr/bl/lesson24/lesson24.pdf');return false;">Lesson 24: Bugs for Dinn
    er</a></td>
    </tr>


    <tr class="content">
    <td  ><a href="#" tabindex=5 onclick="launcher('lr/bl/lesson5/lesson5.pdf');return false;">Lesson 5: At the Fair</a></
    td>
        <td  ><a href="#" tabindex=15 onclick="launcher('lr/bl/lesson15/lesson15.pdf');return false;">Lesson 15: Look Up!</a
    ></td>
        <td><a href="#" tabindex=25 onclick="launcher('lr/bl/lesson25/lesson25.pdf');return false;">Lesson 25: The Baker</a>
    </td>
    </tr>

    <tr class="content">
    <td><a href="#" tabindex=6 onclick="launcher('lr/bl/lesson6/lesson6.pdf');return false;">Lesson 6: The Market</a></td>

        <td><a href="#" tabindex=16 onclick="launcher('lr/bl/lesson16/lesson16.pdf');return false;">Lesson 16: Animals in th
    e Woods</a></td>
        <td><a href="#" tabindex=26 onclick="launcher('lr/bl/lesson26/lesson26.pdf');return false;">Lesson 26: Time for Brea
    kfast!</a></td>
    </tr>

    <tr class="content">
    <td><a href="#" tabindex=7 onclick="launcher('lr/bl/lesson7/lesson7.pdf');return false;">Lesson 7: A Walk in the &nbsp
    ;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Woods</a></td>
        <td><a href="#" tabindex=17 onclick="launcher('lr/bl/lesson17/lesson17.pdf');return false;">Lesson 17: Bug Parts</a>
    </td>
        <td><a href="#" tabindex=27 onclick="launcher('lr/bl/lesson27/lesson27.pdf');return false;">Lesson 27: Our Room</a><
    /td>
    </tr>

    <tr class="content">
    <td  ><a href="#" tabindex=8 onclick="launcher('lr/bl/lesson8/lesson8.pdf');return false;">Lesson 8: Let's Climb!</a><
    /td>
        <td  ><a href="#" tabindex=18 onclick="launcher('lr/bl/lesson18/lesson18.pdf');return false;">Lesson 18: The Sea</a>
    </td>
        <td><a href="#" tabindex=28 onclick="launcher('lr/bl/lesson28/lesson28.pdf');return false;">Lesson 28: Up and Away,
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Curious George</a>
    </td>
    </tr>

    <tr class="content">
    <td  ><a href="#" tabindex=9 onclick="launcher('lr/bl/lesson9/lesson9.pdf');return false;">Lesson 9: In the City</a></
    td>
        <td  ><a href="#" tabindex=19 onclick="launcher('lr/bl/lesson19/lesson19.pdf');return false;">Lesson 19: Taking Pict
    ures</a></td>
        <td><a href="#" tabindex=29 onclick="launcher('lr/bl/lesson29/lesson29.pdf');return false;">Lesson 29: Zoom!</a></td
    >
    </tr>

    <tr class="content">
    <td  ><a href="#" tabindex=10 onclick="launcher('lr/bl/lesson10/lesson10.pdf');return false;">Lesson 10: It's a Party!
    </a></td>
        <td><a href="#" tabindex=20 onclick="launcher('lr/bl/lesson20/lesson20.pdf');return false;">Lesson 20: Curious Georg
    e Visits &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Animal Fr
    iends</a></td>
        <td  ><a href="#" tabindex=30 onclick="launcher('lr/bl/lesson30/lesson30.pdf');return false;">Lesson 30: Our Class B
    and</a></td>
    </tr>

    </table>
            </div>
            <!-- Lesson List End -->

            <div id="footerbl"><img src="image/logo.jpg"  border="0" alt=""></div>

    </div>
    </body>
    </html>


    '''

    '''
    page = urllib.urlopen(url2)

    reg = r'launcher\(\'(.*pdf).*>(Lesson \d+:.*)</a>'
    pdf_re = re.compile(reg)
    pdfurl_name_list = re.findall(pdf_re,str_page)
    print imglist
    '''
