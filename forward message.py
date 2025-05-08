# first of all import requests and threading 
import requests 
import threading
import os
import dotenv
dotenv.load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
# mention chat id of person B and from chat id of person A with message id because here we want to forward a message from A to B 
chat_id =		5211817036
from_chat_id=	5412578346
message_id=364
# function with parameters 
def forward_message(chat_id,from_chat_id,message_id):
    try:     ##check type of errors 
        # respose variable store the entire path of forward msg 
        response = requests.get(f"https://api.telegram.org/bot{TOKEN}/forwardMessage?chat_id={chat_id}&from_chat_id={from_chat_id}&message_id={message_id}")
        # print("STATUS:", response.status_code)
        # print response in json file 
        print(response.json())


        # type of error 
    except Exception as e:
        print("ERROR:", e)   

# thread for sending that msg in multiple times 
#     list_of_threads = []
#     for i in range(2):
#         # t variable store the info of threading 
#         t = threading.Thread(target = forward_message,args =(chat_id,from_chat_id,message_id))
#         list_of_threads.append(t)   ##append the response 
#         t.start()

# # here we want to add multiple thread  and join them 
#     for thread1 in list_of_threads:
#         thread1.join()
#         print("all thread finished")
forward_message(chat_id,from_chat_id,message_id)


## when we using thread it does not show output 