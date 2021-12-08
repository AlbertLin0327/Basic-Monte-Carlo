# Import Black Scholes Model
from MonteCarlo import MonteCarlo

# main function
def main():

    # take in the input from user
    print(
        "Enter: spot price, time interval, interest(%), dividend(%), volatility(%), period, stimulations"
    )

    while True:
        try:
            spot, time, interest, dividend, volatility, period, simulations = map(
                float, input().split()
            )
            break

        except:
            print("WRONG FORMAT!!!")

    Model = MonteCarlo(spot, time, interest, dividend, volatility, period, simulations)

    # Calculating Price
    Model.random_path()
    Model.pricing()

    print("")
    print("-----------------------------")
    print(f"Price: {Model.mean}")
    print(f"Std: {Model.std}")
    print("-----------------------------")
    print("")

    # Plot distribution
    Model.plot()


if __name__ == "__main__":
    main()
