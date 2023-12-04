# Conversor-de-pdf

Script para Mesclar PDFs
Este script em Python utiliza a biblioteca PyPDF2 para mesclar vários arquivos PDF em um único documento PDF. O script segue os seguintes passos:

Listar Arquivos PDF: Utiliza o módulo os para listar todos os arquivos no diretório "arquivos" e os ordena para consistência.

Inicialização do Mesclador de PDF: Inicializa um objeto PdfMerger da PyPDF2, que será responsável por mesclar os arquivos PDF.

Iterar pelos Arquivos: Para cada arquivo na lista ordenada, o script verifica se o arquivo tem a extensão ".pdf" para evitar mesclar arquivos indesejados.

Anexar ao Mesclador: Se o arquivo for um PDF, ele o anexa ao objeto PdfMerger usando o método append. O caminho do arquivo é construído usando f-strings.

Escrever PDF Mesclado: Por fim, o script escreve o PDF mesclado em um arquivo chamado "arquivo final" usando o método write.

Como Usar:
Certifique-se de que os arquivos PDF de destino estão no diretório "arquivos".
Execute o script.
Observação:
Certifique-se de ajustar o diretório e os nomes dos arquivos conforme necessário.
O PDF mesclado será salvo como "arquivo final" no mesmo diretório do script.
Sinta-se à vontade para personalizar o script de acordo com seu caso de uso específico ou integrá-lo aos seus projetos conforme necessário.
