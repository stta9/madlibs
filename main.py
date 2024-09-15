import random

templates = [
    "It was about {} {} ago when I arrived at the hospital in a {}. The hospital is a/an {} place, there are a lot of "
    "{} {}s/es here. "
    "There are nurses here who have {} {}. If someone wants to come into my room I told them that they have to {} "
    "first. "
    "I’ve decorated my room with {} {}. Today I talked to a doctor and they were wearing a {} on their {}. "
    "I heard that all doctors {} {} every day for breakfast. The most {} thing about being in the hospital is the {} "
    "{}!",

    "This weekend I am going camping with {}. I packed my lantern, sleeping bag, and {}. I am so {} to {} in a tent. "
    "I am {} we might see a(n) {}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, "
    "and {}. "
    "I have heard that the {} lake is great for {}. Then we will {} hike through the forest for {} {}. "
    "If I see a {} {} while hiking, I am going to bring it home as a pet! At night we will tell {} {} stories and "
    "roast {} around the campfire!",

    "Dear {}, I am writing to you from a {} castle in an enchanted forest. I found myself here one day after going "
    "for a ride on a {} {} in {}."
    "There are {} {} and {} {} here! In the {} there is a pool full of {}. I fall asleep each night on a {} of {} and "
    "dream of {} {}. "
    "It feels as though I have lived here for {} {}. I hope one day you can visit, although the only way to get here "
    "now is {} on a {} {}!"
]

prompts = [
    ["Number", "Measure of time", "Mode of Transportation", "Adjective", "Adjective2", "Noun", "Color",
     "Part of the Body",
     "Verb", "Number2", "Noun2", "Noun3", "Part of the Body 2", "Verb", "Noun4", "Adjective3", "Silly Word",
     "Noun"],

    ["Proper Noun (Person’s Name)", "Noun", "Adjective (Feeling)", "Verb", "Adjective (Feeling) 2", "Animal",
     "Verb2",
     "Color", "Verb (ending in ing)", "Adverb (ending in ly)", "Number", "Measure of Time", "Color", "Animal",
     "Number", "Silly Word", "Noun2"],

    ["Proper Noun (Person’s Name)", "Adjective", "Color", "Animal", "Place", "Adjective2",
     "Magical Creature (Plural)",
     "Adjective3", "Magical Creature (Plural)2", "Room in a House", "Noun", "Noun2", "Noun (Plural)", "Adjective4",
     "Noun (Plural)", "Number", "Measure of time", "Verb (ending in ing)", "Adjective5", "Noun5"]
]

events = [
    "Suddenly, a loud noise echoed through the area!",
    "Out of nowhere, a mysterious figure appeared in the distance.",
    "A sudden storm began, changing the atmosphere completely."
]

print("Hi! This is a little interactive game aimed for making u feel some fun today. I promise you will not regret!"
      "Follow the instructions, please :)")
print("Please choose a template by entering a number (1, 2, or 3):")
for i, template in enumerate(templates, start=1):
    print(f"{i}. Template {i}")

choice = int(input("Enter the number of the template you want: ")) - 1
selected_template = templates[choice]
selected_prompts = prompts[choice]


def get_user_input(prompts):
    inputs = []
    for prompt in prompts:
        user_input = input(f"Type {prompt}: ")
        inputs.append(user_input)
    return inputs


def generate_story(template, inputs):
    return template.format(*inputs)


user_inputs = get_user_input(selected_prompts)
random_event = random.choice(events)
story = generate_story(selected_template, user_inputs) + f" {random_event}"

print("\nHere is you go! Your story is ready! \n")
print(story)
