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

def get_courses(student):
    name = student.get('name')
    courses = student.get("courses")
    math = courses[0]
    science = courses[1]
    history = courses[2]
    return f"{name} does {math}, {science} and {history}."
print(get_courses(another))