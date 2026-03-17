"""
models.py - Data models for Project 25: Personal Finance Tracker With Forecasts
================================================================================

Defines:
    - Tracker configuration (file paths, starting balance, forecast horizon)
    - Transaction records (date, description, amount, category)
    - Monthly summary records (income, expenses, net, running balance)
    - Forecast point records (predicted future balance per month)
    - Final run summary record for reporting and persistence
"""

from datetime import datetime
from typing import Dict, Any, Optional, List


def _utc_timestamp() -> str:
    """Return an ISO-8601 UTC timestamp string.

    Returns:
        str: UTC timestamp with trailing Z.
    """
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"


def create_tracker_config(
    transaction_file: str = "data/transactions.csv",
    category_map_file: str = "data/categories.json",
    starting_balance: float = 0.0,
    months_to_forecast: int = 3,
    forecast_method: str = "linear_regression",
) -> Dict[str, Any]:
    """Create a default tracker configuration record.

    Parameters:
        transaction_file (str): Path to the CSV file containing raw transactions.
        category_map_file (str): Path to the JSON file mapping keywords to categories.
        starting_balance (float): Opening account balance before the first transaction.
        months_to_forecast (int): Number of future months to project.
        forecast_method (str): Forecasting algorithm identifier ('linear_regression').

    Returns:
        dict: Configuration dictionary used throughout the tracker pipeline.

    TODO: Implement configuration creation with default values and basic validation.
    """
    pass


def create_transaction(
    date: str,
    description: str,
    amount: float,
    category: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a normalized transaction record.

    Parameters:
        date (str): ISO-8601 date string (YYYY-MM-DD) of the transaction.
        description (str): Raw description string from the bank export.
        amount (float): Transaction amount; positive=income, negative=expense.
        category (str | None): Category label assigned by categorization step.

    Returns:
        dict: Normalized transaction record including a year_month derived field
              and a created_at timestamp.

    TODO: Implement transaction record creation with year_month derived field.
    """
    pass


def create_monthly_summary(
    year_month: str,
    income: float,
    expenses: float,
    net: float,
    running_balance: float,
    by_category: Dict[str, float],
) -> Dict[str, Any]:
    """Create a monthly aggregation summary record.

    Parameters:
        year_month (str): Month identifier in 'YYYY-MM' format.
        income (float): Total positive amounts for the month.
        expenses (float): Total absolute negative amounts for the month.
        net (float): income minus expenses for the month.
        running_balance (float): Cumulative balance at end of this month.
        by_category (dict): Mapping of category label to total spent amount.

    Returns:
        dict: Monthly summary record ready for display and persistence.

    TODO: Implement summary record creation.
    """
    pass


def create_forecast_point(
    year_month: str,
    predicted_balance: float,
    lower_bound: Optional[float] = None,
    upper_bound: Optional[float] = None,
) -> Dict[str, Any]:
    """Create one forecast data point for a future month.

    Parameters:
        year_month (str): Predicted month in 'YYYY-MM' format.
        predicted_balance (float): Model-projected account balance.
        lower_bound (float | None): Optional lower confidence interval.
        upper_bound (float | None): Optional upper confidence interval.

    Returns:
        dict: Forecast point record for display and chart rendering.

    TODO: Implement forecast point creation.
    """
    pass


def create_run_summary(
    config: Dict[str, Any],
    transaction_count: int,
    months_covered: int,
    avg_monthly_income: float,
    avg_monthly_expenses: float,
    avg_monthly_net: float,
    forecast_points: List[Dict[str, Any]],
    artifacts: Dict[str, str],
) -> Dict[str, Any]:
    """Create the final run summary record.

    Parameters:
        config (dict): Tracker configuration snapshot.
        transaction_count (int): Total transactions imported and processed.
        months_covered (int): Number of distinct calendar months in the data.
        avg_monthly_income (float): Mean monthly income over covered months.
        avg_monthly_expenses (float): Mean monthly expenses over covered months.
        avg_monthly_net (float): Mean monthly net over covered months.
        forecast_points (list[dict]): Forecast data points generated.
        artifacts (dict): Saved output paths (JSON summary, forecast chart, etc.).

    Returns:
        dict: Complete run summary for display and persistence.

    TODO: Implement summary creation with timestamp.
    """
    pass
