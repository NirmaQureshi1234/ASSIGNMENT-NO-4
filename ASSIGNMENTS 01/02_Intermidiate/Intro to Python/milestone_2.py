def main():
    print("Welcome to the Planetary Weight Calculator!")
    
    # Ask the user for their weight on Earth
    earth_weight = float(input("Enter your weight on Earth: "))
    
    # Gravity constants for each planet
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }
    
    # Ask the user for the name of a planet
    planet = input("Enter a planet: ")
    
    if planet in gravity_factors:
        # Calculate weight on the selected planet
        planet_weight = round(earth_weight * gravity_factors[planet], 2)
        print(f"The equivalent weight on {planet}: {planet_weight}")
    else:
        print("Invalid planet name. Please enter a valid planet name from the solar system.")
    

if __name__ == "__main__":
    main()
