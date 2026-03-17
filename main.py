"""
main.py - Entry point for Project 25: Personal Finance Tracker With Forecasts
=============================================================================

Thin-controller module that only orchestrates calls to:
    - operations.py for finance tracker workflow logic
    - display.py for presentation formatting
    - storage.py for persistence setup
    - models.py for configuration records
"""

from display import format_header, format_startup_guide, format_run_report
from models import create_tracker_config
from operations import load_finance_profile, run_core_flow
from storage import ensure_data_dirs


def main() -> None:
    """Run one complete finance tracker session.

    Workflow:
        1. Ensure data directories exist
        2. Print header banner
        3. Build tracker config and startup profile
        4. Print startup guide
        5. Run finance tracker pipeline (operations.run_core_flow)
        6. Print final run report

    Returns:
        None

    TODO: Implement any additional orchestration needs for advanced CLI options.
    """
    # Prepare directories before any file operations.
    ensure_data_dirs()

    # Print session header.
    print(format_header())

    # Build tracker configuration.
    config = create_tracker_config()

    # Build startup profile for display.
    profile = load_finance_profile()

    # Print startup guide.
    print(format_startup_guide(config, profile))

    # Run finance tracker workflow.
    summary = run_core_flow()

    # Print final report.
    print(format_run_report(summary))


if __name__ == "__main__":
    # Guard keeps imports side-effect free for tests and reuse.
    main()
