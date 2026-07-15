import json
from pathlib import Path


def load_report():
    """Load the generated report."""
    with open("/app/report.json", "r") as f:
        return json.load(f)


def test_report_exists():
    """Verify that the report file exists at /app/report.json."""
    assert Path("/app/report.json").exists()


def test_report_is_valid_json():
    """Verify that report.json contains valid JSON."""
    report = load_report()
    assert isinstance(report, dict)


def test_report_schema():
    """Verify the report has exactly the required fields."""
    report = load_report()

    assert set(report.keys()) == {
        "total_requests",
        "unique_ips",
        "top_path"
    }


def test_total_requests():
    """Verify the total number of requests."""
    report = load_report()

    assert report["total_requests"] == 6


def test_unique_ips():
    """Verify the number of unique client IP addresses."""
    report = load_report()

    assert report["unique_ips"] == 3


def test_top_path():
    """Verify the most frequently requested URL path."""
    report = load_report()

    assert report["top_path"] == "/index.html"