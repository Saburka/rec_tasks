# Task 1. "Rocket science" script

def group_by(stream, field, success = False):
    headers = stream.readline()
    markers = stream.readline()


    # positions of #
    boundaries = []
    for i in range(0, len(markers)):
        if markers[i] == "#":
            boundaries.append(i)
    # there is no # after last column, so let's add length of the column
    boundaries.append(len(markers))

    # read data
    data_set = dict()
    for line in stream:
        date_start = boundaries[1]
        date_end = boundaries[2]
        status_start = boundaries[9]
        status_end = boundaries[10]

        date = line[date_start : date_end].strip()
        status = line[status_start : status_end].strip()

        year = date[0:4]
        month = date[5:8]

        if field == "year":
            sort_item = year
        elif field == "month":
            sort_item = month
        else:
            return None
        
        # sort data
        if success == True and status == "S":
            data_set[sort_item] = 1 + (data_set[sort_item] if sort_item in data_set else 0)
        elif success == False and status == "F":
            data_set[sort_item] = 1 + (data_set[sort_item] if sort_item in data_set else 0)
        else:
            data_set[sort_item] = 1 + (data_set[sort_item] if sort_item in data_set else 0)

    return data_set

# Let's test!
print(group_by(open("launchlog.txt"), "year", success = True))
