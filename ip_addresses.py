import csv
import main
from colorama import Fore, Style

directory = "/Volumes/MacXdrive/Python3/Final/"

# Main method
def ip_prog():

    print(Fore.GREEN + "\n1. View IP addresses to be scanned" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Add an IP address to be scanned" + Style.RESET_ALL)
    print(Fore.GREEN + "3. Delete an IP address" + Style.RESET_ALL)
    print(Fore.GREEN + "4. Reset the IP addresses to be scanned" + Style.RESET_ALL)
    print(Fore.GREEN + "5. Go back to main menu" + Style.RESET_ALL)


    ip_selection = int(input("\nPlease make a selection: \n"))
    switch_program(ip_selection)


# Switch statement to run different parts of the program
def switch_program(ip_selection):


    if ip_selection == 1:
        file_name = "ip_addresses.csv"
        running_directory = directory + file_name
        with open(running_directory, "r") as csv_file:
    # Create a CSV reader object
            reader = csv.reader(csv_file)
    # Iterate over the rows in the CSV file
            for row in reader:
                print(row)
    
        ip_prog()

    elif ip_selection == 2:
        print("Please type an ip address to add. EX: ")
        print("127.0.0.1")
        ip_add = str(input())

        file_name = "ip_addresses.csv"
        running_directory = directory + file_name
        with open(running_directory, "a", newline="") as csv_file:
        # Create a CSV writer object
            writer = csv.writer(csv_file)
        
            # Write a CSV row using user input
            writer.writerow([ip_add])
        ip_prog()

    elif ip_selection == 3:

        with open(running_directory, "r") as csv_file:
            new_ip_list = []
            reader = csv.reader(csv_file)
            for row in reader:
                print(row)

        remove = input("Type the IP address that you would like to delete: ")
        remove_ip = "['" + remove +"']"

        with open(running_directory, "r") as csv_file:
            new_ip_list = []
            reader = csv.reader(csv_file)
            for rows in reader:
                if rows[0] != remove:
                    new_ip_list.append(rows)

        with open(running_directory, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)

        # Write each row to the file
            for row in new_ip_list:
                writer.writerow(row)
    
        ip_prog()

    elif ip_selection == 4:

        file_name = "ip_addresses.csv"
        running_directory = directory + file_name

        new_ip_list = []

        with open(running_directory, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)

        # Write each row to the file
            for row in new_ip_list:
                writer.writerow(row)
        
        ip_prog()

    elif ip_selection == 5:
            if __name__ == '__main__':
                main.main()

    else:
        ip_selection = int(input("Please make a valid selection: "))
        switch_program(ip_selection)


# Run the main method
if __name__ == "__main__":
    ip_prog()