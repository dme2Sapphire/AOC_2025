
import numpy as np
import pulp

machines = []
with open("input10.txt", 'r') as ipt:
    for line in ipt.readlines():
        mipt = line.split(' ')
        m_ind = [1 if x == '#' else 0 for x in mipt[0][1:-1]]
        m_opers = [x[1:-1].split(',') for x in mipt[1:-1]]
        for idx, m_oper in enumerate(m_opers):
            m_oper = [int(x) for x in m_oper]
            m_opers[idx] = m_oper
        m_jv = [int(x) for x in (mipt[-1].strip('\n'))[1:-1].split(',')]
        # print(m_opers)
        machines.append({'i_lights': m_ind, 'opers': m_opers, 'jvs': m_jv})

def pos2blist(pos, l):
    blist = [0]*l
    for p in pos:
        blist[p] = 1
    return blist



#damn it why should I suffer after willingly given up forbidden knowledge of linear algebra
solutions=[]
fail=0
for idx, machine in enumerate(machines):

    var_num=len(machine['opers'])
    equa_num=len(machine['jvs'])
    sol=np.array(machine['jvs'])
    opers = [pos2blist(oper, equa_num) for oper in machine['opers']]
    coeff=np.array(opers).T
    # print(coeff.shape,sol.shape)
    # print(coeff,sol)
    solution=np.linalg.lstsq(coeff,sol)
    # equation_full=np.concatenate((coeff,sol))
    # print(coeff)
    solvalid=1
    for x in solution[0].tolist():
        if (x<-1e-5 or abs(x-round(x))>1e-5):
            solvalid=0
    # if solvalid==1:
    #THERE'S PROBLEM WITH lstsq
    if False:
        solutions.append([idx,solution[0]])
        print(solution[0])
    else:
        #wtf is integar programming????
        solution=[]
        print(f'Multiple Solution for {idx}')
        print('try using pulp')
        problem=pulp.LpProblem(f"Problp{idx}",sense=pulp.LpMinimize)
        dec_var=[]
        str_obj=''
        for i in range(var_num):
            if i>0:
                str_obj+=' + '
            str_obj+=f'dec_var[{i}]'
        
            dec_var.append(pulp.LpVariable(f'x{i}',lowBound=0,upBound=max(sol),cat='Integer'))
        for j in range(coeff.shape[0]):
            
            str_cons=''
            for i in range(var_num):
                if i>0:
                    str_cons+=' + '
                str_cons+=f'dec_var[{i}] * {coeff[j,i]}'
            
            str_cons+=f' == {sol[j]}'
            problem += eval(str_cons)
        problem+=eval(str_obj)
        problem.solve()
        for i in range(var_num):
            solution.append(dec_var[i].varValue)
        print(f'pulp solution:{solution}')
        solutions.append([idx,solution])
        # quit()
            # problem += (dec_var[i]*coeff[i,j])
        # fail+=1
        # print(solution[0])
        # constrain_coeff_1=np.reshape(coeff.sum(axis=0)-coeff.sum(axis=0).mean(),(1,-1))
        # constrain_sol=np.zeros((1))
        # coeff_con=np.concatenate((coeff,constrain_coeff_1))
        # sol_con=np.concatenate((sol,constrain_sol))
        # # print(coeff_con,sol_con)
        # solution=np.linalg.lstsq(coeff_con,sol_con)
        # print(solution[0])
    # print(np.triu(coeff))
    # rank=np.linalg.matrix_rank(np.array(opers))

    # print(var_num,rank,equa_num)
    #As you can see all of them have rank(opers)<=len(jv) which means there's only one/1 series of solutions.
# print(solutions)
print(sum([sum(solution[1]) for solution in solutions]))

# print(fail)

def min_press_to_jv(machine):

    jvs = machine['jvs']
    j_num=len(jvs)
    o_num = len(machine['opers'])
    opers = [pos2blist(oper, j_num) for oper in machine['opers']]
    return minp(jvs,opers)

def jvhs(jv):
    return str(jv)

#That will take forever
state_memo={}
def minp(jv,opers):
    prevstates=[]
    if len(state_memo)%1000000==0 and len(state_memo)>0:
        print(len(state_memo))
    if jvhs(jv) in state_memo:
        return state_memo[jvhs(jv)]
    for oper in opers:
        if jv == oper:
            return 1
        if (sum([x<0 for x in jv])>0) or (sum(jv)==0):
            return 0
        prevstates.append([a-b for a,b in zip(jv,oper)])
    minp_num=min([minp(state,opers) for state in prevstates])
    state_memo[jvhs(jv)]=minp_num
    return minp_num

# min_press_to_jv(machines[0])