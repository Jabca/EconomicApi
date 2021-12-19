from typing import TypedDict, List, Dict, Any, Union, Optional
from pandas import DataFrame


class PriceType(TypedDict):
    time: str
    price: float


class ProfitType(TypedDict):
    time: str
    profit: float


class CompanyParamsType(TypedDict):
    name: str
    info: Dict[str, Any]
    d_prices: List[PriceType]
    y_prices: List[PriceType]


class ResponseType(TypedDict):
    name: str
    depth: int
    sharpe: Union[None, float]
    variation: Union[None, float]
    information: Union[None, float]
    sortino: Union[None, float]
    treynor: Union[None, float]


class CompanyPortfolioInfoType(TypedDict):
    number: float
    company_params: CompanyParamsType


class PortfolioInfoType(TypedDict):
    depth: int
    benchmark: Union[None, DataFrame]
    data_sets: Dict[str, CompanyPortfolioInfoType]
