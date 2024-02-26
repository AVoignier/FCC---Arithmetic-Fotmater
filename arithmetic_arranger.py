def arithmetic_arranger(problems,  display_result = False):

  problem_space = '    '
  
  if len(problems) > 5:
    return 'Error: Too many problems.'

  lines = ['','','','']
  
  for index_problem, problem in enumerate(problems):
    str_problem = problem.split(' ')

    #check values
    try:
      value1 = int(str_problem[0])
      value2 = int(str_problem[2])
    except ValueError:
      return "Error: Numbers must only contain digits."

    if len(str_problem[0]) > 4 or len(str_problem[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    
    #check operator
    if str_problem[1] == '+':
        result = value1 + value2
    elif str_problem[1] == '-':
        result = value1 - value2
    else:
      return "Error: Operator must be '+' or '-'."

    length_line = max( len(str_problem[0]), len(str_problem[2]) )

    #update displayed lines
    lines[0] += '  ' + str_problem[0].rjust(length_line)
    lines[1] += str_problem[1] + ' ' + str_problem[2].rjust(length_line)
    lines[2] += f'--{"-"*length_line}' 
    if display_result:
      lines[3] += str(result).rjust(length_line+2)
    
    lines[0] += problem_space if index_problem < len(problems)-1 else "\n"
    lines[1] += problem_space if index_problem < len(problems)-1 else '\n'
    lines[2] += problem_space if index_problem < len(problems)-1 else '\n'
    if display_result:
      lines[3] += problem_space if index_problem < len(problems)-1 else '\n'

  arranged_problems = ''.join(lines)[0:-1]

  print(arranged_problems)

  return arranged_problems
