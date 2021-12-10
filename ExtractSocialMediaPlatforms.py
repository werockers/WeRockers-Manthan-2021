# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 13:09:55 2021

@author: WeRockers
"""

import streamlit as st
import pandas as pd

user_input = st.text_input("Enter the Profile (URL): ", "")
st.button("Submit")

user_name = user_input.rsplit('/', 1)[-1]
st.header("Username: ")
st.subheader(user_name)

# 'Retrieval of Contact details from social media account of terrorists'
import tweepy

api_key = "U1d6W3VZP5dlh1TPLflGvXjhO"
api_secret_key = "OLd3dwvwGuzEHasgx0FpWB8OnL5DjMZWu6ql9VCaPyLkLG1a79"
access_token = "1040850962594713600-F4Uf0izGQXZKtfr17zDgI13RZaOwVi"
access_token_secret = "p08gQA0bLNxg4sZQi0ZoBlL76n7gelv9OPjqE1S4XKQlu"

# Create The Authenticate Object
authenticate = tweepy.OAuthHandler(api_key, api_secret_key)

# Set The Access Token & Access Token Secret
authenticate.set_access_token(access_token, access_token_secret)

# Create The API Object
api = tweepy.API(authenticate, wait_on_rate_limit = True)

tweets = api.user_timeline(screen_name = user_name, count = 5, lang = "en", tweet_mode = "extended")
# get the last 200 tweets from the twitter handle "_____"
st.header("Tweets by: ")
st.subheader(user_name)


df = pd.DataFrame([[tweet.full_text, tweet.user.screen_name, tweet.user.location] for tweet in tweets], columns = ["tweet", "username","location"])
st.dataframe(df)
for tweet in tweets:
    st.caption(f"- {tweet.full_text}")
    
st.header("Mentions in the tweets: ")
# describe the dataframe 'tweet'
#st.dataframe(df['tweet','username','location'])


# extract usernames
import re
def ExtractUsers(a):
  return re.findall("@([a-zA-Z0-9_]+)", a)

df['tweet1'] = df['tweet'].apply(ExtractUsers)
df['tweet1']


#Write data to CSV file
import csv
f = open('Manthan_usernames.csv', 'w')
writer = csv.writer(f)
for i in df['tweet1']:
  writer.writerow(i)
f.close()


# Scrape website details phone number and email

#user_website = st.text_input("Enter the Website (URL): ", "")
#st.button("Exatrct Emails from Website")

st.header("Exatrct Emails and contact details from Website")

import pandas as pd
import requests
import bs4



src_df = pd.read_csv('src_file.csv')


def get_phone(soup):
    try:
        phone = soup.select("a[href*=callto]")[0].text
        return phone
    except:
        pass

    try:
        phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-][2-9][0-9]{2}[-][0-9]{4}\b', response.text)[0]
        return phone
    except:
        pass

    try:
       phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b', response.text)[-1]
       return phone
    except:
        print ('Phone number not found')
        phone = ''
        return phone



def get_email(soup):
    try:
        email = re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', response.text)[-1]
        return email
    except:
        pass

    try:
        email = soup.select("a[href*=mailto]")[-1].text
    except:
        print ('Email not found')
        email = ''
        return email


for i, row in src_df.iterrows():
    url = 'http://www.' + row['website']
    try:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
    except:
        print ('Unsucessful: ' + str(response))
        continue

    phone = get_phone(soup)
    email = get_email(soup)

    src_df.loc[i,'Phone'] = phone
    src_df.loc[i,'Email'] = email
    print ('website:%s\nphone: %s\nemail: %s\n' %(url, phone, email))

src_df.to_csv('output.csv', index=False)

st.dataframe(src_df)



# Sherlock

import os
os.system('python ./sherlock/sherlock/sherlock.py babydew5 > sherlock.txt')
f = open("./sherlock.txt", "r")
st.write(f.read())
st.write("Sherlock txt file created")

# infoga to retrive IP Address
ip_add = st.text_input("Enter domain name: ", "")
st.button("Get IP Address Details")

import os
os.system('python ./Infoga/infoga.py --domain welingkar.org --source all --breach -v 2 --report ./welingkarorg.txt')
f = open("./Infoga/welingkarorg.txt", "r")
st.write(f.read())



# IP Address details
import requests

ip_add = st.text_input("Enter IP Address: ", "")
st.button("Get Details from IP Address")

response = requests.post("http://ip-api.com/batch", json=[
  {"query": ip_add}
]).json()

for ip_info in response:
    for k,v in ip_info.items():
        st.write(k,v)
        
    st.write("\n")



#df_details = pd.DataFrame(ip_info)
#df_details = pd.DataFrame(ip_info.items(), columns=['Key', 'Value'])
#st.write(df_details)

import geocoder
import folium
import streamlit.components.v1 as components

#ip_add = "104.244.42.65"
geo_location = geocoder.ip(ip_add)
location_cord = geo_location.latlng
print("Lat: " + str(location_cord[0]))
print("Lng: " + str(location_cord[1]))


map_data = folium.Map(location=location_cord, zoom_start=12)
folium.CircleMarker(location=location_cord, radius=120, popup="Yorkshire").add_to(map_data)
folium.Marker(location=location_cord, popup="Yorkshire").add_to(map_data)
map_data.save("map_location.html")
HtmlFile = open("map_location.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code)


# Send Email to get the IP Address

# =============================================================================
# import smtplib, ssl
# #import js2py
# 
# port = 587  # For starttls
# smtp_server = "smtp.gmail.com"
# sender_email = "malvikap0307@gmail.com"
# receiver_email = "subodh.deolekar@welingkarmail.org"
# password = input("Type your password and press enter:")
# message = """\
# Subject: Hare and the tortoise
# 
# A Hare was making fun of the Tortoise one day for being so slow. ... 
# The Tortoise meanwhile kept going slowly but steadily, and, after a time, passed the place where the Hare was sleeping. 
# But the Hare slept on very peacefully; and when at last he did wake up, the Tortoise was near the goal..
# 
# """
# 
# context = ssl.create_default_context()
# with smtplib.SMTP(smtp_server, port) as server:
#     server.ehlo()  # Can be omitted
#     server.starttls(context=context)
#     server.ehlo()  # Can be omitted
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)
# =============================================================================
    






    
    
    