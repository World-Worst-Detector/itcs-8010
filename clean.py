import pydot
graph = pydot.graph_from_dot_file('w_nottear_loan.dot')
file = open("notear_loan.dot",'r')
lines = file.readlines()
lines = [line.replace(' ', '') for line in lines]
lines = [line.replace('\n', '') for line in lines]
lines = [line.replace('\t', '') for line in lines]
with open('Final_t.dot', 'w') as f:
    f.writelines(lines)