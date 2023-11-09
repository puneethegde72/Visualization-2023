# -*- coding: utf-8 -*-

# Pandas is a tool for Python that lets you work with sets of data. It has tools for discovering, cleaning, analysing, and changing data.
import pandas as pnds
# Python is the language that people use for Matplotlib is a Python tool for plotting data that lets you make static, animate, and interactive graphs.
from matplotlib import pyplot as p_plot
# Set the maximum number of columns to be displayed.
pnds.set_option('display.max_columns', None)

# Make a function called "reading_data_file" that takes an argument called "File_name."
def reading_data_file(File_name):
    #Read a CSV file with pandas, skip the first four rows, and save the data in the "dataset" field.
    dataset = pnds.read_csv(File_name, skiprows=4)
    # Return the 'dataset' to the caller.
    return dataset


# Put the path of the CSV file in the "File_name" field.
File_name = "API_19_DS2_en_csv_v2_4700503.csv"
# Give the method "reading_data_file" the name of a file as an argument, and keep the result in "CO2_Emission_Data."
CO2_Emission_Data = reading_data_file(File_name)

# Line Chart

# Creating the function to plot line graph with some parameters.
def create_line_graph(data, countries, title, x_label, y_label, colors):
    # Set the plot's figure size.
    p_plot.figure(figsize=(14, 6))

    # Go through a list of countries one by one to plot the numbers for each one.
    for i, country in enumerate(countries):
        p_plot.plot(data['index'], data[country], label=country, color=colors[i])

    # Turn the labels on the x-axis so they are easier to read.
    p_plot.xticks(rotation=45)
    # Put a legend in the top left spot.
    p_plot.legend(loc='upper left')
    # Set the x-axis label.
    p_plot.xlabel(x_label)
    # Set the y-axis label.
    p_plot.ylabel(y_label)
    # Set the title of the plot.
    p_plot.title(title)
    # Make grid lines appear with a dashed style and less transparency.
    p_plot.grid(True, linestyle='--', alpha=0.7)
    # Display data for every 5 years on the x-axis.
    x_labels = data['index'].iloc[::5]
    p_plot.xticks(x_labels)
    # Display the plot.
    p_plot.show()


# Filter the DataFrame to get data for 'Arable land (% of land area)'.
Data_Extract_for_Arable_land = CO2_Emission_Data[CO2_Emission_Data['Indicator Name'] == 'Arable land (% of land area)']

# Set "Country Name" as the index.
Data_Extract_for_Arable_land = Data_Extract_for_Arable_land.set_index("Country Name")

# Drop unnecessary columns.
Data_Extract_for_Arable_land = Data_Extract_for_Arable_land.drop(['Country Code',
                                                                  'Indicator Name',
                                                                  'Indicator Code'],
                                                                 axis=1)

# Transpose the DataFrame.
Data_Extract_for_Arable_land = Data_Extract_for_Arable_land.T

# Reset the index.
Data_Extract_for_Arable_land = Data_Extract_for_Arable_land.reset_index()

# Select the specific countries you want to compare.
countries_to_compare = ['Vietnam', 'United States', 'Thailand',
                        'Turkmenistan', 'Saudi Arabia', 'Nigeria',
                        'Mexico', 'Canada', 'France', 'Spain']
Data_Extract_from_Arable_land_for_10_countries = Data_Extract_for_Arable_land[['index'] + countries_to_compare]

# Define a color palette for the lines.
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'purple', 'orange', 'brown']

create_line_graph(Data_Extract_from_Arable_land_for_10_countries, countries_to_compare,
                  'Comparison of Arable land (% of land area) For Different Countries Over the Years',
                  'Year', 'Arable land (% of land area)',
                  colors)

# Bar Chart

# Creating the function to plot bar graph with some parameters.
def create_bar_graph(data, custom_colors, title, x_label, y_label, x_rotation=90):
    #Make a figure or a line for a plot with a certain size figure.
    fig, ax = p_plot.subplots(figsize=(12, 8))
    #Make a bar chart via your own colours and choose which line to use for the data.
    data.plot.bar(color=custom_colors, ax=ax)
    # Set the x-axis label.
    p_plot.xlabel(x_label)
    # Set the y-axis label.
    p_plot.ylabel(y_label)
    # Set the title of plot.
    p_plot.title(title)
    # Turn the x-axis tick marks around (90 degrees is the default).
    p_plot.xticks(rotation=x_rotation)

    #Get the names for the legends from the information columns as strings.
    legend_labels = data.columns.astype(str)
    #Put the legend labels on a legend and give the legend a title.
    ax.legend(legend_labels, title='Year')

    #Add horizontal grid lines that are dashed and have less transparency.
    p_plot.grid(axis='y', linestyle='--', alpha=0.7)
    # display the plot.
    p_plot.show()


