class Fone:
   def __init__(self,id:str, number:str):
        self.id = id
        self.number = number

   def isValid(self):
      validos = "0123456789().-"
      for c in self.number:
         if c not in validos:
            return False
      return True

   def getld(self):
      return self.id
    
   def getNumber(self):
      return self.number
    
   def toString(self):
      return f"{self.id}:{self.number}"
    
class Contact:
   def __init__(self, name: str):
      self.name = name
      self.favorited = False
      self.fones = []

   def addFone(self, id, number):
      f = Fone(id, number)
      if f.isValid():
         self.fones.append(f)
      else:
         print("fail: invalid number")

   def rmFone(self, index: int):
      if 0 <= index < len(self.fones):
         self.fones.pop(index)

   def toogleFavorited(self):
      self.favorited = not self.favorited

   def isFavorited(self):
      return self.favorited

   def getFones(self):
      return self.fones
   
   def getName(self):
      return self.name

   def setName(self, name:str):
      self.name = name

   def toString(self):
      pref = "@ " if self.favorited else "- "
      fones_str = ", ".join([f.toString() for f in self.fones])
      return f"{pref}{self.name} [{fones_str}]"

class Agenda:
   def __init__(self):
      self.contacts = []

   def findPosByName(self,name : str):
      for i, c in enumerate(self.contacts):
         if c.getName() == name:
            return i
      return -1

   def addContact(self, name: str, fones):
      pos = self.findPosByName(name)

      if pos != -1:
         for f in fones:
            if f.isValid():
               self.contacts[pos].getFones().append(f)
         return
      
      c = Contact(name)
      for f in fones:
         if f.isValid():
            c.getFones().append(f)

      self.contacts.append(c)
      self.contacts.sort(key=lambda x: x.getName())

   def getContact(self, name: str):
      pos = self.findPosByName(name)
      if pos == -1:
         return None
      return self.contacts[pos]
   
   def rmContact(self, name : str):
      pos = self.findPosByName(name)
      if pos != -1:
         self.contacts.pop(pos)

   def search(self, pattern : str):
      result = []
      for c in self.contacts:
         if pattern in c.toString():
            result.append(c)
      return result

   def getFavorited(self):
      return [c for c in self.contacts if c.isFavorited()]
   
   def getContacts(self):
      return self.contacts
       
   def toString(self):
      return "\n".join([c.toString() for c in self.contacts])
   

agenda = Agenda()

while True:
   try:
      line = input().strip()
   except EOFError:
      break

   if line == "":
      continue

   print("$" + line)
   args = line.split()

   cmd = args[0]

   if cmd == "end":
      break

   elif cmd == "add":
      name = args[1]
      fones = []
      for token in args[2:]:
         id, number = token.split(":")
         fones.append(Fone(id, number))
      agenda.addContact(name, fones)

   elif cmd == "show":
      for c in agenda.getContacts():
         print(c.toString())

   elif cmd == "rmFone":
      name = args[1]
      index = int(args[2])
      c = agenda.getContact(name)
      if c:
         c.rmFone(index)

   elif cmd == "rm":
      agenda.rmContact(args[1])
   
   elif cmd == "search":
      pattern = args[1]
      r = agenda.search(pattern)
      for c in r:
         print(c.toString())

   elif cmd == "tfav":
      name = args[1]
      c = agenda.getContact(name)
      if c:
         c.toogleFavorited()
   
   elif cmd == "favs":
      favs = agenda.getFavorited()
      for c in favs:
         print(c.toString())

