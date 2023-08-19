from datetime import datetime

def time_conversion(time_str):
    try:
        input_time = datetime.strptime(time_str, "%I:%M %p")
        converted_time = input_time.strftime("%H%M")
        return converted_time
    except ValueError:
        return "Invalid time format"


input_time_str = input("Enter time (hh:mm AM/PM): ") # user enters time in that format (hour and minute and the time format it is in)
converted_time_str = time_conversion(input_time_str)
print(f"Converted time: {converted_time_str}hrs")
