import PyPDF2
import  os  #----->  usada para listar  arquivos do sistema

merger  =  PyPDF2.PdfMerger()   #------> Pdfmerger vai ser o responsavel pela juncao dos pdfs 

lista_arquivos = os.listdir("arquivos") #---->  lista os arquivos dentro da pasta arquivos
lista_arquivos.sort() #-------->  .sort seria para ordenar os arquivos 
print(lista_arquivos) 

for arquivo in lista_arquivos: #--------------> para cada arquivo na lista arquirvos entao 
    if ".pdf" in arquivo: #----------------> cria uma condicao para checar se o ,pdf esta dentro do arquivo para evitar agrupar arquivos indesejaos
        merger.append(f"arquivos/{arquivo}") #--------------> Adiciona o merger e usa o appender para adicionar ao mesclador, deve se informa qual arquivo voce quer passar e o local do arquivo
merger.write("arquivo final") #------------->  .write "escreve" os arquivos e salva o arquivo!