from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_AUTH_CREDENTIALS")

def search_sample(search_query: str):
    """
    Performs a Discovery Engine search for the given query,
    then prints only the title and snippet of each result.
    """
    project_id = "kisan-466906"
    location = "global"
    engine_id = "finalapp_1753526696930"

    # Configure endpoint if needed
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )
    client = discoveryengine.SearchServiceClient(client_options=client_options)

    # Build the serving config resource name
    serving_config = (
        f"projects/{project_id}/locations/{location}"
        f"/collections/default_collection/engines/{engine_id}"
        f"/servingConfigs/default_config"
    )

    # Optional: configure content search specs (snippets/summaries)
    content_search_spec = discoveryengine.SearchRequest.ContentSearchSpec(
        snippet_spec=discoveryengine.SearchRequest.ContentSearchSpec.SnippetSpec(
            return_snippet=True
        ),
        summary_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec(
            summary_result_count=5,
            include_citations=True,
            ignore_adversarial_query=True,
            ignore_non_summary_seeking_query=True,
            model_prompt_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec.ModelPromptSpec(
                preamble="Give all the schemes related to this query"
            ),
            model_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec.ModelSpec(
                version="stable",
            ),
        ),
    )

    # Construct the search request
    request = discoveryengine.SearchRequest(
        serving_config=serving_config,
        query=search_query,
        page_size=5,
        content_search_spec=content_search_spec,
        query_expansion_spec=discoveryengine.SearchRequest.QueryExpansionSpec(
            condition=discoveryengine.SearchRequest.QueryExpansionSpec.Condition.AUTO,
        ),
        spell_correction_spec=discoveryengine.SearchRequest.SpellCorrectionSpec(
            mode=discoveryengine.SearchRequest.SpellCorrectionSpec.Mode.AUTO
        ),
    )

    # Execute the search
    page_result = client.search(request)

    output_lines = []
    for hit in page_result.results:
        doc = hit.document
        sd = doc.struct_data or {}
        title       = sd.get("Title", "N/A")
        description = sd.get("Description", "N/A")
        link        = sd.get("Link", "N/A")
        tags        = sd.get("Tags", "N/A")
        ministry    = sd.get("Ministry/State", "N/A")

        output_lines.append(f" ID: {hit.id}")
        output_lines.append(f" Title: {title}")
        output_lines.append(f" Description: {description}")
        output_lines.append(f" Link: {link}")
        output_lines.append(f" Tags: {tags}")
        output_lines.append(f" Ministry/State: {ministry}")
        output_lines.append("—" * 60)

    # Join into one big string
    return "\n".join(output_lines)

    return result

if __name__ == "__main__":
    # Example usage
    print(search_sample("irrigation"))
