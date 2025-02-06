#Mt is good for i/o like reading files or getting data from Apis

import threading
import time
#ex have chores

def walk_dog(first,last):
    time.sleep(8)
    print(f"The dawg {first} {last} has been walked")

def take_out_thrash():
    time.sleep(2)
    print("You take out the thrash")

def get_mail():
    time.sleep(4)
    print("You are getting the mail")

#keyword arg of target end arg with comma to let know its a tuple
chore1_thread = threading.Thread(target=walk_dog,args=("Bob","Jr",))
chore1_thread.start()
chore2_thread = threading.Thread(target=take_out_thrash)
chore2_thread.start()
chore3_thread = threading.Thread(target=get_mail)
chore3_thread.start()

#wait for threads to finish using join
chore1_thread.join()
chore2_thread.join()
chore3_thread.join()

print("All tasks have been completed")
#walk_dog()take_out_thrash()get_mail()