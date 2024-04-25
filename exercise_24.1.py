import sympy as sp

Ri, Ro, Rc, Re = sp.symbols('Ri Ro Rc Re', positive=True)
miu, Br = sp.symbols('miu Br',real=True)

coeff = sp.Matrix([[1,-1,0,Ri**(-2),-Ri**(-2),0],
                   [0,1,-1,0,Ro**(-2),-Ro**(-2)],
                   [-1,0,0,Rc**(-2),0,0],
                   [-miu,1,0,miu*Ri**(-2),-Ri**(-2),0],
                   [0,-1,miu,0,Ro**(-2),-miu*Ro**(-2)],
                   [0,0,-1,0,0,Re**(-2)]])

const = sp.Matrix([[-Br*sp.log(Ri)],
                   [Br*sp.log(Ro)],
                   [0],
                   [Br*sp.log(Ri)],
                   [-Br*sp.log(Ro)],
                   [0]])

sp.init_printing()
print(coeff**(-1)*const)
