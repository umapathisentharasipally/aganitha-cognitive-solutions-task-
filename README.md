# PubMed Paper Fetcher

## Overview

This Python program fetches research papers from PubMed based on a user-specified query. It identifies papers with at least one author affiliated with a pharmaceutical or biotech company and returns the results as a CSV file.

---

## Features

- Fetch papers using the PubMed API with support for PubMed's full query syntax.
- Identify non-academic authors affiliated with pharmaceutical/biotech companies.
- Outputs results in a CSV file with the following columns:
  - **PubmedID**: Unique identifier for the paper.
  - **Title**: Title of the paper.
  - **Publication Date**: Date of publication.
  - **Non-academic Author(s)**: Names of authors affiliated with non-academic institutions.
  - **Company Affiliation(s)**: Names of pharmaceutical/biotech companies.
  - **Corresponding Author Email**: Email of the corresponding author.

---

## Dependencies

This project uses Python 3.8 or later. The following dependencies are required:
- `requests`: For making API calls to PubMed.
- `argparse`: For parsing command-line arguments.
- `csv`: For generating CSV output.

Dependencies are managed using [Poetry](https://python-poetry.org/).

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pubmed-paper-fetcher.git
   cd pubmed-paper-fetcher
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

---

## Usage

### Command-Line Interface

Run the program using the `get-papers-list` command provided by Poetry:
```bash
poetry run get-papers-list "your query" -f output.csv -d
```

#### Options:
- **`query`** (required): The search query for PubMed papers.
- **`-f` / `--file`**: Specify the output CSV file name (default: `output.csv`).
- **`-d` / `--debug`**: Enable debug mode for additional logging.

---

## Example

Fetch papers with the query `"COVID-19 vaccine"` and save them to `covid_papers.csv`:
```bash
poetry run get-papers-list "COVID-19 vaccine" -f covid_papers.csv
```

Enable debug mode:
```bash
poetry run get-papers-list "machine learning in healthcare" -d
```

---

## Development

### Code Structure
1. **`pubmed_paper_fetcher`**: Contains the core logic for fetching and filtering papers.
2. **`cli.py`**: The command-line interface script.

---

## Notes

- This program uses heuristics (e.g., affiliation keywords like "pharma", "biotech") to identify non-academic authors.
- API errors and invalid queries are handled gracefully.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- PubMed API: [https://pubmed.ncbi.nlm.nih.gov/](https://pubmed.ncbi.nlm.nih.gov/)
- Poetry: [https://python-poetry.org/](https://python-poetry.org/)

