# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from API's
#                  threading.Thread(target=my_myfunction)

import threading
import time
import datetime

def walk(first_name,last_name):
    time.sleep(8)
    print(f"{first_name} {last_name} Went for walk .")

def take_out_garbage(qty):
    time.sleep(2)
    print(f"Took {qty} qty garbage out .")

def get_mail(now):
    time.sleep(4)
    print(f"sent mail to friend at {now}.")

work1 = threading.Thread(target=walk,args=("kakashi","hatake"))
work2 = threading.Thread(target=take_out_garbage,args=("large",))   # args used to send parameters to target functions but beaware sent parameters are in form of tuple so place a comma side of parameter if only sending one parameter for clarifing compiler that you were sending tuple .
work3 = threading.Thread(target=get_mail,args=(datetime.datetime.now(),))

work1.start()
work2.start()   # start exceution of created threads .
work3.start()

work1.join()
work2.join()    # join is used that the 3 threads are joined to one another and next line excecuted after the threads are excecuted .
work3.join()

print("All works are complete")