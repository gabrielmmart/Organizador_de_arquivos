import os
import shutil

def mover_arquivo_para_pasta(endereco, arquivo, destination_folder):
    if os.path.exists(destination_folder):
        shutil.move(os.path.join(endereco, arquivo), os.path.join(destination_folder, arquivo))
    else:
        os.makedirs(destination_folder)
        shutil.move(os.path.join(endereco, arquivo), os.path.join(destination_folder, arquivo))

def mover_arquivo_para_pasta_extensao(endereco, arquivo, pasta_pai):
    filename, extension = os.path.splitext(arquivo)
    extension = extension[1:].lower()
    destination_folder = os.path.join(endereco, pasta_pai, extension)

    mover_arquivo_para_pasta(endereco, arquivo, destination_folder)

endereco = input("Entre com o endereco da pasta: ")
arquivos = os.listdir(endereco)
print("Deseja criar pastas separadas para cada formato?")
escolha = 'oi'
while(escolha != 's' and escolha != 'n'):
    escolha = input("(s/n): ")

if(escolha == 'n'):
    for arquivo in arquivos:
        filename, extension = os.path.splitext(arquivo)
        extension = extension[1:].lower()

        if extension.lower() in ['rar', 'zip', '7z']:
            mover_arquivo_para_pasta(endereco, arquivo, os.path.join(endereco, 'Compressos'))

        elif extension.lower() in ['jpg', 'jpeg', 'png', 'gif', 'webp']:
            mover_arquivo_para_pasta(endereco, arquivo, os.path.join(endereco, 'Imagens'))

        elif extension.lower() in ['mp4', 'avi', 'mkv', 'mov', 'wav', 'webm']:
            mover_arquivo_para_pasta(endereco, arquivo, os.path.join(endereco, 'Videos'))

        elif extension.lower() in ['exe', 'bat', 'com', 'cmd', 'inf', 'ipa', 'osx', 'pif', 'run', 'wsh']:
            mover_arquivo_para_pasta(endereco, arquivo, os.path.join(endereco, 'Executaveis'))

        elif extension.lower() in ['txt', 'doc', 'docx', 'pdf', 'epub']:
            mover_arquivo_para_pasta(endereco, arquivo, os.path.join(endereco, 'Arquivos de Texto'))

else:
    for arquivo in arquivos:
        filename, extension = os.path.splitext(arquivo)
        extension = extension[1:].lower()

        if extension in ['rar', 'zip', '7z']:
            mover_arquivo_para_pasta_extensao(endereco, arquivo, 'Compressos')

        elif extension in ['jpg', 'jpeg', 'png', 'gif', 'webp']:
            mover_arquivo_para_pasta_extensao(endereco, arquivo, 'Imagens')

        elif extension in ['mp4', 'avi', 'mkv', 'mov', 'wav', 'webm']:
            mover_arquivo_para_pasta_extensao(endereco, arquivo, 'Videos')

        elif extension.lower() in ['exe', 'bat', 'com', 'cmd', 'inf', 'ipa', 'osx', 'pif', 'run', 'wsh']:
            mover_arquivo_para_pasta_extensao(endereco, arquivo, os.path.join(endereco, 'Executaveis'))    

        elif extension in ['txt', 'doc', 'docx', 'pdf', 'epub']:
            mover_arquivo_para_pasta_extensao(endereco, arquivo, 'Arquivos de texto')






