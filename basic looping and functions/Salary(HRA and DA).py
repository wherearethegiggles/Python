def Salary_cal():
  Basic_Salary = float(input(f"Enter your salary: "))

  DA = 0.4 * Basic_Salary
  HRA = 0.2 * Basic_Salary

  print("Basic Salary" , Basic_Salary)
  print("DA" , DA)
  print("HRA", HRA)
Salary_cal()