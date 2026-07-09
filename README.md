# E2E-ML-NetworkSecurity

E2E Machine Learning project for Network Security — ingestion, preprocessing, and pipeline components to train and evaluate models on network/phishing dataset.

## Quick start

- Create and activate a Python environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirement.txt
```

- Create a `.env` file in the project root with the MongoDB connection string:

```
MONGO_DB_URL="your_mongodb_uri_here"
```

## Run

- To run the main pipeline (data ingestion -> split -> artifacts):

```powershell
python main.py
```

- To run the helper that reads the CSV and pushes to MongoDB:

```powershell
python push_data.py
```

## Project layout

- `main.py` — entrypoint which initializes configs and starts data ingestion.
- `push_data.py` — utility to convert CSV to JSON and insert into MongoDB.
- `networkSecurity/` — package containing components, entity definitions, logging, exceptions and pipeline code.
- `Network_data/` — sample data CSV (`phisingData.csv`).

## Troubleshooting

- If you see `ModuleNotFoundError: No module named 'networksecurity'`, some imports use the wrong case. The package folder is named `networkSecurity` (capital S). Use the correct imports like:

```py
from networkSecurity.logging.logger import logging
from networkSecurity.exception.exception import NetworkSecurityException
```

- If you get `SyntaxWarning: invalid escape sequence` for Windows paths, either use raw strings or forward slashes:

```py
FILE_PATH = r"Network_Data\phisingData.csv"
# or
FILE_PATH = "Network_Data/phisingData.csv"
```

- Ensure `MONGO_DB_URL` is set in `.env` and reachable by your machine.

## Notes

- Tests / quick checks: `test_mongo_db.py` contains a connection URI example; replace with your credentials for quick connectivity tests.
- If you'd like, I can add a short script to create the required database/collection and seed sample data automatically.

## License

MIT
