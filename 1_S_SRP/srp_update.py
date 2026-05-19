# ==========================================
# 1. SERVIÇO DE COMUNICAÇÃO E NOTIFICAÇÕES
# ==========================================
class NotificationService:
    """
    Responsável estritamente pela comunicação externa, conexões de API
    e envio de alertas ou documentos aos utilizadores.
    """
    
    def connect_api(self) -> None:
        """Estabelece a ligação com o serviço externo de comunicação."""
        pass

    def send_notification(self, message: str) -> None:
        """Envia uma notificação direta para o utilizador."""
        pass

    def send_report(self, report_data: dict) -> None:
        """Envia um relatório gerado para o destino final (e-mail, webhook, etc)."""
        pass


# ==========================================
# 2. GERADOR DE RELATÓRIOS
# ==========================================
class ReportGenerator:
    """
    Responsável apenas por processar dados e construir relatórios.
    Não sabe como os dados são guardados nem como o relatório é enviado.
    """
    
    def generate_report(self, tasks: list) -> dict:
        """Processa a lista de tarefas e gera a estrutura de um relatório."""
        # Lógica para somar tarefas concluídas, pendentes, etc.
        report = {"total_tasks": len(tasks), "status": "Processed"}
        return report


# ==========================================
# 3. GESTOR DE TAREFAS (CORE BUSINESS)
# ==========================================
class TaskRepository:
    """
    Responsável única e exclusivamente por gerir o ciclo de vida das tarefas
    (Criar, Atualizar, Remover).
    """
    
    def __init__(self):
        # Simulando uma base de dados interna em memória
        self.tasks = []

    def create_task(self, task_data: dict) -> None:
        """Adiciona uma nova tarefa ao sistema."""
        self.tasks.append(task_data)

    def update_task(self, task_id: int, new_data: dict) -> None:
        """Atualiza os dados de uma tarefa existente."""
        pass

    def remove_task(self, task_id: int) -> None:
        """Remove uma tarefa do sistema."""
        pass
    