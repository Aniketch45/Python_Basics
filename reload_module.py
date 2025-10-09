import module2
import time
from importlib import reload

module2.prod(2,5)
time.sleep(10)
print("Hello Welcome")
reload(module2)