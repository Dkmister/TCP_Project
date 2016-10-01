from Message import *


sender = User("Sender")
receiver = User("Receiver")

firstMsg = Message(sender, receiver, "Eai")
secondMsg = Message(sender, receiver, "Oii")

print(firstMsg == secondMsg)
print(firstMsg != secondMsg)
