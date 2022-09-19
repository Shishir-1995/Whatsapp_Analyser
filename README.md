# Whatsapp_Analyser

This analyses your whatsapp chat which is uploaded in .txt format and gives you insight on the group chat as well as personal chat. It doesn't read or save the content of the chat to maintain and respect the privacy of the user.


### Guideline to extract chat

1. Open the individual or group chat.
2. Tap More : options > More > Export chat.
3. Choose to export without media.


## Introduction 
<hr>
Whatsapp has been the most used mode of communication and has been an efficient one too. It consists of
many conversations in groups and individuals. So, there might be some hidden facts in them. This project takes
those chats and provide a deep analysis of that data. Being any topic, the chats are it provide the analysis in an
efficient and accurate way. The main advantage of this project is that it has been built using libraries like
pandas, seaborn, matplotlib, emoji etc. They are used to create data frames and plot graphs in an efficient way.

Tech Used: Whatsapp Chat, Python, Streamlit, Analysis, Nature Language Processing, Emoji, Pandas, Matplotlib

## How it works
<hr>

- After uploading the chat, it make use of Regular Expression to seggregate different components of a whatsapp chat as any whatsapp chat follows a specific pattern
 Date, Time - Person : Message
- Dates can be of various format like dd/mm/yy, dd/mm/YYYY, mm/dd/YYYY, mm/dd/yy so initial Idea was to make user select the date format but then later it was added and 
  now it works on all possible date formats
- Similarily, time can be of 12h format or 24 hr format 
- After seaparting different part of the chat , it groups the words and emoji of the message section to find the highest words frequency. It make use of NLP Bag of words.
- The groups are formed on Years, Months, Dates, Time, User, Words
- After extracting all the data it plots them in the form of graph to show them visually

## Modules used
- Streamlit
- Matplotlib
- Word Cloud
- Pandas

Tech Stack : Python | Jupyter notes

## Flow-Chart 
  ![FLow_chart](https://user-images.githubusercontent.com/70420133/191099294-22c0f659-b621-4557-a125-92be84ed9253.jpg)
  
  
## Glimpse

1. Landing Page
This Page also contains the detail about extracting whatsapp chat in txt without media files. The Upload button is in sidebar menu.
![Home_page](https://user-images.githubusercontent.com/70420133/191101613-548d12af-aa5d-48c2-8a94-aae916879a57.jpg)
<hr>

2. After Upload
After Uploading the file , the main page will not get updated with the statistics and analysis. Select the type of analysis you want and then choose *Show Analysis*
![After_Upload](https://user-images.githubusercontent.com/70420133/191102285-92c9a7d2-eed2-4e5d-be68-9899265e909e.jpg)
<hr>

3. After Analysis
The initial analysis is little numerical as you will be seeing the numerical data on different analysis
![Stats_numbers](https://user-images.githubusercontent.com/70420133/191102631-9be216b9-e41a-4c94-adca-6b58f87ff813.jpg)
<hr>

4. Graphs & Maps
Then it shows different types of data as graphs and maps to make it visually more appealing

![Monthly-timeline](https://user-images.githubusercontent.com/70420133/191102871-636713ac-e1cf-4e3b-917e-314606241ba7.jpg)
![activity-map](https://user-images.githubusercontent.com/70420133/191102903-85d53501-22ce-4487-8dec-7ccf062110f3.jpg)
![heatmap](https://user-images.githubusercontent.com/70420133/191102954-08a9d9dc-f882-428f-8099-1d4b1d81ef65.jpg)

<hr>

### Read more about it <a href="https://www.irjmets.com/uploadedfiles/paper//issue_5_may_2022/22029/final/fin_irjmets1651575263.pdf" alt="NLP">here</a>

#### Do checkout the project <a href="http://whatsapp-shishir.herokuapp.com/" alt="Project">Whatsapp_Analyse</a>





