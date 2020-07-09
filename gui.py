from check import find
from display_map import show_map
#import time
import tkinter
def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  
    msg_list.insert(tkinter.END, "You: "+msg)
    if msg=="y" or msg=="n" or msg=="N" or msg=="Y":
        if(msg=="Y" or msg=="y"):
            msg_list.insert(tkinter.END, "Bot: Showing map...")
        show_map(msg)
        """if(msg=="N" or msg=="n"):
            msg_list.insert(tkinter.END, "Bot: Your decision doesn't matter. I'll show it anyways *_*")
            
            msg_list.insert(tkinter.END, "Bot: Showing map... 凸ಠ益ಠ)凸")
            #time.sleep(1)
            show_map('y')"""
        
    else:
        response=find(msg)
        msg_list.insert(tkinter.END, "Bot: "+response)
        msg_list.insert(tkinter.END, "Bot: Do you want to view the map? Y/N")
        #c=input()
        
top = tkinter.Tk()
top.title("NaviBot")
messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
msg_list = tkinter.Listbox(messages_frame, height=35, width=60, yscrollcommand=scrollbar.set)
msg_list.insert(tkinter.END,"Bot: Enter your destination UwU")
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()
entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()
#top.protocol("WM_DELETE_WINDOW", on_closing)
tkinter.mainloop()
