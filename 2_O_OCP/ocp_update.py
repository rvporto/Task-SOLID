from abc import ABC, abstractmethod

# ==========================================
# 1. A INTERFACE (MOLDE PADRÃO PARA EXAMES)
# ==========================================
class Exame(ABC):
    """
    Esta é a nossa classe abstrata (interface). 
    Ela serve como um contrato: qualquer novo exame criado na clínica
    OBRIGATORIAMENTE precisa criar o método 'verificar_condicoes'.
    """
    
    @abstractmethod
    def verificar_condicoes(self) -> bool:
        """Deve retornar True se o exame for aprovado ou False se falhar."""
        pass


# ==========================================
# 2. CLASSES ESPECÍFICAS (EXTENSÕES)
# ==========================================
class ExameSangue(Exame):
    """Classe responsável apenas pelas regras do Exame de Sangue."""
    
    def verificar_condicoes(self) -> bool:
        # Aqui colocarias as regras reais (ex: verificar níveis de plaquetas)
        print("A verificar condições do laboratório de sangue...")
        return True  # Simulação de aprovação


class ExameRaioX(Exame):
    """Classe responsável apenas pelas regras do Raio-X."""
    
    def verificar_condicoes(self) -> bool:
        # Aqui colocarias as regras reais (ex: verificar nitidez da imagem)
        print("A verificar calibração da máquina de Raio-X...")
        return True  # Simulação de aprovação


# ==========================================
# 3. O PROCESSADOR (FECHADO PARA MODIFICAÇÕES)
# ==========================================
class AprovaExame:
    """
    Esta classe está FECHADA para modificações.
    Repara que ela não tem nenhum 'if' ou 'elif' para checar o tipo de exame.
    Ela aceita qualquer objeto que siga o molde 'Exame'.
    """
    
    def aprovar_solicitacao_exame(self, exame: Exame) -> None:
        # Chamamos o método do contrato. Não importa qual é o exame, ele sabe se verificar.
        if exame.verificar_conditions():
            print("=> Solicitação de exame APROVADA com sucesso!\n")
        else:
            print("=> Solicitação de exame REJEITADA.\n")