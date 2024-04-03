from inputimeout import inputimeout

def timer():

    try: 

        # Take timed input using inputimeout() function 
        time_over = inputimeout(prompt='Name your best friend:', timeout=3) 

    # Catch the timeout error 
    except Exception: 

        # Declare the timeout statement 
        time_over = 'Your time is over!'
        print(time_over) 

    # Print the statement on timeoutprint(time_over) 
