# Descrição do Programa

a) O programa consiste em um software que irá receber entrada de comandos do usuário através do teclado e baseado em tais entradas tocará sons com notas, volume e batidas de acordo.

b)
## Partitura 
Classe que irá representar a música como um todo. Possui como atributo todo o texto que o usuário entrou para determinado arquivo. No futuro poderá possuir também uma lista ordenada de Notas e Tempos, provavelmente transformados em um objeto apenas do tipo Comando(padrão de implementação).

## Nota
Classe que irá representar as notas musicais: lá, sí, dó, etc..  Inclui a frequencia base da nota, e no futuro deverá incluir também algum atributo que auxilie nas diferentes oitavas que ela pode ter.

## Tempo
Classe ainda não foi implementada, mas achamos que será necessária para controlar o ritmo da musica.

## TrechoDeSom
Achamos que teremos de implementar uma classe que sirva como buffer para o som, algo que é comum em aplicações que lidam com áudio.