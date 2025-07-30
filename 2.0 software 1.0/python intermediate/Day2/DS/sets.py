## Creating sets - like building unique collections
unique_numbers = {1, 2, 3, 4, 5}
colors = {"red", "blue", "green", "yellow"}
mixed_set = {1, "hello", 3.14, True}
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5]
unique_numbers_from_list = set(numbers_with_duplicates)
empty_set = set()

print(f"Unique numbers: {unique_numbers}")
print(f"Colors: {colors}")
print(f"From list with duplicates: {unique_numbers_from_list}")
print(f"Empty set: {empty_set}")

## Set Operations
python_students = {"Alice", "Bob", "Charlie", "Diana"}
java_students = {"Bob", "Charlie", "Eve", "Frank"}
javascript_students = {"Charlie", "Diana", "Eve", "Grace"}

all_programming_students = python_students | java_students | javascript_students
print(f"All programming students: {all_programming_students}")

python_and_java = python_students & java_students
print(f"Students taking both Python and Java: {python_and_java}")

python_only = python_students - java_students
print(f"Students taking Python but not Java: {python_only}")

python_xor_java = python_students ^ java_students
print(f"Students taking Python or Java but not both: {python_xor_java}")

## Modifying Sets
my_skills = {"Python", "JavaScript", "HTML"}
print(f"Initial skills: {my_skills}")

my_skills.add("CSS")
my_skills.add("React")
print(f"After learning CSS and React: {my_skills}")

new_skills = {"Node.js", "MongoDB", "Docker"}
my_skills.update(new_skills)
print(f"After bootcamp: {my_skills}")

my_skills.remove("HTML")
print(f"After forgetting HTML: {my_skills}")

my_skills.discard("PHP")
print(f"After trying to remove PHP: {my_skills}")

removed_skill = my_skills.pop()
print(f"Randomly removed skill: {removed_skill}")
print(f"Remaining skills: {my_skills}")

## Practical Set Examples
def manage_email_subscriptions():
    newsletter_subscribers = {"alice@email.com", "bob@email.com", "charlie@email.com"}
    promotion_subscribers = {"bob@email.com", "diana@email.com", "eve@email.com"}

    both_subscriptions = newsletter_subscribers & promotion_subscribers
    print(f"Subscribers getting both: {both_subscriptions}")

    all_subscribers = newsletter_subscribers | promotion_subscribers
    print(f"All subscribers: {all_subscribers}")

    newsletter_only = newsletter_subscribers - promotion_subscribers
    print(f"Newsletter only: {newsletter_only}")

    return all_subscribers

def find_unique_words(text1, text2):
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    words1 = {word.strip(".,!?;:") for word in words1}
    words2 = {word.strip(".,!?;:") for word in words2}

    common_words = words1 & words2
    unique_to_text1 = words1 - words2
    unique_to_text2 = words2 - words1

    return {
        "common": common_words,
        "unique_to_first": unique_to_text1,
        "unique_to_second": unique_to_text2
    }

def track_inventory_categories():
    electronics = {"laptop", "phone", "tablet", "headphones"}
    discounted_items = {"laptop", "book", "shirt", "headphones"}
    popular_items = {"phone", "book", "laptop", "shoes"}

    discounted_electronics = electronics & discounted_items
    print(f"Discounted electronics: {discounted_electronics}")

    popular_electronics = electronics & popular_items
    print(f"Popular electronics: {popular_electronics}")

    all_products = electronics | discounted_items | popular_items
    print(f"All products: {all_products}")
