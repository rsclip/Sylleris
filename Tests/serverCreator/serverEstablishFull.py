import subprocess
import os
from threading import Thread

executable = r'java -XX:+UseG1GC -Xmx3G -Xms3G -jar "C:\Users\Cyclip-06b\Desktop\sylleristestserver/server.jar" nogui'
path = r'C:\Users\Cyclip-06b\Desktop\sylleristestserver/'

os.chdir(path)

server = subprocess.Popen(executable, stdout=subprocess.PIPE, stdin=subprocess.PIPE)

while True:
    output = server.stdout.readline().decode()
    if len(output) > 3 and True:
        print(output.strip('\n'))
    if 'Timings Reset' in output or 'Stopping server' in output:
        server.stdin.write(bytes('stop' + "\r\n", "ascii"))
        server.stdin.flush()
        break
