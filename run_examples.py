import examples
import sys
import os
from dotenv import load_dotenv

load_dotenv()

examples_to_run = sys.argv[1:]
apikey = os.getenv("RIOT_API_KEY")

for method_name in dir(examples):
  method = getattr(examples, method_name)
  if not callable(method):
    continue
  if len(examples_to_run) > 0 and method_name not in examples_to_run:
    continue
  message = "Method \"{}\" \nresponse: {}".format(method_name, method(apikey))
  print(message + "\n\n")