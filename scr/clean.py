import pandas as pd


def load_practice(path):
    df = pd.read_csv(path)
    assert df["ACH_DATE"].nunique() == 1, "Expected a single data date in the practice file"
    wide = df.pivot(
        index=["ODS_CODE", "NAME"],
        columns="BREAKDOWN",
        values="VALUE",
    ).reset_index()
    wide.columns.name = None
    wide.columns = wide.columns.str.lower()
    wide["ach_date"] = pd.to_datetime(df["ACH_DATE"].iloc[0], format="%d-%b-%y")
    return wide


def load_mapping(path):
    cols = ["PRACTICE_CODE", "SUB_ICB_LOCATION_CODE", "SUB_ICB_LOCATION_NAME",
            "ICB_CODE", "ICB_NAME", "COMM_REGION_CODE", "COMM_REGION_NAME"]
    df = pd.read_csv(path, usecols=cols)
    df = df.rename(columns={
        "PRACTICE_CODE": "ods_code",
        "SUB_ICB_LOCATION_CODE": "sub_icb_code",
        "SUB_ICB_LOCATION_NAME": "sub_icb_name",
        "ICB_CODE": "icb_code",
        "ICB_NAME": "icb_name",
        "COMM_REGION_CODE": "comm_region_code",
        "COMM_REGION_NAME": "comm_region_name",
    })
    return df


def load_rates(path):
    df = pd.read_csv(path)
    df = df[df["ORG_TYPE"] == "SUB_ICB_LOC"]
    df = df.pivot(
        index=["ORG_CODE", "NAME"],
        columns="MEASURE",
        values="VALUE",
    ).reset_index()
    assert len(df) == 106, f"Expected 106 Sub-ICBs for this release, got {len(df)}"
    df.columns.name = None
    df = df.rename(columns={
        "ORG_CODE": "sub_icb_code",
        "NAME": "sub_icb_name",
        "DEMENTIA_ESTIMATE_65_PLUS": "dementia_estimate",
        "DEMENTIA_REGISTER_65_PLUS": "dementia_register",
        "DIAG_RATE_65_PLUS": "diag_rate",
        "DIAG_RATE_65_PLUS_LL": "diag_rate_ll",
        "DIAG_RATE_65_PLUS_UL": "diag_rate_ul",
    })
    return df


def main():
    practice = load_practice("data/raw/practice_sep_2026.csv")
    mapping = load_mapping("data/raw/mapping_oct_2026.csv")
    rates = load_rates("data/raw/rate_sep_2026.csv")

    merged = practice.merge(mapping, how="left", on="ods_code", validate="many_to_one")
    assert merged["sub_icb_code"].notna().all(), "Some practices have no Sub-ICB after the merge"

    merged.to_csv("data/clean/practice_clean.csv", index=False)
    rates.to_csv("data/clean/sub_icb_rates.csv", index=False)
    print(f"practice_clean: {merged.shape}, sub_icb_rates: {rates.shape}")


if __name__ == "__main__":
    main()