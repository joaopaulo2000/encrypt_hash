from cryptography.fernet import Fernet

message = 'Teste'

key = Fernet.generate_key()
tamanhoHash = 0

retornoEnviar = []
def enviar(mensagem, segredo, chave):
    mensagemComSegredo = mensagem + segredo
    hashMsgSeg = str(hash(mensagemComSegredo))
    # print(hashMsgSeg)
    hashMsg = mensagem + hashMsgSeg
    hashMsg = hashMsg.replace("b'", "")
    hashMsg = hashMsg.replace("'", "")
    fernet = Fernet(chave)
    encryptMsg = fernet.encrypt(hashMsg.encode())

    return [encryptMsg, hashMsgSeg]
def receber(encryptMsg, segredo, chave):
    fernet = Fernet(chave)
    descriptografada = fernet.decrypt(encryptMsg)
    descriptografada = str(descriptografada)
    diminuir = len(descriptografada) - tamanhoHash -1


    msgDescriptografada = descriptografada[0:diminuir]
    msgDescriptografada = msgDescriptografada.replace("b'", "")
    msgDescriptografada = msgDescriptografada.replace("'", "")

    # print("mensagem:", msgDescriptografada)

    
    
    print ( msgDescriptografada if retornoEnviar[1] == str(hash(msgDescriptografada+segredo)) else "null")

    

retornoEnviar = enviar(message, "tac", key)
tamanhoHash = len(retornoEnviar[1])
receber(retornoEnviar[0], "tac", key)
