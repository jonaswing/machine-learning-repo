from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_digits
import pydotplus


digits = load_digits()


X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.10, random_state=1)


model = DecisionTreeClassifier(random_state=1)
model.fit(X_train, y_train)


dot_data = tree.export_graphviz(model,
                                feature_names=[f'feature_{i}' for i in range(digits.data.shape[1])],
                                class_names=[str(x) for x in digits.target_names],
                                filled=True,
                                rounded=False,
                                special_characters=True,
                                node_ids=True,
                                proportion=True,
                                precision=1,
                                leaves_parallel=False,
                                out_file=None,
                                rotate=True)


print("DOT representation:\n", dot_data)


graph = pydotplus.graph_from_dot_data(dot_data)
graph.set('rankdir', 'LR')  # Draw from left to right
graph.dpi = 300

# Add colors to boxes to indicate majority class
for node in graph.get_nodes():
    label = node.get('label')
    if label is not None and 'value' in label:
        values = label.split('\\n')
        if len(values) > 1:
            values = values[1]
            majority_class = max(values.split(','), key=lambda x: int(x.split()[1]))
            if int(majority_class.split()[1]) / sum([int(x.split()[1]) for x in values.split(',')]) > 0.5:
                node.set_fillcolor('#ccffcc')  # Light green for majority class
            else:
                node.set_fillcolor('#ffccff')  # Light purple for minority class


graph.write_png("DigitsClassificationTree.png")





