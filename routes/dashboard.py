from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import cast

from auth.oauth2 import get_current_user
from database.user import User

from database.db import SessionLocal
from database.metrics import FinancialMetric
from rag.ai_insights import generate_insights

from utils.financial_parser import metric_response



router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/companies/list")
def get_user_companies(
    current_user: User = Depends(
        get_current_user
    )
):

    db: Session = SessionLocal()

    companies = (
        db.query(
            FinancialMetric.company,
            FinancialMetric.year
        )
        .filter(
            FinancialMetric.user_id == current_user.id
        )
        .order_by(
            FinancialMetric.company,
            FinancialMetric.year.desc()
        )
        .all()
    )

    db.close()

    return [
        {
            "company": row.company,
            "year": row.year
        }
        for row in companies
    ]
    

@router.get("/{company}/{year}")
def get_dashboard_data(
    company: str,
    year: int,
    current_user: User = Depends(get_current_user)
):
    
    db: Session = SessionLocal()
    
    metric = (
        db.query(FinancialMetric)
        .filter(
            FinancialMetric.company == company,
            FinancialMetric.year == year,
            FinancialMetric.user_id == current_user.id
        )
        .first()
    )
    
    db.close()
    
    if not metric:
        raise HTTPException(
            status_code=404,
            detail="Company data not found."
        )
        
    return {
        "company": metric.company,
        "year": metric.year,

        "revenue": metric_response(metric.revenue),
        "net_income": metric_response(metric.net_income),
        "cash_flow": metric_response(metric.cash_flow),
        "debt": metric_response(metric.debt),
        "operating_margin": metric_response(metric.operating_margin),
        "r_and_d_expense": metric_response(metric.r_and_d_expense),
    }
    

@router.get("/{company}/{year}/insights")
def get_ai_insights(
    company: str,
    year: int,
    current_user: User = Depends(get_current_user)
):

    user_id = cast(int, current_user.id)

    return generate_insights(
        company=company,
        year=year,
        user_id=user_id
    )