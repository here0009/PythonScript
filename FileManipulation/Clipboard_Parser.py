# coding: utf-8

# # Clipboard Parser
# **Input:** texts that I want to add in note.
# 
# **Process:** 
# 1. strip the \n after each line.
# 2. Attach it to the content previously stored.
# 
# **Output:**
# borad_contents.txt that contain the the contents from the clipboard 
#Maybe later it can contain images

# In[1]:

import clipboard
import sys
import os
import time


# In[2]:

def text_format(text):
    output_text = text.replace('\r\n', ' ')
    # output_text = output_text + '\n'
    return output_text


# In[5]:

previous_value = ""
line_number = 0
# sys.stdout=open('clipboard_content.txt','w',encoding='utf-8')
fhand = open('board_content.txt','w',encoding='utf-8')
# fhand = open('board_content.txt','w',encoding='GB2312')
while True:
    current_value = clipboard.paste()
    if current_value != previous_value:
        line_number +=1
        current_value_formatted = text_format(current_value)
        previous_value = current_value
        fhand.write(current_value_formatted+'\n')
        print("Write {:d} lines.".format(line_number))
    time.sleep(2)
fhand.close()