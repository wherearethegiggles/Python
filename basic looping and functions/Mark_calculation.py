def mark_cal():
  marks = []
  total_marks = 0

  #Input
  for i in range(5):
    subject_marks = float(input(f"Enter each subject marks {i+1}: "))
    marks.append(subject_marks)
    total_marks += subject_marks
  
  Avg = total_marks / 5
  Percentage = (total_marks / (5 * 100) * 100)

  #Output
  print("\nmarks entered", marks)
  print("Total marks", total_marks)
  print("Average", Avg)
  print("Percentage", Percentage)

mark_cal()