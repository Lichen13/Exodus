import threading
import time
import subprocess
import platform
####################################

class loadingScreen:
   def __init__(self):
      self.thread1_stop = threading.Event()
      self.thread2_stop = threading.Event()

      thread1 = threading.Thread(target=self.loadingText, args=(self.thread1_stop,))
      thread2 = threading.Thread(target=self.do_task, args=(self.thread2_stop,))

      thread1.start()
      thread2.start()

      thread1.join()
      thread2.join()

      if self.load_logo == True:
         self.loadLogo()
   ####################################
   def loadingText(self, thread1_stop):
      while not self.thread1_stop.is_set():
         frames = ["[|] Loading Exodus, please be patient...", "[/] Loading Exodus, please be patient...", "[-] Loading Exodus, please be patient...", "[\\] Loading Exodus, please be patient..."]
         for i in frames:
            print(i, end="\r")
            time.sleep(0.5)
      else:
         return
   ####################################
   def do_task(self, thread2_stop):
      result = subprocess.run(["ping", "-c", "1", "google.com"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      if result.returncode == 0:
         self.ping_status = True
         self.load_logo = True
         self.thread1_stop.set()
      else:
         self.ping_status = False
         self.load_logo = True
         self.thread1_stop.set()
   ####################################
   def reportError(self, text):
      print(f"\n➥ An error occured: '{text}'.")
      self.load_logo = False
      if not self.thread1_stop.is_set():
         self.thread1_stop.set()
      else:
         pass

      if not self.thread2_stop.is_set():
         self.thread2_stop.set()
      else:
         pass
   ####################################
   def loadLogo(self):
      print("\n ____ __  _ ___  ___  __ __ ___")
      print("|  __|\ \/ /   \|   \|  |  / __|")
      print("|  _|  |  |  |  | |  |  |  \__ \\")
      print("|____|/_/\_\___/|___/ \___/|___/")
      print("+ ---------------------------- +")
      print("|  By:        Lichen           |")
      print("|  Version:   Beta             |")
      if self.ping_status == True:
         print("|  Ping:      Positive         |")
      else:
         print("|  Ping:      Negative         |")
      print("+ ---------------------------- +")
      print("[1] ChestGuard           Password saver")
      print("[2] Tool2                Another tool")



class program_launcher:
   def __init__(self):
      pass


if __name__ == "__main__":
   if platform.system() == "Linux":
      loadingScreen()
   else:
      print("Exodus is only working for Linux.")
