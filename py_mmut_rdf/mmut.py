from pathlib import Path
from rdflib.namespace import DefinedNamespace
from rdflib import URIRef
from .ontology_reader import OntologyReader


# Absoluten Pfad zum aktuellen Skript-Verzeichnis bestimmen
current_dir = Path(__file__).parent

# TTL-Datei im gleichen Verzeichnis finden
ontology_file = current_dir / "mmut.ttl"
ontology = OntologyReader(str(ontology_file))


class MMUT(DefinedNamespace):

    _NS = ontology.get_namespace()

    MicroModel: URIRef = ontology.get_class('#MicroModel')
    RDFMicroModel: URIRef = ontology.get_class('#RDFMicroModel')
    BinaryMicroModel: URIRef = ontology.get_class('#BinaryMicroModel')
    SysMLMicroModel: URIRef = ontology.get_class('#SysMLMicroModel')

    Transformation: URIRef = ontology.get_class('#Transformation')
    PythonScriptTransformation: URIRef = ontology.get_class('#PythonScriptTransformation')

    isInputModelOf: URIRef = ontology.get_object_property('#isInputModelOf')
    hasOutputModel: URIRef = ontology.get_object_property('#hasOutputModel')
    hasLooseCoupling: URIRef = ontology.get_object_property('#hasLooseCoupling')
    extendsModel: URIRef = ontology.get_object_property('#extendsModel')
