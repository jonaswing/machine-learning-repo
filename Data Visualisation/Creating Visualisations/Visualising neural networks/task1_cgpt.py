import cv2
import numpy as np
from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

# Load the iris data set.
data_set = load_iris()
# Setting the data argument of the iris set to be the independent variables
# and the target attribute to be the dependent variable.
X = data_set.data
y = data_set.target

# Generate training and test data sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=1)

# Create a MLPClassifier which will iterate over a maximum of 5000 epochs.
# It uses a preset random seed, for reproducibility and generates output
# as it trains/fits the model. The model has a single hidden layer with 10 nodes.
model = MLPClassifier(random_state=1,
                      max_iter=5000,
                      verbose=True,
                      hidden_layer_sizes=(10,))
model.fit(X_train, y_train)


# Define image details
WIDTH = 1920
HEIGHT = 1080
LINE_WIDTH = 5


# A list to store the number of layers and the number
# of nodes in each layer.
layers = list()
# Retrieve the number of nodes in each layer.
# Every object in model.coefs_ is a list containing
# weights associated with the next layer. Each of these
# lists represents a node.
for current in model.coefs_:
    layers.append(len(current))
# model_coefs_ does not contain node details for the output layer.
# To determine the number of nodes in the output layer, model.n_outputs_
# may be used.
layers.append(model.n_outputs_)


# Determine how far the layers should be drawn from one another.
h_increment = WIDTH / (len(layers) + 1)
# Create an empty list to store the node coordinates.
coordinates = list()
# Iterate through each of the layers and calculate
# the coordinates for each node by incrementing
# the horisontal and vertical coordinates.
current_x = h_increment

for i in range(0, len(layers)):
    # For each layer, calculate the vertical spacing
    v_increment = HEIGHT / (layers[i] + 1)
    current_y = v_increment
    # Generate the coordinates for each layer's nodes.
    layer = list()
    for j in range(0, layers[i]):
        # Append the current node's coordinates.
        layer.append((int(current_x), int(current_y)))
        # Increment the vertical increment.
        current_y += v_increment

    # Append the coordinates for each layer to the coordinates list.
    coordinates.append(layer)
    # Increment the horisontal increment.
    current_x += h_increment


# Create a white image with 3 channels 1920 x 1080 pixels in size.
img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
img.fill(255)

# Iterate over all the layers in the coordinates list.
for i in range(0, len(coordinates)):
    # Iterate over all of the nodes in the current layer.
    for j in range(0, len(coordinates[i])):
        # Test to see if there is another layer following the current one.
        # If there is, iterate over all of the nodes in the next layer.
        # This is necessary as a line needs to be drawn from the current
        # node to each node in the next layer.
        if i < len(coordinates) - 1:
            for k in range(0, len(coordinates[i + 1])):
                # Use the coefficient value to draw lines thinner or thicker.
                # Since larger positive values and smaller negative values have a greater
                # impact on the model, they are drawn thicker. To make them easier to compare,
                # each coefficient is converted to its absolute equivalent.
                current_line_width = int(LINE_WIDTH * (abs(model.coefs_[i][j][k]) / 1))
                if current_line_width == 0:
                    current_line_width = 1

                # Ensure that positive coefficient lines are drawn in red and negative in blue.
                color = (0, 0, 255)
                if model.coefs_[i][j][k] < 0:
                    color = (255, 0, 0)

                # Draw a line from a node in the current layer to a node in the next layer.
                cv2.line(img, coordinates[i][j], coordinates[i+1][k], color, current_line_width)
        # Draw the node for the current layer
        cv2.circle(img, coordinates[i][j], 40, (255, 255, 255), -1)
        cv2.circle(img, coordinates[i][j], 40, (0, 0, 0), 1)
        # Add the node text
        cv2.putText(img, str(i+1) + str(j + 1),
                    (coordinates[i][j][0] - 18, coordinates[i][j][1] + 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (0, 0, 0), 1, cv2.LINE_AA)
        # Display node weights
        if i < len(coordinates) - 1:
            for k in range(0, len(coordinates[i + 1])):
                weight_text = '{:.2f}'.format(model.coefs_[i][j][k])
                cv2.putText(img, weight_text,
                            (int((coordinates[i][j][0] + coordinates[i+1][k][0]) / 2),
                             int((coordinates[i][j][1] + coordinates[i+1][k][1]) / 2)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                            (0, 0, 0), 1, cv2.LINE_AA)

# Display the image
cv2.imshow("The image", img)
# Waits for user to press any key
cv2.waitKey(0)
# Close all open windows
cv2.destroyAllWindows()
