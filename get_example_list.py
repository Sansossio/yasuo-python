import examples

def get_example_list():
  example_list = []
  for method_name in dir(examples):
    method = getattr(examples, method_name)
    if callable(method):
      example_list.append(method_name)
  return example_list

if __name__ == '__main__':
  print(get_example_list())
