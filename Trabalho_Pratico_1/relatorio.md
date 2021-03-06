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



# Trabalho Prático - Fase 1

## Projeto Funcional e Definição de Classes

### Partitura
Essa é a principal classe do trabalho. Em alto nível, representa a interpretação musical de um trecho de texto, conforme a especificação inicial do trabalho.

#### Nota
Esse atributo trata as diferentes notas que o som pode assumir, assim como suas oitavas. Ainda resta a ser decidido como elas serão codificadas.

#### Timbre
Esse atributo existe para tratar as diferenças entre instrumentos. O timbre, a grosso modo, é a 'assinatura' de cada instrumento.

#### Tempo
Esse atributo trata o tempo, ou beat, do som.

### TrechoDeSom
Essa classe é mais baixo-nível. Ela é basicamente um buffer de som já processado pelos algoritmos de conversão e pronto para ser tocado. O grupo concluiu que é melhor fazer toda a bufferização/renderização do som e só então tocar, para que a experiência do usuário seja a melhor possível.

## Projeto de Interface do Usuário

### Menu
Essa classe é responsável pela interface da interação com o usuário. A partir de alguma seleção selecionada, esta classe irá interagir com as outras classes responsáveis pelas partes relativas às funcionalidades do programa.

#### Métodos

##### __init__
Responsável pela mensagem de boas-vindas ao usuário e por inicializar a classe Menu.

![Init](Menu_init.png?raw=true "Init")

##### __menu__
Responsável pela seleção de escolhas feitas pelo usuário. São elas:

1. Abrir um .txt para executar o áudio
2. Escrever um texto e possibilitar salvar para futuramente digitar
3. Sair do programa

![Menu](Menu_selec.png?raw=true "Menu")

##### ___exit___
Responsável pela mensagem de despedida ao usuário. Exibe ao fim do programa

![Exit](Menu_exit.png?raw=true "Exit")

## Lista de Requisitos

### Funcionais

- O programa deve permitir a digitação assim que aberto - como um editor de texto.
- Antes de rodar a codificação para áudio pela primeira vez, deve oferecer a opção de salvar o texto digitado como .txt.
- Deve tanto aceitar a digitação de comandos para sua execução (por meio de um console), como ter uma interface gráfica de usuário intuitiva e simples.
- Deve ter a funcionalidade de abrir arquivos .txt já existentes, de salvar o .txt atual, e de criar um novo .txt.
- Deve rodar em qualquer sistema operacional que tenha suporte a Python 2.7 (ou seja, praticamente em qualquer SO atual).
- Em termos de hardware, o único requisito 'extra' é uma saída de som - podendo ela ser onboard (speaker interno) ou offboard (caixas de som, fones de ouvido).
- Deve ser capaz de rodar em ambientes Unix.


#### Não-funcionais
- Não deve gerar custos financeiros, apenas mão-de-obra do grupo de trabalho.
- O desenvolvimento deve respeitar o cronograma previsto. Devem ser conduzidas reuniões, de quinzenais a semanais, entre os membros membros do grupo, para manter o alinhamento quanto ao desenvolvimento, assim como também reuniões extraordinárias, para sanar imprevistos e urgências.
- A interface gráfica de usuário deve ter a aparência do sistema operacional em uso, para melhor experiência.
