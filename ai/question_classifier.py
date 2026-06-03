# # ai/question_classifier.py

# def classify_question(question):

#     question = question.lower().strip()

#     dataset_keywords = [
#         "dataset",
#         "data",
#         "describe",
#         "summary",
#         "summarize",
#         "explain",
#         "columns",
#         "features",
#         "schema",
#         "about this dataset",
#         "about this data",
#         "what can i analyze",
#         "what is this dataset",
#         "what is this data",
#         "tell me about",
#         "overview"
#     ]

#     for keyword in dataset_keywords:

#         if keyword in question:
#             return "dataset"

#     return "analysis"


# ai/question_classifier.py
def classify_question(question):

    q = question.lower()

    analysis_keywords = {
        "show", "top", "highest", "lowest", "average", "avg",
        "sum", "count", "group", "sales", "quantity", "price",
        "products", "records", "country", "chart", "trend",
        "top 10", "top 5", "compare", "distribution"
    }

    dataset_keywords = {
        "what is this dataset",
        "describe dataset",
        "columns",
        "schema",
        "summary",
        "about this data",
        "what does this data contain"
    }

    # Dataset check first (more specific)
    if any(k in q for k in dataset_keywords):
        return "dataset"

    # Analysis check
    if any(k in q for k in analysis_keywords):
        return "analysis"

    # Default fallback (IMPORTANT)
    return "analysis"