"""
equations

You should not edit this file unless there is an equation error.  This file 
contains all of the equations that make solver.py work.
"""
from std_includes import *
from variables import *

i["xy"] = (I["xy_b"]/I["xx_b"]).magnitude
i["xz"] = (I["xz_b"]/I["xx_b"]).magnitude
i["yx"] = (I["xy_b"]/I["yy_b"]).magnitude
i["yz"] = (I["yz_b"]/I["yy_b"]).magnitude
i["zx"] = (I["xz_b"]/I["zz_b"]).magnitude
i["zy"] = (I["yz_b"]/I["zz_b"]).magnitude


C['L0'] = (W / (1/2 * rho * V_0 ** 2 * S_w)).magnitude
C['L'] = (W * cos(theta_0) / (1/2 * rho * V_0 ** 2 * S_w * cos(phi_0))).magnitude
C['D'] = C['D0'] + (C['D,alpha'] * C['L0'] / (2 * C['L,alpha'])) * ((C['L'] / C['L0']) ** 2 - 1)
C['D,alpha'] = C['D,alpha'] * C['L'] / C['L0']
C['X,alpha'] = C['L'] - C['D,alpha']
C['Z,alpha'] = - C['L,alpha'] - C['D']
deltaalpha = (((C['L'] - C['L0']) / C['L,alpha']) * ur.radian).to(ur.degree).magnitude
phi = -deltaalpha

B['x,muprime'] = (rho * S_w * cbar_w * C['X,muhat'] / (4 * W / g)).magnitude
B['z,muprime'] = (rho * S_w * cbar_w * C['Z,muhat'] / (4 * W / g)).magnitude
B['m,muprime'] = (rho * S_w * cbar_w ** 2 * l_ref * C['m,muhat'] / (4 * I['yy_b'])).magnitude
B['x,alphaprime'] = (rho * S_w * cbar_w * C['X,alphahat'] / (4 * W / g)).magnitude
B['z,alphaprime'] = (rho * S_w * cbar_w * C['Z,alphahat'] / (4 * W / g)).magnitude
B['m,alphaprime'] = (rho * S_w * cbar_w ** 2 * l_ref * C['m,alphahat'] / (4 * I['yy_b'])).magnitude

A['g'] = (g * l_ref / V_0 ** 2).magnitude
A['x,mu'] = (rho * S_w * l_ref / (2 * W / g)).magnitude * (2 * C['X_0'] + C['X,mu'] + (T[',V'] * cos(alpha_T0)).magnitude / (0.5 * rho * V_0 * S_w).magnitude)
A['z,mu'] = (rho * S_w * l_ref / (2 * W / g)).magnitude * (2 * C['Z_0'] + C['Z,mu'] + (T[',V'] * sin(alpha_T0)).magnitude / (0.5 * rho * V_0 * S_w).magnitude)
A['m,mu'] = (rho * S_w * cbar_w * l_ref** 2 / (2 * I['yy_b'])).magnitude * (2 * C['m_0'] + C['m,mu'] + (T[',V'] * (z_T * cos(alpha_T0) + x_T * sin(alpha_T0))).magnitude / (0.5 * rho * V_0 * S_w * cbar_w).magnitude)

A['x,alpha'] = ((rho * S_w * l_ref)/(2*W/g)*C['X,alpha']).magnitude
A['z,alpha'] = ((rho * S_w * l_ref)/(2*W/g)*C['Z,alpha']).magnitude
A['m,alpha'] = ((rho * S_w * l_ref)/(2*W/g)*C['m,alpha']).magnitude

A['y,beta'] = ((rho * S_w * l_ref)/(2*W/g)*C['Y,beta']).magnitude
A['l,beta'] = ((rho * S_w * b_w * l_ref ** 2)/(2*I['xx_b'])*C['l,beta']).magnitude
A['n,beta'] = ((rho * S_w * b_w * l_ref ** 2)/(2*I['zz_b'])*C['n,beta']).magnitude

A['l,alpha'] = ((rho * S_w * b_w * l_ref ** 2)/(2*I['xx_b'])*C['l,alpha']).magnitude
A['m,beta'] = ((rho * S_w * cbar_w * l_ref ** 2)/(2*I['yy_b'])*C['m,beta']).magnitude
A['n,alpha'] = ((rho * S_w * b_w * l_ref ** 2)/(2*I['zz_b'])*C['n,alpha']).magnitude

A['y,pswoosh'] = ((rho * S_w * b_w)/(4*W/g)*C['Y,pbar']).magnitude
A['l,pswoosh'] = ((rho * S_w * b_w ** 2 * l_ref)/(4*I['xx_b'])*C['l,pbar']).magnitude
A['n,pswoosh'] = ((rho * S_w * b_w ** 2 * l_ref)/(4*I['zz_b'])*C['n,pbar']).magnitude

A['x,qswoosh'] = ((rho * S_w * cbar_w)/(4*W/g)*C['X,qbar']).magnitude
A['z,qswoosh'] = ((rho * S_w * cbar_w)/(4*W/g)*C['Z,qbar']).magnitude
A['m,qswoosh'] = ((rho * S_w * cbar_w ** 2 * l_ref)/(4*I['yy_b'])*C['m,qbar']).magnitude

