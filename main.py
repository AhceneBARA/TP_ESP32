from struct import *


class Message:

    def __init__(self, type, clientID,reqID, data, action):
        """Initialize a new message."""
        self.type = {'REQ', 'REP'}
        self.clientID= clientID
        self.reqID = reqID
        self.data = data
        self.action = action

    def Pack(self):
        return print("le message en binaire est :",[bin(b) for b in pack("BBBiB",0,200,150,1000,2)])

    "Le unpack dans la classe message me serviva à quoi, genre si je fais un unpack dans client le message sera deja unpacketé ?"


class Client:
    "il me faut un moyen pour envoyer le message à une destination precise ? "
    def send_message(self, *Message):
        return print("le message est envoyé ")

    "Je ne suis pas sure de la syntax pour faire passer un param de type objet dans une methode ?"
    def receive_message(self, *Message):
        return print("le message a été bien reçu ")

    "Ici je ne vois pas trop à quoi va servir la fonction pack, si le message à envoyer est deja packeté dans la class message ?"
    def Pack_m(self, *Message):
        resultat = pack("BBBiB",Message(0), Message(1), Message(2), Message(3), Message(4))
        return resultat


    def Unpack_m(self, *Message):
        resultat = unpack("BBBiB",Message)
        return resultat



if __name__ == "__main__":

    msg1=Message('REQ',200,150,1000,2)
    res = msg1.Pack()
    "res_unp=res.unpack()"










