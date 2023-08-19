from datetime import datetime

#function that performs the conversion, called later when user inputs time value
def time_conversion(time_str):
    try:
        input_time = datetime.strptime(time_str, "%I:%M %p")
        converted_time = input_time.strftime("%H%M")
        return converted_time
    except ValueError:
        return "Invalid time format"


current_time_str = input("Enter time (hh:mm AM/PM): ") # prompts user for time value input
converted_time_str = time_conversion(current_time_str)
print(f"Converted time: {converted_time_str}hrs")
