from spectrum_frame_work import *
from threading import *

# Class to run multiple threads
class App(Thread):
    def __init__(self, full_address):
        Thread.__init__(self)
        self.full_address = full_address
        self.plan = {}


    def run(self):
        self.plan = plan_set(self.full_address)

    def get_plan(self):
        return self.plan

# Change Path to file we want to read
path = 'sample.csv'
# Change Path to file we want to write to
middle_path = 'sample2.csv'
end_path = 'sample3.csv'

# First open file to see if there is more than one line
with open(path) as f:
    main_csv = []
    lastline = False
    all_lines = f.readlines()
    # If there is more than one line, then we can start reading the file
    if len(all_lines) > 1:
        # Get the last line for future reference
        last_line = all_lines[-1].strip().split(',')
        # Open the file again from the beginning
        with open(path) as read_file:
            # Open the file we want to write to
            with open(middle_path, 'w') as f2:
                # Get the header
                header = read_file.readline().strip().split(',')
                # Remove the third column, which is City
                header.pop(2)
                # Remove extra whitespace
                header[1] = header[1][1:]
                # Create a list of current addresses we want to run
                address_book = []
                # Loop through the file
                for line in read_file:
                    # If the line is not empty
                    if len(line) > 1:
                        # Still a list
                        newline = line.strip().split(',')
                        # Check to see if we are in the last line
                        if newline == last_line:
                            # Set to true
                            lastline = True
                        # Make sure there are 4 columns
                        if len(newline) == 4:
                            # Remove the third column, which is City
                            newline.pop(2)
                            # Append the address to the address_book list
                            address_book.append(newline)
                        # Once address_book list has 10 addresses, or we are in the last line
                        if len(address_book) == 10 or lastline == True:
                            # Try to create threads, can create more if wanted
                            try:
                                address_one = App(address_book[0])
                                address_two = App(address_book[1])
                            except:
                                pass

                            # Try to start threads
                            try:
                                address_one.start()
                                address_two.start()
                            except:
                                pass
                            # Run threads at the same time
                            try:
                                address_one.join()
                                address_two.join()
                            except:
                                pass
                            # Try to get the plan from the threads
                            try:
                                plan_one = address_one.get_plan()
                                plan_two = address_two.get_plan()

                            except:
                                pass
                            # Try to append the plans to a list
                            try:
                                plans = []
                                plans.append(plan_one)
                                plans.append(plan_two)
                            except:
                                pass
                            # Loop through the address_book list
                            for ad in address_book:
                                # Get the index of the address
                                index = address_book.index(ad)
                                # Create a dictionary with the address
                                first_dict = {"Street": ad[0], "Unit": ad[1], "Zipcode": ad[2]}
                                # Loop through the plan at the indexed address
                                for key in plans[index]:
                                    # Make sure only internet plans were collected
                                    if "Channels" not in key:
                                        # Add the plan to the dictionary
                                        first_dict[key] = plans[index][key]
                                # Append the dictionary to the main_csv list
                                main_csv.append(first_dict)
                                # Go through each dictionary
                                for plan in main_csv:
                                    # Go through each key in the dictionary
                                    for key in plan:
                                        # Make sure the header accounts for all keys
                                        if key not in header:
                                            header.append(key)
                                # Create a list to write to the file
                                write_line = []
                                # Go through each item in the header
                                for item in header:
                                    # If the item is in the dictionary, then add it to the list
                                    if item in first_dict:
                                        write_line.append(first_dict[item])
                                    # If the item is not in the dictionary, then add an empty string
                                    else:
                                        write_line.append("")
                                # Write the list to the file
                                f2.write(",".join(write_line) + "\n")
                            # Clear the lists
                                main_csv = []
                            address_book = []
    # Write the header to the file
    with open(end_path, "w") as f:
        f.write(",".join(header) + "\n")
        contents = (line for line in open(middle_path))
        f.writelines(contents)