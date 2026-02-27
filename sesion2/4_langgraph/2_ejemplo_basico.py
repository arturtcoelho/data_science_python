# Ejemplo básico de LangGraph
# Requiere: pip install langgraph langchain-openai

from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END

# 1. Definir el estado
class ChatState(TypedDict):
    messages: list[str]
    user_input: str

# 2. Definir nodos (funciones)
def ask_question(state: ChatState) -> ChatState:
    """Nodo que hace una pregunta al usuario"""
    pregunta = state.get("user_input", "¿Qué datos quieres analizar?")
    print(f"🤖: {pregunta}")
    return state

def process_response(state: ChatState) -> ChatState:
    """Nodo que procesa la respuesta"""
    # Simular procesamiento
    state["messages"].append(f"Procesando: {state.get('user_input', '')}")
    return state

def analyze_data(state: ChatState) -> ChatState:
    """Nodo que analiza datos"""
    # Aquí iría la lógica de análisis real
    result = "Análisis completado: 150 registros procesados"
    state["messages"].append(result)
    return state

def generate_report(state: ChatState) -> ChatState:
    """Nodo que genera reporte"""
    report = "Reporte generado: resumen_2024.pdf"
    state["messages"].append(report)
    return state

# 3. Crear el grafo
def create_workflow():
    graph = StateGraph(ChatState)
    
    # Añadir nodos
    graph.add_node("ask", ask_question)
    graph.add_node("process", process_response)
    graph.add_node("analyze", analyze_data)
    graph.add_node("report", generate_report)
    
    # Definir flujo
    graph.set_entry_point("ask")
    graph.add_edge("ask", "process")
    graph.add_edge("process", "analyze")
    graph.add_edge("analyze", "report")
    graph.add_edge("report", END)
    
    return graph.compile()

# 4. Ejecutar (simulado)
if __name__ == "__main__":
    # Este código mostraría cómo ejecutar el grafo
    # Requiere API key de OpenAI/Anthropic para funcionar realmente
    
    workflow = create_workflow()
    
    # Estado inicial
    initial_state = {
        "messages": [],
        "user_input": "Analiza las ventas del mes pasado"
    }
    
    print("=== Ejemplo de flujo LangGraph ===")
    print(f"Input: {initial_state['user_input']}")
    print("\nFlujo del agente:")
    print("ask -> process -> analyze -> report")
    print("\nNodos implementados:")
    print("1. ask_question: Solicita input al usuario")
    print("2. process_response: Procesa la solicitud")
    print("3. analyze_data: Ejecuta análisis de datos")
    print("4. generate_report: Genera reporte final")
    
    # Descomenta para ejecutar realmente (requiere API key):
    # result = workflow.invoke(initial_state)
    # print(result["messages"])
