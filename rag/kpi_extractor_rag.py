from rag.extract_metric import extract_metric


def extract_kpis(
    company: str,
    year: int,
    user_id: int
) -> dict:
    
    questions = {
        "revenue":
            f"Return only the total revenue for {year}.",

        "net_income":
            f"Return only the net income for {year}.",

        "cash_flow":
            f"Return only the operating cash flow for {year}.",

        "debt":
            f"Return only the total debt for {year}.",

        "operating_margin":
            f"Return only the operating margin percentage for {year}. Do not calculate.",

        "r_and_d_expense":
            f"Return only the research and development expense for {year}."
    }
    
    results = {}
    
    for metric, question in questions.items():
        
        # print(f"Extracting {metric}...")
        
        answer = extract_metric(
            metric=metric,
            question=question,
            company=company,
            year=year,
            user_id=user_id
        )
        
        results[metric] = answer
        
    return results