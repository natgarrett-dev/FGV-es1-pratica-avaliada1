# Análise de Processo - AgileTech Solutions

## Questão 1 - A) 

### Alguns Valores do Manifesto Ágil

**1. Indivíduos e interações mais que processos e ferramentas**

A AgileTech possui uma equipe pequena de apenas 5 desenvolvedores e 1 product owner. Nesse cenário, melhor que depender de processos critériosos e documentações extensas a comunicação direta entre os membro é a base pra eficiência. A colaboração constante entre o PO e os desenvorlvedores garante alinhamento rápido sobre prioridades e mudanças.

**2. Software em funcionamento mais que documentação abrangente**

O histórico da empresa revela um problema claro: documentações extensas eram constantemente desatualizadas. A abordagem ágil inverte essa lógica — o software funcional é o q se entende do progresso. Ao invés de ter volumes de documentos, a equipe entrega incrementos de software utilizáveis ao final de cada sprint, o que torna claro a importância de ter o cliente no centro.

**3. Colaboração com o cliente mais que negociação de contratos**

O cliente da AgileTech é participativo, mesmo com recurso limitado. Isso é um ativo valioso. O modelo ágil capitaliza essa participação através de revisões (sprint reviews), feedbacks e priorização colaborativa do backlog. Com requisitos vagos e mutáveis, a presença do cliente no processo evita o desperdício de construir que não é necessária.

**4. Responder a mudanças mais que seguir um plano**

O modelo ágil é excelente quando se trata de mudanças, incorporando-as naturalmente ao fluxo de trabalho através de alinhamentos e replanejamentos durante a sprint.

---

### Justificativa: Abordagem Ágil vs. Cascata

Para o cenário da AgileTech, a adoção de uma metodologia ágil é com certeza superior ao modelo cascata pelos seguintes motivos:

**Requisitos vagos e mutáveis**: O modelo cascata exige que os requisitos muito mais definidos antes do início do desenvolvimento. Na AgileTech, os requisitos são vagos e mudam com frequência — aplicar cascata nesse caso seria resultado massivo de retrabalho ou entrega de um produto sem a necessidade real do cliente.

**Pressão por entregas rápidas**: A cascata só entrega valor ao cliente no final do projeto, que pode durar alguns meses. O modelo ágil entrega software funcional em curtos períodos (sprints de 1 a 4 semanas), demonstrando valor ao mercado muito mais rápido.

**Equipe pequena e dinâmica**: Processos pesados de cascata com papéis rígidos e documentações extensas não se é necessário aem equipes menores. O ágil favorece times pequenos, auto-organizados e multidisciplinares.

**Documentação que envelhece**: O histórico de documentações desatualizadas é o clássico de um processo orientado a planos. O ágil trata documentação como meio, não como fim.

---

### Três Práticas Ágeis para Adoção Imediata

1. **Sprint Planning e Sprint Review**: Organizar seu trabalho em ciclos curtos (sprints de 2 semanas), planejando o que será entregue no início e revisando os resultados com o cliente ao final. Isso cria ritmo previsível e feedback constante.

2. **Reunião Diária**: Uma reunião rápida de 15 minutos, todos os dias, onde cada membro responde o que fez, e quais impedimentos passou ou irá passar. Mantém a equipe em sintonia e expõe problemas rapidamente.

3. **Refinamento do Backlog**: Sessões regulares onde o PO e os desenvolvedores revisam, detalham e priorizam as histórias de usuário. Fundamental para uma equipe com requisitos vagos e mutáveis, pois garante que o backlog esteja sempre pronto e bem compreendido antes do próximo planejamento.

---

## Questão 1 - B)

### Conceito de Pair Programming e seus Benefícios

Pair Programming (Programação em Pares) é uma prática do Extreme Programming (XP) em que dois desenvolvedores trabalham juntos em um único computador. Um assume o papel de de digitar o código e o outro atua como quem revisa, questiona e pensa na estratégia. Os papéis são trocados regularmente.

**Benefícios:**

