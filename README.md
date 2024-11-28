# Assistente de Priorização de Tarefas

Este projeto é um sistema assistente de priorização de tarefas, desenvolvido para ajudar na organização e aumento de produtividade dos usuários. Ele permite cadastrar tarefas, gerenciar suas prioridades automaticamente e enviar notificações de lembretes.

## Funcionalidades

- **Cadastro e autenticação de usuário**: Permite o cadastro e login do usuário no sistema.
- **Gerenciamento de tarefas (CRUD)**: Criação, leitura, atualização e exclusão de tarefas.
- **Priorização automática de tarefas**: O sistema sugere uma ordem de execução das tarefas com base em prazos e histórico utilizando uma API de Inteligência Artificial.
- **Notificações**: O sistema envia lembretes sobre as tarefas pendentes.
- **Relatórios de atividades**: O sistema gera relatórios sobre as tarefas realizadas.
- **Integração com calendário**: Sincroniza as tarefas com o calendário do usuário.

## Como rodar o projeto

### Pré-requisitos
- [Node.js](https://nodejs.org/) - Para rodar o frontend (caso seja em JavaScript).
- [Python](https://www.python.org/) - Caso o backend utilize Python.
- Banco de dados MySQL.

### Passos para rodar localmente

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/assistente-priorizacao-tarefas.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd assistente-priorizacao-tarefas
    ```

3. Instale as dependências (caso existam dependências para instalar):

    Para frontend (se for JavaScript):
    ```bash
    npm install
    ```

    Para backend (se for Python):
    ```bash
    pip install -r requirements.txt
    ```

4. Inicialize o servidor local (para backend ou frontend conforme o caso):

    Para o **frontend** (por exemplo, se for React):
    ```bash
    npm start
    ```

    Para o **backend** (por exemplo, Flask):
    ```bash
    python app.py
    ```

5. Acesse o sistema no navegador:

    ```
    http://localhost:3000  # ou outra porta configurada
    ```

## Como contribuir

1. Faça um fork deste repositório.
2. Crie uma branch para a sua feature (`git checkout -b feature/nova-feature`).
3. Faça o commit das suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Envie para o seu fork (`git push origin feature/nova-feature`).
5. Crie um Pull Request para a branch principal deste repositório.

## Licença

Este projeto está licenciado sob a licença MIT - consulte o [arquivo LICENSE](LICENSE) para mais detalhes.
