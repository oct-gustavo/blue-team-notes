# Relatório 01 · Força bruta via SSH no srv-web

02/11/2026 · Luis Gustavo

Um ataque de força bruta via SSH comprometeu a conta `deploy` e chegou a privilégio de root em menos de 2 minutos. Exercício de treinamento, com servidor fictício e IPs reservados para documentação.

## Resumo

| Campo | Descrição |
| --- | --- |
| O que aconteceu | Ataque de força bruta via SSH que resultou em acesso ao servidor `srv-web` e leitura do arquivo de senhas com privilégio de root |
| Quem | IP `192.0.2.77`, autenticado como o usuário `deploy` |
| Quando | 28/10/2026, das 21:31:50 (primeira falha) às 21:33:40 (leitura do `/etc/shadow`) |
| Fonte analisada | `/var/log/auth.log` do servidor `srv-web` ([cópia do log](auth.log)) |
| Causa provável | Senha fraca na conta `deploy` e servidor aceitando login por senha no SSH |

## Linha do tempo e evidências

O acesso aconteceu após 6 falhas em 18 segundos, uma a cada 3 segundos: ritmo de ferramenta automatizada, não de uma pessoa digitando. A tabela segue a ordem cronológica do ataque.

| Horário (28/10) | Evento | Evidência no log |
| --- | --- | --- |
| 21:31:50 a 21:32:05 | 6 tentativas de senha falhas para `deploy` | `Failed password for deploy from 192.0.2.77` (6 linhas) |
| 21:32:08 | Login aceito para `deploy` vindo do mesmo IP | `Accepted password for deploy from 192.0.2.77 port 60023 ssh2` |
| 21:32:09 | Sessão aberta para `deploy` | `pam_unix(sshd:session): session opened for user deploy` |
| 21:33:40 | Leitura do arquivo de senhas como root | `sudo: deploy : ... USER=root ; COMMAND=/usr/bin/cat /etc/shadow` |

No mesmo período, os IPs `203.0.113.45` (10 falhas) e `198.51.100.23` (4 falhas) também tentaram força bruta, mas nenhum conseguiu entrar.

## Por que é grave

O atacante foi direto ao arquivo de senhas menos de 2 minutos depois de entrar, o que indica que sabia o que procurava.

- **Fato:** o atacante teve acesso de root e visualizou os hashes de senha de todos os usuários, incluindo o root. A conta `deploy` tinha permissão de usar `sudo`.
- **Hipótese:** ele copiou os hashes para quebrá-los offline e obter outras senhas, o que daria acesso a outras contas sem depender do `deploy`.
- **Não confirmado:** não há registro de logout no log, então o invasor pode ainda estar conectado.

## Recomendações

As ações seguem as fases de resposta a incidentes do NIST: primeiro conter, depois investigar e corrigir.

**Contenção (imediato)**

- Salvar uma cópia dos logs do servidor
- Verificar sessões ativas e derrubar a do `deploy`
- Bloquear o IP `192.0.2.77` no firewall
- Bloquear a conta `deploy` e remover a permissão de `sudo`

**Erradicação**

- Procurar persistência: usuários novos, chaves SSH no `authorized_keys`, tarefas agendadas (`cron`) e comandos executados após 21:33:40

**Recuperação**

- Trocar a senha de todos os usuários, incluindo o root, somente depois de remover o invasor

**Lições aprendidas**

- Desativar login por senha no SSH e usar só chaves
- Bloquear automaticamente IPs com muitas falhas de login (`fail2ban`)
- Revisar as contas com `sudo` pelo princípio do menor privilégio

## Aprendizados

**O que é persistência:** é o mecanismo que o invasor deixa no sistema para conseguir voltar mesmo depois de ser expulso. Por isso, depois de uma invasão, não basta derrubar a sessão do atacante: é preciso procurar o que ele pode ter deixado para trás.

- **Chaves SSH** adicionadas no `authorized_keys`, que permitem entrar sem senha
- **Usuários novos** criados pelo atacante
- **Tarefas agendadas** no `cron`, que executam algo dele de tempos em tempos
- **Comandos executados** após a leitura do `/etc/shadow`, revisados nos logs e no histórico de comandos

**Por que a contenção vem primeiro:** enquanto o invasor continua dentro do sistema, ele segue agindo. Se eu começar investigando, ele pode perceber que foi descoberto, apagar os rastros, criar novas formas de persistência ou roubar mais dados. Conter primeiro, isolando o atacante, limita o estrago e me dá um ambiente estável para investigar com calma. A ordem é: conter, erradicar o que ele deixou, recuperar o ambiente e, por fim, corrigir o que permitiu o ataque. A exceção é salvar uma cópia dos logs antes de tudo, para não perder as evidências.
