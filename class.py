#CLASSLAR
#self=>this
#self o tanımlanan fonksiyonu temsıl eder

class Human:
    
    #built-in
    #constructor
    #initialize
    def __init__(self,name):
        self.name=name
        print("Bir human instance i üretildi")
    def __str__(self):
        return f"STR Fonksiyonundan dönen değer:{self.name}"
      
    def talk(self,sentence):
        name="Ercan"
        print(f"{self.name} : {sentence}")
    def walk(self):
        print(f"{self.name} is walking")
#instance=>örnek
human1=Human("Enes")
human1.name="Enes"
human1.talk("Merhaba")
human1.walk()
print(human1)
human2=Human("Halit")
#human2.name="Cem"
human2.talk("Selam")
human2.walk()
print(human2)



