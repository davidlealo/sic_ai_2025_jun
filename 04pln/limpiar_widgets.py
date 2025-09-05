import nbformat

ruta = "clase_24.ipynb"

with open(ruta, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

if "widgets" in nb["metadata"]:
    print("🔧 Eliminando metadata.widgets...")
    del nb["metadata"]["widgets"]
else:
    print("✅ El notebook no tiene metadata.widgets")

with open(ruta, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("✅ Notebook guardado limpio.")
