% Load the Zoo data set
data = readtable('zoo.csv');

% Extract feature columns and label column
features = data(:, 2:17);
labels = data(:, 18);

% Split data set into training and testing sets
cv = cvpartition(size(data, 1), 'HoldOut', 0.3);
train_features = features(training(cv), :);
train_labels = labels(training(cv), :);
test_features = features(test(cv), :);
test_labels = labels(test(cv), :);

% Define KNN classifier to process the data
k = 5; % Number of neighbors
classifier = fitcknn(train_features, train_labels, 'NumNeighbors', k);

% Train KNN classifier
trained_classifier = train(classifier, train_features, train_labels);

% Use trained classifier to predict labels of testing set
predicted_labels = predict(trained_classifier, test_features);

% Evaluate performance of KNN classifier
accuracy = sum(predicted_labels == test_labels) / numel(test_labels);
confusion_matrix = confusionmat(test_labels, predicted_labels);
precision = diag(confusion_matrix) ./ sum(confusion_matrix, 1)';
recall = diag(confusion_matrix) ./ sum(confusion_matrix, 2);
f1_score = 2 * precision .* recall ./ (precision + recall);


