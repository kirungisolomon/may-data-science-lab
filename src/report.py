from pathlib import Path

REPORT_PATH = Path(__file__).resolve().parents[1] / "outputs" / "summary.md"


def write_report(summary):
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(
        "# May Data Science Lab Report\n\n"
        f"- Average response time: {summary['avg_response_time']}\n"
        f"- Average engagement score: {summary['avg_engagement']}\n"
        f"- Average readmission risk: {summary['avg_readmission_risk']}\n"
        f"- Regions: {summary['regions']}\n",
        encoding="utf-8",
    )

    print(f"Report written to {REPORT_PATH}")
