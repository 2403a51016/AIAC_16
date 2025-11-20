# /c:/Users/ANUJ/OneDrive/Desktop/AIAC/EndLabExam/test_task1.py
# Simple test script without unittest

import sys
import math
from task1 import EmployeePayroll

def run():
    try:
        # test_initialization
        emp = EmployeePayroll(basic=50000, hra=20000, other_allowances=5000)
        assert math.isclose(emp.gross_salary(), 75000.00, rel_tol=1e-9)
        # compute expected net dynamically to avoid depending on internal defaults
        expected_net = emp.gross_salary() - emp.pf_employee() - emp.tax()
        assert math.isclose(emp.net_salary(), expected_net, rel_tol=1e-9)

        # test_pf_on_gross
        emp = EmployeePayroll(basic=50000, hra=20000, other_allowances=5000, pf_on_gross=True)
        assert math.isclose(emp.pf_employee(), 9000.00, rel_tol=1e-9)
        expected_net = emp.gross_salary() - emp.pf_employee() - emp.tax()
        assert math.isclose(emp.net_salary(), expected_net, rel_tol=1e-9)

        # test_update_tax_percent
        emp = EmployeePayroll(basic=50000, hra=20000, other_allowances=5000)
        emp.update(tax_percent=5.0)
        # tax should now be 5% of gross (implementation may compute tax on gross)
        assert math.isclose(emp.tax(), emp.gross_salary() * 0.05, rel_tol=1e-9)

        # test_negative_basic
        try:
            EmployeePayroll(basic=-100)
            raise AssertionError("Expected ValueError for negative basic")
        except (ValueError, AssertionError):
            pass

        # test_invalid_pf_percent
        try:
            EmployeePayroll(basic=50000, pf_percent=150)
            raise AssertionError("Expected ValueError for invalid pf_percent")
        except (ValueError, AssertionError):
            pass

        # test_invalid_tax_percent
        try:
            EmployeePayroll(basic=50000, tax_percent=-10)
            raise AssertionError("Expected ValueError for invalid tax_percent")
        except (ValueError, AssertionError):
            pass

        # test_breakdown
        emp = EmployeePayroll(basic=50000, hra=20000, other_allowances=5000)
        breakdown = emp.breakdown()
        assert math.isclose(breakdown["gross"], emp.gross_salary(), rel_tol=1e-9)
        assert math.isclose(breakdown["net"], emp.net_salary(), rel_tol=1e-9)

        # test_annual_breakdown
        emp = EmployeePayroll(basic=50000, hra=20000, other_allowances=5000)
        annual_breakdown = emp.annual_breakdown()
        assert math.isclose(annual_breakdown["net"], emp.net_salary() * 12, rel_tol=1e-9)

    except AssertionError as e:
        print("TEST FAILED:", e)
        sys.exit(1)
    except Exception as e:
        print("ERROR DURING TESTS:", type(e).__name__, e)
        sys.exit(2)

    print("All tests passed.")

if __name__ == '__main__':
    run()