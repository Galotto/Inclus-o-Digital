import hashlib
import uuid

def hash_senha(senha: str) -> str:
    """Retorna o hash SHA-256 de uma senha."""
    return hashlib.sha256(senha.encode()).hexdigest()

def gerar_id_anonimo(email: str) -> str:
    """Gera um identificador anônimo baseado no email + UUID."""
    base = email + str(uuid.uuid4())
    return hashlib.sha256(base.encode()).hexdigest()

def validar_senha_forte(senha: str) -> bool:
    """Verifica se a senha atende aos critérios mínimos de segurança."""
    return (
        len(senha) >= 6 and
        any(c.islower() for c in senha) and
        any(c.isupper() for c in senha) and
        any(c.isdigit() for c in senha)
    )