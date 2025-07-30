## Creating tuples - like sealing important information
point_coordinates = (10, 20)
rgb_color = (255, 128, 0)
student_record = ("Alice", 20, "Computer Science", 3.8)
another_point = 5, 15
single_item_tuple = (42,)

print(f"Point coordinates: {point_coordinates}")
print(f"RGB color: {rgb_color}")
print(f"Student record: {student_record}")
print(f"Single item tuple: {single_item_tuple}")



## Accessing Tuple Elements
book_info = ("1984", "George Orwell", 1949, "Dystopian Fiction")

title = book_info[0]
author = book_info[1]
year = book_info[2]
genre = book_info[3]

print(f"Book: {title}")
print(f"Author: {author}")
print(f"Published: {year}")
print(f"Genre: {genre}")

title, author, year, genre = book_info
print(f"Using unpacking - Book: {title} by {author} ({year})")

first_name, last_name, *other_info = ("John", "Smith", 30, "Engineer", "New York")
print(f"Name: {first_name} {last_name}")
print(f"Other info: {other_info}")



## Tuple Methods and Operations
grades = (85, 90, 78, 90, 92, 85, 88)

print(f"Number of grades: {len(grades)}")
print(f"Highest grade: {max(grades)}")
print(f"Lowest grade: {min(grades)}")
print(f"Number of 90s: {grades.count(90)}")
print(f"Number of 85s: {grades.count(85)}")
print(f"First occurrence of 90: {grades.index(90)}")
print(f"Is 95 in grades? {95 in grades}")
print(f"Is 85 in grades? {85 in grades}")
print(f"First three grades: {grades[:3]}")
print(f"Last three grades: {grades[-3:]}")



## Practical Tuple Examples
def get_distance_between_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

home = (0, 0)
work = (3, 4)
store = (1, 2)

print(f"Distance from home to work: {get_distance_between_points(home, work):.2f}")
print(f"Distance from home to store: {get_distance_between_points(home, store):.2f}")

def analyze_text(text):
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    return (word_count, char_count, sentence_count)

sample_text = "Python is amazing! It's powerful and easy to learn. Try it today!"
word_count, char_count, sentence_count = analyze_text(sample_text)

print(f"Text analysis:")
print(f"Words: {word_count}")
print(f"Characters: {char_count}")
print(f"Sentences: {sentence_count}")

employee_records = [
    ("Alice", "Johnson", "Software Engineer", 75000),
    ("Bob", "Smith", "Data Scientist", 80000),
    ("Charlie", "Brown", "Product Manager", 85000)
]

print("Employee Directory:")
for first_name, last_name, position, salary in employee_records:
    print(f"{first_name} {last_name} - {position} - ${salary:,}")
