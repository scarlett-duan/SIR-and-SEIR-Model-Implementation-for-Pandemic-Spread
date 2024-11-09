## Part C
![SIR Model Over 150 Days](https://github.com/scarlett-duan/SIR-and-SEIR-Model-Implementation-for-Pandemic-Spread/blob/main/SIR_Model_Year.png)
### i. Infection Peak:
- **Peak Timing and Level**: The infection reaches its peak at approximately day 40, with the highest number of individuals infected at this point.
- **Contributing Factors**: The peak is influenced by a high initial number of susceptible individuals and the transmission rate (β). As the disease spreads rapidly, the pool of susceptible individuals decreases, which eventually reduces the rate of new infections.

### ii. Basic Reproductive Number (R0):
- **Calculation and Value**: Given β = 0.0003 (0.3/1000) and γ = 0.1:
  \[
  R_0 = \frac{\beta}{\gamma} = \frac{0.0003}{0.1} = 3
  \]
- **Interpretation**: An R0 of 3 indicates that, on average, each infected individual is expected to infect three other susceptible individuals. This value suggests that the infection will spread significantly unless interventions are put in place to reduce transmission.

### iii. Pandemic Dynamics:
- **Susceptible (S)**: The number of susceptible individuals declines as more people become infected, reducing the pool of those who can contract the virus.
- **Infected (I)**: The number of infected individuals initially rises, peaks, and then falls as the number of susceptible individuals decreases and more infected individuals recover.
- **Recovered (R)**: Continues to increase as more individuals recover from the infection, contributing to a decrease in the spread of the virus.
- **Interactions Between Compartments**: The interactions between the susceptible, infected, and recovered populations illustrate the flow of the epidemic. The rates of transmission and recovery dictate the progression of the epidemic, influencing how quickly it reaches its peak and subsides.

## Part D
![SEIR Model Over 365 Days]([https://github.com/scarlett-duan/SIR-and-SEIR-Model-Implementation-for-Pandemic-Spread/blob/main/SIR_Model_Year.png](https://github.com/scarlett-duan/SIR-and-SEIR-Model-Implementation-for-Pandemic-Spread/blob/main/SEIR_Model_365_Days.png))
![SEIR Model Over 1200 Days]([https://github.com/scarlett-duan/SIR-and-SEIR-Model-Implementation-for-Pandemic-Spread/blob/main/SIR_Model_Year.png](https://github.com/scarlett-duan/SIR-and-SEIR-Model-Implementation-for-Pandemic-Spread/blob/main/SEIR_Model_1200_Days.png))
### iii. Discuss the Pattern Observed in the Number of Infections in Terms of Waves of the Pandemic

- **Initial and Subsequent Waves**: The initial analysis of the SEIR model over 365 days shows a single pronounced wave of infection. This peak suggests a rapid spread followed by a significant decline in the number of infections. However, the extended analysis over 1200 days reveals a more complex pattern with multiple waves. These subsequent waves indicate that the pandemic can resurge after the initial wave has subsided. This pattern could be due to several factors, including waning immunity, changes in social behavior, or introduction of new susceptible individuals into the population.

- **Long-term Trends**: The multi-year perspective provided by the 1200-day plot highlights that after the initial sharp decline, the number of infections stabilizes but with smaller amplitude fluctuations. This suggests a move towards an endemic state where the disease persists at a low level in the population, potentially punctuated by periodic outbreaks that do not reach the magnitude of the initial wave.

### iv. Discuss the Effect of the Exposed Compartment and Birth/Death Rates on the Pandemic Dynamics

- **Exposed Compartment**: The addition of the exposed compartment significantly influences the dynamics of the model by introducing a delay between when individuals contract the infection and when they become infectious. This delay can impact the timing and effectiveness of public health interventions aimed at controlling the spread. For instance, if interventions are implemented based on the number of symptomatic cases, a significant number of exposed but not yet infectious individuals could be overlooked, allowing the disease to spread unnoticed.

- **Birth and Death Rates**: The inclusion of birth and death rates in the model introduces a dynamic element that continuously affects the susceptible population. Over long periods, as shown in the 1200-day plot, the birth rate sustains the susceptible population even as the disease causes deaths in other compartments. This can lead to a steady state where the disease remains present in the population but at manageable levels, or it can fuel new waves if the birth rate significantly exceeds the death rate. The balance between these rates is crucial for predicting the long-term behavior of the pandemic and for planning sustainable public health strategies.

## Part E
![SEIR Sensitivity Analysis](https://github.com/scarlett-duan/SIR-and-SEIR-Model-Implementation-for-Pandemic-Spread/blob/main/SEIR_Sensitivity_Analysis.png)
### iii. Discuss the Implications for Public Health Interventions, Relating β to Social Distancing and γ to Medical Treatments

- **Impact of Varying β (Transmission Rate)**:
  - **Lower β Values**: As seen in the plots with lower β values (e.g., β=0.0001), the peak of the infection is significantly flattened and delayed. This suggests that reducing the transmission rate through measures like social distancing can effectively decrease the spread of the disease and delay the peak, which is crucial for preventing healthcare systems from being overwhelmed.
  - **Higher β Values**: Conversely, higher β values (e.g., β=0.0005) lead to earlier and sharper peaks. This indicates a more rapid spread of the disease, which could quickly overburden medical facilities and lead to higher mortality if not managed properly.

- **Impact of Varying γ (Recovery Rate)**:
  - **Higher γ Values**: Increasing γ, which could be influenced by effective medical treatments that speed up recovery, results in quicker resolution of individual cases, reducing the number of infectious individuals at any given time. This not only shortens the disease duration but also lowers the peak of active cases, as observed in plots where γ increases from 0.05 to 0.20.
  - **Lower γ Values**: Lower recovery rates mean that individuals remain infectious for longer, potentially increasing the disease's spread if infectious individuals continue to interact with the population. This would require prolonged and more intensive use of healthcare resources.

- **Public Health Strategy Implications**:
  - **Balancing β and γ**: The sensitivity analysis demonstrates the importance of balancing interventions that reduce transmission (β) and those that enhance recovery (γ). Effective public health strategies might include promoting social distancing and mask-wearing to reduce β, alongside improving healthcare responses and treatment protocols to increase γ.
  - **Dynamic Adjustments**: The ability to adjust these parameters dynamically in response to changing epidemic conditions can help manage and mitigate the impact effectively. For instance, as new variants of a virus emerge that might spread more easily (increasing β), enhancing medical treatment capabilities and recovery rates (increasing γ) becomes even more critical.

