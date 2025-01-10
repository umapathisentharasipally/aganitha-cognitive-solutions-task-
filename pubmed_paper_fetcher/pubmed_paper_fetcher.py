import re  # For matching patterns in author affiliations
import requests  # To send HTTP requests to the PubMed API
from typing import List, Dict  # For type hinting

class PubMedPaperFetcher:
    """
    A class to fetch research papers and filter non-academic authors.
    """

    def __init__(self):
        # Base URLs for PubMed search and summary endpoints
        self.base_search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        self.base_summary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

    def fetch_papers(self, query: str) -> List[str]:
        """
        Fetch a list of PubMed IDs (PMIDs) based on a search query.
        """
        params = {
            "db": "pubmed",  # Specify the PubMed database
            "term": query,  # The search query term
            "retmode": "json",  # Return results in JSON format
            "retmax": 200  # Limit to 100 results
        }
        response = requests.get(self.base_search_url, params=params)  # Send GET request
        response.raise_for_status()  # Raise an error if the request fails
        return response.json().get("esearchresult", {}).get("idlist", [])  # Extract IDs

    def fetch_paper_details(self, paper_ids: List[str]) -> List[Dict]:
        """
        Fetch detailed information for a list of PubMed IDs.
        """
        params = {
            "db": "pubmed",  # Fetch from the PubMed database
            "id": ",".join(paper_ids),  # List of IDs separated by commas
            "retmode": "json"  # Return details in JSON format
        }
        response = requests.get(self.base_summary_url, params=params)  # Send GET request
        response.raise_for_status()  # Raise an error if the request fails
        details = response.json().get("result", {})  # Parse the result section
        return [details[pid] for pid in paper_ids if pid in details]  # Return details for valid IDs

    def filter_non_academic_authors(self, authors: List[Dict]) -> List[Dict]:
        """
        Identify authors with non-academic affiliations using keyword matching.
        """
        non_academic_authors = []
        for author in authors:
            # Get the affiliation field of the author
            affiliation = author.get("affiliation", "")
            # Check if the affiliation matches non-academic keywords
            if re.search(r"pharma|biotech|inc|corp|company", affiliation, re.IGNORECASE):
                non_academic_authors.append({
                    "name": author.get("name", "Unknown"),  # Author's name
                    "affiliation": affiliation  # Author's affiliation
                })
        return non_academic_authors  # Return the filtered list
