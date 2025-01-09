class Employee:
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary
    
    def calculate_salary(self):
        raise NotImplementedError("Subclasses should implement this method.")

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, base_salary):
        super().__init__(name, employee_id, base_salary)
    
    def calculate_salary(self):
        tax_deduction = self.base_salary * 0.10
        pf_deduction = self.base_salary * 0.12
        
        final_salary = self.base_salary - tax_deduction - pf_deduction
        return final_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, base_salary):
        super().__init__(name, employee_id, base_salary)
    
    def calculate_salary(self):
        tax_deduction = self.base_salary * 0.10
        pf_deduction = self.base_salary * 0.12
        
        final_salary = self.base_salary - tax_deduction - pf_deduction
        return final_salary

class ContractorEmployee(Employee):
    def __init__(self, name, employee_id, base_salary):
        super().__init__(name, employee_id, base_salary)
    
    def calculate_salary(self):
        tax_deduction = self.base_salary * 0.10
        
        final_salary = self.base_salary - tax_deduction
        return final_salary

def main():
    ft_employee = FullTimeEmployee("Awani", "FT001", 5000)
    print(f"Full-time employee {ft_employee.name} (ID: {ft_employee.employee_id}) Final Salary: {ft_employee.calculate_salary()}")

    pt_employee = PartTimeEmployee("Akshat", "PT001", 3000)
    print(f"Part-time employee {pt_employee.name} (ID: {pt_employee.employee_id}) Final Salary: {pt_employee.calculate_salary()}")

    contractor_employee = ContractorEmployee("Bhavik", "CT001", 4000)
    print(f"Contractor employee {contractor_employee.name} (ID: {contractor_employee.employee_id}) Final Salary: {contractor_employee.calculate_salary()}")

if __name__ == "__main__":
    main()