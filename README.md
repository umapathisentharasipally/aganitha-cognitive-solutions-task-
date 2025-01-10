 12W222APubMed Paper Fetcher
A Python program to fetch research papers from PubMed based on a user-specified query, filter papers authored by individuals affiliated with pharmaceutical or biotech companies, and save the results to a CSV file.
Features
* Fetches research papers from the PubMed API.
* Filters for papers with at least one author affiliated with non-academic institutions.
* Outputs results as a CSV file with fields like PubmedID, Title, Publication Date, etc.
* Command-line options for query input, debug mode, and file naming.
Requirements
* Python 3.8 or higher
* Poetry for dependency management
Installation
1. Clone the repository:
* git clone https://github.com/yourusername/pubmed-paper-fetcher.git cd     pubmed-paper-fetcher
* install dependencies using Poetry: poetry install
* Activate the virtual environment: poetry shell
Usage
Run the command-line interface (CLI) to fetch papers:

poetry run get-papers-list "cancer research" -f results.csv -d

Command-Line Options

Option


Description

query
(Required) Query to search for papers.
-f, --file
(Optional) Name of the output CSV file. Default: output.csv.
-d, --debug
(Optional) Enable debug mode to print logs.
-h, --help





Display usage instructions.




Example
Fetch papers related to "cancer research" and save them to results.csv:
poetry run get-papers-list "cancer research" -f results.csv -d
The output will include a CSV file with the following columns:
* PubmedID: Unique identifier for the paper.
* Title: Title of the paper.
* Publication Date: Date the paper was published.
* Non-academic Author(s): Names of authors affiliated with non-academic institutions.
* Company Affiliation(s): Names of pharmaceutical/biotech companies.
* Corresponding Author Email: Email address of the corresponding author.

Project Structure:

pubmed_paper_fetcher/
??? pubmed_paper_fetcher/                   # Package directory
?   ??? __init__.py                                       # Package initialization
?   ??? pubmed_paper_fetcher.py          # Core logic for fetching and filtering papers
?   ??? cli.py                                                # Command-line interface logic
??? pyproject.toml                                    # Poetry configuration
??? README.md                                        # Project documentation

Development
Running Tests
To add tests, place them in the tests/ directory. Run tests with: pytest
Type Checking
Use mypy for static type checking:
mypy pubmed_paper_fetcher




How It Works
1. Fetching Papers: The program uses PubMed's esearch and esummary APIs to search for papers based on the user query and retrieve paper details.
2. Filtering Authors: The program identifies authors affiliated with pharmaceutical or biotech companies by analyzing the authors' affiliations using regular expressions.
3. Output to CSV: Results are saved as a CSV file with the specified fields.
Notes on PubMed API
* The PubMed API provides JSON responses for paper data, such as PubmedID, Title, Authors, etc.
* Ensure to adhere to PubMed's API usage limits.
Tools and Libraries Used
* Requests: For making HTTP requests to the PubMed API.
* Poetry: For dependency management and packaging.
* CSV: For writing the output file.
Known Limitations
* Non-academic Heuristics: The detection of non-academic affiliations relies on regex heuristics, which may not catch all cases.
* Pagination: Currently, the program fetches only the first 100 papers (adjustable in the code).
Publishing the Package
 To publish the package to TestPyPI:
1. Build the package:  poetry build
2. Publish to TestPyPI: poetry publish -r testpypi
License: 
This project is licensed under the MIT License. See the LICENSE file for details.