# Obtaining all of the information needed to create the bar graph for electric power consumption.
Data_Extraction_for_electric_power_counsumption = CO2_Emission_Data[CO2_Emission_Data['Indicator Name'] == 'Electric power consumption (kWh per capita)']
create_pivot_table_with_index_and_values = Data_Extraction_for_electric_power_counsumption.pivot_table(index=['Country Name'],
                                                                                                       values=['1960', '1965', '1970', '1975',
                                                                                                               '1980', '1985', '1990', '1995',
                                                                                                               '2000', '2005', '2010', '2015',
                                                                                                               '2020'])

# Showing the top 20 country data.
select_data_for_top_20_countries = create_pivot_table_with_index_and_values.head(20)

# Define custom colors for the bars.
custom_colors = ['#FF5733', '#338DFF', '#FFC733', '#33FF57', '#FF33C7',
                 '#33FFC7', '#B533FF', '#9b59b6', '#3498db', '#95a5a6',
                 '#e74c3c', '#34495e', '#2ecc71']

create_bar_graph(select_data_for_top_20_countries, custom_colors,
                 'Comparison of Electric power consumption (kWh per capita) For Different Countries Over the Years',
                 'Countries', 'Electric power consumption (kWh per capita)')

# Pie Chart

# Extracting all the data for total population to make pie chart.
Extracting_the_data_for_total_population = CO2_Emission_Data[CO2_Emission_Data['Indicator Name']=='Population, total']

# Calculate the top 10 countries with the highest population in the year 1960.
In_1960_Top_10_Countries_with_total_population = Extracting_the_data_for_total_population.groupby('Country Name')['1960'].max().sort_values(ascending = False).head(10)
# Calculate the top 10 countries with the highest population in the year 1980.
In_1980_Top_10_Countries_with_total_population = Extracting_the_data_for_total_population.groupby('Country Name')['1980'].max().sort_values(ascending = False).head(10)
# Calculate the top 10 countries with the highest population in the year 2000.
In_2000_Top_10_Countries_with_total_population = Extracting_the_data_for_total_population.groupby('Country Name')['2000'].max().sort_values(ascending = False).head(10)
# Calculate the top 10 countries with the highest population in the year 2020.
In_2020_Top_10_Countries_with_total_population = Extracting_the_data_for_total_population.groupby('Country Name')['2020'].max().sort_values(ascending = False).head(10)

# Create a subplot layout.
fig, axs = p_plot.subplots(2, 2, figsize=(15, 15))

# Define a color palette for the pie charts.
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Function to customize the pie chart.
def customize_pie_chart(pie, title):
    pie.set_title(title, fontsize=16)
    pie.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


# Customize and plot the pie charts for different years.
In_1960_Top_10_Countries_with_total_population.plot.pie(autopct='%1.0f%%', colors=colors, ax=axs[0, 0])
customize_pie_chart(axs[0, 0], 'Top 10 Countries in 1960 With Population')

In_1980_Top_10_Countries_with_total_population.plot.pie(autopct='%1.0f%%', colors=colors, ax=axs[0, 1])
customize_pie_chart(axs[0, 1], 'Top 10 Countries in 1980 With Population')

In_2000_Top_10_Countries_with_total_population.plot.pie(autopct='%1.0f%%', colors=colors, ax=axs[1, 0])
customize_pie_chart(axs[1, 0], 'Top 10 Countries in 2000 With Population')

In_2020_Top_10_Countries_with_total_population.plot.pie(autopct='%1.0f%%', colors=colors, ax=axs[1, 1])
customize_pie_chart(axs[1, 1], 'Top 10 Countries in 2020 With Population')

# Adjust layout.
p_plot.tight_layout()

# Display the pie charts.
p_plot.show()



