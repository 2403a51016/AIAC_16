from dataclasses import dataclass, field
from typing import Dict

@dataclass
 
class EmployeePayroll:
    basic: float = 0.0
    hra: float = 0.0
    other_allowances: float = 0.0
    pf_percent: float = 12.0
    tax_percent: float = 0.0
    other_deductions: float = 0.0
    pf_on_gross: bool = False
    employer_pf_match: bool = True

    _gross: float = field(init=False, repr=False, default=0.0)
    _pf_employee: float = field(init=False, repr=False, default=0.0)
    _pf_employer: float = field(init=False, repr=False, default=0.0)
    _tax: float = field(init=False, repr=False, default=0.0)
    _total_deductions: float = field(init=False, repr=False, default=0.0)
    _net: float = field(init=False, repr=False, default=0.0)

    def __post_init__(self):
        for name, val in (
            ("basic", self.basic),
            ("hra", self.hra),
            ("other_allowances", self.other_allowances),
            ("pf_percent", self.pf_percent),
            ("tax_percent", self.tax_percent),
            ("other_deductions", self.other_deductions),
        ):
            if not isinstance(val, (int, float)):
                raise TypeError(f"{name} must be a number")
            if val < 0:
                raise ValueError(f"{name} must be non-negative")

        if not (0.0 <= self.pf_percent <= 100.0):
            raise ValueError("pf_percent must be between 0 and 100")
        if not (0.0 <= self.tax_percent <= 100.0):
            raise ValueError("tax_percent must be between 0 and 100")

        self._recalculate()

    def _recalculate(self):
        self._gross = float(self.basic) + float(self.hra) + float(self.other_allowances)
        pf_base = self._gross if self.pf_on_gross else float(self.basic)
        self._pf_employee = (pf_base * float(self.pf_percent)) / 100.0
        self._pf_employer = self._pf_employee if self.employer_pf_match else 0.0
        self._tax = (self._gross * float(self.tax_percent)) / 100.0
        self._total_deductions = self._pf_employee + self._tax + float(self.other_deductions)
        self._net = self._gross - self._total_deductions

    def gross_salary(self) -> float:
        return self._gross

    def pf_employee(self) -> float:
        return self._pf_employee

    def pf_employer(self) -> float:
        return self._pf_employer

    def tax(self) -> float:
        return self._tax

    def total_deductions(self) -> float:
        return self._total_deductions

    def net_salary(self) -> float:
        return self._net

    def breakdown(self) -> Dict[str, float]:
        return {
            "gross": round(self.gross_salary(), 2),
            "pf_employee": round(self.pf_employee(), 2),
            "pf_employer": round(self.pf_employer(), 2),
            "tax": round(self.tax(), 2),
            "other_deductions": round(float(self.other_deductions), 2),
            "total_deductions": round(self.total_deductions(), 2),
            "net": round(self.net_salary(), 2),
        }

    def annual_breakdown(self) -> Dict[str, float]:
        monthly = self.breakdown()
        return {k: round(v * 12, 2) for k, v in monthly.items()}

    def update(self, **kwargs):
        for k, v in kwargs.items():
            if not hasattr(self, k):
                raise AttributeError(f"Unknown attribute: {k}")
            setattr(self, k, v)
        self.__post_init__()

    def __repr__(self) -> str:
        return f"<EmployeePayroll gross={self._gross:.2f} net={self._net:.2f}>"

if __name__ == "__main__":
    emp1 = EmployeePayroll(
        basic=50000, hra=20000, other_allowances=5000,
        pf_percent=12.0, tax_percent=10.0, other_deductions=1000, pf_on_gross=False
    )
    b1 = emp1.breakdown()
    assert b1["gross"] == 75000.00
    assert b1["pf_employee"] == 6000.00
    assert b1["tax"] == 7500.00
    assert b1["total_deductions"] == 14500.00
    assert b1["net"] == 60500.00

    emp2 = EmployeePayroll(
        basic=50000, hra=20000, other_allowances=5000,
        pf_percent=12.0, tax_percent=10.0, other_deductions=1000, pf_on_gross=True
    )
    b2 = emp2.breakdown()
    assert b2["pf_employee"] == 9000.00
    assert b2["total_deductions"] == 17500.00
    assert b2["net"] == 57500.00

    emp1.update(tax_percent=5.0)
    assert emp1.tax() == 3750.0

    try:
        EmployeePayroll(basic=-100)
        raise SystemExit("Negative basic salary should have raised ValueError")
    except ValueError:
        pass

    print("All tests passed.")
    print(emp1.breakdown())
    print(emp1.annual_breakdown())

        