from operator import index

import pandas as pd
import os

# checking whether csv already exist
if not os.path.exists("user.csv"):
    # creating csv file
    data = pd.DataFrame(columns=['unique_id', 'name', 'address', 'designation'])
    data.to_csv("user.csv", index=False)

else:
    print("User file already exist")

 # auto increment the unique id
def generate_unique_id(df):
    return len(df) + 1



def add_user(name, address, designation):

    if not name or not address or not designation:
        return "Error: All fields are required."

    #  Avoid duplicate entries for name
    data = pd.read_csv("user.csv")
    if name in data["name"].values:
        return "Error: User name already exists."

    # append data into csv file
    user_data = pd.DataFrame([{"unique_id": generate_unique_id(data), "name": name, "address": address, "designation": designation}])
    data = pd.concat([data, user_data])
    data.to_csv("user.csv", index=False)
    print("data entered successfully")


def update_user():
    df = pd.read_csv("user.csv")
    unique_id = int(input("Enter the unique id : "))

    # Add error messages for invalid operations (e.g., updating a non-existent user)
    if unique_id not in df["unique_id"].values:
        print("User not found")
        return

    user_index = df[df["unique_id"] == unique_id].index[0]
    print(user_index)
    print(
        f"Current details :\n Name: {df.at[user_index, 'name']} \n Address :{df.at[user_index, 'address']} \n Designation : {df.at[user_index, 'designation']}")
    name = input("Enter new name : ")
    address = input("Enter new address:")
    designation = input("Enter new designation:")

    if name:
        df.at[user_index, "name"] = name
    if address:
        df.at[user_index, "address"] = address
    if designation:
        df.at[user_index, "designation"] = designation

    df.to_csv("user.csv", index=False)
    print("User updated successfully")


def view_user_details():
    data = pd.read_csv("user.csv")
    unique_id = int(input("Enter the unique id : "))

    # check for unique_id entered by user
    if unique_id not in data["unique_id"].values:
        print("User not found")

    user_details = data[data["unique_id"] == unique_id]
    print(user_details.to_string(index=False))

    # print("Name:",user_details['name'].to_string(index=False))
    # print("Address: ",user_details['address'].to_string(index=False))
    # print("Designation: ",user_details['designation'].to_string(index=False))


def list_all_user():

    data = pd.read_csv("user.csv")
    print(data.to_string(index=False))


def delete_user():
    df = pd.read_csv("user.csv")
    unique_id = int(input("Enter your id : "))

    # check id in dataframe id's:
    if unique_id not in df['unique_id'].values:
        print("User not found")
    else:
        df.drop(df[df['unique_id'] == unique_id].index, inplace=True)
        df.to_csv("user.csv", index=False)
        print("User deleted successfully")


def search_user():

    data = pd.read_csv("user.csv")

    # Ask the user for the value to search
    search = input("Enter the value to search: ").lower()

    # Initialize an empty DataFrame to store matches
    matching_data = pd.DataFrame()


    for column in data.columns:

        if column != "unique_id":
            # Filter rows where the column contains the search value
            filtered_data = data[data[column].str.contains(search, case=False, na=False)]

            # Append matches to the result DataFrame
            matching_data = pd.concat([matching_data, filtered_data])

    # Drop duplicate rows (if multiple columns match the same row)
    matching_data = matching_data.drop_duplicates()

    # Display results or notify the user if no matches found
    if matching_data.empty:
        print("No matches found!")
    else:
        print("Search results:")
        print(matching_data.to_string(index=False))


def main():
    while True:
        print("******** User Information Management System **********")
        print(
            "1. Add User\n 2. Update User \n 3. View User Details \n 4. List All Users \n 5. Delete User\n 6. Search User \n 7. Exit ")

        choice = int(input("Enter your choice:"))

        match choice:
            case 1:
                name = input("Enter name: ")
                address = input("Enter address: ")
                designation = input("Enter designation: ")

                # calling add user function
                add_user(name, address, designation)

            case 2:
                update_user()
            case 3:
                view_user_details()
            case 4:
                list_all_user()
            case 5:
                delete_user()
            case 6:
                search_user()
            case 7:
                exit()


main()