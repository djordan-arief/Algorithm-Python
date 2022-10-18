def arithmetic_arranger(problems, bool= False):  
  line1 = []
  line2 = []
  line3 = []
  line4 = []
  # check if the list contains 5 or more problems 
  if len(problems) > 5:
    return "Error: too many problems"
  else:
    # loop through the list
    for operations in problems:
      operation = operations.split()
      operand1 = operation[0]
      operator = operation[1]
      operand2 = operation[2]
      
      # check if the operator is either a '+' or '-'
      if not operator == '+' and not operator == '-':
        return "Error: Operator must be '+' or '-'."
        break;
        
      # check if it's a string of number
      if operand1.isnumeric() == False or operand2.isnumeric() == False:
        return "Error: Numbers must only contain digits."
          
      # check if the digit number is not more than 4
      if len(operand1) > 4 or len(operand2) > 4:
        return ("Error: Numbers cannot be more than four digits.")
        break;
          
      # Get the answer of the problem 
      sum = 0 
      if operator == '+':
        sum = int(operand1) + int(operand2)
      else:
        sum = int(operand1) - int(operand2)


      #format the answer
      # Top operand / line1
      if len(operand1) > len(operand2):
        line1.append(" "*2 + operand1)
      else: 
        line1.append(" "*(len(operand2) - len(operand1) + 2) + operand1)

      # Operator and second operand /line 2
      if len(operand2) > len(operand1):
        line2.append(operator + " " + operand2)
      else:
        line2.append(operator + " "*(len(operand1) - len(operand2) + 1) + operand2)

      # Dash /line3
      line3.append("-"*(max(len(operand1), len(operand2)) + 2))

      # Display results / line4
      if bool: 
        line4.append(' '*2 + str(sum))
        arranged_problems = "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(line3) + "\n" + "    ".join(line4)
      else: 
        arranged_problems = "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(line3)
      
  return arranged_problems


arithmetic_arranger(["1 + 1", "43 - 23"], True)