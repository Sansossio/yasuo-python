import examples
import sys
import os
import time
from dotenv import load_dotenv
from get_example_list import get_example_list

load_dotenv()

examples_to_run = sys.argv[1:]
apikey = os.getenv("RIOT_API_KEY")

for method_name in get_example_list():
  if (len(examples_to_run) > 0 and method_name not in examples_to_run):
    continue
  init_time = time.time()
  method = getattr(examples, method_name)
  print("Runnig method " + method_name)
  method_response = method(apikey)
  method_time = time.time() - init_time
  message = "Method \"{}\" \nresponse: {} \ntime: {:0.2f} seconds".format(method_name, method_response, method_time)
  print(message + "\n\n")
