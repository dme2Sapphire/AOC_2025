import re
import itertools as it

shapes=[]
ctrees=[]
inshape=0
with open("input12.txt",'r') as ipt:
    for line in ipt.readlines():
        if re.match('[0-9]+:',line):
            inshape=1
            shape=[]
        elif re.match('[0-9]{1,2}x[0-9]{1,2}: *',line):
            ctree_size=[int(l) for l in line.split(':')[0].split('x')]
            ctree_shapenum=[int(snum) for snum in line.strip('\n').split(':')[1].split(' ')[1:]]
            ctrees.append({'shape':ctree_size,'giftlist':ctree_shapenum})
        elif inshape and re.match('[#,.]+',line):
            shape.append([1 if s=='#' else 0 for s in line.strip('\n') ])
        elif inshape and line=="\n":
            inshape=0
            shapes.append(shape)
        else:
            assert False
shape_tnum=len(shapes)
ctree_num=len(ctrees)
print(shape_tnum)
print(ctree_num)
naive_valid=[((ctree['shape'][0]//3)*(ctree['shape'][1]//3)>=sum(ctree['giftlist'])) for ctree in ctrees] #460/1000
# naive_surpass=[max((sum(ctree['giftlist'])-(ctree['shape'][0]//3)*(ctree['shape'][1]//3)),0) for ctree in ctrees]
print(sum(naive_valid))
shape_area_c=[sum(list(it.chain.from_iterable(shape) )) for shape in shapes]
print(shape_area_c)
naive_invalid=[(ctree['shape'][0]*ctree['shape'][1]<sum([a*b for a,b in zip(shape_area_c,ctree['giftlist'])])) for ctree in ctrees]
print(sum(naive_invalid))
print(sum(naive_valid)+sum(naive_invalid)==ctree_num) #WTF DO YOU MEAN THAT THIS IS TRUE??????