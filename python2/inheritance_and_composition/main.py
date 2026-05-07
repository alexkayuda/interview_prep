from CommissionEmp import CommissionEmployee
from HourlyEmp import HourlyEmployee
from SalaryEmp import SalaryEmployee

from PayrollSys import PayrollSystem


if __name__ == "__main__":
    salary_employee = SalaryEmployee(1, 'John Smith', 1500)
    hourly_employee = HourlyEmployee(2, 'Jane Doe', 40, 15)
    commission_employee = CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
    
    payroll_system = PayrollSystem()
    payroll_system.calculate_payroll([salary_employee,hourly_employee,commission_employee])