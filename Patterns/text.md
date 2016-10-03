# Parte II : Seleção e Descrição de 6 Padrões de Implementação
O grupo pode (re)usar a estrutura de descrição presente no livro e resumir as características principais de cada padrão. Esta descrição deve ser feita visando a distribuição para os colegas de turma, de modo que todos se beneficiem de seu esforço.

### 2 padrões de classe 
- Interfaces
  - O uso de interfaces permite que o programador afirme que certa classe irá possuir certas capacidades. Sabendo que os métodos esperados estarão presentes os usuários dessas classes não precisam se preocupar em como foi implementada a solução.
  - Este encapsulamento da implementação permite que mudanças possam ser feitas sem adicionar trabalho aos diversos usuários da classe, minimiza o efeito colateral de mudanças na implementação.
  - Em Java, interfaces não podem incluir declarações de propriedades, assim como todos os métodos devem ser públicos.
  - Uma classe pode implementar mais de uma interface.
  - Outras linguagens tem pequenas diferenças na implementação do conceito de interfaces. Em Swift, por exemplo, existem protocolos, que são interfaces onde também é possível declarar propriedades. 

- Objeto Valor
  - Quando vamos lidar com conceitos imutáveis podemos fazer deles um objeto que se comporta como um valor. Ou seja, uma classe que apresenta o mesmo comportamento que um Int ou Float. 
  - Todos os campos são inicializados ao mesmo tempo e após a inicialização não mais serão alterados.
  - A igualdade nesse caso não é dada pela instancia, mas sim pela igualdade de cada um dos campos.
  - O objeto não possui estado, porém ele pode encapsular outros objetos que contém estado.
  - Java e Python não possuem o conceito de Valor Objeto na sua forma pura, porém existem bibliotecas de terceiros para facilitar a implementação do padrão, apesar de não ser necessário.

### 4 padrões de estado, de comportamento e de método.
- Guard (Comportamento) 
  - Usado em situações para desviar do fluxo comum.
  - Usado quando a situação fora do normal é simples e tem consequencias locais.
  - Apropriado quando um dos caminhos é menos importante, pois se ambos caminhos são importantes deverá ser usado um if-else convencional.
  - Seu uso vai contra a convenção de que métodos deveriam ter um único ponto de entrada e de saída. O que em linguagens modernas não é preocupante.
  - Sua implementação na maioria das linguagens se da por meio de um if comum sem clausula de else, já que dentro do if haverá um retorno.


- Nome refletindo intenção (Método)
  - Nomes dos métodos devem refletir a inteção de quem está chamando.
  - Estratégias de implementação geralmente não devem constar no nome. Em casos raros, saber sobre a implementação pode ser útil, podendo ela, então, constar no nome.
  - Nomes dos métodos devem ajudar a contar a história do código: pense sobre o contexto em que ele será chamado.
  - Tente evitar prefixos nos nomes; cheque se está usando a metáfora correta antes.
  - Como curiosidade, incluimos um exemplo de um longo nome de método encontrado no framework UIKit da Apple: automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers, contendo 70 caracteres.


- Construtor Completo (Método)
  - Métodos Construtores são responsáveis por retornar objetos prontos para serem computados.
  - Construtores devem expressar os requisitos básicos que eles precisam para retornar tal objeto.
  - Se existe mais de uma combinação de requisitos possíveis, devemos disponibilizar construtores para cada uma delas.
  - Eles permitem que deixemos claro quais propriedades devem ser populadas antes de usarmos um objeto, o que não aconteceria caso o criássemos vazio e permitíssemos que o usuário o populasse livremente.
  - Quando disponibilizando mais de um construtor, faça com que todos eles usem o mesmo construtor pai, isso garante que todas as variações respeitarão os requisitos básicos comuns a elas.

- Inicialização Tardia (Estado)
  - Alguns campos ou objetos filhos de um outro objeto podem ter um custo muito grande de inicialização. Isso nos leva a propor que sua inicialização seja atrasada o máximo possível, talvez apenas quando alguém tentar acessá-la.
  - O fato de que a inicialização da variável estará distante da declaração dificulta a leitura do código, mas passa a ideia de que performance é crucial nesse trecho.
  - Essa separação também dificulta a programação, pois temos mais dificuldade em determinar se no ponto em que estamos ela estará ou não inicializada.
