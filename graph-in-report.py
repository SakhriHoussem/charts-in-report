import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from datetime import datetime

User_Location =[{'User_Location': 'Ontario, Canada', 'User_Location__count': 1}, {'User_Location': '', 'User_Location__count': 7}, {'User_Location': 'togo', 'User_Location__count': 1}, {'User_Location': '?????-?????????, ??????', 'User_Location__count': 1}, {'User_Location': '????', 'User_Location__count': 1}, {'User_Location': 'Earth', 'User_Location__count': 1}, {'User_Location': 'Bruxelles, Belgique', 'User_Location__count': 1}, {'User_Location': 'Wilderness, USA', 'User_Location__count': 1}, {'User_Location': '??', 'User_Location__count': 1}]
Tweet_Created = [{'Tweet_Created_At': '2018-04-29 23:58:24', 'Tweet_Created_At__count': 10}, {'Tweet_Created_At': '2018-04-29 23:57:09', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:55:10', 'Tweet_Created_At__count': 8}, {'Tweet_Created_At': '2018-04-29 23:54:48', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:54:42', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:51:41', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:50:52', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:50:49', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:50:37', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:49:32', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:48:49', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:48:06', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:45:59', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:45:00', 'Tweet_Created_At__count': 1}, {'Tweet_Created_At': '2018-04-29 23:42:24', 'Tweet_Created_At__count': 1}]

graphs = 3
fig = plt.figure(figsize=(10, 20))

xaxes = []
yaxes = []

# first graph
graph = 1
sub = fig.add_subplot(graphs,1,graph)
sub.set_title('tweet volume (by seconds)')
for data in Tweet_Created:
    xaxes.append(datetime.strptime(data['Tweet_Created_At'],'%Y-%m-%d %H:%M:%S'))
    yaxes.append(data['Tweet_Created_At__count'])
sub.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
plt.xticks(rotation=60)
sub.plot(xaxes,yaxes)

# second graph
graph = 2
sub = fig.add_subplot(graphs,1,graph)
sub.set_title('tweet volume (by Location)')
xaxes = []
yaxes = []

for data in User_Location:
    xaxes.append(data['User_Location'])
    yaxes.append(data['User_Location__count'])

yaxes = list(map(lambda x: x/sum(yaxes)*100,yaxes))

sub.pie(yaxes, labels=xaxes, autopct='%1.1f%%',shadow=True, startangle=90)
sub.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
# filename = 'plot'+str(name[0])+str(strftime("%d%m%Y-%H%M%S"))+'.pdf'
filename = 'plot'
plt.savefig(filename+'.pdf')


