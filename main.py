import random
import math


# quadratic function
def calculate_distance_for_parabolic_flight(initial_velocity, angle=45):
    g = 9.81  # Acceleration due to gravity (m/s^2)
    time = (2 * initial_velocity * math.sin(math.radians(angle))) / g  # Total time of flight (s)
    distance = initial_velocity * math.cos(math.radians(angle)) * time
    return distance


# linear function
def calculate_distance_for_parabolic_flight_by_energy(energy, initial_distance=0, constant=100):
    return energy * constant + initial_distance


def main():
    random_list = [random.uniform(1, 100) for _ in range(50)]

    W = random.gauss(10, 10)
    for energy in random_list:
        actual_value = calculate_distance_for_parabolic_flight_by_energy(energy)
        prediction = W * energy
        error = actual_value - prediction

        learning_rate = 0.0001
        W += learning_rate * error * energy
        # print(f"{W:.2f} {energy:.2f} {actual_value:.2f} {prediction:.2f} {error:.2f}")

    print(f"Final W: {W:.2f}")
    error = sum([abs(calculate_distance_for_parabolic_flight_by_energy(energy) - W * energy) for energy in random_list])
    print(f"Test Error: {error:.2f}")


if __name__ == "__main__":
    main()
