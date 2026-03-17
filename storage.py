"""
storage.py - Persistence layer for Project 25: Personal Finance Tracker With Forecasts
=======================================================================================

Handles:
    - Local data directory setup
    - CSV transaction file import
    - JSON transaction and summary persistence
    - Plotly forecast chart export
"""

from pathlib import Path
import json

DATA_DIR = Path(__file__).resolve().parent / "data"
OUTPUTS_DIR = DATA_DIR / "outputs"


def ensure_data_dirs() -> None:
    """Create local data and outputs directories if missing.

    Returns:
        None
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)


def load_csv(filepath: str) -> list:
    """Load raw transaction rows from a CSV file.

    Parameters:
        filepath (str): Path to the CSV file to import.

    Returns:
        list[dict]: Raw rows as dictionaries keyed by column header.

    Raises:
        FileNotFoundError: If the CSV file does not exist at the given path.

    TODO: Implement CSV loading using csv.DictReader with encoding handling.
    """
    pass


def load_category_map(filename: str) -> dict:
    """Load keyword-to-category mapping from a JSON file in the data directory.

    Parameters:
        filename (str): JSON filename inside DATA_DIR.

    Returns:
        dict: Mapping of lowercase keyword strings to category label strings.
              Returns an empty dict if the file is missing.

    TODO: Implement JSON load with a safe fallback for missing files.
    """
    pass


def save_transactions(filename: str, transactions: list) -> None:
    """Persist processed transaction records to JSON in the data directory.

    Parameters:
        filename (str): Output JSON filename.
        transactions (list): List of transaction record dicts.

    Returns:
        None

    TODO: Implement JSON serialization with indentation.
    """
    pass


def load_transactions(filename: str) -> list:
    """Load previously saved transaction records from the data directory.

    Parameters:
        filename (str): JSON filename to load.

    Returns:
        list: Previously saved transaction records, or empty list if missing.

    TODO: Implement JSON load with fallback for missing files.
    """
    pass


def save_run_summary(filename: str, summary: dict) -> None:
    """Save final run summary as JSON in the outputs directory.

    Parameters:
        filename (str): Output summary filename.
        summary (dict): Summary record.

    Returns:
        None

    TODO: Implement JSON save to OUTPUTS_DIR with indentation.
    """
    pass


def save_forecast_chart(filename: str, fig) -> None:
    """Export a Plotly figure as an interactive HTML file in the outputs directory.

    Parameters:
        filename (str): Output HTML filename.
        fig: Plotly Figure object to export.

    Returns:
        None

    TODO: Implement fig.write_html() save to OUTPUTS_DIR.
    """
    pass


def load_json(filename: str):
    """Load JSON data from the data directory.

    Parameters:
        filename (str): JSON filename in data directory.

    Returns:
        object: Parsed JSON, or empty list if file missing.
    """
    ensure_data_dirs()
    path = DATA_DIR / filename
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))
