class User(object):
    def __init__(self, id):
        self.id = id
        
    def sendMessage(self, message):
        print("Mensagem encaminhada para o " + self.id)

    def serverDidReceiveMessage(self, message):
        print(self.id + " recebeu o aviso de que a mensagem chegou no servidor")

class Message(object):
    _payload = None
    _senderID = None
    _receiverID = None
    
    def __init__(self, sender, receiver, payload):
        _payload = payload
        _senderID = sender.id
        _receiverID = receiver.id
        sender.serverDidReceiveMessage(self)
        receiver.sendMessage(self)

    def __eq__(self, other):
        if (self._payload != other._payload):
            return False
        if (self._receiverID != other._receiverID):
            return False
        if (self._senderID != other._senderID):
            return False
        return True

    def __ne__(self, other):
        return not (self == other)
