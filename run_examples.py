import examples
import sys
import os
from dotenv import load_dotenv
from get_example_list import get_example_list

load_dotenv()

examples_to_run = sys.argv[1:]
apikey = os.getenv("RIOT_API_KEY")

for method_name in get_example_list():
  if (len(examples_to_run) > 0 and method_name not in examples_to_run):
    continue
  method = getattr(examples, method_name)
  message = "Method \"{}\" \nresponse: {}".format(method_name, method(apikey))
  print(message + "\n\n")
