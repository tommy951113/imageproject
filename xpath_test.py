# -*- coding:utf-8 -*-
from lxml import etree
import re

html = '''听力语料库打卡。一章的5节，想要结束的心是有的，能力好弱啊。。。(ง •̀_•́)ง <a data-url=\"http://t.cn/z8ISdiX\" href=\"https://m.weibo.cn/p/index?containerid=2306570042B2094655D665A4FC4792&luicode=10000011&lfid=100101B2094655D665A4FC4792_-_weibofeed\" data-hide=\"\"><span class='url-icon'><img style='width: 1rem;height: 1rem' src='https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_location_default.png'></span><span class=\"surl-text\">南京·东南大学文科楼</span></a>'''
html2 = '''85岁老先生，娓娓道来，一场法治的学术盛宴，一份职业，融入生命，真的很珍贵，不忘初心，加油！ <a data-url=\"http://t.cn/z8ISdiX\" href=\"https://m.weibo.cn/p/index?containerid=2306570042B2094655D665A4FC4792&luicode=10000011&lfid=100101B2094655D665A4FC4792_-_weibofeed\" data-hide=\"\"><span class='url-icon'><img style='width: 1rem;height: 1rem' src='https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_location_default.png'></span><span class=\"surl-text\">南京·东南大学文科楼</span></a>'''
html3 = '''学术努力程度在学生时代末期达到了顶点<span class=\"url-icon\"><img alt=[跪了] src=\"//h5.sinaimg.cn/m/emoticon/icon/default/d_guile-7b3e474f7f.png\" style=\"width:1em; height:1em;\" /></span><span class=\"url-icon\"><img alt=[跪了] src=\"//h5.sinaimg.cn/m/emoticon/icon/default/d_guile-7b3e474f7f.png\" style=\"width:1em; height:1em;\" /></span><span class=\"url-icon\"><img alt=[跪了] src=\"//h5.sinaimg.cn/m/emoticon/icon/default/d_guile-7b3e474f7f.png\" style=\"width:1em; height:1em;\" /></span> <a data-url=\"http://t.cn/z8ISdiX\" href=\"https://m.weibo.cn/p/index?containerid=2306570042B2094655D665A4FC4792&luicode=10000011&lfid=100101B2094655D665A4FC4792_-_weibofeed\" data-hide=\"\"><span class='url-icon'><img style='width: 1rem;height: 1rem' src='https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_location_default.png'></span><span class=\"surl-text\">南京·东南大学文科楼</span></a>'''
# html = '<div><ul>            <li class="item-0"><a href="link1.html">first item</a></li>            <li class="item-1"><a href="link2.html">second item</a></li>            <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>            <li class="item-1"><a href="link4.html">fourth item</a></li>            <li class="item-0"><a href="link5.html">fifth item</a></li>        </ul>    </div>'
# data = etree.HTML(html)
# result = data.xpath('//a')
# result = etree.tostring(result[0])
# html = html.replace(result,'')
# print(html)
# pass
# res = etree.tostring(result[0]).decode('utf-8')
# fin = html.replace(res,'')
# print(fin)

html = re.sub( r'<.+>','',html)
# print(html)
pass