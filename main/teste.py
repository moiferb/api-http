import os

caminho = input("Digite o caminho da pasta que deseja verificar: ")

# Cria o arquivo de texto na mesma pasta
with open(os.path.join(caminho, 'arquivos.txt'), 'w') as arq_txt:
    for arquivo in os.listdir(caminho):
        if os.path.isfile(os.path.join(caminho, arquivo)) and not arquivo.endswith('.srt'):
            nome_arquivo, extensao = os.path.splitext(arquivo)
            arq_txt.write(nome_arquivo + '\n')

# Imprime o texto em vermelho com "sucesso!" em verde
print('\033[91m' + "Arquivo de texto com os nomes dos arquivos criado com " + '\033[92m' + "SUCESSO!" + '\033[0m')
