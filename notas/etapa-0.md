# Etapa 0 · Base de dev

Anotações do que aprendi na primeira etapa da trilha: ler logs de autenticação e usar Python para analisá-los.

## Dia 1 · 02/11/2026

### Como ler uma linha de log de SSH

Cada linha do `/var/log/auth.log` conta uma pequena história. Quebrando em partes:

```
Oct 28 21:14:02 srv-web sshd[1423]: Failed password for root from 203.0.113.45 port 52211 ssh2
```

- `Oct 28 21:14:02` → quando aconteceu
- `srv-web` → em qual máquina
- `sshd[1423]` → qual programa registrou (o serviço de SSH)
- `Failed password` → o que aconteceu
- `root` → qual usuário foi tentado
- `203.0.113.45` → de onde veio a tentativa

### O que procurar num log de autenticação

- **Muitas falhas do mesmo IP em pouco tempo:** força bruta.
- **Tentativas com usuários que não existem** (`invalid user`): varredura automatizada.
- **Falhas seguidas de um sucesso do mesmo IP:** o alerta mais grave, porque o atacante entrou.
- **Prioridade não é volume:** o IP que mais tentou nem sempre é o mais perigoso. O que conseguiu entrar vem primeiro.

### Linux: caminhos e arquivos importantes

- Tudo começa na raiz `/`. Um caminho como `/etc/shadow` significa: o arquivo `shadow`, dentro da pasta `etc`, na raiz.
- `/etc/` guarda as configurações do sistema.
- `/etc/shadow` guarda os hashes das senhas de todos os usuários, inclusive do root.
- `/var/log/auth.log` guarda os registros de login.
- `sudo` executa um comando como root (`USER=root` no log), o administrador que pode tudo.

### Hash de senha

A senha não fica salva como é escrita: ela vira um hash, um embaralhamento de mão única. Quem rouba os hashes tenta quebrá-los offline, testando milhões de senhas comuns até alguma gerar o mesmo hash. Senhas fracas caem rápido.

### Python usado no script de contagem

O script [`contar_falhas.py`](../scripts/contar_falhas.py) conta as falhas de login por IP. Conceitos usados:

- `with open(...)` → abre o arquivo e fecha sozinho no final
- `for linha in arquivo` → passa por cada linha
- `if "texto" in linha` → filtra as linhas que interessam
- `linha.split()` → quebra a linha numa lista de palavras
- `.index("from")` → encontra a posição de uma palavra na lista; o IP vem logo depois
- dicionário `{}` → guarda pares de chave e valor (IP e número de falhas)
- `sorted(..., reverse=True)` → ordena do maior para o menor

### Persistência e contenção

Resumo no [relatório 01](../relatorios/01-forca-bruta-ssh/relatorio.md), seção Aprendizados.

### Pendente

- [ ] Refazer a contagem de falhas em Bash com `grep`, `awk`, `sort` e `uniq -c`
