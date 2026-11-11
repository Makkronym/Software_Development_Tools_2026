import sys

errors = 2
fatal = 1
info = 1

def notify_user():
  print(f"Errors: {errors} | Info: {info}")

def notify_user():
  print(f"Fatal errors: {fatal} | Minor errors: {errors} | Info: {info}")

def process_fatal_errors():
  sys.exit()

def error_handler():
  print("Errors are not yet handled.")

  if __name__ == "__main__":
  notify_user()

  if fatal != 0:
      process_fatal_errors()