# Parte 2 - Análise de arquivos PE

Os arquivos dos scripts foram feitos conforme as especificações descritas no moodle, utilizando a biblioteca `pefile` para parsear os arquivos PE.



## Script parte2
=============

Recebe como entrada obrigatória a especificação de um arquivo(`-a`) ou de um caminho para um diretório(`-dp`) que contenha os arquivos PE a serem utilizados.
Considera-se que o(s) arquivo(s) passado(s) sejam compatíveis com o uso da biblioteca `pefile`
Requer um, dentre dois, parâmetro obrigatório: `-dp` em conjunto com o caminho do diretório que conmtenha os executáveis ou `-a` seguido do arquivo executável


## Script compare
=============

Recebe como entradas obrigatórias os dois arquivos PE para comparar suas sessões.
Considera-se que o(s) arquivo(s) passado(s) sejam compatíveis com o uso da biblioteca `pefile`

## Script output
=============

Contém funções para printar a saída conforme o especificado no moodle