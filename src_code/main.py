#!/usr/bin/env python
import sys
import crew

def run():
    inputs = {
        'tasks': 
            "Preparar uma apresentação para a reunião de amanhã.",
        'description': '''Tenho as seguintes tarefas para realizar:

Preparar uma apresentação para a reunião de amanhã.
Escrever um relatório que deve ser entregue na próxima semana.
Revisar um contrato que é urgente.
Responder e-mails importantes de clientes.
Fazer uma pesquisa sobre novos fornecedores.
Para cada tarefa, inclua as seguintes informações para que eu possa avaliar a prioridade com precisão:

Task Name: Um breve nome descritivo para a tarefa.
Description: Uma explicação mais detalhada do que a tarefa envolve.
Due Date (if applicable): A data e hora em que a tarefa precisa ser concluída. Se não houver uma data específica, por favor, indique isso.
Impact: Descreva o impacto positivo potencial de concluir essa tarefa. Seja o mais específico possível (por exemplo, "Aumentar as vendas em 10%", "Melhorar a satisfação do cliente em 5 pontos"). Se a tarefa previne um resultado negativo, descreva isso também.
Complexity: Estime o nível de esforço necessário para concluir a tarefa. Você pode usar termos como "Baixo", "Médio" ou "Alto", ou fornecer uma estimativa mais granular (por exemplo, "1 hora", "2 dias", "1 semana"). Considere as habilidades, recursos e dependências envolvidos.'''

    }
    crew.SistemaMultiAgentesCrew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
