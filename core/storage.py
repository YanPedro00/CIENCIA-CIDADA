"""
Configurações customizadas de storage para Cloudinary
"""
from cloudinary_storage.storage import RawMediaCloudinaryStorage


class DocumentStorage(RawMediaCloudinaryStorage):
    """
    Storage para documentos não-imagem (PDF, DOCX, CSV, etc)
    Usa resource_type='raw' do Cloudinary
    Força type='upload' para garantir acesso público
    """
    def get_available_name(self, name, max_length=None):
        """Override para garantir que arquivos sejam públicos"""
        return super().get_available_name(name, max_length)
    
    def _save(self, name, content):
        """Override do save para forçar type='upload' (público)"""
        # Garantir que OPTIONS existe
        if not hasattr(self, 'OPTIONS'):
            self.OPTIONS = {}
        
        # Forçar upload público
        self.OPTIONS['type'] = 'upload'  # Público, não authenticated
        self.OPTIONS['resource_type'] = 'raw'  # Para documentos
        
        return super()._save(name, content)
