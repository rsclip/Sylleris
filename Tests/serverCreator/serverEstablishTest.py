import subprocess
import os
from threading import Thread

executable = r'java -XX:+UseG1GC -Xmx3G -Xms3G -jar "C:\Users\Cyclip-06b\Desktop\sylleristestserver/server.jar" nogui'
path = r'C:\Users\Cyclip-06b\Desktop\sylleristestserver/'

os.chdir(path)

def printOutput():
    while True:
        output = server.stdout.readline().decode()
        if len(output) > 3:
            print()
            server.stdout.flush()

server = subprocess.Popen(executable, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
Thread(target=printOutput).start()
while True:
    command = input("> ")
    if command:
        server.stdin.write(bytes(command + "\r\n", "ascii"))
        server.stdin.flush()
