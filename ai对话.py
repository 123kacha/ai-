#!/usr/bin/env python
# coding: utf-8

# In[48]:


import tkinter as tk
import openai
import threading

openai.api_key = "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"  # supply your API key however you choose

def submit_text():
   # Get the content of the text box and print it
   text = text_input.get("1.0", "end-1c") # Get text without the newline character
   text_doing.insert(tk.END, "莫着急，正在等待网页响应中。。。")
   completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": text}])
   print(completion.choices[0].message.content)
   text_doing.delete("1.0", 'end')
   text_output.insert(tk.END, completion.choices[0].message.content + '\n')
def start_submit_text():
    threading.Thread(target=submit_text).start()

# Create the main windo
root = tk.Tk()

# Create a text box
text_input = tk.Text(root, height=20, width=100,font=(16))
text_input.pack()

text_output = tk.Text(root, height=20, width=100,font=(16))
text_output.pack()
text_doing = tk.Text(root, height=1, width=30,font=(16))
text_doing.place(x=100,y=100)
text_doing.pack()
# Create a button
submit_button = tk.Button(root, text="提交", command=start_submit_text,height=5,width=50)
submit_button.pack()

# Start the main loop
root.mainloop()

