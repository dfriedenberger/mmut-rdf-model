# py-mmut-rdf

A Python library providing RDF ontology definitions for MMUT (MicroModel and Transformations). This library contains a generated TTL (Turtle) file with MMUT ontology definitions and provides a convenient Python interface to access the ontology classes and properties.

## Ontology Visualization

Visualized the ontology with [WebVOWL](https://service.tib.eu/webvowl/)

![SysML Ontology](./mmut-0.0.1.ttl.svg)


## Installation
See: https://pypi.org/project/py_mmut_rdf/
```bash
pip install py-mmut-rdf
```

## Usage

```python
from py_mmut_rdf import MMUT
from rdflib import URIRef, Graph, RDF

g = Graph()
g.bind("mmut", MMUT._NS)
g.add((URIRef("http://example.org#model_x"), RDF.type, MMUT.RDFMicroModel))
```

## Development


### Regenerating the Ontology

If you need to recreate the TTL file:

```bash
python create_mmut_ontology.py
```


### Testing

Run the test script to verify everything works:

```bash
python -m pytest tests/
```
### Building the Package

```bash
poetry build
```

### Publish the Package
```bash
poetry publish --username __token__ --password <TOKEN>
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)