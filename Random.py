import os, platform

 

try:

 

        import requests

 

except:

 

        os.system('pip2 install requests')

 

 

 

import requests

 

bit = platform.architecture()[0]

 

if bit == "64bit":

 

        from dark64 import __Dark__

 

        __Dark__()

 

 

 

elif bit == "32bit":

 

        from dark32 import __Dark__

 

        __Dark__()
