# Análise YAGNI — Classe Usuario

## Questão 3 - A) 

O princípio **YAGNI (You Aren't Gonna Need It)** determina que o desenvolvedor deve implementar apenas o que é necessário *agora*, evitando antecipar necessidades futuras que podem nunca se concretizar. O sistema atual precisa somente de três funcionalidades: **cadastrar usuários**, **fazer login** e **listar todos os usuários**.

---

## Atributos Desnecessários na Classe `Usuario`

| Atributo | Por que viola YAGNI |
|---|---|
| `ultimo_login` | Nenhum dos requisitos atuais exige rastrear a data do último login. |
| `perfil` | Os requisitos não mencionam tipos de perfil ou diferenciação entre usuários. |
| `permissoes` | Controle de permissões não faz parte das funcionalidades necessárias. |
| `configuracoes` | Personalização de configurações por usuário não é um requisito atual. |
| `historico_logins` | Manter histórico de logins é uma funcionalidade não solicitada. |
| `foto_perfil_url` | Fotos de perfil não são requeridas pelo sistema atual. |
| `telefone` | Dados de contato extras não fazem parte dos requisitos. |
| `endereco` | Endereço não é necessário para cadastrar, logar ou listar usuários. |
| `empresa` | Dados profissionais não são requisitos do sistema atual. |
| `cargo` | Idem — não há necessidade de armazenar o cargo do usuário. |
| `departamento` | Idem — informação profissional fora do escopo atual. |

---

## Métodos Desnecessários na Classe `Usuario`

| Método | Por que viola YAGNI |
|---|---|
| `adicionar_permissao()` | O sistema não possui controle de permissões nos requisitos atuais. |
| `remover_permissao()` | Idem — sem controle de permissões, este método não tem utilidade. |
| `tem_permissao()` | Idem — verificar permissões não é uma necessidade atual. |
| `atualizar_configuracao()` | Configurações personalizadas por usuário não são requeridas. |
| `registrar_login()` | Registrar histórico de logins vai além do necessário para validar autenticação. |
| `exportar_json()` | Exportação de dados não é um requisito do sistema atual. |
| `exportar_xml()` | Idem — exportação em XML não foi solicitada. |
| `atualizar_foto_perfil()` | Fotos de perfil não são requisito. |
| `atualizar_dados_profissionais()` | Dados profissionais não fazem parte do escopo atual. |

---

## Métodos Desnecessários na Classe `GerenciadorUsuarios`

| Método | Por que viola YAGNI |
|---|---|
| `cache` (atributo) | Um cache de usuários é otimização prematura para uma lista simples. |
| `buscar_por_id()` | Busca por ID não é um dos três requisitos solicitados. |
| `buscar_por_perfil()` | Não há requisito de perfil, logo buscar por perfil é desnecessário. |
| `buscar_por_permissao()` | Idem ao controle de permissões — fora do escopo. |
| `exportar_todos_json()` | Exportação não é um requisito do sistema. |
| `importar_usuarios_json()` | Importação não solicitada e sequer implementada (corpo vazio com `pass`). |
| `gerar_relatorio_atividade()` | Relatórios de atividade não fazem parte dos requisitos atuais. |
| `_atualizar_cache()` | Função auxiliar do cache desnecessário. |

---

## Resumo

O código original, ao tentar antecipar necessidades futuras, adicionou **11 atributos extras**, **9 métodos extras na classe `Usuario`** e **7 métodos/atributos extras na classe `GerenciadorUsuarios`**. Todo esse código adicional:

- Aumenta a complexidade cognitiva para quem lê e mantém o código
- Cria superfície de bugs em funcionalidades que nunca serão usadas
- Viola o princípio de Design Simples do XP
- Torna o código mais difícil de refatorar quando os requisitos reais chegarem, pois há mais dependências e estruturas a considerar

O princípio YAGNI não proíbe pensar no futuro — proíbe *implementar* o futuro antes que ele seja necessário.
