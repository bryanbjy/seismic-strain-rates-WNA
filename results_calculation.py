#Strain 
from numpy import*

def strain(mu,V,M):
    strain = []
    for i in M:
        i = (1/(2*mu*V))*i
        strain.append(i)
        
    return strain 

#Strain rate
def strain_rate(mu,V,t,M):
    strain_r = []
    for i in M:
        i = (1/(2*mu*V*t))*i
        strain_r.append(i)
    
    return strain_r

def strain_rate_2(mu,V,t,M):
    
    return (1/(2*mu*V*t))*M

#Plate Velocity
def plate_vel(mu,L,W,t,M_0):
    
    return (1/(mu*L*W*t))*M_0