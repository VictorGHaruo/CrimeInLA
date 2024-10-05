.. f documentation master file, created by
   sphinx-quickstart on Sat Sep 28 19:23:15 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Crime in Los Angeles - Data Analysis
====================================
by Victor Iwamoto, Eric Ribeiro and Lucas Menezes.

Introduction
------------

O presente trabalho tem como propósito a aplicação das técnicas de análise de dados utilizando 
ferramentas disponíveis na linguagem de programação Python. Além disso, constitui um método 
avaliativo da disciplina Linguagens de Programação do 2º Período do Curso de Matemática Aplicada
da Fundação Getúlio Vargas. Dessa maneira, o grupo de alunos composto por Victor Gabriel Haruo Iwamoto,
Eric Manoel Ribeiro de Sousa e Lucas Menezes de Lima escolheram um dataset referente aos crimes ocorridos
em Los Angeles no intervalo de tempo de 2020 à meados de 2024 dispobilizados pelo Departamento de Polícia
de Los Angeles. 

Hypothesis
----------
* Gender & Crimes by Victor Iwamoto
* Pandemia & Crimes by Eric Ribeiro
* Location & Crimes by Lucas Menezes

Challenges
----------
* O dataset se encontrava incompleto e, as vezes, até errado. Dessa maneira, foi necessário o uso de métodos 
  de tratamento de dados para que as informações com problemas não influenciassem negativamente a ánalise proposta.

* A utilização do Sphinx se deu como uma problemática ao tentar documentar a função `main`, pois o Sphinx estava 
  gerando erros genéricos - sem muita descrição - ao executar o comando `make html`, assim necessitou a pesquisa em relação ao erro.

* A implementação das bibliotecas também se mostrou desafiadora. Inicialmente, o arquivo da main e os modulos auxiliares 
  estavam no mesmo `folder`, o que ocasionou em severos erros ao utilizar o comando para a documentação automática 
  `sphinx-apidoc -o <output_dir> <source_dir>`, assim necessitou a criação de um subdiretório com as 
  bibliotecas e a inserção do arquivo `__init__.py`, para deixar claro ao Python que o subdiretório é uma 
  biblioteca. Dessa maneira, como o arquivo da `main` mudou de diretório a importação das bibliotecas tiveram que 
  ser feitas por meio de um caminho absoluto, pois ao utilizar um caminho relativo a autodocumentação do Sphinx 
  dava erro.

Documentation
-------------



References
----------
* `Dataset Download <https://catalog.data.gov/dataset/crime-data-from-2020-to-present>`_
* `Column Description <https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8/about_data>`_


.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   modules
   hypothesis_three
