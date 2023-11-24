import argparse

def ip_http_requests(path:str, sort_results=False):
    '''Prints unique IPs and count of occurrences from a given web server log'''
    ip_dict = {}
    with open(path, 'r') as file:
        for line in file:
            # Split the line by spaces
            parts = line.split()

            # Extract the IP address from the first field
            ip_address = parts[0]

            if ip_address in ip_dict:
                # Increment the count for the IP address
                ip_dict[ip_address] += 1
            else:
                # If the IP address is not in the dictionary, add it with a count of 1
                ip_dict[ip_address] = 1
    if sort_results:
        ip_dict = dict(sorted(ip_dict.items(), key=lambda item:item[1], reverse=True))

    # Print the results
    for ip, count in ip_dict.items():
        print(f'{ip}: {count} requests')
 
def user_agent_count(path: str, sort_results=False):
    '''Prints unique User agents and count of occurrences from a given web server log'''
    ua_dict = {}
    with open(path, 'r') as file:
        for line in file:
            # Split the line by spaces
            parts = line.split()

            # Extract the UA field
            user_agent = ' '.join(parts[11:-1]).strip('"') # remove last dash

            if user_agent in ua_dict:
                # Increment the count for the user agent
                ua_dict[user_agent] += 1
            else:
                # If the UA is not in the dictionary, add it with a count of 1
                ua_dict[user_agent] = 1

    # Sort dictionary
    if sort_results:
        ua_dict = dict(sorted(ua_dict.items(), key=lambda item:item[1], reverse=True))


    # Print the results
    for ua, count in ua_dict.items():
        print(f"{ua}: {count} requests")


def busiest_hour(path: str):
    '''Prints the busiest hour each day from a given web server log'''
    date_hour_dict = {}

    with open(path, 'r') as file:
        for line in file:
            # Split the line by spaces
            parts = line.split()

            # Extract the date and hour from the timestamp
            date,time = parts[3][1:].split(':', 1)  # Remove the leading '[' and split timestamp
            hour = time.split(':')[0]

            # Create a unique key for each date
            date_key = date

            # If the date doesn't exist in the dictionary, add
            if date_key not in date_hour_dict:
                date_hour_dict[date_key] = {}

            # Update the count for the hour in the dictionary
            if hour in date_hour_dict[date_key]:
                date_hour_dict[date_key][hour] += 1
            else:
                date_hour_dict[date_key][hour] = 1

    # Print the results
    for date, hour_dict in date_hour_dict.items():
        busiest_hour = max(hour_dict, key=hour_dict.get)
        print(f'{date}: {busiest_hour} is the busiest hour with {hour_dict[busiest_hour]} requests')


def main():
    parser = argparse.ArgumentParser(description="Analyse CLF format web server logs.")
    parser.add_argument("PATH", help="Path to .log file")
    parser.add_argument("-i", "--ipcounts", action="store_true", help="Find unique IPs and the number of HTTP requests sent.")
    parser.add_argument("-b", "--busyhours", action="store_true", help="Find the busiest hour of each day (in chronological order).")
    parser.add_argument("-u", "--useragents", action="store_true", help="Find unique User Agents and number of occurrences.")
    parser.add_argument("-s", "--sort", action="store_true", help="Sorts results DESC (only for -i|-u)")

    args=parser.parse_args()
    path=args.PATH
    do_ip = args.ipcounts
    do_busy = args.busyhours
    do_ua = args.useragents
    do_sort = args.sort

    try:
        if do_ip:
            ip_http_requests(path,do_sort)
        if do_ua:
            user_agent_count(path,do_sort)
        if do_busy:
            busiest_hour(path)
        
    except Exception as e:
        print(f"An error occurred reading the log file: {e}")

if __name__ == "__main__":
    main()
