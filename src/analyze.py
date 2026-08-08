from pathlib import Path

import pandas as pd

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "sample_health_metrics.csv"


def load_data():
    return pd.read_csv(DATA_FILE)


def build_summary():
    df = load_data()
    summary = {
        "rows": len(df),
        "avg_response_time": round(df["response_time"].mean(), 2),
        "avg_engagement": round(df["engagement_score"].mean(), 2),
        "avg_readmission_risk": round(df["readmission_risk"].mean(), 2),
        "regions": df["region"].nunique(),
    }
    return summary


def main():
    summary = build_summary()
    print("May Data Science Lab Summary")
    print("=" * 32)
    print(f"Rows: {summary['rows']}")
    print(f"Average response time: {summary['avg_response_time']} minutes")
    print(f"Average engagement score: {summary['avg_engagement']}")
    print(f"Average readmission risk: {summary['avg_readmission_risk']}")
    print(f"Regions covered: {summary['regions']}")


if __name__ == "__main__":
    main()
