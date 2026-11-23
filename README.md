# How does dementia diagnosis vary across England's NHS regions and Sub-ICBs?


A reproducible pipeline that cleans, joins and validates NHS primary care dementia data, reconciles it against published figures, and analyses regional gaps in diagnosis for people aged 65+.

## Data

All data is from NHS England's Primary Care Dementia Data publication ([September 2026 release](https://digital.nhs.uk/data-and-information/publications/statistical/primary-care-dementia-data/september-2026)), accessed 22 Nov 2026.

| File | What it contains | Data date |
|---|---|---|
| `practice_sep_2026.csv` | Dementia register, list size and care plan counts per GP practice | 30 Sep 2026 |
| `rate_sep_2026.csv` | Published estimates and diagnosis rates by Sub-ICB, ICB, region and England | 30 Sep 2026 |
| `mapping_oct_2026.csv` | Practice to Sub-ICB to ICB to region mapping | 1 Oct 2026 |

Licence: Contains information from NHS England, licensed under the current version of the [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

## How to run it

Run everything from the repo root.

```
pip install -r requirements.txt
python src/clean.py
```

## Repo structure

```
├── data/
│   ├── raw/          # untouched downloads
│   └── clean/        # output of clean.py
├── src/
│   └── clean.py      # raw -> clean tables
├── docs/
│   └── data_dictionary.md
├── requirements.txt
└── README.md
```

## Next steps

TBC


## AI use

I used Claude to help plan and debug this project. I wrote, ran, and debugged the code,

## Author

Keon Phillips