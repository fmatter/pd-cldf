from cldfbench import CLDFSpec

# from pycldf.sources import Source
# import pybtex
from cldfbench.cldf import CLDFWriter

spec = CLDFSpec(dir="tests/data/cldf", module="Generic", metadata_fname="metadata.json")
with CLDFWriter(spec) as writer:
    writer.cldf.add_component("FormTable")
    writer.objects["FormTable"].append(
        {"ID": "1", "Form": "yëye", "Parameter_ID": "tree", "Language_ID": "yab"}
    )
    ds = writer.cldf
ds.validate()