A['y,rswoosh'] = ((rho * S_w * b_w)/(4*W/g)*C['Y,rbar']).magnitude
A['l,rswoosh'] = ((rho * S_w * b_w ** 2 * l_ref)/(4*I['xx_b'])*C['l,rbar']).magnitude
A['n,rswoosh'] = ((rho * S_w * b_w ** 2 * l_ref)/(4*I['zz_b'])*C['n,rbar']).magnitude

D['y,delta_a'] = ((rho * S_w * l_ref)/(2*W/g)*C['Y,delta_a']).magnitude
D['l,delta_a'] = ((rho * S_w * b_w * l_ref ** 2)/(2*I['xx_b'])*C['l,delta_a']).magnitude
D['n,delta_a'] = ((rho * S_w * b_w * l_ref ** 2)/(2*I['zz_b'])*C['n,delta_a']).magnitude

D['x,delta_e'] = ((rho * S_w * l_ref)/(2*W/g)*C['X,delta_e']).magnitude
D['z,delta_e'] = ((rho * S_w * l_ref)/(2*W/g)*C['Z,delta_e']).magnitude
D['m,delta_e'] = ((rho * S_w * cbar_w * l_ref ** 2)/(2*I['yy_b'])*C['m,delta_e']).magnitude

D['y,delta_r'] = ((rho * S_w * l_ref)/(2*W/g)*C['Y,delta_r']).magnitude
D['l,delta_r'] = ((rho * S_w * b_w * l_ref ** 2)/(2*I['xx_b'])*C['l,delta_r']).magnitude
D['n,delta_r'] = ((rho * S_w * b_w * l_ref ** 2)/(2*I['zz_b'])*C['n,delta_r']).magnitude

eta['xx'] = (A['g'] * (I['xz_b'] * tan(phi_0) * sin(phi_0) * cos(theta_0) - I['xy_b'] * sin(phi_0) * cos(theta_0)) / I['xx_b']).magnitude
eta['xy'] = (h['z_b'] * l_ref / (I['xx_b'] * V_0)).magnitude + (A['g'] * ((I['zz_b'] - I['yy_b']) * sin(phi_0) * cos(theta_0) - 2 * I['yz_b'] * tan(phi_0) * sin(phi_0) * cos(theta_0) + I['xz_b'] * tan(phi_0) * sin(theta_0)) / I['xx_b']).magnitude
eta['xz'] = (h['y_b'] * l_ref / (I['xx_b'] * V_0)).magnitude + (A['g'] * ((I['yy_b'] - I['zz_b']) * tan(phi_0) * sin(phi_0) * cos(theta_0) - 2 * I['yz_b'] * sin(phi_0) * cos(theta_0) + I['xy_b'] * tan(phi_0) * sin(theta_0)) / I['xx_b']).magnitude
eta['yx'] = (h['z_b'] * l_ref / (I['yy_b'] * V_0)).magnitude + (A['g'] * ((I['zz_b'] - I['xx_b']) * sin(phi_0) * cos(theta_0) - 2 * I['xz_b'] * tan(phi_0) * sin(theta_0) + I['xz_b'] * tan(phi_0) * sin(phi_0) * cos(theta_0)) / I['yy_b']).magnitude 
eta['yy'] = (A['g'] * (I['xy_b'] * sin(phi_0) * cos(theta_0) - I['xz_b'] * tan(phi_0) * sin(theta_0)) / I['yy_b']).magnitude
eta['yz'] = (h['x_b'] * l_ref / (I['yy_b'] * V_0)).magnitude + (A['g'] * ((I['zz_b'] - I['xx_b']) * tan(phi_0) * sin(theta_0) - 2 * I['yz_b'] * sin(phi_0) * cos(theta_0) + I['xy_b'] * tan(phi_0) * sin(phi_0) * cos(theta_0)) / I['yy_b']).magnitude 
eta['zx'] = (h['y_b'] * l_ref / (I['zz_b'] * V_0)).magnitude + (A['g'] * ((I['yy_b'] - I['xx_b']) * tan(phi_0) * sin(phi_0) * cos(theta_0) - 2 * I['xy_b'] * tan(phi_0) * sin(theta_0) + I['yz_b'] * sin(phi_0) * cos(theta_0)) / I['zz_b']).magnitude
eta['zy'] = (h['x_b'] * l_ref / (I['zz_b'] * V_0)).magnitude + (A['g'] * ((I['yy_b'] - I['xx_b']) * tan(phi_0) * sin(theta_0) - 2 * I['xy_b'] * tan(phi_0) * sin(phi_0) * cos(theta_0) + I['xz_b'] * sin(phi_0) * cos(theta_0)) / I['zz_b']).magnitude
eta['zz'] = (A['g'] * (-I['yz_b'] * tan(phi_0) * sin(theta_0) - I['xz_b'] * tan(phi_0) * sin(phi_0) * cos(theta_0)) / I['zz_b']).magnitude



