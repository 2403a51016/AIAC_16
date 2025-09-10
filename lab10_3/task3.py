class Employee:
    """
    Represents an employee with a name and salary.
    Provides functionality to increase salary and display employee information.
    """
    def __init__(self, name: str, salary: float):
        self._name = name
        self._salary = salary
    def increase_salary(self, percentage: float) -> None:
        """
        Increases the employee's salary by a given percentage.
        Args:
            percentage (float): The percentage increase to apply.
        """
        if percentage < 0:
            raise ValueError("Percentage increase cannot be negative.")
        self._salary += self._salary * (percentage / 100)
    def display_info(self) -> None:
        """
        Displays the employee's name and current salary.
        """
        print(f"Employee: {self._name}, Salary: ₹{self._salary:,.2f}")
emp = Employee("Amit", 50000)
emp.display_info()
emp.increase_salary(10)
emp.display_info()