class Student:
    """
    A class to represent a student's basic information and marks.
    """
    def __init__(self, name: str, age: int, marks: list[int]):
        """
        Initializes a new Student object.

        Args:
            name (str): The name of the student.
            age (int): The age of the student.
            marks (list[int]): A list of the student's marks in three subjects.
        """
        if len(marks) != 3:
            raise ValueError("The 'marks' list must contain exactly three values.")
        self.name = name
        self.age = age
        self.marks = marks
    def get_details(self) -> None:
        """
        Prints the student's name and age in a readable format.
        """
        print(f"Name: {self.name}\nAge: {self.age}")
    def get_total_marks(self) -> int:
        """
        Calculates and returns the sum of the student's marks.
        Returns:
            int: The total sum of the marks.
        """
        return sum(self.marks)
# Example Usage
student1 = Student("Alice", 17, [85, 92, 78])
student1.get_details()
print(f"Total Marks: {student1.get_total_marks()}")
print("\n---")
student2 = Student("Bob", 16, [95, 88, 90])
student2.get_details()
print(f"Total Marks: {student2.get_total_marks()}")