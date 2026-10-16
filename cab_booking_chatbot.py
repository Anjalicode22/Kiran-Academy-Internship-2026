
import random

def main():
    # Predefined cab rates
    cab_rates = {
        1: ("Auto", 12),
        2: ("Sedan", 18),
        3: ("SUV", 25)
    }

    # Predefined routes: source, destination, distance
    routes = {
        1: ("Pune Station", "Shivajinagar", 5),
        2: ("Swargate", "Kothrud", 8),
        3: ("Hinjawadi", "Wakad", 10)
    }

    while True:
        print("\n========== CAB BOOKING CHATBOT ==========")
        print("1. Book Ride")
        print("2. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter 1 or 2.")
            continue

        if choice == 1:
            # Choose cab type
            print("\n---------- Choose Cab Type ----------")
            print("1. Auto  - Rs. 12/km")
            print("2. Sedan - Rs. 18/km")
            print("3. SUV   - Rs. 25/km")

            try:
                cab_choice = int(input("Select cab type (1-3): "))
            except ValueError:
                print("Invalid cab choice! Returning to main menu.")
                continue

            if cab_choice not in cab_rates:
                print("Invalid cab choice! Returning to main menu.")
                continue

            cab_name, rate = cab_rates[cab_choice]

            # Choose predefined route
            print("\n---------- Choose Route ----------")
            for route_no, route in routes.items():
                source, destination, distance = route
                print(
                    f"{route_no}. {source} to {destination} "
                    f"({distance} km)"
                )

            try:
                route_choice = int(input("Select route (1-3): "))
            except ValueError:
                print("Invalid route choice! Returning to main menu.")
                continue

            if route_choice not in routes:
                print("Invalid route choice! Returning to main menu.")
                continue

            source, destination, distance = routes[route_choice]

            # Calculate and display fare
            fare = rate * distance

            print("\n========== RIDE DETAILS ==========")
            print(f"Cab Type       : {cab_name}")
            print(f"Source         : {source}")
            print(f"Destination    : {destination}")
            print(f"Distance       : {distance} km")
            print(f"Rate per km    : Rs. {rate}")
            print(f"Total Fare     : Rs. {fare}")

            # Confirm booking before sharing OTP
            print("\n---------- Booking Confirmation ----------")
            print("1. Confirm & Share OTP")
            print("2. Cancel Ride")

            try:
                confirm_choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input! Booking cancelled.")
                continue

            if confirm_choice == 2:
                print("Ride cancelled successfully. No OTP was shared.")
                continue

            elif confirm_choice == 1:
                # Generate and share OTP only after confirmation
                otp = random.randint(1000, 9999)

                print("\nBooking confirmed successfully!")
                print(f"Your ride OTP is: {otp}")
                print("Please share this OTP with the driver.")
                print(
                    "IMPORTANT: Once the OTP is shared, "
                    "the ride cannot be cancelled."
                )

            else:
                print("Invalid choice! Booking cancelled. No OTP was shared.")

        elif choice == 2:
            print("\nThank you for using Cab Booking Chatbot!")
            print("Goodbye!")
            break

        else:
            print("Invalid menu choice! Please select 1 or 2.")


if __name__ == "__main__":
    main()
