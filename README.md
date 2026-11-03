# Blue Team Notes

Registro da minha transição do desenvolvimento de software para a **segurança defensiva (Blue Team)**: estudos, laboratórios práticos e relatórios de investigação.

**Objetivo:** atuar como **Analista SOC N1** e evoluir para **Resposta a Incidentes e Forense Digital (DFIR)**.

---

## Por que Blue Team

Venho do desenvolvimento, com base em código, arquitetura de software e infraestrutura. Gosto de reconstruir os passos de um problema a partir de evidências, de redes e servidores Linux, e de explicar questões técnicas em relatórios claros. Esse é o dia a dia de quem investiga incidentes de segurança.

A base de dev entra como diferencial: automatizar análises com Python e Bash e entender como as aplicações funcionam por dentro.

## Método de estudo

Cada tema segue o mesmo ciclo:

1. **Teoria:** entender o conceito antes de tocar nas ferramentas.
2. **Prática:** aplicar em laboratório, com dados e cenários simulados.
3. **Registro:** documentar neste repositório o que foi feito, o que foi encontrado e o que aprendi.

Acredito que prática documentada mostra mais do que certificados. Cada investigação aqui tem as evidências junto, para quem quiser conferir o raciocínio.

## Trilha de estudos

| Etapa | Tema | Status |
| --- | --- | --- |
| 0 | Base de dev: Python e Bash para análise de logs | Em andamento |
| 1 | Redes: TCP/IP, DNS, HTTP/TLS, Wireshark | Não iniciada |
| 2 | Linux e Windows: logs, processos, permissões, Active Directory | Não iniciada |
| 3 | Fundamentos de segurança: ameaças, controles, criptografia | Não iniciada |
| 4 | Operação de SOC: SIEM, triagem de alertas, MITRE ATT&CK, phishing | Não iniciada |
| 5 | Resposta a incidentes e introdução à forense digital | Não iniciada |

Cada etapa termina com um **marco**: uma tarefa prática que prova que o conteúdo foi entendido antes de avançar.

## Relatórios de investigação

| Nº | Caso | Técnicas e conceitos |
| --- | --- | --- |
| 01 | [Força bruta via SSH no srv-web](relatorios/01-forca-bruta-ssh/relatorio.md) | Análise de `auth.log`, força bruta, escalonamento com `sudo`, acesso ao `/etc/shadow`, persistência, ciclo de resposta do NIST |

## Estrutura do repositório

```
blue-team-notes/
├── README.md
├── relatorios/
│   └── 01-forca-bruta-ssh/
│       ├── relatorio.md     ← relatório do incidente
│       └── auth.log         ← log usado como evidência
├── scripts/
│   └── contar_falhas.py     ← conta falhas de login por IP
└── notas/
    └── etapa-0.md           ← anotações de estudo por etapa
```

## Ferramentas e plataformas

- **Linguagens:** Python, Bash
- **Análise de logs e tráfego:** `grep`, `awk`, Wireshark
- **SIEM:** Wazuh, Splunk, Elastic (Etapa 4)
- **Prática:** [TryHackMe](https://tryhackme.com/path/outline/soclevel1), LetsDefend, CyberDefenders, OverTheWire
- **Frameworks:** MITRE ATT&CK, Cyber Kill Chain, ciclo de resposta a incidentes do NIST

## Sobre os dados

Todos os cenários deste repositório são **exercícios de treinamento**. Servidores, usuários e logs são fictícios, e os IPs pertencem a faixas reservadas para documentação (RFC 5737) ou a redes privadas. Nenhum dado real de pessoas ou empresas é publicado aqui.

---

**Contato:** [LinkedIn](https://www.linkedin.com/in/gustavo92aaa5394) · dearaujoluisgustavo95@gmail.com
