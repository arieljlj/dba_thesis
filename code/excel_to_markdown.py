from pathlib import Path
import pandas as pd
from tabulate import tabulate
import re

def safe_name(text: str) -> str:
    text = text.strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "_", text)
    return text or "sheet"

def excel_sheet_to_markdown(df: pd.DataFrame) -> str:
    return tabulate(df.fillna(""), headers="keys", tablefmt="github", showindex=False)

def excel_to_markdown_all_sheets(excel_path: Path, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    sheets = pd.read_excel(excel_path, sheet_name=None, engine="openpyxl")

    for sheet_name, df in sheets.items():
        markdown = excel_sheet_to_markdown(df)
        file_name = f"{excel_path.stem}_{safe_name(sheet_name)}.md"
        markdown_path = output_dir / file_name
        markdown_path.write_text(markdown, encoding="utf-8")
        print(f"Generado: {markdown_path}")

if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parents[1]
    excel_file = (
        repo_root
        / "docs"
        / "04_cap3_metodologia_resultados"
        / "Matriz_Operacionalizacion_Variables_DBA-1.xlsx"
    )
    output_folder = (
        repo_root
        / "docs"
        / "04_cap3_metodologia_resultados"
        / "markdown_from_excel"
    )

    excel_to_markdown_all_sheets(excel_file, output_folder)