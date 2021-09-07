"""

https://www.w3resource.com/python-exercises/python-basic-exercise-40.php

"""

import time, math, sys, json, os
import pyautogui as pag
import numpy as np
from pynput.keyboard import Listener, Key
from pywinauto import Application
from loguru import logger


#Rererenced in the W3 article to find distance between things
def distance(p1, p2):
  return math.sqrt( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 )

def countdown(secs):
  while secs > 0:
    logger.info(str(secs) + "...")
    time.sleep(1)
    secs = secs - 1

def get_single_loc(name):
  logger.info("Point to location of %s for 1 sec in..." % name)
  countdown(3)
  point = None
  last_point = (0,0)
  start_time = time.time()
  while True:
    x, y = pag.position()
    if last_point == (x,y):
      if time.time() - start_time > 1:
        logger.info(f"Casting location at {x}, {y}")
        return (x, y)
    else:
      start_time = time.time()
      curr_time = start_time
    time.sleep(0.05)
    last_point = (x, y)
