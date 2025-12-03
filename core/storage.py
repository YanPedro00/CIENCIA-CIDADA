"""
Configurações customizadas de storage para Cloudinary
"""
from cloudinary_storage.storage import RawMediaCloudinaryStorage


class DocumentStorage(RawMediaCloudinaryStorage):
    """
    Storage para documentos não-imagem (PDF, CSV, DOCX, etc)
    Usa resource_type='raw' do Cloudinary
    """
    pass

