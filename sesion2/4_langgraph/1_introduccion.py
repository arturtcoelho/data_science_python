# LangGraph - Introducción
# LangGraph es una biblioteca para crear agentes y flujos de trabajo con LLMs

# Nota: Requiere instalar langgraph
# pip install langgraph langchain langchain-openai

"""
Conceptos básicos de LangGraph:

1. **State**: Estado compartido entre nodos (diccionario)
2. **Nodes**: Funciones que procesan el estado
3. **Edges**: Conexiones entre nodos (flujo del grafo)
4. **Graph**: Define la estructura del workflow

Estructura básica:
- state = {"messages": []}
- node(state) -> state actualizado
- graph.add_node("nombre", node)
- graph.add_edge("start", "nombre")
"""

# Ejemplo conceptual (no ejecuta sin API key)
from typing import TypedDict

# Definir el estado
class AgentState(TypedDict):
    messages: list
    data: dict

# Ejemplo de nodo
def process_data(state: AgentState) -> AgentState:
    # Procesar datos
    state["data"] = {"resultado": "procesado"}
    return state

# Ejemplo de grafo (sintaxis)
"""
from langgraph.graph import StateGraph

graph = StateGraph(AgentState)
graph.add_node("process", process_data)
graph.set_entry_point("process")
graph.set_finish_point("process")

app = graph.compile()
"""

print("Conceptos de LangGraph:")
print("1. State - Estado compartido")
print("2. Nodes - Funciones que procesan") 
print("3. Edges - Flujo entre nodos")
print("4. Graph - Estructura completa")
print("\nCasos de uso en Data Science:")
print("- Automatizar análisis de datos")
print("- Pipelines de ML automatizados")
print("- Agentes de investigación")
print("- Chatbots con contexto")
