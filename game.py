import random

# Grade 1 Tamil Words
words = [
    {"tamil": "அணில்", "akuru": "அ", "meaning": "Squirrel"},
    {"tamil": "ஆடு", "akuru": "ஆ", "meaning": "Goat"},
    {"tamil": "இலை", "akuru": "இ", "meaning": "Leaf"},
    {"tamil": "ஈ", "akuru": "ஈ", "meaning": "Fly"},
    {"tamil": "உழவு", "akuru": "உ", "meaning": "Ploughing"},
    {"tamil": "ஊசி", "akuru": "ஊ", "meaning": "Needle"},
    {"tamil": "எலி", "akuru": "எ", "meaning": "Mouse"},
    {"tamil": "ஏணி", "akuru": "ஏ", "meaning": "Ladder"},
    {"tamil": "ஐந்து", "akuru": "ஐ", "meaning": "Five"},
    {"tamil": "ஒன்று", "akuru": "ஒ", "meaning": "One"}
]

score = 0
random.shuffle(words)

print("=== Grade 1 Tamil Word Game ===")
print("Select the correct answer! \n")

for i, word in enumerate(words, 1):
    print(f"Question {i}: '{word['meaning']}' kiyanne mokakda?")

    # Multiple choice options
    options = [word['tamil']]
    while len(options) < 4:
        w = random.choice(words)['tamil']
        if w not in options:
            options.append(w)
    random.shuffle(options)

    for j, opt in enumerate(options, 1):
        print(f"  {j}. {opt}")

    # User Input Validation
    while True:
        try:
            answer = int(input("Your answer (1-4): "))
            if 1 <= answer <= 4:
                break
            print("Please check,Give number between 1 and 4!")
        except ValueError:
            print("Please enter a valid number (1-4).")

    if options[answer - 1] == word['tamil']:
        print("✅ Correct! well done!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is: {word['tamil']}\n")

print(f"Game Over! Your Score: {score}/10")
if score >= 8:
    print("Super! Y0u passed Grade 1 Tamil vocabulary! 🎉")