import time
import subprocess
import sys
import platform
import threading
####################################
class loadingScreen:
   ####################################
   def __init__(self):
      self.loadLogo = False
      self.connected = False

      thread1 = threading.Thread(target=self.loadingText)
      thread2 = threading.Thread(target=self.do_task)

      thread1.start()
      thread2.start()

      thread1.join()
      thread2.join()

      self.logo()
   ####################################
   def loadingText(self):
      while self.loadLogo != True:
         subprocess.run(["clear"])
         print("")
         text = ["[|] Loading Exodus, please be patient...", "[/] Loading Exodus, please be patient...", "[-] Loading Exodus, please be patient...", "[\\] Loading Exodus, please be patient..."]
         for i in text:
            print(i, end="\r", flush=True)
            time.sleep(1)
   ####################################
   def reportError(self, description):
      print(f"\n ➥  An error occured: '{description}'.")
      sys.exit(1)
   ####################################
   def logo(self):
       self.line1 = "| By: Lichen                   |"
       self.line2 = "| Version: Beta                |"
       if self.connected == True:
          self.line3 = "| Ping: Positive               |"
       else:
          self.line3 = "| Ping: Negative               |"
       if self.loadLogo == True:
          print("[|] Loading Exodus, please be patient...")
          print(" ____ __  _ ___  ___  __ __ ___")
          print("|  __|\ \/ /   \|   \|  |  / __|")
          print("|  _|  |  |  |  | |  |  |  \__ \\")
          print("|____|/_/\_\___/|___/ \___/|___/")
          print("+ ---------------------------- +")
          print(self.line1)
          print(self.line2)
          print(self.line3)
          print("+ ---------------------------- +")
   ####################################
   def do_task(self):
      time.sleep(1)
      osname = platform.system()
      if osname == "Linu":
         pass
      else:
         self.reportError("Exodus is only working for Linux")
      try:
         result = subprocess.run(["ping", "-c", "1", "google.com"], timeout=5, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
         self.connected = True
         self.loadLogo = True
      except subprocess.TimeoutExpired as e:
         self.connected = False
         self.loadLogo = True

loadingScreen()
