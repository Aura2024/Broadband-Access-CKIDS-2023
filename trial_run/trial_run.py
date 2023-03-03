from frontier_frame_work_trial import plan_set as frontier_set
from spectrum_frame_work_trial import plan_set as spectrum_set
sample_address = [['90803','1 62nd Place','203','Long Beach',"34.30125","-118.45398", "0000000"],["1 72nd Place","","Long Beach","90803"]]
new_address = []

def frontier_test(address):
    address=address[:4]
    zip_code = address[0]
    address.pop(0)
    address.append(zip_code)
    return frontier_set(address)

def spectrum_test(address):
    address.pop(2)
    address = address[:3]
    zip_code = address[0]
    address.pop(0)
    address.append(zip_code)
    return spectrum_set(address)

for individual_address in sample_address:
    copy_address = individual_address[:]
    index = sample_address.index(individual_address)
    frontier_plan = frontier_test(individual_address)
    spectrum_plan = spectrum_test(individual_address)

    # spectrum_plan = spectrum_test(sample_address)
    for i in frontier_plan:
        frontier_speed = "Frontier Speed: " + i
        frontier_price = "Frontier Price: " + frontier_plan[i]
        copy_address.append(frontier_speed)
        copy_address.append(frontier_price)
    for i in spectrum_plan:
        spectrum_speed = "Spectrum Speed: " + i
        spectrum_price = "Spectrum Price: " + spectrum_plan[i]
        copy_address.append(spectrum_speed)
        copy_address.append(spectrum_price)
    new_address.append(copy_address)



print(new_address)