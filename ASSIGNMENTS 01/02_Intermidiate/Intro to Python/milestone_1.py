def main():
    print("Welcome to the Mars Weight Calculator!")
    earth_weight = float(input("Enter your weight on Earth: "))
    
    # Mars gravity constant
    mars_gravity = 0.378
    
    # Calculate weight on Mars
    mars_weight = round(earth_weight * mars_gravity, 2)
    
    print(f"The equivalent weight on Mars: {mars_weight}")


if __name__ == "__main__":
    main()
