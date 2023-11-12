from dataclasses import dataclass


@dataclass
class Result:
    subject_of_purchase: str
    customer_name: str
    location: str
    item: str
    estimated_cost: str
    closing_date_for_proposals: str
    region: str
