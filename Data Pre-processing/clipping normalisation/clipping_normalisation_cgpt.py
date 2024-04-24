def clipping_normalisation(values, min_clip, max_clip):
    """
    Normalize a list of values using clipping.

    Parameters:
    - values: List of numerical values to be normalized.
    - min_clip: Minimum clipping value (no normalized values below this).
    - max_clip: Maximum clipping value (no normalized values above this).

    Returns:
    - List of clipped (normalized) values.
    """
    # Check if the input list is not empty
    if not values:
        raise ValueError("Input list 'values' must not be empty.")

    # Calculate the range of the values
    value_range = max(values) - min(values)

    # Check if the range is zero to avoid division by zero
    if value_range == 0:
        raise ValueError("Cannot normalize a list with zero range.")

    # Calculate normalized values using clipping
    normalized_values = [(min(max(value, min_clip), max_clip) - min_clip) / value_range for value in values]

    return normalized_values

# Example usage:
input_values = [15, 20, 30, 40, 50]
min_clip_value = 10
max_clip_value = 45

normalized_values = clipping_normalisation(input_values, min_clip_value, max_clip_value)
print(normalized_values)
