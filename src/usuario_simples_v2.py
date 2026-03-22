# usuario_simples.py
import hashlib
import uuid
from datetime import datetime
from typing import List, Optional


class Usuario:
    """Representa um usuário do sistema com os dados essenciais."""

    def __init__(self, nome: str, email: str, senha: str):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.email = email
        self.senha = self._hash_senha(senha)
        self.data_cadastro = datetime.now()

    def _hash_senha(self, senha: str) -> str:
        """Retorna o hash SHA-256 da senha fornecida."""
        return hashlib.sha256(senha.encode()).hexdigest()

    def validar_senha(self, senha: str) -> bool:
        """Verifica se a senha fornecida corresponde à senha cadastrada."""
        return self._hash_senha(senha) == self.senha


class GerenciadorUsuarios:
    """Gerencia o cadastro e autenticação de usuários."""

    def __init__(self):
        self.usuarios: List[Usuario] = []
        self._indice_email: dict = {}

    def cadastrar(self, nome: str, email: str, senha: str) -> Usuario:
        """Cadastra um novo usuário. Lança ValueError se o e-mail já estiver em uso."""
        if email in self._indice_email:
            raise ValueError("Email já cadastrado")

        usuario = Usuario(nome, email, senha)
        self.usuarios.append(usuario)
        self._indice_email[email] = usuario
        return usuario

    def fazer_login(self, email: str, senha: str) -> Optional[Usuario]:
        """Autentica o usuário pelo e-mail e senha. Retorna o usuário ou None."""
        usuario = self._indice_email.get(email)
        if usuario and usuario.validar_senha(senha):
            return usuario
        return None

    def listar_todos(self) -> List[Usuario]:
        """Retorna a lista de todos os usuários cadastrados."""
        return self.usuarios
