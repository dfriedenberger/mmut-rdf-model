from rdflib import Graph, Namespace, RDF, RDFS, OWL, URIRef, DCTERMS, Literal, XSD


VERSION = "0.0.1"
KEY = "mmut"

# Definition des NameNSraums
NS = Namespace(f"http://frittenburger.de/ontology/{KEY}#")

# Erstellung des Graphen
g = Graph()
g.namespace_manager.bind(KEY, NS)

# Ontology
ontology = URIRef(f"https://gitlab.hpi.de/dfriedenberger/{KEY}")
g.add((ontology, RDF.type, OWL.Ontology))
g.add((ontology, DCTERMS.title, Literal("Micro Model and Transformation Ontology")))
g.add((ontology, DCTERMS.description, Literal("A rdf Ontology for model Micro Models and Transformation.", lang='en')))

g.add((ontology, OWL.versionInfo, Literal(VERSION)))
g.add((ontology, DCTERMS.creator, Literal("Dirk Friedenberger")))
g.add((ontology, DCTERMS.creator, URIRef("https://www.researchgate.net/profile/Dirk_Friedenberger")))
g.add((ontology, DCTERMS.identifier, Literal(NS)))

# concepts

# Model Taxonomy
g.add((NS.MicroModel, RDF.type, OWL.Class))
g.add((NS.MicroModel, RDFS.label, Literal("An abstract micro model.", lang='en')))

g.add((NS.RDFMicroModel, RDF.type, OWL.Class))
g.add((NS.RDFMicroModel, RDFS.label, Literal("An RDF micro model.", lang='en')))
g.add((NS.RDFMicroModel, RDFS.subClassOf, NS.MicroModel))

g.add((NS.BinaryMicroModel, RDF.type, OWL.Class))
g.add((NS.BinaryMicroModel, RDFS.label, Literal("An Binary micro model.", lang='en')))
g.add((NS.BinaryMicroModel, RDFS.subClassOf, NS.MicroModel))

g.add((NS.SysMLMicroModel, RDF.type, OWL.Class))
g.add((NS.SysMLMicroModel, RDFS.label, Literal("An SysML micro model.", lang='en')))
g.add((NS.SysMLMicroModel, RDFS.subClassOf, NS.MicroModel))

# Transformation Taxonomy
g.add((NS.Transformation, RDF.type, OWL.Class))
g.add((NS.Transformation, RDFS.label, Literal("An abstract transformation.", lang='en')))

g.add((NS.PythonScriptTransformation, RDF.type, OWL.Class))
g.add((NS.PythonScriptTransformation, RDFS.subClassOf, NS.Transformation))
g.add((NS.PythonScriptTransformation, RDFS.label, Literal("A Python-based transformation.", lang='en')))


# relations
g.add((NS.isInputModelOf, RDF.type, OWL.ObjectProperty))
g.add((NS.isInputModelOf, RDFS.domain, NS.MicroModel))
g.add((NS.isInputModelOf, RDFS.range, NS.Transformation))
g.add((NS.isInputModelOf, RDFS.label, Literal("model used for transformation", lang='en')))

g.add((NS.hasOutputModel, RDF.type, OWL.ObjectProperty))
g.add((NS.hasOutputModel, RDFS.domain, NS.Transformation))
g.add((NS.hasOutputModel, RDFS.range, NS.MicroModel))
g.add((NS.hasOutputModel, RDFS.label, Literal("transforms to model", lang='en')))

g.add((NS.hasLooseCoupling, RDF.type, OWL.ObjectProperty))
g.add((NS.hasLooseCoupling, RDFS.domain, NS.MicroModel))
g.add((NS.hasLooseCoupling, RDFS.range, NS.MicroModel))
g.add((NS.hasLooseCoupling, RDFS.label, Literal("couples loose to", lang='en')))

g.add((NS.extendsModel, RDF.type, OWL.ObjectProperty))
g.add((NS.extendsModel, RDFS.domain, NS.MicroModel))
g.add((NS.extendsModel, RDFS.range, NS.MicroModel))
g.add((NS.extendsModel, RDFS.label, Literal("extends model", lang='en')))


# Serialisierung der Ontologie in RDF/XML-Syntax
g.serialize(destination=f"py_mmut_rdf/{KEY}.ttl", format='turtle')
