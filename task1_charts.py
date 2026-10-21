import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the employees.csv file
df = pd.read_csv("employees.csv")

print("Employee Data:")
print(df)

# --------------------------------------------------
# CHART 1: Bar Chart - Average Salary per Department
# --------------------------------------------------

# Calculate the average salary for each department
avg_salary = df.groupby("department")["salary"].mean()

# Create the bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar(avg_salary.index, avg_salary.values)

# Add title and axis labels
plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

# Display salary values on top of each bar
plt.bar_label(bars, fmt="%.0f")

# Adjust layout and save the chart
plt.tight_layout()
plt.savefig("average_salary_by_department.png")
plt.close()


# --------------------------------------------------
# CHART 2: Histogram - Salary Distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))

# Create a histogram with 5 bins
plt.hist(df["salary"], bins=5, edgecolor="black")

plt.title("Distribution of Employee Salaries")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("salary_histogram.png")
plt.close()


# --------------------------------------------------
# CHART 3: Scatter Plot - ID vs Salary
# --------------------------------------------------

plt.figure(figsize=(8, 5))

# Get each department separately
departments = df["department"].unique()

# Plot each department with a separate colour and legend entry
for department in departments:
    department_data = df[df["department"] == department]

    plt.scatter(
        department_data["id"],
        department_data["salary"],
        label=department
    )

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend(title="Department")

plt.tight_layout()
plt.savefig("id_vs_salary_scatter.png")
plt.close()


# --------------------------------------------------
# CHART 4: Line Chart - Monthly Sales
# --------------------------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(8, 5))

# Draw the line and show markers at each month
plt.plot(months, sales, marker="o", label="Monthly Sales")

plt.title("Monthly Sales from January to June")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()

plt.tight_layout()
plt.savefig("monthly_sales_line.png")
plt.close()


# --------------------------------------------------
# FINISH
# --------------------------------------------------

print("\nAll four charts have been saved successfully!")