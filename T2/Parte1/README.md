# Parte 1 - Análise de APKS
## Script "parte1"
=====

Os arquivo parte1.py foi feito conforme as especificações descritas no moodle, contendo um parâmetro obrigatório `-dp`, que deve receber o caminho até o diretório que contenha os manifestos (database) a serem utilizados. Como default, o script printa as permissões de cada um dos apks. O script suporta parâmetros `-u`,`-c`, `-ppa` para, respectivamente: printar as permissões únicas por cada apk, printar as permissões comuns a todos os apks e desativar a escrita de todas as permissões de todos os apks (`python3 parte1.py -dp ./manifests -ppa -u` escreverá somente as permissões únicas por apks)
O diretório `manifests` contém os manifestos extraídos de cada uma das apks selecionadas, todas provindas de https://www.apkmirror.com/.

As aplicações selecionadas pertencem a um total de 4 categorias: Communication(4), Entertainment(4), Food & Drink(4) e Maps & Navigation(2).

O script considerará somente os arquivos que tenham a extensão ".xml" dentro do diretório dado como parâmetro.

## Script "output"
=============

Arquivo contendo funções para printar a saída conforme o especificado no moodle

