8888888b. Y88b   d88P 88888888888 888    888  .d88888b.  888b    888 
888   Y88b Y88b d88P      888     888    888 d88P" "Y88b 8888b   888 
888    888  Y88o88P       888     888    888 888     888 88888b  888 
888   d88P   Y888P        888     8888888888 888     888 888Y88b 888 
8888888P"     888         888     888    888 888     888 888 Y88b888 
888           888         888     888    888 888     888 888  Y88888 
888           888         888     888    888 Y88b. .d88P 888   Y8888 
888           888         888     888    888  "Y88888P"  888    Y888 
                                                                     
 
import webbrowser   //importando um navegador

import requests //EMBREVE

from time import sleep  //importando o tempo

time //A função localtime recebe um tempo em segundos

print //A grosso modo a função print() serve para imprimir os argumentos passados a ela no terminal.

sleep //espera um valor inteiro positivo que representa a quantidade milissegundos que é necessário esperar

finally //finally() O método finally() retorna uma Promise . Quando a promise for estabelecida, tenha ela sido realizada ou rejeitada, executa-se a função callback especificada. Isso permite a execução de um código que acontecerá independentemente da Promise ter sido realizada (com sucesso) ou rejeitada (com falha).                                                                    

os.system ("COLOQUE O NOME DO COMANDO")

ua = {
    "colocar aqui o user agent do navegador que está no sistema operacional"
}

client.disconnect() //disconnect() pode ser usado apenas no lado do cliente, não no lado do servidor. Client. emit('disconnect') dispara o evento de desconexão no servidor, mas não desconecta efetivamente o cliente. ... disconnect() pode ser usado no lado do servidor.
----------------------------------------------------------------------------------------------
//importação de um cliente para codigo de confirmação de telefone verificação em etapas
client = TelegramClient("session/" + phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input("\n\n\n\033[1;0mEnter Your Code : "))
    except SessionPasswordNeededError:
        passw = input("\033[1;0mYour 2fa Password : ")
        me = client.start(phone_number, passw)
myself = client.get_me()
----------------------------------------------------------------------------------------
