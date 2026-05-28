import random
import string
from datetime import datetime

# Generate a random string to change the file content
random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
content = f"Last auto-commit: {datetime.now()} - ID: {random_str}\n"

should_commit = random.choice([True, False])

# Append to a file named 'autocommit.txt'
if should_commit:
    with open("autocommit.txt", "a") as f:
        f.write(content)

    print("File updated")
else:
    print("No changes made")
