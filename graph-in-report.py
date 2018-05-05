import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from datetime import datetime
from time import strftime

# data
User_Location =[{'User_Location': 'Ontario, Canada', 'User_Location__count': 1}, {'User_Location': '', 'User_Location__count': 7}, {'User_Location': 'togo', 'User_Location__count': 1}, {'User_Location': '?????-?????????, ??????', 'User_Location__count': 1}, {'User_Location': '????', 'User_Location__count': 1}, {'User_Location': 'Earth', 'User_Location__count': 1}, {'User_Location': 'Bruxelles, Belgique', 'User_Location__count': 1}, {'User_Location': 'Wilderness, USA', 'User_Location__count': 1}, {'User_Location': '??', 'User_Location__count': 1}]
Tweet_Created = [{'Tweet_Created_At': '2018-04-29 23:58:24', 'Tweet_Created_At__count': 10}, {'Tweet_Created_At': '2018-04-29 23:57:09', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:55:10', 'Tweet_Created_At__count': 8}, {'Tweet_Created_At': '2018-04-29 23:54:48', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:54:42', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:51:41', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:50:52', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:50:49', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:50:37', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:49:32', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:48:49', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:48:06', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:45:59', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:45:00', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:42:24', 'Tweet_Created_At__count': 1}]



# configuration
project_name = 'project name'
graphs = 2
rowspan = 4
filename = 'report'
fig = plt.figure(figsize=(5, 10))

# header
sub = plt.subplot2grid((graphs*rowspan+1,1),(0,0))
sub.axis('off')
sub.text(-0.06,0.1,project_name)
sub.text(0.03,0.1,strftime("%d/%m/%Y"))
sub.plot()

# first graph
sub = plt.subplot2grid((graphs*rowspan+1,1),(1,0),rowspan=rowspan-2)
sub.axis('on')
xaxes = []
yaxes = []
sub.set_title('tweet volume (by seconds):\n', color='blue', loc='left')
for data in Tweet_Created:
    xaxes.append(datetime.strptime(data['Tweet_Created_At'],'%Y-%m-%d %H:%M:%S'))
    yaxes.append(data['Tweet_Created_At__count'])
sub.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d\n %H:%M'))
plt.xticks(rotation=60)
# plot data
sub.plot(xaxes,yaxes)

# second graph
graph = 2
sub = plt.subplot2grid((graphs*rowspan+1,1),(rowspan+1,0),rowspan=rowspan-1)
sub.set_title('tweet volume (by Location):\n', color='blue', loc='left')
xaxes = []
yaxes = []

for data in User_Location:
    xaxes.append(data['User_Location'])
    yaxes.append(data['User_Location__count'])
# convert data to %
yaxes = list(map(lambda x: x/sum(yaxes)*100,yaxes))

# plot data
sub.pie(yaxes, labels=xaxes, autopct='%1.1f%%',shadow=True, startangle=90)
sub.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# save report
# filename = 'plot'+str(name[0])+str(strftime("%d%m%Y-%H%M%S"))+'.pdf'
plt.savefig(filename+'.pdf')
