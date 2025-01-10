import argparse  # For parsing command-line arguments
import csv  # For reading and writing CSV files
from pubmed_paper_fetcher import PubMedPaperFetcher  # Custom module to fetch papers from PubMed
from typing import List, Dict  # For type annotations

def save_to_csv(filename: str, data: List[Dict]):
    """
    Saves the extracted data to a CSV file.

    Parameters:
    - filename (str): Name of the output CSV file.
    - data (List[Dict]): List of dictionaries, each containing paper details.
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        # Define column headers for the CSV file
        writer = csv.DictWriter(file, fieldnames=[
            "PubmedID", "Title", "Publication Date", 
            "Non-academic Author(s)", "Company Affiliation(s)", 
            "Corresponding Author Email"
        ])
        writer.writeheader()  # Write headers to the CSV file
        writer.writerows(data)  # Write rows of paper details

def main():
    """
    Main function to parse arguments, fetch PubMed papers, process data,
    and save results to a CSV file.
    """
    # Set up the argument parser for command-line inputs
    parser = argparse.ArgumentParser(description="Fetch PubMed research papers.")
    parser.add_argument("query", help="Query to search for papers")  # Positional query argument
    parser.add_argument("-f", "--file", help="Output CSV file name", default="output.csv")  # Optional output file
    parser.add_argument("-d", "--debug", help="Enable debug mode", action="store_true")  # Debug flag

    # Parse the provided arguments
    args = parser.parse_args()

    # Initialize the PubMedPaperFetcher
    fetcher = PubMedPaperFetcher()
    query = args.query  # Get the search query
    output_file = args.file  # Get the output file name
    debug = args.debug  # Check if debug mode is enabled

    if debug:
        print(f"Fetching papers for query: {query}")  # Debug: Print the query

    # Fetch PubMed IDs for the query
    paper_ids = fetcher.fetch_papers(query)
    if debug:
        print(f"Found {len(paper_ids)} papers")  # Debug: Print the number of papers found

    # Fetch detailed information for the papers
    papers = fetcher.fetch_paper_details(paper_ids)
    results = []  # Initialize a list to hold processed results

    for paper in papers:
        # Extract authors and filter non-academic authors
        authors = paper.get("authors", [])
        non_academic_authors = fetcher.filter_non_academic_authors(authors)

        # Extract non-academic author names and affiliations
        non_academic_authors_names = "; ".join([a["name"] for a in non_academic_authors]) if non_academic_authors else "N/A"
        non_academic_authors_affiliations = "; ".join([a["affiliation"] for a in non_academic_authors]) if non_academic_authors else "N/A"

        # Append extracted details to results
        results.append({
            "PubmedID": paper.get("uid", "N/A"),  # PubMed ID
            "Title": paper.get("title", "N/A"),  # Title of the paper
            "Publication Date": paper.get("pubdate", "N/A"),  # Publication date
            "Non-academic Author(s)": non_academic_authors_names,  # Non-academic authors
            "Company Affiliation(s)": non_academic_authors_affiliations,  # Company affiliations
            "Corresponding Author Email": paper.get("corresponding_author_email", "N/A")  # Corresponding author email
        })

    # Save the results into a CSV file
    save_to_csv(output_file, results)

    if debug:
        print(f"Results saved to {output_file}")  # Debug: Print success message

# Entry point: Runs the main function when the script is executed
if __name__ == "__main__":
    main()
