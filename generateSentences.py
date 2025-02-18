import random
from bagOfWords import BAG_OF_WORDS

# Simple grammar templates
TEMPLATES = [
    "{det} {person} {verb_stative} {unk} {animal}.",
    "{det} {adj1} {animal} {verb_motion} {unk} {adj2} {person}.",
    "{det} {person} {verb_motion} {unk} {adj} {animal}!",
    "{det} {person} {verb_stative} {unk} {animal}.",
    "{det} {adj1} {animal} {verb_motion} {unk} {adj2} {person}.",
    "{det} {person} {verb_motion} {unk} {adj} {animal}!",
    "{det} {person} {verb_communication} {adv} about {det2} {noun_comm}.",
    "{noun_qty} of {adj1} {animal} {verb_motion} {adv} across {det2} {noun_location}.",
    "{det} {adj2} {person} {verb_social} {det2} {adj3} {person} {adv} for {det3} {noun_object}.",
    "{det} {animal} {verb_possession} {noun_food} from {det2} {person}'s {noun_artifact} {adv}.",
    "Whenever {det} {person} {verb_motion} {unk} {noun_location}, {det2} {adj4} {animal} {verb_perception} them {adv}.",
    "Suddenly, {det} {adv2} {verb_creation} {noun_artifact} transforms {det2} {noun_location} into {det3} {adj5} {noun_state}."
]

# Randomly choose a word from a list
def pick_word(category, default=None):
    return random.choice(BAG_OF_WORDS.get(category, [default])) if category in BAG_OF_WORDS else default

# Function to generate a random sentence
def random_sentence():
    """
    Create a random sentence using a simple grammatical structure.
    The structure and word choices can be expanded for variety.
    """
    # Choose a template
    template = random.choice(TEMPLATES)

    # Define placeholders and pick random words for them
    placeholders = {
        'det': random.choice(["The", "A"]),
        'person': pick_word("noun.person"),
        'verb_stative': pick_word("verb.stative"),
        'unk': pick_word("unknown"),
        'animal': pick_word("noun.animal"),
        'adj1': pick_word("adj.all"),
        'adj2': pick_word("adj.all"),
        'adj': pick_word("adj.all"),
        'verb_motion': pick_word("verb.motion"),
        'det2': random.choice(["the", "a", "some"]),
        'det3': random.choice(["the", "a", "some"]),
        'adv': pick_word("adverb", "quickly"),
        'adv2': pick_word("adverb", "quietly"),
        'verb_communication': pick_word("verb.communication", "tells"),
        'verb_social': pick_word("verb.social", "meets"),
        'noun_comm': pick_word("noun.communication", "news"),
        'noun_location': pick_word("noun.location", "place"),
        'noun_qty': pick_word("quantifier", "Many"),
        'verb_possession': pick_word("verb.possession", "has"),
        'noun_food': pick_word("noun.food", "bread"),
        'noun_artifact': pick_word("noun.artifact", "bag"),
        'verb_perception': pick_word("verb.perception", "sees"),
        'verb_creation': pick_word("verb.creation", "makes"),
        'noun_state': pick_word("noun.state", "chaos"),
        'noun_object': pick_word("noun.object", "gift"),
        'adj3': pick_word("adj.all", "tall"),
        'adj4': pick_word("adj.all", "happy"),
        'adj5': pick_word("adj.all", "glorious")
    }

    # Create the sentence by replacing placeholders in the template
    sentence = template.format(**placeholders)

    # Capitalize and ensure it ends with proper punctuation
    sentence = sentence[0].upper() + sentence[1:]
    if not sentence.endswith(('.', '!', '?')):
        sentence += '.'

    return sentence

# Function to generate multiple random sentences
def generate_sentences(n=5):
    """
    Generate n random sentences and return them in a list.
    """
    return [random_sentence() for _ in range(n)]

if __name__ == "__main__":
    # Example usage: print out a few random sentences
    sentences = generate_sentences(5)
    for s in sentences:
        print(s)
