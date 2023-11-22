#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 13:38:01 2023

@author: FernandoPeinado

This Python program file calculates the optimal crime levels and the optimal punishment 
levels from the simulations and robutsness checks reported in Peinado, F. (2023) "Aggravation, 
Environmental Bias and Mitigation of Prospective Crimes." The code has been run in 
version 3.9 of Python and uses the function ‘fsolve’ from the ‘scipy.optimize’ library.
This code provides the results in the form of the figures presented in the same pice of 
work using the ‘matplotlib’ library. These figures are automatically saved as .png files 
in the same directory where this Python program file might be.
"""

import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


# Optimal crime and punishment levels

# Aggravation and Mitigation

# Equation (5)
def function5(sigma, beta, psi, d, rho):
    return ((- sigma) / (beta * d * rho * (psi ** (1 / beta)))) ** (beta / (rho * beta + beta - sigma))

# Equation (6)
def function6(sigma, beta, psi, d, rho):
    return - (((- sigma) / (beta * d * rho * (psi ** ((1 + rho) / sigma)))) ** (sigma / (rho * beta + beta - sigma)))

# Equation (7) = - Equation (6) / Equation (5)  
def function7(sigma, beta, psi, d, rho):
    return - function6(sigma, beta, psi, d, rho) / function5(sigma, beta, psi, d, rho)

# Environmental bias (8)

def function8(sigma, beta, psi, d, rho):
    return 1 / (psi ** (1 / beta))




# Reference Point (Reference Offender)

weight_pr_cr_value = function8(0.88, 0.88, 2.25, -1, 0.88)




# Aggravation


# Set of predefined values for sigma, beta, psi, d and rho
sigma_values = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85]  # Update with your desired values for sigma (must be between 0 and beta)
beta_value = [0.88]  # Update with your desired value for beta (must be between 0 and 1)
psi_value = [2.25]  # Update with your desired value for psi (must be >1)
d_value = [-1]  #Update with your desired value for d (must be <0)
rho_value = [0.88]  #Update with your desired value for rho (must be >=1)

# List to store the weight of pa over ca
weight_pa_ca_list = []

# Solve the equation for each combination of values
for sigma in sigma_values:
    for beta in beta_value:
        for d in d_value:
            for rho in rho_value:
                for psi in psi_value:
                    # Calculate the corresponding weight of pa over ca values
                    weight_pa_ca_values = function7(sigma, beta, psi, d, rho)

                    # Append the weight of pa over ca values to the list
                    weight_pa_ca_list.append(weight_pa_ca_values)

weight_pa_ca_list.append(weight_pr_cr_value)

sigma_values_p = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.88] # Copy your desired list of sigma values from above adding the value of sigma at the reference point

# Print the weight of pa over ca values
for i in range(len(sigma_values_p)):
    print("Intersection points for values psi =", psi_value[i%len(beta_value)], ", beta =", beta_value[i%len(beta_value)], ", sigma =", sigma_values_p[i], ", d =", d_value[i%len(beta_value)], " and rho =", rho_value[i%len(beta_value)])
    print("-pa/ca =", weight_pa_ca_list[i])
    print()

# Set the font properties
font = {'family': 'sans-serif',
        'size': 16,
        'style': 'italic'}

# Create the plot
fig, ax = plt.subplots(figsize=(6, 6))

# Plot the sigma-values and the weights of pa over ca
ax.plot(sigma_values_p, weight_pa_ca_list, 'o', color='black', alpha=0.8)

# Add labels and title
ax.set_xlabel('σ', fontdict=font)
ax.set_ylabel('-$p_A$/$c_A$', fontdict=font)

# Remove the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Adjust subplot spacing
plt.tight_layout()

# Save the plot with DPI=1000
plt.savefig('Figure_6.png', dpi=1000)

# Show the plot
plt.show()




# Aggravation - Robustness checks (different values of rho)


# Set of predefined values for sigma, beta, psi, d and rho
sigma_values = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85]  # Update with your desired values for sigma (must be between 0 and beta)
beta_value = [0.88]  # Update with your desired value for beta
psi_value = [2.25]  # Update with your desired value for psi (must be >1)
d_value = [-1]  #Update with your desired value for d (must be <0)
rho_values = [1, 0.88, 0.5, 0.25]  #Update with your desired values for rho (must be >=0)

# List of lists to store the weight of pa over ca for each rho
weight_pa_ca_lists_rho = [[] for _ in rho_values]

# Solve the equation for each combination of values
for rho_index, rho in enumerate(rho_values):
    for sigma in sigma_values:
        for beta in beta_value:
            for d in d_value:
                for psi in psi_value:
                    # Calculate the corresponding weight of pa over ca values
                    weight_pa_ca_values = function7(sigma, beta, psi, d, rho)

                    # Append the weight of pa over ca values to the list of lists
                    weight_pa_ca_lists_rho[rho_index].append(weight_pa_ca_values)

for rho_index, rho in enumerate(rho_values):
    weight_pa_ca_lists_rho[rho_index].append(weight_pr_cr_value)

sigma_values_p = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.88] # Copy your desired list of sigma values from above adding the value of sigma at the reference point

# Set the font properties
font = {'family': 'sans-serif',
        'size': 16,
        'style': 'italic'}

# Create the plot
fig, ax = plt.subplots(figsize=(6, 6))

# Define marker shapes for different rho values
marker_shapes = ['^', 'o', 'v', 'D']

# Plot the sigma-values and weight of pa-values over ca-values for each rho
for rho_index, rho in enumerate(rho_values):
    marker = marker_shapes[rho_index]
    ax.plot(sigma_values_p, weight_pa_ca_lists_rho[rho_index], marker, label='ρ='+str(rho), color='black', alpha=0.8)

# Add labels and title
ax.set_xlabel('σ', fontdict=font)
ax.set_ylabel('-$p_A$/$c_A$', fontdict=font)

# Remove the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Add legend
ax.legend()

# Adjust subplot spacing
plt.tight_layout()

# Save the plot with DPI=1000
plt.savefig('Figure_7_1.png', dpi=1000)

# Show the plot
plt.show()




# Aggravation - Robustness checks (different values of d)


# Set of predefined values for sigma, beta, psi, d and rho
sigma_values = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85]  # Update with your desired values for sigma (must be between 0 and beta)
beta_value = [0.88]  # Update with your desired value for beta (must be between 0 and 1)
psi_value = [2.25]  # Update with your desired value for psi (must be >1)
d_values = [-1, -2.25, -3, -4]  #Update with your desired values for d (must be <0)
rho_value = [0.88]  #Update with your desired value for rho (must be >=1)

# List of lists to store the weight of pa over ca for each d
weight_pa_ca_lists_d = [[] for _ in d_values]

# Solve the equation for each combination of values
for d_index, d in enumerate(d_values):
    for sigma in sigma_values:
        for beta in beta_value:
            for rho in rho_value:
                for psi in psi_value:
                    # Calculate the corresponding weight of pa over ca values
                    weight_pa_ca_values = function7(sigma, beta, psi, d, rho)

                    # Append the weight of pa over ca values to the list of lists
                    weight_pa_ca_lists_d[d_index].append(weight_pa_ca_values)

for d_index, d in enumerate(d_values):
    weight_pa_ca_lists_d[d_index].append(weight_pr_cr_value)

sigma_values_p = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.88] # Copy your desired list of sigma values from above adding the value of sigma at the reference point

# Set the font properties
font = {'family': 'sans-serif',
        'size': 16,
        'style': 'italic'}

# Create the plot
fig, ax = plt.subplots(figsize=(6, 6))

# Define marker shapes for different rho values
marker_shapes = ['o', 'v', '^', 'D']

# Plot the sigma-values and weight of pa-values over ca-values for each d
for d_index, d in enumerate(d_values):
    marker = marker_shapes[d_index]
    ax.plot(sigma_values_p, weight_pa_ca_lists_d[d_index], marker, label='d='+str(d), color='black', alpha=0.8)

# Add labels and title
ax.set_xlabel('σ', fontdict=font)
ax.set_ylabel('-$p_A$/$c_A$', fontdict=font)

# Remove the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Add legend
ax.legend()

# Adjust subplot spacing
plt.tight_layout()

# Save the plot with DPI=1000
plt.savefig('Figure_7_2.png', dpi=1000)

# Show the plot
plt.show()




# Mitigation


# Set of predefined values for sigma, beta, psi, d and rho
sigma_values = [0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99]  # Update with your desired values for sigma (must be between beta and 1)
beta_value = [0.88]  # Update with your desired value for beta (must be between 0 and 1)
psi_value = [2.25]  # Update with your desired value for psi (must be >1)
d_value = [-1]  #Update with your desired value for d (must be <0)
rho_value = [0.88]  #Update with your desired value for rho (must be >=1)

# List to store the weight of pa over cm
weight_pm_cm_list = [weight_pr_cr_value]

# Solve the equation for each combination of values
for sigma in sigma_values:
    for beta in beta_value:
        for d in d_value:
            for rho in rho_value:
                for psi in psi_value:
                    # Calculate the corresponding weight of pm over cm values
                    weight_pm_cm_values = function7(sigma, beta, psi, d, rho)

                    # Append the weight of pm over cm values to the list
                    weight_pm_cm_list.append(weight_pm_cm_values)

sigma_values_p = [0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99]  # Copy your desired list of sigma values from above adding the value of sigma at the reference point

# Print the weight of pm over cm values
for i in range(len(sigma_values_p)):
    print("Intersection points for values psi =", psi_value[i%len(beta_value)], ", beta =", beta_value[i%len(beta_value)], ", sigma =", sigma_values_p[i], ", d =", d_value[i%len(beta_value)], " and rho =", rho_value[i%len(beta_value)])
    print("-pm/cm =", weight_pm_cm_list[i])
    print()

# Set the font properties
font = {'family': 'sans-serif',
        'size': 16,
        'style': 'italic'}

# Create the plot
fig, ax = plt.subplots(figsize=(6, 6))

# Plot the sigma-values and the weights of pm over cm
ax.plot(sigma_values_p, weight_pm_cm_list, 'o', color='black', alpha=0.8)

# Add labels and title
ax.set_xlabel('σ', fontdict=font)
ax.set_ylabel('-$p_M$/$c_M$', fontdict=font)

# Remove the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Adjust subplot spacing
plt.tight_layout()

# Save the plot with DPI=1000
plt.savefig('Figure_8.png', dpi=1000)

# Show the plot
plt.show()




# Mitigation - Robustness checks (different values of rho)


# Set of predefined values for sigma, beta, psi, d and rho
sigma_values = [0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99]  # Update with your desired values for sigma (must be between beta and 1)
beta_value = [0.88]  # Update with your desired value for beta (must be between 0 and 1)
psi_value = [2.25]  # Update with your desired value for psi (must be >1)
d_value = [-1]  #Update with your desired value for d (must be <0)
rho_values = [1, 0.88, 0.5, 0.25]  #Update with your desired values for rho (must be >=1)

# List of lists to store the weight of pm over cm for each rho
weight_pm_cm_lists_rho = [[] for _ in rho_values]

# Solve the equation for each combination of values
for rho_index, rho in enumerate(rho_values):
    weight_pm_cm_lists_rho[rho_index].append(weight_pr_cr_value)

for rho_index, rho in enumerate(rho_values):
    for sigma in sigma_values:
        for beta in beta_value:
            for d in d_value:
                for psi in psi_value:
                    # Calculate the corresponding weight of pm over cm values
                    weight_pm_cm_values = function7(sigma, beta, psi, d, rho)

                    # Append the weight of pm over cm values to the list of lists
                    weight_pm_cm_lists_rho[rho_index].append(weight_pm_cm_values)

sigma_values_p = [0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99]  # Copy your desired list of sigma values from above adding the value of sigma at the reference point

# Set the font properties
font = {'family': 'sans-serif',
        'size': 16,
        'style': 'italic'}

# Create the plot
fig, ax = plt.subplots(figsize=(6, 6))

# Define marker shapes for different rho values
marker_shapes = ['^', 'o', 'v', 'D']

# Plot the sigma-values and weight of pm-values over cm-values for each rho
for rho_index, rho in enumerate(rho_values):
    marker = marker_shapes[rho_index]
    ax.plot(sigma_values_p, weight_pm_cm_lists_rho[rho_index], marker, label='ρ='+str(rho), color='black', alpha=0.8)

# Add labels and title
ax.set_xlabel('σ', fontdict=font)
ax.set_ylabel('-$p_M$/$c_M$', fontdict=font)

# Remove the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Add legend
ax.legend()

# Adjust subplot spacing
plt.tight_layout()

# Save the plot with DPI=1000
plt.savefig('Figure_9_1.png', dpi=1000)

# Show the plot
plt.show()




# Mitigation - Robustness checks (different values of d)


# Set of predefined values for sigma, beta, psi, d and rho
sigma_values = [0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99]  # Update with your desired values for sigma (must be between beta and 1)
beta_value = [0.88]  # Update with your desired value for beta (must be between 0 and 1)
psi_value = [2.25]  # Update with your desired value for psi (must be >1)
d_values = [-1, -2.25, -3, -4]  #Update with your desired values for d (must be <0)
rho_value = [0.88]  #Update with your desired value for rho (must be >=1)

# List of lists to store the weight of pm over cm for each d
weight_pm_cm_lists_d = [[] for _ in d_values]

# Solve the equation for each combination of values
for d_index, d in enumerate(d_values):
    weight_pm_cm_lists_d[d_index].append(weight_pr_cr_value)

for d_index, d in enumerate(d_values):
    for sigma in sigma_values:
        for beta in beta_value:
            for rho in rho_value:
                for psi in psi_value:
                    # Calculate the corresponding weight of pm over cm values
                    weight_pm_cm_values = function7(sigma, beta, psi, d, rho)

                    # Append the weight of pm over cm values to the list of lists
                    weight_pm_cm_lists_d[d_index].append(weight_pm_cm_values)
    
sigma_values_p = [0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99]  # Copy your desired list of sigma values from above adding the value of sigma at the reference point

# Set the font properties
font = {'family': 'sans-serif',
        'size': 16,
        'style': 'italic'}

# Create the plot
fig, ax = plt.subplots(figsize=(6, 6))

# Define marker shapes for different rho values
marker_shapes = ['o', 'v', '^', 'D']

# Plot the sigma-values and weight of pa-values over ca-values for each d
for d_index, d in enumerate(d_values):
    marker = marker_shapes[d_index]
    ax.plot(sigma_values_p, weight_pm_cm_lists_d[d_index], marker, label='d='+str(d), color='black', alpha=0.8)

# Add labels and title
ax.set_xlabel('σ', fontdict=font)
ax.set_ylabel('-$p_M$/$c_M$', fontdict=font)

# Remove the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Add legend
ax.legend()

# Adjust subplot spacing
plt.tight_layout()

# Save the plot with DPI=1000
plt.savefig('Figure_9_2.png', dpi=1000)

# Show the plot
plt.show()



