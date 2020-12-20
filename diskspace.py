import subprocess
threshold = 10
child = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
output = child.communicate()[0].strip().split("\n")
for x in output[1:]:
     if int(x.split()[-2][:-1]) >= threshold:
        print x


import os                                                                                                                                                                     
du = os.popen("df -h").readlines()
from pprint import pprint
pprint(du)