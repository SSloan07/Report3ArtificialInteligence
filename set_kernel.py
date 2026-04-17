import json
import sys
from pathlib import Path


def set_notebook_kernel(notebook_path: str, kernel_name: str, display_name: str) -> None:
    path = Path(notebook_path)

    if not path.exists():
        raise FileNotFoundError(f"No existe el archivo: {path}")

    if path.suffix != ".ipynb":
        raise ValueError(f"El archivo no es un notebook .ipynb: {path}")

    with path.open("r", encoding="utf-8") as f:
        notebook = json.load(f)

    notebook.setdefault("metadata", {})
    notebook["metadata"]["kernelspec"] = {
        "name": kernel_name,
        "display_name": display_name,
        "language": "python",
    }

    notebook.setdefault("metadata", {})
    notebook["metadata"]["language_info"] = {
        "name": "python"
    }

    with path.open("w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)

    print(f"Kernel actualizado correctamente en '{path}'")
    print(f"name         : {kernel_name}")
    print(f"display_name : {display_name}")


def main():
    if len(sys.argv) < 2:
        print("Uso:")
        print('  python set_kernel.py archivo.ipynb [kernel_name] [display_name]')
        print('Ejemplo:')
        print('  python set_kernel.py Report.ipynb report3env "Python (report3env)"')
        sys.exit(1)

    notebook_path = sys.argv[1]
    kernel_name = sys.argv[2] if len(sys.argv) >= 3 else "report3env"
    display_name = sys.argv[3] if len(sys.argv) >= 4 else f"Python ({kernel_name})"

    set_notebook_kernel(notebook_path, kernel_name, display_name)


if __name__ == "__main__":
    main()
