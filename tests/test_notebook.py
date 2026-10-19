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


def test_logic_is_causal_and_normalised():
    """Runs the notebook, then checks in the same kernel that:
    - the rolling Z for the first k bars is identical when later bars are dropped (no lookahead),
    - the latest Z equals the textbook rolling formula,
    - normalised delta volume is within [-100, 100] %, and high == low days contribute 0."""
    nb = nbformat.read(NB, as_version=4)
    nb.cells.append(nbformat.v4.new_code_cell("""
import numpy as np
c = data['Close', 'GOOG']
k = len(c) - 10
early = rolling_z(c.iloc[:k], z_len)
pd.testing.assert_series_equal(early, rolling_z(c, z_len).iloc[:k])
w = c.iloc[-z_len:]
assert abs(last_zscores['GOOG'] - (w.iloc[-1] - w.mean()) / w.std()) < 1e-9
for t, v in delta_pct.items():
    assert v.dropna().between(-100, 100).all(), t
idx = pd.date_range('2024-01-01', periods=3)
s = lambda x: pd.Series(x, index=idx, dtype=float)
cd, cv = delta_vol(s([100, 100, 100]), s([10, 12, 10]), s([10, 12, 11]), s([10, 10, 9]))
assert list(cd) == [0.0, 100.0, 100.0]          # flat bar -> 0, close at high -> +vol, mid -> 0
"""))
    NotebookClient(nb, timeout=300, kernel_name="python3", allow_errors=False).execute()
