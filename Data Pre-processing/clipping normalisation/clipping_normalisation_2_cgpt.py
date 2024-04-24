def min_max_normalisation(data):
    min_val = min(data)
    max_val = max(data)
    normalized_data = [(x - min_val) / (max_val - min_val) for x in data]
    return normalized_data

def z_score_normalisation(data):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    normalized_data = [(x - mean_val) / std_dev for x in data]
    return normalized_data

def decimal_scaling_normalisation(data):
    max_val = max(abs(x) for x in data)
    if max_val == 0:
        return data
    scale = len(str(max_val))
    normalized_data = [x / (10 ** scale) for x in data]
    return normalized_data

def clipping_normalisation(data, min_clip, max_clip):
    clipped_data = [min(max(x, min_clip), max_clip) for x in data]
    return clipped_data

def main():
    values = []

    while True:
        try:
            user_input = input("Enter a numeric value (press Enter to finish): ")
            if user_input == '':
                break
            value = float(user_input)
            values.append(value)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    print("\nSelect a normalisation technique:")
    print("1. Min-Max Normalisation")
    print("2. Z-Score Normalisation")
    print("3. Decimal Scaling Normalisation")
    print("4. Clipping Normalisation")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        result = min_max_normalisation(values)
    elif choice == '2':
        result = z_score_normalisation(values)
    elif choice == '3':
        result = decimal_scaling_normalisation(values)
    elif choice == '4':
        min_clip = float(input("Enter the minimum clipping value: "))
        max_clip = float(input("Enter the maximum clipping value: "))
        result = clipping_normalisation(values, min_clip, max_clip)
    else:
        print("Invalid choice. Exiting.")
        return

    print("\nOriginal values:", values)
    print("Normalized values:", result)

if __name__ == "__main__":
    main()
