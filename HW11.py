import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# A) Model Implementation for SIR model
def SIR_model(y, t, beta, gamma):
    S, I, R = y
    dS_dt = -beta * S * I
    dI_dt = beta * S * I - gamma * I
    dR_dt = gamma * I
    return [dS_dt, dI_dt, dR_dt]

# D) SEIR Model with Births and Deaths
def SEIR_model(y, t, beta, gamma, sigma, mu):
    S, E, I, R = y
    dS_dt = -beta * S * I + mu * (S + E + I + R) - mu * S
    dE_dt = beta * S * I - (sigma + mu) * E
    dI_dt = sigma * E - (gamma + mu) * I
    dR_dt = gamma * I - mu * R
    return [dS_dt, dE_dt, dI_dt, dR_dt]

# B) SIR Model Simulation
# Parameters for the SIR model
beta = 0.3 / 1000  # Transmission rate
gamma = 0.1        # Recovery rate
initial_conditions_SIR = [999, 1, 0]  # Initial conditions: S0, I0, R0
t_SIR = np.linspace(0, 150, 150)  # Time grid for 150 days

# Solve the SIR model
solution_SIR = odeint(SIR_model, initial_conditions_SIR, t_SIR, args=(beta, gamma))
S_SIR, I_SIR, R_SIR = solution_SIR.T

# Generate a plot showing the dynamics of S, I, and R over time. Label each curve clearly to indicate the compartment it represents.
plt.figure(figsize=(10, 6))
plt.plot(t_SIR, S_SIR, label='Susceptible')
plt.plot(t_SIR, I_SIR, label='Infected')
plt.plot(t_SIR, R_SIR, label='Recovered')
plt.title('SIR Model over 150 Days')
plt.xlabel('Time / days')
plt.ylabel('Number of people')
plt.legend()
plt.grid(True)
plt.savefig('SIR_Model_Year.png')
plt.show()

# Solve the SEIR model

# Parameters
total_population = 1000
beta = 0.3 / 1000  # Transmission rate
gamma = 0.1        # Recovery rate
sigma = 0.2        # Rate of progression from exposed to infectious
mu = 0.01          # Birth/death rate
initial_conditions_SEIR = [990, 9, 1, 0]

# Time grids for simulations
t_365 = np.linspace(0, 365, 365)
t_1200 = np.linspace(0, 1200, 1200)

# Solve the SEIR model for 365 days
solution_SEIR_365 = odeint(SEIR_model, initial_conditions_SEIR, t_365, args=(beta, gamma, sigma, mu))
S_365, E_365, I_365, R_365 = solution_SEIR_365.T

# Solve the SEIR model for 1200 days
solution_SEIR_1200 = odeint(SEIR_model, initial_conditions_SEIR, t_1200, args=(beta, gamma, sigma, mu))
S_1200, E_1200, I_1200, R_1200 = solution_SEIR_1200.T

# Plot SEIR model results for 365 days
plt.figure(figsize=(10, 6))
plt.plot(t_365, S_365, label='Susceptible')
plt.plot(t_365, E_365, label='Exposed')
plt.plot(t_365, I_365, label='Infected')
plt.plot(t_365, R_365, label='Recovered')
plt.title('SEIR Model over 365 Days')
plt.xlabel('Time / days')
plt.ylabel('Number of people')
plt.legend()
plt.grid(True)
plt.savefig('SEIR_Model_365_Days.png')
plt.show()

# Plot SEIR model results for 1200 days
plt.figure(figsize=(10, 6))
plt.plot(t_1200, S_1200, label='Susceptible')
plt.plot(t_1200, E_1200, label='Exposed')
plt.plot(t_1200, I_1200, label='Infected')
plt.plot(t_1200, R_1200, label='Recovered')
plt.title('SEIR Model over 1200 Days')
plt.xlabel('Time / days')
plt.ylabel('Number of people')
plt.legend()
plt.grid(True)
plt.savefig('SEIR_Model_1200_Days.png')
plt.show()

# E) Sensitivity analysis for various β and γ values
# Parameters
initial_conditions = [990, 9, 1, 0]
sigma = 0.2
mu = 0.01
t = np.linspace(0, 365, 365)

# Parameter ranges for sensitivity analysis
beta_values = np.linspace(0.1e-3, 0.5e-3, 5)
gamma_values = np.linspace(0.05, 0.2, 4)

# Prepare the plot
fig, axes = plt.subplots(len(beta_values), len(gamma_values), figsize=(20, 16), sharex=True, sharey=True)

for i, beta in enumerate(beta_values):
    for j, gamma in enumerate(gamma_values):
        # Solve the SEIR model
        solution = odeint(SEIR_model, initial_conditions, t, args=(beta, gamma, sigma, mu))
        S, E, I, R = solution.T
        
        # Plot the infected population
        ax = axes[i, j]
        ax.plot(t, I, label=f'Infected (β={beta:.4f}, γ={gamma:.2f})')
        ax.set_title(f'β={beta:.4f}, γ={gamma:.2f}')
        ax.grid(True)
        
        if i == len(beta_values) - 1:
            ax.set_xlabel('Days')
        if j == 0:
            ax.set_ylabel('Infected Population')

fig.suptitle('SEIR Model Sensitivity Analysis over 365 Days')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('SEIR_Sensitivity_Analysis.png')
plt.show()