from backends.xml.serializer import Serializer


def create_serializer(backend, filepath):
    if backend == "xml.gz":
        return Serializer(filepath)