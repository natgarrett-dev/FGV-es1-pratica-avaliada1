# Processo XP e Scrum - AgileTech Solutions

## Questão 2 - a)

### 5 Práticas de XP

**1. TDD (Test-Driven Development)**
Escrever o teste antes do código: testar → implementar o mínimo → refatorar. Garante código confiável e fácil de manter.

**2. Refatoração Contínua**
Melhorar o código sem mudar o comportamento. Evita dívida técnica e mantém a base do código "limpa".

**3. Design Simples (YAGNI)**
Implementar apenas o necessário, com o foco no cliente. Reduz complexidade e acelera entregas.

**4. Integração Contínua (CI)**
Integrar código várias vezes ao dia com testes automatizados. Detecta erros rápido e mantém o sistema estável.

**5. Padrões de Código**
Seguir convenções de código. Facilita leitura, colaboração e revisões.

---

### XP + Scrum (integração)

| Prática XP          | Onde entra no Scrum | Aplicação                          |
| ------------------- | ------------------- | ---------------------------------- |
| TDD                 | Sprint              | Só está “Done” com testes          |
| Refatoração         | Durante a Sprint    | Parte do Definition of Done        |
| Design Simples      | Planning            | Define escopo sem excessos         |
| Integração Contínua | Diário              | Cada commit roda testes            |
| Padrões de Código   | Sempre              | Aplicado em reviews e no dia a dia |

**Ou seja:** Scrum define o processo; XP garante a qualidade técnica.

---

### Fluxo Semanal

**Segunda:** Daily + desenvolvimento + CI + pair programming
**Terça:** Daily + TDD + refinamento do backlog
**Quarta:** Daily + desenvolvimento + code review
**Quinta:** Daily + desenvolvimento + refatoração
**Sexta:** Daily + finalização + organização do Kanban

---

### Quadro Kanban — GitHub Projects

> **Link para o quadro:** [GitHub Projects](https://github.com/users/natgarrett-dev/projects/1)

**Colunas configuradas:**

- **Backlog** — Histórias priorizadas aguardando sprint
- **Sprint Backlog** — Itens comprometidos na sprint atual
- **Em Progresso** — Histórias sendo desenvolvidas
- **Em Revisão (Code Review)** — PRs abertos aguardando aprovação
- **Concluído** — Itens que atendem ao Definition of Done

**Cards (User Stories) no quadro:**

1. `[US-01]` Como usuário, quero me cadastrar no sistema com nome, e-mail e senha para ter acesso à plataforma.
2. `[US-02]` Como usuário cadastrado, quero fazer login com e-mail e senha para acessar minha conta.
3. `[US-03]` Como administrador, quero listar todos os usuários cadastrados para monitorar o acesso à plataforma.
4. `[US-04]` Como usuário, quero criar um projeto ágil com nome e descrição para organizar meu trabalho.
5. `[US-05]` Como usuário, quero visualizar o backlog do meu projeto para gerenciar as histórias de usuário.

---

## Questão 2 - b) Cronograma de Sprint de 2 Semanas

### Sprint de 2 Semanas (resumo direto)

#### Semana 1

* **Segunda (Dia 1):** Sprint Planning (2h) + início do desenvolvimento (TDD)
* **Terça a Quinta:** Daily (15 min) + desenvolvimento + CI
* **Quarta:** Refinamento do backlog (1h)
* **Sexta:** Code review + consolidação (2h)

#### Semana 2

* **Segunda a Quarta:** Daily (15 min) + desenvolvimento + refatoração
* **Quinta (Dia 9):** Preparação da Review (1h)
* **Sexta (Dia 10):** Sprint Review (1h) + Retrospectiva (1h)

---

### Cerimônias (essencial)

**Sprint Planning**
Definir histórias, estimar, selecionar escopo.

**Daily (15 min)**
Ontem / hoje / impedimentos. Foco em destravar o time.

**Sprint Review**
Apresentar o incremento e coletar feedback do cliente.

**Retrospectiva**
Ajustar o processo com ações práticas para a próxima sprint.

---

### XP na Sprint

* **TDD:** todos os dias
* **CI:** a cada commit
* **Refatoração:** contínua + foco no fim das tarefas
* **Design Simples:** guia decisões
* **Padrões de Código:** aplicados em reviews

---

### Entregas ao final

* Software funcional e testado
* Histórias concluídas e aprovadas
* Backlog atualizado
* Melhorias definidas
* Código limpo e integrado

---

### Scrum vs Kanban

| Critério     | Scrum              | Kanban          |
| ------------ | ------------------ | --------------- |
| Tempo        | Sprints fixas      | Fluxo contínuo  |
| Papéis       | Definidos          | Flexíveis       |
| Planejamento | Por sprint         | Contínuo        |
| WIP          | Implícito          | Explícito       |
| Mudanças     | Evitadas na sprint | Permitidas      |
| Entrega      | Por sprint         | Contínua        |

---

### Quando usar

**Scrum:** previsibilidade, ciclos definidos, produto em evolução
**Kanban:** demandas variáveis, suporte/operações, alta flexibilidade

---

### Scrumban (híbrido)

Usa **estrutura do Scrum** + **fluxo e WIP do Kanban**.
Resultado: mais previsibilidade com melhor controle de gargalos.