import pywinauto
import time
import socket

print(socket.gethostname())
PCName = socket.gethostname()

loop = True
count = 0

while loop==True:
    time.sleep(5)
    windows = pywinauto.findwindows.find_elements(active_only=False, class_name='SunAwtFrame', title_re='RuneLite')
    LengthString = str(len(windows))

    if PCName == 'DESKTOP-2EOK9QJ':
        text_file = open("PC.txt", "w")
        n = text_file.write(LengthString + '\nAccounts\nOpen')
        text_file.close()
    count+=1
    print(count)