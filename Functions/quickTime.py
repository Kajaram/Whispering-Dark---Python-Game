from inputimeout import inputimeout

def timer(time, prompt):

    try: 
        # Take timed input using inputimeout() function 
        time_over = inputimeout(prompt=f'{prompt} You have {time} seconds!\n', timeout=time) 
        return time_over, True

    # Catch the timeout error 
    except Exception: 

        # Declare the timeout statement 
        time_over = 'Too slow!'

        print(time_over)
        return time_over, False