- **Revisão em tempo real**: Erros são detectados imediatamente, antes de chegar ao repositório ou à revisão de código.
- **Transferência de conhecimento**: O conhecimento não fica concentrado em um único desenvolvedor; toda a equipe evolui junto.
- **Design de melhor qualidade**: A presença de dois pontos de vista leva a soluções mais bem pensadas e refatorações.
- **Redução de bugs**: Estudos mostram que código produzido em par possui menos defeitos que código individual.
- **Integração de novos membros**: Um desenvolvedor sênior junto de um júnior acelera o onboarding e o aprendizado.
- **Foco e disciplina**: A presença do parceiro reduz distrações e o desenvolvedor tende a manter o foco.

---

### Desafios de Pair Programming em Cursos a Distância (EAD)

Aplicar programação em pares em contextos EAD tem desafios:

- **Fuso horário e disponibilidade**: Alunos em regiões diferentes têm janelas de horário distintas, dificultando sincronizar sessões ao vivo.
- **Qualidade de conexão**: Chamadas de vídeo e compartilhamento de tela tende a precisar de uma boa internet, que nem sempre está disponível para todos.
- **Ausência de presença física**: A comunicação não-verbal acaba sendo perdida de certa maneira, o que pode diminuir a qualidade da comunicação e aumentar mal-entendidos.
- **Ferramentas**: A falta de familiaridade com ferramentas de colaboração remota pode criar dificuldades no início dessa junção.
- **Motivação e comprometimento**: Em ambientes assíncronos, é mais difícil manter o comprometimento de ambos os participantes para sessões síncronas regulares.

---

### Duas Alternativas Viáveis para Equipes Remotas

**Alternativa 1 — Live Share assíncrono com revisão gravada**

Tem uma extensão chamada **Live Share do VS Code**, onde um pode escreve o código enquanto outro acompanha remoto e comenta em tempo real. Na sequência, podem trocam os papéis. Essa abordagem preserva o pair programming (dois olhares sobre o mesmo código) sem exigir sincronia perfeita.

**Alternativa 2 — Pair Programming orientado a Pull Request (PR Review em dupla)**

Um aluno implementa uma funcionalidade em uma branch e abre um PR. Em vez de uma revisão solo, a dupla agenda uma sessão curta via Discord, Meet nesse caso tanto faz a ferramenta, mas apenas para revisar juntos o PR, discutir decisões de design e sugerir melhorias em tempo real antes de aprovar o merge.

---

## Questão 1 - C)

### Dificuldades Mais Relevantes no Contexto da AgileTech

Fred Brooks identificou quatro dificuldades essenciais no desenvolvimento de software. Analisando o contexto da AgileTech, duas se destacam como as mais críticas:

**1. Mutabilidade (Changeability)**

Os "requisitos iniciais vagos e sujeitos a mudanças frequentes" refletem exatamente a natureza mutável do software. Diferente de um produto físico, o software é constantemente pressionado a mudar conforme o ambiente, o mercado e o entendimento do usuário evoluem.

**2. Complexidade (Complexity)**

Com uma equipe de apenas 6 pessoas construindo um sistema de gestão de projetos ágeis. Sistemas de software são complexos por natureza — as interações entre componentes crescem de forma não-linear.

---

### Como os Métodos Ágeis Mitigam Essas Dificuldades

**Mitigando a Mutabilidade:**

O ágil é justamente para lidar com mudanças. Em vez de resistir à mutabilidade. Ciclos curtos de sprint significam que nenhuma mudança de requisito precisa esperar meses para ser absorvida — ela entra no próximo planejamento. 
O backlog refinado continuamente permite reordenar prioridades sem trauma.
A entrega incremental reduz o custo de uma mudança de direção, pois menos trabalho foi investido na direção errada.

**Mitigando a Complexidade:**

Em vez de tentar antecipar toda a complexidade futura no início, o sistema evolui de forma incremental: implementa-se somente o que é necessário agora, e o design é melhorado continuamente conforme o entendimento cresce.