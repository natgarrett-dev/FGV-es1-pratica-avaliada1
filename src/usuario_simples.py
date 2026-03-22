import hashlib
import uuid
from datetime import datetime
from typing import List, Optional

class Usuario:
    """
        Usuários do sistema 
    """

    def __init__(self, nome: str, email: str, senha: str):
       self.id = str(uuid.uuid4)
       self.nome = nome
       self.email = email
       self.senha = self._hash_senha(senha)
       self.data_cadastro = datetime.now()

    def _hash_senha(self, senha: str) -> str:
        return hashlib.sha256(senha.encode()).hexdigest() # Hash - SHA-256 da senha fornecida

    def validar_senha(self, senha: str) -> bool:
        return self._hash_senha(senha) == self.senha # Veririfica - senha fornecida corresponde à senha cadastrada

class GerenciadorUsuarios:

    """
    Gerencia o cadastro e autenticação de usuários
    """

    def __init__(self):
        self.usuarios: List[Usuario] = []
        self._indice_email: dict = {}
    
    # Cadastro do usuário - caso já tenha um e-mail cadastrado retorna um erro
    def cadastrar(self, nome: str, email: str, senha: str) -> Usuario:
        if email in self._indice_email:
            raise ValueError("E-mail já cadastrado")
        
        usuario = Usuario(nome, email, senha)
        self.usuarios.append(usuario)
        self._indice_email[email] = usuario
        return usuario
    
    # Login com autenticação
    def fazer_login(self, email: str, senha: str) -> Optional[Usuario]:
        usuario = self._indice_email.get(email)
        if usuario and usuario.validar_senha(senha):
            return usuario
        return None
    
    def listar_todos(self) -> List[Usuario]:
        return self.usuarios