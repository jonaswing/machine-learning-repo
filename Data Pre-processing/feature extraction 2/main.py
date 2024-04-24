def generate_char_ngrams(instance, n_gram_length):
    # Converts the sentence to lowercase to limit the number of n-grams
    sentence = instance.lower()
    # Declares a set to store the n-grams. n-grams only allow unique elements, so no duplicate n-grams will be added.
    n_grams = set()
    # Process the sentence but stop short of the length of the n-gram to ensure the final n-gram can be added.
    for i in range(0, len(sentence) + 1 - n_gram_length):
        # Create an empty string as the starting point for the n-gram.
        n_gram = ""
        # For each character, select the current character and the next few, as required by the n-gram length
        for j in range(i, i + n_gram_length):
            # Add the current character to the n-gram
            n_gram += sentence[j]
        # Add the n-gram to the set
        n_grams.add(n_gram)

    return n_grams

# Modify the main program to include the new function
# Call the generate_data() function to generate the data set.
data = generate_data()
# A header for the input values
print("{0}Input data{1}".format("-" * 20, "-" * 20))
# Call the generate_output function to output the data set to the console window.
generate_output(data)

# A header for the n-grams generated
print("\n{0}Char N-grams{1}".format("-" * 20, "-" * 20))
# Process every attribute in turn
for i in range(0, len(data)):
    # Calculates a new feature by calculating the unique number of trigrams in an input sentence.
    # This example generates n-grams at a character level from sentences, e.g. 3 characters form a trigram.
    char_n_grams = generate_char_ngrams(data[i][0], 3)
    # Outputs the trigrams generated from the sentence as a sorted list
    print(sorted(char_n_grams))
    # Uses the len function to determine the number of trigrams generated from the sentence
    # and add them to the end of the current instance as a new feature.
    data[i].append(len(char_n_grams))

# A header for the output values
print("\n{0}Output data{1}".format("-" * 20, "-" * 20))
# Call the generate_output function to output the data set to the console window.
generate_output(data)
