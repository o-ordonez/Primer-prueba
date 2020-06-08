import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)
print("HELLO")
r = requests.get("https://www.google.com.mx")
print(r.status_code)
