from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
import os
import yaml
from dotenv import load_dotenv, find_dotenv

import os

# Desativa a telemetria (caso suportado pelo crewai)
os.environ["CREWAI_DISABLE_TELEMETRY"] = "1"

def load_env():
    _ = load_dotenv(find_dotenv())

def get_gemini_api_key():
    load_env()
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    return gemini_api_key

LLModel = LLM(
    model="gemini/gemini-1.5-pro",
    temperature=0.5,
    api_key=get_gemini_api_key(),
)

@CrewBase
class SistemaMultiAgentesCrew:
    """SistemaMultiAgentes crew"""

    def __init__(self):
        self.load_config()

    def load_config(self):
        # Carrega as configurações de agentes e tarefas a partir dos arquivos YAML
        with open('config/agents.yaml', 'r') as f:
            self.agents_config = yaml.safe_load(f)
            #print('Agents config loaded:', self.agents_config)

        with open('config/tasks.yaml', 'r') as f:
            self.tasks_config = yaml.safe_load(f)
            #print('Tasks config loaded:', self.tasks_config)

    @agent
    def prioritization_assistant(self) -> Agent:
        return Agent(
            config=self.agents_config['prioritization_assistant'],
            verbose=True,
            llm=LLModel
        )

    @agent
    def task_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['task_analyzer'],
            verbose=True,
            llm=LLModel
        )

    @task
    def prioritization_task(self) -> Task:
        return Task(
            config=self.tasks_config['prioritization_task'],
            verbose=True
        )

    @task
    def task_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['task_analysis_task'],
            output_file='results/report.md',
            verbose=True
        )

    @crew
    def crew(self) -> Crew:
        """Creates the SistemaMultiAgentes crew"""
        #print('Agents:', self.agents)  # Verifica se os agentes foram registrados
        #print('Tasks:', self.tasks)    # Verifica se as tarefas foram registradas

        return Crew(
            agents=self.agents,  # Automaticamente criado pelos decoradores @agent
            tasks=self.tasks,    # Automaticamente criado pelos decoradores @task
            process=Process.sequential,
            verbose=True
        )

    def kickoff(self, inputs=None):
        """
        Inicia o sistema com as entradas fornecidas, utilizando as tarefas personalizadas, se disponíveis.
        """
        if inputs and 'tasks' in inputs:
            print("Iniciando com tarefas personalizadas:", inputs['tasks'])

            # Cria o crew e chama o método kickoff para iniciar a execução com os inputs
            crew_instance = self.crew()
            # Passa `inputs` diretamente para o kickoff do Crew
            crew_instance.kickoff(inputs=inputs)
        else:
            print("Nenhuma tarefa personalizada encontrada. Verifique `inputs` em main.py")
