another = {
  'name':"John Doe",
  'age': 30,
  'is_student': False,
  'courses': ["Math", "Science", "History"],
  'address': {
    'street': "123 Main St",
    'city': "Anytown",
    'zip_code': "12345",
    'co-ordinates': {
      'latitude': 40.7128,
      'longitude': -74.0060
    }
  }

}

def get_full_address(student):
    address = student['address']
    return f"{address['street']}, {address['city']}, {address['zip_code']} {address['co-ordinates']}"

print(get_full_address(another))


def check_student_status(student):
    return student.get('is_student', False)
print(check_student_status(another))