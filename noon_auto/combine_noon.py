from datetime import datetime,timedelta

# 載入html檔案
head = open('head.html','r',encoding = 'utf8').read()
title = open('separate/title.html','r',encoding = 'utf8').read()
ythot10 = open('separate/ythot10.html','r',encoding = 'utf8').read()
ytnews = open('separate/ytnews.html','r',encoding = 'utf8').read()
yt24fast = open('separate/24h_fast.html','r',encoding = 'utf8').read()
fb_fans = open('separate/fb_fans.html','r',encoding = 'utf8').read()
ppt_hate = open('separate/ptt_hate.html','r',encoding = 'utf8').read()

# 建立昨天跟明天的日期
now_time = datetime.now()
today = datetime.now().strftime('%Y-%m-%d')
yesterday = now_time + timedelta(days = -1)
yesterday = yesterday.strftime('%Y-%m-%d')
tomorrow = now_time + timedelta(days = 1)
tomorrow = tomorrow.strftime('%Y-%m-%d')

# 最新的網頁不要有後一天的選項
toggle = ('<div style="text-align:left;">'+
'<span style="color:#000000;font-weight:bold;margin-left:40px;"><a href="http://10.227.58.87/noon-news/history/{}/">前一天</a></span>'.format(yesterday)+
'<span style="color:#000000;font-weight:bold;margin-left:30px;"><a href="http://10.227.58.87/noon-news/">午報最新</a></span>'+
'<span style="color:#000000;font-weight:bold;margin-left:30px;"><a href="http://10.227.58.87/">主頁</a></span>'+
'</div>'
)

# 有前一天跟後一天的選項
toggle_history = ('<div style="text-align:left;">'+
'<span style="color:#000000;font-weight:bold;margin-left:40px;"><a href="http://10.227.58.87/noon-news/history/{}/">前一天</a></span>'.format(yesterday)+
'<span style="color:#000000;font-weight:bold;margin-left:40px;"><a href="http://10.227.58.87/noon-news/history/{}/">後一天</a></span>'.format(tomorrow)+
'<span style="color:#000000;font-weight:bold;margin-left:40px;"><a href="http://10.227.58.87/noon-news/">午報最新</a></span>'+
'<span style="color:#000000;font-weight:bold;margin-left:30px;"><a href="http://10.227.58.87/">主頁</a></span>'+
'</div>'
)


time_now = datetime.now().strftime('%Y-%m-%d_%H：%M')
time_now = str(time_now)

# 一併建立備份檔，留存用
rw = open('index.html','w',encoding = 'utf8')
rw_backup = open('../../晨午晚報_資料/history/noon/午報 - {}.html'.format(time_now),'w',encoding = 'utf8')

rw.write(head+title+toggle+ythot10+ytnews+yt24fast+fb_fans+ppt_hate)
#rw.write(head+title+toggle+ythot10+ytnews+yt24fast+ppt_hate)
rw_backup.write(head+title+toggle_history+ythot10+ytnews+yt24fast+fb_fans+ppt_hate)
#rw_backup.write(head+title+toggle_history+ythot10+ytnews+yt24fast+ppt_hate)

rw.close()
rw_backup.close()
