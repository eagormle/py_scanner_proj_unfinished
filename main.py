import subprocess
import ip_addresses
import scanner_test_build
import data_report
from colorama import Fore, Style

# Main method
def main():

    print(Fore.GREEN + "\n1. View ip addresses to be scanned" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Run the port scanner" + Style.RESET_ALL)
    print(Fore.GREEN + "3. View SQL Table" + Style.RESET_ALL)
    print(Fore.GREEN + "4. Exit program" + Style.RESET_ALL)

    selection = int(input("\nPlease make a selections: "))
    
    switch_program(selection)


# Switch statement to run different parts of the program
def switch_program(selection):
    if selection == 1:
        if __name__ == '__main__':
            ip_addresses.ip_prog() 
        main()

    elif selection == 2:
        if __name__ == '__main__':
            scanner_test_build.init_scan() 
        main()

    elif selection == 3:
        if __name__ == '__main__':
            data_report.check_table() 
        main()

    elif selection == 4:
       usr_input = str(input("Are you sure you would like to exit, Yes/no: "))
       if usr_input.lower() == 'no':
            main()

    else:
        selection = int(input("Please make a valid selection: "))
        switch_program(selection)


# Run the main method
if __name__ == "__main__":
    main()