import re
import pandas  as pd

def preprocess(data):
    pattern = "\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{1,2}\s\w{1,2}\s-\s"

    messages = re.split(pattern, data)[1:]
    if len(messages) == 0:
        pattern_alt = "\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{1,2}\s-\s"
        messages = re.split(pattern_alt, data)[1:]
    dates = re.findall(pattern, data)
    if len(dates) ==0:
        pattern_alt = "\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{1,2}\s-\s"
        dates = re.findall(pattern_alt, data)

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    if (len(df['message_date'][0])== 22):
        if ((df['message_date'][0][-4] == 'm') or (df['message_date'][0][-4] == 'M')):
            try:
                df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %I:%M %p - ')
            except(ValueError):
                df['message_date'] = pd.to_datetime(df['message_date'], format='%m/%d/%Y, %I:%M %p - ')
        else:
            try:
                df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %H:%M - ')
            except(ValueError):
                df['message_date'] = pd.to_datetime(df['message_date'], format='%m/%d/%Y, %H:%M - ')
    else:
        if ((df['message_date'][0][-4] == 'm') or (df['message_date'][0][-4] == 'M')):
            try:
                df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p - ')
            except(ValueError):
                df['message_date'] = pd.to_datetime(df['message_date'], format='%m/%d/%y, %I:%M %p - ')
        else:
            try:
                df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %H:%M - ')
            except(ValueError):
                df['message_date'] = pd.to_datetime(df['message_date'], format='%m/%d/%y, %H:%M - ')

    df['message_date'] = pd.to_datetime(df['message_date'], format='%x, %I:%M %p - ')

    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(['user_message'], axis=1, inplace=True)

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['day'] = df.date.dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df.date.dt.minute
    df['month_num'] = df['date'].dt.month
    df['day_name'] = df['date'].dt.day_name()

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))
    df['period'] = period

    return  df