#!/usr/bin/env python
# coding: utf-8

# In[6]:


s = "India is a land of ancient civilization. India's social, economic, and cultural configurations are the products of a long process of regional expansion. Indian history begins with the birth of the Indus Valley Civilization and the coming of the Aryans. These two phases are usually described as the pre-Vedic and Vedic age. Hinduism arose in the Vedic period. The fifth century saw the unification of India under Ashoka, who had converted to Buddhism, and it is in his reign that Buddhism spread in many parts of Asia. In the eighth century Islam came to India for the first time and by the eleventh century had firmly established itself in India as a political force. It resulted into the formation of the Delhi Sultanate, which was finally succeeded by the Mughal Empire, under which India once again achieved a large measure of political unity. It was in the 17th century that the Europeans came to India. This coincided with the disintegration of the Mughal Empire, paving the way for regional states. In the contest for supremacy, the English emerged 'victors'. The Rebellion of 1857-58, which sought to restore Indian supremacy, was crushed; and with the subsequent crowning of Victoria as Empress of India, the incorporation of India into the empire was complete. It was followed by India's struggle for independence, which we got in the year 1947.India Timeline Indian timeline takes us on a journey of the history of the subcontinent. Right from the ancient India, which included Bangladesh and Pakistan, to the free and divided India, this time line covers each and every aspect related to the past as well as present of the country. Read on further to explore the timeline of India. Economic History of India Indus valley civilization, which flourished between 2800 BC and 1800 BC, had an advanced and flourishing economic system. The Indus valley people practiced agriculture, domesticated animals, made tools and weapons from copper, bronze and tin and even traded with some Middle East countries."
print (s)


# In[99]:


import operator
encrypttext = ""
size = len(s)-1
for i in range(len(s)):
    s = s.lower()
    if ((s[i].isalpha())):
        text =((ord(s[i])+3) - 97 ) % 26
        text +=97
        encrypttext+=chr(text)

    else:
        encrypttext += s[i]
print (encrypttext)

res = {} 

for keys in encrypttext:
    if (keys.isalpha()):
        res[keys] = res.get(keys, 0) + 1

total=0
for i in range (97,123):
    if (res[chr(i)]):
        total = total + res[chr(i)]
    else :
        res[chr[i]]=0



for i in range (97,123):
    res[chr(i)] = round(((res[chr(i)]/total)*100),2)
print (res)

sorted_res = sorted(res.items(),key=operator.itemgetter(0))
# printing result  
print (" \n" +  str(sorted_res)) 
for i in range(0,26):
    print (sorted_res[i])

    
import matplotlib.pyplot as plt
from math import log
#plt.scatter(*sorted_res)

x, y = zip(*sorted_res) # unpack a list of pairs into two tuples
x_months=['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

plt.bar(x_months, y, color='b')
plt.xticks(x_months, x_months, rotation='vertical')
plt.tight_layout()
plt.show()









