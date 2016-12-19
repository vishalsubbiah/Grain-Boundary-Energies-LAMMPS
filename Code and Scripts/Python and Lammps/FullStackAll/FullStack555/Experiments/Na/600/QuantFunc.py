from Quaternion import Quat, normalize
from math import cos, sin, radians, sqrt
from fractions import Fraction, gcd

def QuatMat(q):
    
    qw=q[0]
    qx=q[1]
    qy=q[2]
    qz=q[3]
    
    m11=1-(2*qy*qy)-(2*qz*qz)
    m12=2*qx*qy-2*qz*qw
    m13=2*qx*qz+2*qy*qw
    
    m21=2*qx*qy+2*qz*qw
    m22=1-2*qx*qx-2*qz*qz
    m23=2*qy*qz-2*qx*qw
    
    m31=2*qx*qz-2*qy*qw
    m32=2*qy*qz+2*qx*qw
    m33=1-2*qx*qx-2*qy*qy
    
    M=[[m11,m12,m13],[m21,m22,m23],[m31,m32,m33]]    
    
    return M

def QuatInv(q1):
    
    normsqr=q1[0]**2+q1[1]**2+q1[2]**2+q1[3]**3
    
    q1inv=[q1[0]/normsqr,-q1[1]/normsqr,-q1[2]/normsqr,-q1[3]/normsqr]
    
    return q1inv

def QuatMult(q1,q2):
    
    Q0 = q1[0]*q2[0] - q1[1]*q2[1] - q1[2]*q2[2] - q1[3]*q2[3]
    Q1 = q1[0]*q2[1] + q1[1]*q2[0] - q1[2]*q2[3] + q1[3]*q2[2]
    Q2 = q1[0]*q2[2] + q1[1]*q2[3] + q1[2]*q2[0] - q1[3]*q2[1]
    Q3 = q1[0]*q2[3] - q1[1]*q2[2] + q1[2]*q2[1] + q1[3]*q2[0]
    
    q=[Q0,Q1,Q2,Q3]
  
    return q
       
def find_orient(theta,A,q1):
    
    qw= cos(radians(theta)/2.0)
    qi=A[0]*sin(radians(theta)/2.0)
    qj=A[1]*sin(radians(theta)/2.0)
    qk=A[2]*sin(radians(theta)/2.0)
    
    q=normalize([qw,qi,qj,qk])
    qInv=normalize(QuatInv(q))
    q2=QuatMult(q1,qInv)
    
    return q2   
    
def scale(M):

    x1=Fraction(M[0][0]).limit_denominator(20)
    x2=Fraction(M[0][1]).limit_denominator(20)
    x3=Fraction(M[0][2]).limit_denominator(20)

    X1=x1.numerator*x2.denominator*x3.denominator
    X2=x2.numerator*x1.denominator*x3.denominator
    X3=x3.numerator*x2.denominator*x1.denominator

    y1=Fraction(M[1][0]).limit_denominator(20)
    y2=Fraction(M[1][1]).limit_denominator(20)
    y3=Fraction(M[1][2]).limit_denominator(20)

    Y1=y1.numerator*y2.denominator*y3.denominator
    Y2=y2.numerator*y1.denominator*y3.denominator
    Y3=y3.numerator*y2.denominator*y1.denominator

    z1=Fraction(M[2][0]).limit_denominator(20)
    z2=Fraction(M[2][1]).limit_denominator(20)
    z3=Fraction(M[2][2]).limit_denominator(20)

    Z1=z1.numerator*z2.denominator*z3.denominator
    Z2=z2.numerator*z1.denominator*z3.denominator
    Z3=z3.numerator*z2.denominator*z1.denominator

    M=[[X1,X2,X3],[Y1,Y2,Y3],[Z1,Z2,Z3]]

    return M

