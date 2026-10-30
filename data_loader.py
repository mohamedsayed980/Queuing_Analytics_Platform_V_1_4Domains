"""Find and load domain CSV files from the repository's data/ folder."""
from __future__ import annotations

import io
import re
from pathlib import Path

import pandas as pd
import streamlit as st

DATA_DIR = Path(__file__).resolve().parent / "data"


def _norm(value: str) -> str:
    """Normalize a filename/key so spaces, underscores, and hyphens are ignored."""
    return re.sub(r"[\s_-]+", "", value.casefold())


def find_files(key: str) -> list[Path]:
    """Return CSVs in data/ whose filename contains the normalized key."""
    if not DATA_DIR.is_dir():
        return []
    needle = _norm(key)
    return sorted(
        (p for p in DATA_DIR.iterdir()
         if p.is_file() and p.suffix.casefold() == ".csv" and needle in _norm(p.name)),
        key=lambda p: p.name.casefold(),
    )


def _pick_files(key: str) -> list[Path]:
    files = find_files(key)
    full_files = [p for p in files if "part" not in p.stem.casefold()]
    if full_files:
        return [min(full_files, key=lambda p: len(p.name))]
    return [p for p in files if "part" in p.stem.casefold()]


@st.cache_data(show_spinner=False)
def _read_files(paths: tuple[str, ...], _mtimes: tuple[float, ...]) -> pd.DataFrame:
    frames = []
    for path in paths:
        try:
            frame = pd.read_csv(path, encoding="utf-8-sig")
        except UnicodeDecodeError:
            frame = pd.read_csv(path, encoding="latin-1")
        frames.append(frame)
    result = pd.concat(frames, ignore_index=True) if len(frames) > 1 else frames[0]
    result.columns = result.columns.astype(str).str.strip()
    return result


def load_domain_data(key: str, uploaded=None) -> pd.DataFrame | None:
    """Load an uploaded CSV or a matching CSV from data/. Return None if absent."""
    if uploaded is not None:
        contents = uploaded.getvalue() if hasattr(uploaded, "getvalue") else uploaded
        result = pd.read_csv(io.BytesIO(contents), encoding="utf-8-sig")
        result.columns = result.columns.astype(str).str.strip()
        return result

    files = _pick_files(key)
    if not files:
        return None
    return _read_files(
        tuple(str(path) for path in files),
        tuple(path.stat().st_mtime for path in files),
    )


def explain_missing(key: str) -> None:
    """Display where the loader searched and ask for an upload if no CSV matched."""
    st.error(f"No usable CSV found for '{key}'.")
    st.code(f"Searched folder: {DATA_DIR}\nFolder exists: {DATA_DIR.is_dir()}")
    if DATA_DIR.is_dir():
        names = sorted(p.name for p in DATA_DIR.iterdir())
        st.code("Files found: " + (", ".join(names) if names else "(none)"))
    st.info("Upload the CSV in the sidebar, or place a matching CSV in the data/ folder.")
