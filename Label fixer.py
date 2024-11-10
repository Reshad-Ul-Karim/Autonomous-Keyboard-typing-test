import os

def fix_labels(path, max_class_id):
    issues = []
    for label_file in os.listdir(path):
        file_path = os.path.join(path, label_file)
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Filter out lines with invalid class IDs
        valid_lines = [line for line in lines if int(line.split()[0]) <= max_class_id]

        if len(lines) != len(valid_lines):
            issues.append(label_file)
            # Overwrite the file with only valid lines
            with open(file_path, 'w') as file:
                file.writelines(valid_lines)

    return issues

# Directories for training and validation labels
train_labels_dir = 'merged_dataset2/train/labels'
val_labels_dir = 'merged_dataset2/valid/labels'

# Maximum class ID allowed (nc - 1)
max_class_id = 0

# Run the script to fix the label files
train_issues_fixed = fix_labels(train_labels_dir, max_class_id)
val_issues_fixed = fix_labels(val_labels_dir, max_class_id)

# Print results
if train_issues_fixed:
    print("Fixed issues in training labels:", train_issues_fixed)
else:
    print("No issues found in training labels.")

if val_issues_fixed:
    print("Fixed issues in validation labels:", val_issues_fixed)
else:
    print("No issues found in validation labels.")
