#!/usr/bin/env python


import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


if __name__ == "__main__":
  event_handler = LoggingEventHandler()
  observer = Observer()
  observer.schedule(event_handler, path='/Library/Preferences/SystemConfiguration/preferences.plist', recursive=True)
  observer.start()
  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    observer.stop()
  observer.join()

