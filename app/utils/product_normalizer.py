from rapidfuzz import fuzz

SIMILARITY_THRESHOLD = 85

def normalize_products(items):
    """
    Step 9: Normalize similar product names (e.g., 'HT BREAKER' vs 'HT Circuit Breaker').
    Fuzzy merge items with high similarity into the same name to prevent duplicates.
    """
    normalized = []

    for item in items:
        found = False
        item_desc = item["description"]
        item_brand = item["brand"]

        for existing in normalized:
            # Check similarity between descriptions
            score = fuzz.ratio(
                str(item_desc).lower(),
                str(existing["description"]).lower()
            )

            # If descriptions are very similar and brands match, merge quantities
            if score >= SIMILARITY_THRESHOLD and item_brand == existing["brand"]:
                # Keep the descriptive (longer) name
                if len(str(item_desc)) > len(str(existing["description"])):
                    existing["description"] = item_desc
                
                existing["quantity"] += item["quantity"]
                found = True
                break

        if not found:
            normalized.append(item.copy())

    return normalized
