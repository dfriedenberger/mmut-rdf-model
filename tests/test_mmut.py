from py_mmut_rdf import MMUT
from rdflib import URIRef, Graph, RDF


def test_namespace_exists():
    """Test that the MMUT namespace is properly defined."""
    assert MMUT._NS is not None
    assert str(MMUT._NS).startswith("http://")


def test_classes_exist():
    """Test that all expected classes are defined."""
    assert isinstance(MMUT.RDFMicroModel, URIRef)
    assert isinstance(MMUT.PythonScriptTransformation, URIRef)


def test_object_properties_exist():
    """Test that all expected object properties are defined."""
    assert isinstance(MMUT.isInputModelOf, URIRef)
    assert isinstance(MMUT.hasOutputModel, URIRef)


def test_workflow():
    g = Graph()
    g.bind("mmut", MMUT._NS)
    g.add((URIRef("http://example.org#model_x"), RDF.type, MMUT.RDFMicroModel))

    assert (URIRef("http://example.org#model_x"), RDF.type, MMUT.RDFMicroModel) in g
