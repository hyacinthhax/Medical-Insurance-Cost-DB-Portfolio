import pandas as pd
import matplotlib.pyplot as plt


class dbEvaluator:
	def __init__(self):
		with open("insurance.csv", "r") as csv_file:
			self.df = pd.read_csv(csv_file)

	def ageToBMI(self):
		# Plotting a scatter plot
		plt.scatter(self.df['age'], self.df['bmi'])
		plt.xlabel('Age')
		plt.ylabel('BMI')
		plt.title('Scatter Plot of Age vs BMI')
		plt.grid(True)
		plt.show()

		# Calculate correlation coefficient
		correlation_coefficient = self.df['age'].corr(self.df['bmi'])
		print("Correlation Coefficient of Age VS BMI:", correlation_coefficient)

	def childrenToCharges(self):
		# Plotting a scatter plot
		plt.scatter(self.df['children'], self.df['charges'])
		plt.xlabel('Children')
		plt.ylabel('Charges')
		plt.title('Scatter Plot of Children and Charges')
		plt.grid(True)
		plt.show()

		# Calculate correlation coefficient
		correlation_coefficient = self.df['children'].corr(self.df['charges'])
		print("Correlation Coefficient of Children VS Charges:", correlation_coefficient)


	def regionToBMI(self):
		average_bmi = self.df.groupby('region')['bmi'].mean()

		# Plotting a bar graph
		average_bmi.plot(kind='bar')
		plt.xlabel('Region')
		plt.ylabel('BMI Average')
		plt.title('Bar Graph of Average Region BMI')
		plt.grid(axis='y')  # Show gridlines only on the y-axis

		plt.show()


	def smokerToRegion(self):
		smoker_counts_by_region = self.df.groupby('region')['smoker'].value_counts().unstack()

		# Plotting a bar graph
		smoker_counts_by_region.plot(kind='bar', stacked=True)
		plt.xlabel('Region')
		plt.ylabel('Count')
		plt.title('Number of Smokers by Region')
		plt.legend(title='Bar of Smokers by Region')
		plt.grid(axis='y')

		plt.show()

	def smokerToSex(self):
		smoker_counts_by_sex = self.df.groupby('sex')['smoker'].value_counts().unstack()
		# Plotting a bar graph
		smoker_counts_by_sex.plot(kind='bar', stacked=True)
		plt.xlabel('Sex')
		plt.ylabel('Count')
		plt.title('Number of Smokers by Sex')
		plt.legend(title='Bar of Smokers by Sex')
		plt.grid(axis='y')

		plt.show()

	def sexToBMI(self):
		sex_to_bmi = self.df.groupby('sex')['bmi'].mean()

		# Plotting a bar graph
		sex_to_bmi.plot(kind='bar')
		plt.xlabel('Sex')
		plt.ylabel('BMI Average')
		plt.title('Bar Graph of Average BMI by Sex')
		plt.grid(axis='y')  # Show gridlines only on the y-axis

		plt.show()


db = dbEvaluator()
db.ageToBMI()
db.childrenToCharges()
db.regionToBMI()
db.smokerToRegion()
db.smokerToSex()
db.sexToBMI()

""" A few hypothesis about the graphs:
1: The more children you have the more cost breaks you'll be given.
2: There are more smokers and higher average bmi in the South East.
3: There's almost a solid line in BMI vs Age that young people have lower bmi.
4: There's more male smokers than female smokers.
5: Females tend to have lower BMI than males
"""