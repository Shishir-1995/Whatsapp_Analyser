import emoji


def fetch_stats(selected_user, df):

    if selected_user != "Overall":
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]
    words = []
    for word in df['message']:
        words.extend(word.split())

    num_media_message = df[df['message']=='<Media omitted>\n'].shape[0]
    num_deleted_message = df[df['message']=='This message was deleted\n'].shape[0]

    return num_messages, len(words), num_media_message, num_deleted_message


def most_busy_user(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index':'name', 'user':'percentage'})

    return x, df


def most_used_words(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]

    temp = df[df['user']!= 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']
    temp = temp[temp['message'] != 'This message was deleted\n']

    words = []
    for message in temp['message']:
        words.extend(message.split())

    return words


def emoji_helper(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.UNICODE_EMOJI['en']])

    return emojis

def monthly_timeline(selected_user, df):

    if selected_user != "Overall":
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + '-' + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline

def week_activity(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()


def activity_heatmap(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return user_heatmap

