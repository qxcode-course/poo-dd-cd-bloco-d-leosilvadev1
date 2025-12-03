class Fone:
    def __init__(self,id:str, number:str):
        self.__id = id
        self.__number = number

    def getld(self) -> str:
       return self.__id
    
    def getNumber(self) -> str:
       return self.__number
    
    def isValid(self) -> bool:
       return True
    
    def __str__(self):
       return f"{self.__id}:{self.__number}"
    
class Contact:
    def __init__(self, name: str):
       self.__name: str = name
       self.__favorited: bool = False
       self.__phones: list[Phone] = []

    def addFone(self,id, number):
        f = Fone (id, number)

    def __str__(self):
        result = []
        for contact in self.getContacts():
            mark = "@" if contacts.isFavorite() else "- "
            result.append(mark + str(contact))
        return "\n".join(result)

def main():
    agenda = Agenda()
     while True:
        cmd = input()
        args = cmd.split()  
        print("$" + cmd)
        if args[0] == "add":
           name = args[1]
           phones = []
           for i in range (2,len(args)):
              phone = buildPhoneFromString(args(i))
              phones.append(phone)

            agenda.addContact(name, phones)
           
        elif args[0] == "show":
            print(agenda)
        elif args[0] == "end":
           break
        elif args[0] == "rmFone":
           name = args[1]
           index = int(args[2])
           contact = agenda.getContact(name)
           if contact:
              contact.rmPhone(index)
              agenda.rmContact(name)
              agenda.addContact(contact.getName(), contact.getPhones())

        elif args[0] == "rm"


main()