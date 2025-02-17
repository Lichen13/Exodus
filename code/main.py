import time
import threading
import subprocess
import platform
import os
import sys
##################################
class load:
   def __init__(self):
      if platform.system() == "Linux":
         pass
      else:
         print("Exodus only works on Linux.")
         sys.exit(1)

      self.endLoadingScreen = False

      thread1 = threading.Thread(target=self.text)
      thread2 = threading.Thread(target=self.wheel)
      thread3 = threading.Thread(target=self.do)
      thread1.start()
      thread2.start()
      thread3.start()
      thread1.join()
      thread2.join()
      thread3.join()

      self.logo()
   ##################################
   def wheel(self):
         char = ["[|]", "[/]", "[-]", "[\\]"]
         while self.endLoadingScreen == False:
            for i in char:
               print(i, end="\r")
               time.sleep(0.3)
   ##################################
   def text(self):
      print("    Starting Exodus, please wait...", end="\r")
   ##################################
   def logo(self):
      if self.endLoadingScreen == True:
         print("[|] Starting Exodus, please wait..."); time.sleep(1)
         print(" ____ __  _ ___  ___  __ __ ___")
         print("|  __|\ \/ /   \|   \|  |  / __|")
         print("|  _|  |  |  |  | |  |  |  \__ \\")
         print("|____|/_/\_\___/|___/ \___/|___/")
         print("+ ---------------------------- +")
         print("|   By:        Lichen          |")
         print("|   Version:     Beta          |")
         print("+ ---------------------------- +")
   ##################################
   def do(self):
      self.endLoadingScreen = True
##################################


load()
