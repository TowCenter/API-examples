import requests

# Function to convert "nonstandard JSON" (2D array) from Census API to real JSON
def convert_json(array):
    json = []
    for i in range(1, len(array)):
        temp = {}
        for j in range(0, len(array[0])):
            temp[array[0][j]] = array[i][j]
        json.append(temp)
    return json

# Function to sum up population values for a given variable
def calculate_pop(variable, data):
    sum = 0
    for i in range(0, len(data)):
        sum += int(data[i][variable])
    return sum

########################
# Example 1: Languages in NYC
# Get the response from the API endpoint.
response = requests.get("https://api.census.gov/data/2016/acs/acs5/subject?get=NAME,S1601_C01_001E,S1601_C01_002E,S1601_C01_003E,S1601_C01_004E,S1601_C01_008E,S1601_C01_012E,S1601_C01_016E&for=county:005,047,061,081,085&in=state:36")
data_array = response.json()
data_json = convert_json(data_array)

# Format and print data
print("            LANGUAGES SPOKEN AT HOME IN NYC")
template = "{0:25}|{1:10}|{2:20}" # column widths: 25, 10, 20
print(template.format("     NYC POPULATION", "   COUNT", "     PERCENTAGE"))
total_pop = calculate_pop("S1601_C01_001E", data_json)
print(template.format("Total", total_pop, total_pop/total_pop))
temp_pop = calculate_pop("S1601_C01_002E", data_json)
print(template.format("English only", temp_pop, temp_pop/total_pop))
temp_pop = calculate_pop("S1601_C01_003E", data_json)
print(template.format("Not English", temp_pop, temp_pop/total_pop))
temp_pop = calculate_pop("S1601_C01_004E", data_json)
print(template.format("Spanish", temp_pop, temp_pop/total_pop))
temp_pop = calculate_pop("S1601_C01_008E", data_json)
print(template.format("Other Indo-European", temp_pop, temp_pop/total_pop))
temp_pop = calculate_pop("S1601_C01_012E", data_json)
print(template.format("Asian and Pacific Island", temp_pop, temp_pop/total_pop))
temp_pop = calculate_pop("S1601_C01_016E", data_json)
print(template.format("Other", temp_pop, temp_pop/total_pop))

########################
# Example 2: Median Ages of Racial Populations
# Get the response from the API endpoint
response = requests.get("https://api.census.gov/data/2016/acs/acs5?get=B01002_001E,B01002A_001E,B01002B_001E,B01002C_001E,B01002D_001E,B01002E_001E,B01002F_001E,B01002G_001E,B01002H_001E,B01002I_001E&for=us:*")
data_array = response.json()

# Format and print data (2nd index matches order of query)
print("\n\n          MEDIAN AGES FOR RACIAL POPULATIONS IN U.S.")
template = "{0:50}| {1:12}" # column widths: 50, 12
print(template.format("                    POPULATION", "MEDIAN AGE"))
print(template.format("Total", data_array[1][0]))
print(template.format("White Alone", data_array[1][1]))
print(template.format("Black or African American Alone", data_array[1][2]))
print(template.format("American Indian and Alaskan Native", data_array[1][3]))
print(template.format("Asian Alone", data_array[1][4]))
print(template.format("Native Hawaiian and Other Pacific Islander Alone", data_array[1][5]))
print(template.format("Some Other Race Alone", data_array[1][6]))
print(template.format("Two or More Races", data_array[1][7]))
print(template.format("White Alone, Not Hispanic or Latino", data_array[1][8]))
print(template.format("Hispanic or Latino", data_array[1][9]))

########################
# Example 3: Vietnamese Population by State
# Get the response from the API endpoint
response = requests.get("https://api.census.gov/data/2016/acs/acs5?get=NAME,B01003_001E,B02015_022E&for=state:*")
data_array = response.json()
data_json = convert_json(data_array)

# Format and print data
template = "{0:25}|{1:10}|{2:24}" # column widths: 25, 10, 25
print("\n\n          VIETNAMESE POPULATION BY STATE/TERRITORY")
print(template.format("     STATE/TERRITORY", "   COUNT", "       PERCENTAGE"))
for state in data_json:
    percent = int(state["B02015_022E"])/int(state["B01003_001E"])
    print(template.format(state["NAME"], state["B02015_022E"], percent))
