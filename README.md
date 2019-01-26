# Implement Naive Bayes Classification for Mushroom Data using Python

<b>Language Used :</b> Python<br>
<b>Operating System :</b> MAC OSX<br>
<b>Libraries :</b> csv, random, math<br>
<b>Dataset :</b> Mushroom.csv<br>

The Naïve Bayesian classifier is mainly based on conditional probabilities. In the
data set, the classification variable will be the last column as the code logic is
implemented in that way. Here in order to increase the robustness of the
program and to give it a little more flexibility, instead of using the first 4000
rows for training, I have used a randomization function. Also, instead of
hardcoding the problem for the mushroom set and giving it only 4000 rows for
training, I have set a ratio for setting the training and the testing data so that
dataset of any size can be used with least amount of changes in the code. For
converting the string data into numerical class data, the counting feature is used
wherein the program counts the number of accuracies of each value in the
attribute and assigns that value to the string thus converting the all the data into
numerical based on frequency.

Following are the steps that need to followed in order to implement the Naïve
Bayes Algorithm :

1. Import data from the CSV file.

2. Divide the data into classes for each attribute.

3. The mean and standard deviation of each attribute is calculated.

4. Calculate the class probabilities for each class

5. Select the class which has the highest probability

6. Repeat steps 4 and 5 for each attribute.

The steps to run the program are as follows :
1. Download the contents of the project from the mail server. Now, we need
to check the path for the data file as we need to import the data from a
different location. You will need to modify the file path.

2. Once the path is correctly modified, the program is ready to run.

3. Once all the steps are correctly run, the program will provide the accuracy
of the algorithm.

## Observations :

After running the algorithm multiple number of times, we can see that the
accuracy of the algorithm is in the range of 85 to 88 % which is pretty
satisfactory value.
