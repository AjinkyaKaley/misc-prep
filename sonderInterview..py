
# 0:2 3:5 7:14', stay_length: 1, current_date: 4
def booking_start_date(bookings, stay_length, current_date):

# ?  print()
  result = []
  _bookings = bookings.split(" ")
  # last_end_date = int(_booking[-1][1])

  for i in range(1,len(_bookings)):
    prev_listing = _bookings[i-1].split(":")
    curr_listing = _bookings[i].split(":")

    prev_end_date = int(prev_listing[1])
    curr_start_date = int(curr_listing[0])

    if curr_start_date >= current_date:
      if (curr_start_date-prev_end_date) > stay_length:
        for j in range(i+1,len(_bookings)):
          print("Hello")
        
          _curr_item=_bookings[j].split(":")
          _prev_item = _bookings[j-1].split(":")
          while int(_curr_item[0]) < int(_prev_item[1]):
            result.append(_curr_item[0])
            _curr_item+=1
          
          # return result

  # return int(_bookings[-1].split(":")[1])
  return result
if __name__ == "__main__":
  print(booking_start_date('0:2 5:6 7:14', 1, 3))





# Your last C/C++ code is saved below:
# // Sonder wants to help guests plan their stay
# // by finding check-in and check-out dates that accommodate a desired length of stay.

# // Sonder determines availability based on existing bookings,
# // serialized as colon-separated pairs of integers.
# // The first integer is a check-in date, and the second is a check-out date.
# // Each integer represents an offset since Jan 1, 2019. 
# // E.g. '0:1' represents a booking where the check-in date is Jan 1st 2019,
# // and the check-out date is Jan 2nd 2019.

# // Directions
# // Implement a method, booking_start_date(string bookings, int stay_length, int current_date)
# // that will return the first day that can accommodate a booking of length stay_length.

# // Examples:
# // Input: bookings: '0:2 3:5 7:14', stay_length: 1, current_date: 4
# // Output: 5
# // Input: bookings: '0:3 3:6 7:14', stay_length: 2, current_date: 4
# // Output: 14
# // Input: bookings: '0:2 5:6 7:14', stay_length: 1, current_date: 3
# // Output: 3

# // Rules:
# // Input is well-formed
# // Bookings will not overlap
# // Bookings are sorted in order of check-in date
# // Only dates later than or equal to current date should be returned


