import pandas as pd
import math

output_file = 'sampled_addresses.csv'
main_file = 'Main_LA_City.csv'
with open(output_file, 'w') as out_file:
    with open(main_file, 'r') as in_file:
        df = pd.read_csv(in_file)
        # store the number of addresses in each block group in a dictionary
        block_group_dict = df['Block ID'].value_counts().to_dict()
        second_df = pd.DataFrame()
        # a for loop that iterates through the dictionary and stores a value of 10% of the value. Then a for loop to iterate the number of times the value is stored in the dictionary and randomly choose a row from the dataframe if the block id is the key in the first for loop and store it in a new dataframe
        for key, value in block_group_dict.items():
            percentage = math.ceil(value * 0.1)
            ls = df[df['Block ID'] == key].sample(n=percentage)
            second_df = pd.concat([second_df, ls])
        # write the new dataframe to a csv file
        second_df.to_csv(out_file, index=False)



