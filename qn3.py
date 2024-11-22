import numpy as np
# Define conditional probabilities
P_Cloudy = 0.5
P_Sprinkler_given_Cloudy = {True: 0.1, False: 0.5}
P_Rain_given_Cloudy = {True: 0.8, False: 0.2}
P_WetGrass_given_Sprinkler_Rain = {
    (True, True): 0.99,
    (True, False): 0.90,
    (False, True): 0.80,
    (False, False): 0.00
}

# Monte Carlo simulation to estimate P(WetGrass=True | Rain=True)
def monte_carlo_simulation(sample_count=10000):
    wet_grass_and_rain_count = 0  # Count cases where WetGrass=True and Rain=True
    rain_count = 0               # Count cases where Rain=True
    
    for _ in range(sample_count):
        # Sample Cloudy
        is_cloudy = np.random.rand() < P_Cloudy
        
        # Sample Sprinkler given Cloudy
        is_sprinkler_on = np.random.rand() < P_Sprinkler_given_Cloudy[is_cloudy]
        
        # Sample Rain given Cloudy
        is_raining = np.random.rand() < P_Rain_given_Cloudy[is_cloudy]
        
        # Sample WetGrass given Sprinkler and Rain
        is_wet_grass = np.random.rand() < P_WetGrass_given_Sprinkler_Rain[(is_sprinkler_on, is_raining)]
        
        # Increment counts for Rain and WetGrass given Rain
        if is_raining:
            rain_count += 1
            if is_wet_grass:
                wet_grass_and_rain_count += 1
    
    # Calculate conditional probability
    if rain_count == 0:  # Avoid division by zero
        return 0
    return wet_grass_and_rain_count / rain_count

# Run simulation
estimated_probability = monte_carlo_simulation()
print(f"Estimated P(WetGrass=True | Rain=True): {estimated_probability:.4f}")
