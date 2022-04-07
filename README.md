# Keyword Research Tool in Python
Build a Keyword research tool with google autocomplete suggestions

I reversed engineer two big websites, answerthepublic, and keywordtool.io. and I tried to develop a free alternative!

#What is Answerthepublic.com
Answerthepublic.com is a website that allows users to type in a keyword or phrase and receive a list of related questions that people have searched for on the internet. This can be useful for content creators who are looking for ideas for new articles or blog posts, as well as for people who are looking for answers to specific questions.

#What is Keywordtool.io
Keywordtool.io is a keyword research and analysis tool that helps users find and analyze the best keywords for their website or online business.


After a couple of days researching and trying to understand how both sites work and find a way to develop a keyword tool, finally I discovered that both tools are using google autocomplete suggestion to generate the keywords.
Example: Open Google, and write “python f“, you will see the google will suggest around 10 keyword ideas starting with “python” and letter “f“

#How To Read Google autosuggestions programmatically?
Now it is time to read and automate this process in our code!

We have to approaches:
1. Using Web Automation and Scraping
2. Using Google Search Free API Call
I chose the second approach, simply because with web automation, the operation will be slower, and you may get Recaptcha to solve, and things will be complicated.

#The Magical API Call:
http://google.com/complete/search?output=toolbar&gl=us&q=github
You can change the country, and the query to get google autosuggestion in XML format using this call.


Check out the full video here:
https://youtu.be/zU7ofxsjzsE
