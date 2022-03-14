import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import preprocessor
import helper
import seaborn as sns

st.sidebar.title("Whatsapp Chat Analyser")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
     bytes_data = uploaded_file.getvalue()
     data = bytes_data.decode("utf-8")
     df = preprocessor.preprocess(data)

     # st.dataframe(df)

     user_list = df['user'].unique().tolist()
     user_list.remove('group_notification')
     user_list.sort()
     user_list.insert(0,'Overall')


     selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)

     if st.sidebar.button("Show Analysis"):

          st.header('Top Statistics')

          num_messages, words, num_media_message, num_deleted_message = helper.fetch_stats(selected_user, df)

          col1, col2, col3, col4 = st.columns(4)
          with st.container():

               with col1:
                    st.subheader("Total Messages")
                    st.title(num_messages)
               with col2:
                    st.subheader('Total Words')
                    st.title(words)
               with col3:
                    st.subheader('Media Sent')
                    st.title(num_media_message)
               with col4:
                    st.subheader('Deleted Message')
                    st.title(num_deleted_message)


          st.title('Monthly timeline')
          timeline = helper.monthly_timeline(selected_user, df)
          fig, ax = plt.subplots()
          ax.plot(timeline['time'], timeline['message'], color='green')
          plt.xticks(rotation='vertical')
          st.pyplot(fig)

          st.title('Activity Map')
          col1, col2 = st.columns(2)
          with col1:
              st.header('Most Busy Day')
              busy_day = helper.week_activity(selected_user, df)
              fig, ax = plt.subplots()
              ax.bar(busy_day.index, busy_day.values)
              plt.xticks(rotation='vertical')
              st.pyplot(fig)

          with col2:
               st.header('Most Busy Month')
               busy_month = helper.month_activity(selected_user, df)
               fig, ax = plt.subplots()
               ax.bar(busy_month.index, busy_month.values, color = 'orange')
               plt.xticks(rotation='vertical')
               st.pyplot(fig)



          st.title('Activity Heatmap')
          user_heatmap = helper.activity_heatmap(selected_user, df)
          fig, ax = plt.subplots(figsize = (24, 10))
          ax= sns.heatmap(user_heatmap)
          st.pyplot(fig, figsize = (24, 10))

          if(selected_user == 'Overall'):
               st.title('Most Busy Users')
               x, new_df = helper.most_busy_user(df)
               fig, ax = plt.subplots()

               col1, col2 = st.columns(2)

               with col1:
                    st.subheader('Top 5 Users')
                    ax.bar(x.index, x.values)
                    plt.xticks(rotation = 'vertical')
                    st.pyplot(fig)

               with col2:
                    st.subheader('All user with contribution')
                    st.dataframe(new_df)


          words = helper.most_used_words(selected_user, df)
          words_df = pd.DataFrame(Counter(words).most_common(20))
          words_df = words_df.rename(columns={0: 'Word', 1: 'Count'})
          emojis = helper.emoji_helper(selected_user, df)
          emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

          col5, col6 = st.columns(2)

          with col5:
               st.title('Most Used Words')
               st.dataframe(words_df)

          with col6:
               st.title('Emoji used')
               st.dataframe(emoji_df)

          st.subheader('Word Graph')
          fig, ax = plt.subplots()
          ax.barh(words_df['Word'], words_df['Count'])
          plt.xticks(rotation='vertical')
          st.pyplot(fig)










