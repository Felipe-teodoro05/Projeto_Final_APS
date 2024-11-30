# Diagrama de Objeto

O Diagrama de Objetos mostra exemplos concretos de objetos no sistema, como uma instância de um usuário e suas tarefas no momento da execução. Foi feito utilizando programação orientada a objetos por meio da linguagem Python e o código está disponível no GitHub.

Classe Usuário
```python
class Usuario:
    def __init__(self, nome, email, senha):
        self._nome = nome
        self._email = email
        self._senha = senha
        self._estado = "Logado"

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def email(self):
        return self._email
    
    @property
    def estado(self):
        return self._estado

    def autenticar(self):
        return f"Usuário {self._nome} autenticado."
```

Classe Tarefa
```python
class Tarefa:
    def __init__(self, id_tarefa, titulo, prazo, descricao, status):
        self._id_tarefa = id_tarefa
        self._titulo = titulo
        self._prazo = prazo
        self._descricao = descricao
        self._status = status

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self._titulo = novo_titulo

    @property
    def prazo(self):
        return self._prazo

    @prazo.setter
    def prazo(self, novo_prazo):
        self._prazo = novo_prazo

    @property
    def descricao(self):
        return self._descricao

    @property
    def status(self):
        return self._status

    def criar_tarefa(self):
        return f"Tarefa '{self._titulo}' criada."

    def editar_tarefa(self, novo_titulo):
        self.titulo = novo_titulo
        return f"Tarefa atualizada para '{self._titulo}'."

    def excluir_tarefa(self):
        return f"Tarefa '{self._titulo}' excluída."
```
Classe Notificação
```python
class Notificacao:
    def __init__(self, titulo, data):
        self._titulo = titulo
        self._data = data
        self._estado = "Enviada"

    @property
    def titulo(self):
        return self._titulo

    @property
    def data(self):
        return self._data

    @property
    def estado(self):
        return self._estado

    def enviar_notificacao(self):
        return f"Notificação '{self._titulo}' enviada."
```
```python
class API:
    def consultar_prioridade(self, tarefas):
        return f"Consultando prioridade para {len(tarefas)} tarefas."

    def validar_resposta(self):
        return "Resposta validada."
```
Verificando se deu certo
```python
# Criando objetos 
usuario = Usuario(nome="João", email="joao@example.com", senha="123456")
tarefa1 = Tarefa(id_tarefa=1, titulo="Estudar Python", prazo="2024-11-25", descricao="Revisar listas e dicionários", status="Pendente")
tarefa2 = Tarefa(id_tarefa=2, titulo="Enviar relatório", prazo="2024-11-22", descricao="Relatório semanal para o chefe", status="Concluído")
notificacao = Notificacao(titulo="Lembrete", data="2024-11-20")
api = API()

# Aqui eu conferi se tudo estava rodando
print(usuario.autenticar())
print(tarefa1.criar_tarefa())
print(tarefa2.editar_tarefa("Atualizar relatório semanal"))
print(notificacao.enviar_notificacao())
print(api.consultar_prioridade([tarefa1, tarefa2]))
```