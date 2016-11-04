<p align="center">
  <b>UNIVERSIDADE FEDERAL DO RIO GRANDE DO SUL</b><br>
  <b>INSTITUTO DE INFORMÁTICA</b><br>
  <b>INF01120-B</b><br>
  <b>Prof. Marcelo Soares Pimenta</b><br><br>
  <b>Grupo:</b><br>
  <b>Germano Martinelli - 00216684</b><br>
  <b>Pietro Degrazia - 00243666</b><br>
  <b>Vilmar Neto - 00242276</b><br>
</p>



# Trabalho Prático - Fase 2

## Descrição do Programa

O programa consiste em um software que irá receber entrada de comandos do usuário através do teclado e baseado em tais entradas tocará sons com notas, volume e batidas de acordo.

### Partitura 
Classe que irá representar a música como um todo. Possui como atributo todo o texto que o usuário entrou para determinado arquivo. No futuro poderá possuir também uma lista ordenada de Notas e Tempos, provavelmente transformados em um objeto apenas do tipo Comando (padrão de implementação).

### Nota
Classe que irá representar as notas musicais: lá, sí, dó, etc..  Inclui a frequência base da nota, e no futuro deverá incluir também algum atributo que auxilie nas diferentes oitavas que ela pode ter.

### Tempo
Classe ainda não foi implementada, mas achamos que será necessária para controlar o ritmo da música.

### TrechoDeSom
Achamos que teremos de implementar uma classe que sirva como buffer para o som - algo comum em aplicações que lidam com áudio. Ou, mais provavelmente, importar uma implementação .wav pré-existente.

## Análise sobre Modularidade

### Interfaces e Informação - a tênue linha entre expôr e esconder 
De acordo com o plano, a interface será bastante explícita. O próprio fato de ela ser gráfica contribui naturalmente para isso: todas as opções do que 'se pode fazer' com os objetos estarão elencadas de forma visual. E, pelo lado oposto, toda a informação que não é necessária ao usuário estará escondida dele. O software terá, assim, ambas as características desejáveis de explicit interface e information hiding. Além disso, a interface será concisa, não contendo nada supérfluo - e também a única. Cumprem-se os requisitos de interface pequena e explícita.

### Acoplamento - o específico vs o panorâmico

Em termos de acoplamento, as classes foram pensadas de forma tão específica para a resolução desse problema que algumas ficaram fortemente acopladas entre si.

A TrechoDeSom é, talvez, a mais genérica delas - consiste em uma série de bytes em codificação .wav, que pode facilmente ser importada de uma biblioteca existente (que é o approach que o grupo planeja adotar) ou implementada e usada, sem modificações, por outra aplicação.

A Nota e o Tempo também contêm elementos bastante gerais, que podem ser tanto importados quanto exportados sem menores problemas, visto ambos serem conceitos universais do universo da Teoria Musical.

Por outro lado, a Partitura é bem especificamente desenhada para solucionar esse exato problema. Começa-se pelo fato de que ela, em si, já é uma abstração sobre um conjunto de linhas de texto que poderiam ser tratadas, por si só, meramente como texto.

### Decomposição - a divisão de tarefas 

Em termos de decomposição, a composição do trabalho foi dividida na criação do software: a interface gráfica é acessível ao usuário final, e o processamento, invisível a ele.

Além disso, a visão adotada foi top-down. Começou-se pela descrição em alto nível - linguagem humana, conceitos do mundo real - do problema, e então foi-se baixando o nível de abstração até se chegar em implementação de código em Python.

### Unidades Modulares Linguísticas e Auto-documentação - a importante e não-trivial tarefa de fazer o código falar por si

Duas das principais lições da Engenharia de Software são a noção de que o código é muito mais vezes lido do que escrito, e a de que vale a pena economizar alguns bits de memória ou nanossegundos de execução (que, com a tecnologia atual, hoje existem em abundância) para tornar o código mais facilmente legível e interpretável pelas mentes humanas que terão contato com ele.

Assim, o grupo pretende atentar especialmente para que a implementação seja bastante clara, priorizando a clareza linguística sobre a escovagem de bits. Para isso, os nomes das classes e dos métodos serão descritivos (padrão de implementação), mesmo que resultem longos (o que não é um grande problema com as IDEs de hoje e com o suporte de compiladores e interpretadores a strings longos). E, junto a isso, o grupo buscará codificar de forma a tornar clara a lógica, na medida do possível, até a alguém leigo. Essa é uma métrica exigente e, ainda que inatingível na prática, é uma boa heurística a se adotar.


### Propostas de Soluções

Tendo em vista o propósito específico da aplicação, podemos tentar melhorar a modularidade trocando comunicação entre classes, hoje feitas com acesso direto por acesso indireto, através de métodos declarados em interfaces. Isso por um lado adiciona complexidade no código inicialmente, mas compensa com maior liberdade na hora de dar manutenção e alterar estratégias de implementação em cada classe.
