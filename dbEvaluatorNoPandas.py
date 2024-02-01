import csv
import matplotlib.pyplot as plt
import numpy as np


class dbEvaluator:
    def __init__(self):
        self.df = self.read_csv("insurance.csv")

    def read_csv(self, file_path):
        with open(file_path, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            return list(reader)

    def ageToBMI(self):
        # Plotting a scatter plot
        age_data = [float(row['age']) for row in self.df]
        bmi_data = [float(row['bmi']) for row in self.df]
        plt.scatter(age_data, bmi_data)
        plt.xlabel('Age')
        plt.ylabel('BMI')
        plt.title('Scatter Plot of Age vs BMI')
        plt.grid(True)
        plt.show()

        print("Correlation Coefficient of Age VS BMI:", self.calculate_correlation(age_data, bmi_data))

    def childrenToCharges(self):
        # Plotting a scatter plot
        children_data = [float(row['children']) for row in self.df]
        charges_data = [float(row['charges']) for row in self.df]
        plt.scatter(children_data, charges_data)
        plt.xlabel('Children')
        plt.ylabel('Charges')
        plt.title('Scatter Plot of Children and Charges')
        plt.grid(True)
        plt.show()

        print("Correlation Coefficient of Children VS Charges:", self.calculate_correlation(children_data, charges_data))

    def regionToBMI(self):
        regions = set(row['region'] for row in self.df)
        average_bmi = {region: [] for region in regions}
        for row in self.df:
            average_bmi[row['region']].append(float(row['bmi']))

        # Calculate average BMI for each region
        average_bmi = {region: sum(bmi_list) / len(bmi_list) for region, bmi_list in average_bmi.items()}

        # Plotting a bar graph
        plt.bar(average_bmi.keys(), average_bmi.values())
        plt.xlabel('Region')
        plt.ylabel('BMI Average')
        plt.title('Bar Graph of Average Region BMI')
        plt.grid(axis='y')  # Show gridlines only on the y-axis
        plt.show()

    def smokerToRegion(self):
        smoker_counts_by_region = {'southeast': {'yes': 0, 'no': 0},
            'northeast': {'yes': 0, 'no': 0},
            'northwest': {'yes': 0, 'no': 0},
            'southwest': {'yes': 0, 'no': 0}}

        for row in self.df:
            region = row['region']
            smoker = row['smoker']
            if region in smoker_counts_by_region:  # Check if region exists in dictionary
                if smoker in smoker_counts_by_region[region]:
                    smoker_counts_by_region[region][smoker] += 1

        # Plotting a bar graph
        regions = ['southeast', 'northeast', 'southwest', 'northwest']
        smoker_yes = [smoker_counts_by_region[region]['yes'] for region in regions]
        smoker_no = [smoker_counts_by_region[region]['no'] for region in regions]

        plt.bar(regions, smoker_yes, label='Smoker: yes')
        plt.bar(regions, smoker_no, bottom=smoker_yes, label='Smoker: no')
        plt.xlabel('Region')
        plt.ylabel('Count')
        plt.title('Number of Smokers by Region')
        plt.legend(title='Bar of Smokers by Region')
        plt.grid(axis='y')
        plt.show()

    def smokerToSex(self):
        smoker_counts_by_sex = {'male': {'yes': 0, 'no': 0},
                                'female': {'yes': 0, 'no': 0}}

        for row in self.df:
            sex = row['sex']
            smoker = row['smoker']
            if smoker in smoker_counts_by_sex[sex]:
                smoker_counts_by_sex[sex][smoker] += 1

        # Plotting a bar graph
        sexes = ['male', 'female']
        smoker_yes = [smoker_counts_by_sex[sex]['yes'] for sex in sexes]
        smoker_no = [smoker_counts_by_sex[sex]['no'] for sex in sexes]

        plt.bar(sexes, smoker_yes, label='Smoker: yes')
        plt.bar(sexes, smoker_no, bottom=smoker_yes, label='Smoker: no')
        plt.xlabel('Sex')
        plt.ylabel('Count')
        plt.title('Number of Smokers by Sex')
        plt.legend(title='Bar of Smokers by Sex')
        plt.grid(axis='y')
        plt.show()

    def sexToBMI(self):
        sex_to_bmi = {'male': [], 'female': []}
        for row in self.df:
            sex = row['sex']
            bmi = float(row['bmi'])
            sex_to_bmi[sex].append(bmi)

        # Calculate average BMI for each sex
        sex_to_bmi = {sex: sum(bmi_list) / len(bmi_list) for sex, bmi_list in sex_to_bmi.items()}

        # Plotting a bar graph
        plt.bar(sex_to_bmi.keys(), sex_to_bmi.values())
        plt.xlabel('Sex')
        plt.ylabel('BMI Average')
        plt.title('Bar Graph of Average BMI by Sex')
        plt.grid(axis='y')  # Show gridlines only on the y-axis
        plt.show()

    def ageToCharges(self):
        # Extracting age and charges data
        age_data = [float(row['age']) for row in self.df]
        charges_data = [float(row['charges']) for row in self.df]

        # Plotting a scatter plot
        plt.scatter(age_data, charges_data)
        plt.xlabel('Age')
        plt.ylabel('Insurance Cost')
        plt.title('Scatter Plot of Age vs Insurance Cost')
        plt.grid(True)
        plt.show()

        # Calculate correlation coefficient
        correlation_coefficient = self.calculate_correlation(age_data, charges_data)
        print("Correlation Coefficient of Age VS Insurance Cost:", correlation_coefficient)

    def calculate_correlation(self, x, y):
        x_mean = np.mean(x)
        y_mean = np.mean(y)
        numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(len(x)))
        denominator = np.sqrt(sum((x[i] - x_mean) ** 2 for i in range(len(x))) * sum((y[i] - y_mean) ** 2 for i in range(len(y))))
        correlation_coefficient = numerator / denominator
        return correlation_coefficient

db = dbEvaluator()
db.ageToBMI()
db.childrenToCharges()
db.regionToBMI()
db.smokerToRegion()
db.smokerToSex()
db.sexToBMI()
db.ageToCharges()