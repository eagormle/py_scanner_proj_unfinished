# Import the required libraries
import csv
import nmap
import sqlite3
import subprocess
from colorama import Fore, Style

directory = "/Volumes/MacXdrive/Python3/Final/"


# Method to deternine if a socket connects
def is_alive(ip_address):
  nm = nmap.PortScanner()
  nm.scan(ip_address)
  if nm[ip_address].state() == 'up':
    return 'Conected'
  else:
    return 'Unconnected'

def ping(ip_address):
    # Use the subprocess module to execute the ping command
    ping_output = subprocess.run(["ping", "-c", "4", ip_address], capture_output=True)

    # Extract the relevant information from the ping output
    success = ping_output.returncode == 0
    output = ping_output.stdout.decode()
    latency = None
    if success:
        # Extract the latency from the ping output
        latency_line = [line for line in output.split("\n") if "time=" in line][0]
        latency = float(latency_line.split("time=")[1].split(" ")[0])

    # Return a tuple with the success status and latency
    return (latency)


def init_scan():

    # Get starting number for port range
    port_start = int(input("\nPlease enter a starting number for the port range: "))

    # Get ending number for the port range
    port_end = int(input("Please enter an ending number for the port range: "))

    print(Fore.RED + "\nStarting Scan" + Style.RESET_ALL)


    # Add another number to the port_end because Python is weird
    port_end = port_end+1

    # Generate range using range() method
    port_range = range(port_start, port_end)

    # Create an instance of the nmap.PortScanner class
    nm = nmap.PortScanner()

    # Connect to the SQLite3 database
    conn = sqlite3.connect("scan_results.db")

    # Create a cursor object
    cursor = conn.cursor()

# Create the table to store the scan results
    cursor.execute("""CREATE TABLE IF NOT EXISTS scan_results (
        id INTEGER PRIMARY KEY,
        ip_address TEXT,
        port INTEGER,
        state TEXT,
        alive TEXT,
        latency REAL    
    )""")

    file_name = "ip_addresses.csv"
    running_directory = directory + file_name

    # Open the CSV file containing the IP addresses to scan
    with open(running_directory, "r") as csv_file:
       # Create a CSV reader object
        reader = csv.reader(csv_file)

        # Iterate over the rows in the CSV file
        for row in reader:

        # Iterate over the ports in the port list
            for port in port_range:

                Current_port = str(port)

                # Get the IP address from the CSV row
                ip_address = row[0]

                # Check if the host is up
                print('\nChecking to see if '+ip_address+' is up on port '+Current_port+'.')
                is_alive(ip_address)

                 # Scan the IP address and port range
                print('scanning ' +ip_address+ ' on port ' +Current_port+ "..")
                nm.scan(ip_address, Current_port)

                # Pinging the IP address
                print('Pinging ' +ip_address+ "...")
                ping(ip_address)


                # Iterate over the scan results and insert them into the database
                print('logging info....')
                for host in nm.all_hosts():
                    for port in nm[host]["tcp"]:
                        cursor.execute("INSERT INTO scan_results (ip_address, port, state, alive, latency) VALUES (?, ?, ?, ?, ?)", (host, port, nm[host]["tcp"][port]["state"], is_alive(ip_address), ping(ip_address)))

                # Save the changes to the database
                conn.commit()

    # Close the database connection
    conn.close()

    print(Fore.RED + "\nScan Complete" + Style.RESET_ALL)


if __name__ == "__main__":
    init_scan()