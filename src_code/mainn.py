#!/usr/bin/env python
import sys
import crew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'tasks': 
            '''
            1.Preparar uma apresentação para a reunião de amanhã.
            2.Escrever um relatório que deve ser entregue na próxima semana.
            3.Revisar um contrato que é urgente.
            4.Responder e-mails importantes de clientes.
            5.Fazer uma pesquisa sobre novos fornecedores.
            Para cada tarefa, inclua as seguintes informações para que eu possa avaliar a prioridade com precisão:
        Task Name: Um breve nome descritivo para a tarefa.
        Description: Uma explicação mais detalhada do que a tarefa envolve.
        Due Date (if applicable): A data e hora em que a tarefa precisa ser concluída. Se não houver uma data específica, por favor, indique isso.
        Impact: Descreva o impacto positivo potencial de concluir essa tarefa. Seja o mais específico possível (por exemplo, "Aumentar as vendas em 10%", "Melhorar a satisfação do cliente em 5 pontos"). Se a tarefa previne um resultado negativo, descreva isso também.
        Complexity: Estime o nível de esforço necessário para concluir a tarefa. Você pode usar termos como "Baixo", "Médio" ou "Alto", ou fornecer uma estimativa mais granular (por exemplo, "1 hora", "2 dias", "1 semana"). Considere as habilidades, recursos e dependências envolvidos
            '''
        
    }
    crew.SistemaMultiAgentesCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        crew.SistemaMultiAgentesCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        crew.SistemaMultiAgentesCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": ""
    }
    try:
        crew.SistemaMultiAgentesCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

run()
