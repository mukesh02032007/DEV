import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import datetime
import pytz
from matplotlib.ticker import MaxNLocator
from matplotlib import gridspec
import matplotlib.patches as mpatches
from scipy import ndimage
from scipy.interpolate import interp1d
data = [
    ["Project Update", "alice@example.com", "Mon, 01 Jan 2024 09:15:00 -0500", "bob@example.com", "", "1001"],
    ["Meeting Reminder", "bob@example.com", "Mon, 01 Jan 2024 11:30:00 -0500", "alice@example.com", "", "1002"],
    ["Lab Report Submission", "itsmeskm99@gmail.com", "Mon, 01 Jan 2024 14:45:00 -0500", "prof@example.com", "", "1003"],
    ["Weekend Plans", "charlie@example.com", "Fri, 05 Jan 2024 18:20:00 -0500", "itsmeskm99@gmail.com", "", "1004"],
    ["Follow-up: Project", "itsmeskm99@gmail.com", "Sat, 06 Jan 2024 10:05:00 -0500", "alice@example.com", "", "1005"],
    ["Invitation to Seminar", "prof@example.com", "Wed, 10 Jan 2024 08:00:00 -0500", "itsmeskm99@gmail.com", "", "1006"],
]
dfs = pd.DataFrame(data, columns=['subject','from','date','to','label','thread'])
dfs['date'] = pd.to_datetime(dfs['date'], errors='coerce', utc=True)
dfs = dfs[dfs['date'].notna()]
def extract_email_ID(string):
    email = re.findall(r'<(.+?)>', string)
    if not email:
        email = list(filter(lambda y: '@' in y, string.split()))
    return email[0] if email else np.nan
dfs['from'] = dfs['from'].apply(lambda x: extract_email_ID(x))
myemail = 'itsmeskm99@gmail.com'
dfs['label'] = dfs['from'].apply(lambda x: 'sent' if x == myemail else 'inbox')
dfs.drop(columns='to', inplace=True)
def refactor_timezone(x):
    est = pytz.timezone('US/Eastern')
    return x.astimezone(est)
dfs['date'] = dfs['date'].apply(lambda x: refactor_timezone(x))
dfs['dayofweek'] = dfs['date'].apply(lambda x: x.day_name())
dfs['dayofweek'] = pd.Categorical(dfs['dayofweek'],
    categories=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
    ordered=True)
dfs['timeofday'] = dfs['date'].apply(lambda x: x.hour + x.minute/60 + x.second/3600)
dfs['hour'] = dfs['date'].apply(lambda x: x.hour)
dfs['year_int'] = dfs['date'].apply(lambda x: x.year)
dfs['year'] = dfs['date'].apply(lambda x: x.year + x.dayofyear/365.25)
dfs.index = dfs['date']
del dfs['date']
print(dfs.index.min().strftime('%a, %d %b %Y %I:%M %p'))
print(dfs.index.max().strftime('%a, %d %b %Y %I:%M %p'))
print(dfs['label'].value_counts())
print(dfs.info())
print(dfs.head(10))
def plot_todo_vs_year(df, ax, color='C0', s=50, title=''):
    df.plot.scatter('year','timeofday',s=s,alpha=0.6,ax=ax,color=color)
    ax.set_ylim(0,24)
    ax.yaxis.set_major_locator(MaxNLocator(8))
    ax.set_yticklabels([datetime.datetime.strptime(str(int(np.mod(ts,24))),"%H").strftime("%I %p") for ts in ax.get_yticks()])
    ax.set_title(title)
    ax.grid(ls=':',color='k')
    return ax
sent = dfs[dfs['label']=='sent']
received = dfs[dfs['label']=='inbox']
fig, ax = plt.subplots(nrows=1,ncols=2,figsize=(12,4))
plot_todo_vs_year(sent, ax[0], title='Sent')
plot_todo_vs_year(received, ax[1], title='Received')
plt.show()
sdw = sent.groupby('dayofweek').size() / len(sent)
rdw = received.groupby('dayofweek').size() / len(received)
df_tmp = pd.DataFrame({'Outgoing Email': sdw, 'Incoming Email': rdw})
df_tmp.plot(kind='bar', rot=45, figsize=(8,5), alpha=0.5)
plt.ylabel('Fraction of weekly emails')
plt.grid(ls=':', color='k', alpha=0.5)
plt.show()
