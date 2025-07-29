# Read the story content from the file
with open("story.txt", "r") as file:
    content = file.read()

placeholders = set()
bracket_start = -1

open_tag = "<"
close_tag = ">"

# Extract placeholders enclosed in angle brackets
for index, ch in enumerate(content):
    if ch == open_tag:
        bracket_start = index
    elif ch == close_tag and bracket_start != -1:
        placeholder = content[bracket_start: index + 1]
        placeholders.add(placeholder)
        bracket_start = -1

replacements = {}

# Prompt the user to fill in each placeholder
for tag in placeholders:
    user_input = input(f"Enter a word for {tag}: ")
    replacements[tag] = user_input

# Replace placeholders in the content
for tag in placeholders:
    content = content.replace(tag, replacements[tag])

# Display the final story
print(content)
