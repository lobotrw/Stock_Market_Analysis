"""Smoke test: execute Stock_Market_Project.ipynb top to bottom and fail on any cell error.
Needs network (Yahoo Finance) and: pip install yfinance pandas matplotlib nbclient nbformat ipykernel pytest"""
from pathlib import Path

import nbformat
from nbclient import NotebookClient

NB = Path(__file__).resolve().parents[1] / "Stock_Market_Project.ipynb"


def test_notebook_runs_without_errors():
    nb = nbformat.read(NB, as_version=4)
    NotebookClient(nb, timeout=300, kernel_name="python3", allow_errors=False).execute()
    errors = [o for c in nb.cells for o in c.get("outputs", []) if o.get("output_type") == "error"]
    assert not errors
