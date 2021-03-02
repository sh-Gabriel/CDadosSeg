Respondendo às perguntas:
- Dados em tipos string (dados em si), float e ing (metadados)
- O objetivo é utilizar um classificador da biblioteca `scikit learn` para classificar fake news e, a partir disso, com base nos atributos escolhidos, correlacionar os resultados da classificação com os metadados dos dados.

- A rotulação do dataset: 'texto', sendo o texto da notpicia em si; 'CATEGORY', a categoria/assunto da notícia (eg: política, sociedade...); 'NUM_WITHOUT_PONCT', o número de palavras da notícia sem pontuação; 'NUM_UPPERCASE', número de palavras escritas completamente em maiúsculas; 'NUM_SUBJ_IMP', número de verbos no subjuntivo e no imperativo; 'AVG_SENT_LEN', a média do comprimento das frases da notícia; 'SPEL_ERROR', a porcentagem de erros de digitação.

- 

- O dataset teve que ser feito 'à mão', então as colunas nele presentes já são somente as que interessam. A seleção desses atributos deve-se ao interesse em analisá-las conforme os resultados das classificações.
