from bagOfWords import BAG_OF_WORDS
import random

# This is your big dictionary of words, shortened here for brevity.
# You can copy/paste the entire dictionary from your prompt into BAG_OF_WORDS below.

def random_sentence():
    """
    Create a random sentence by choosing words from several categories
    in a simplistic grammatical structure. You can extend this logic
    for more variety.
    """

    # Some simple grammar templates to choose from:
    templates = [
        # 1) "[The] [noun.person] [verb.stative] [unknown] [noun.animal]."
        "{det} {person} {verb_stative} {unk} {animal}.",
        # 2) "[The] [adj.all] [noun.animal] [verb.motion] [unknown] [adj.all] [noun.person]."
        "{det} {adj1} {animal} {verb_motion} {unk} {adj2} {person}.",
        # 3) "[The] [noun.person] [verb.motion] [unknown] [adj.all] [noun.animal]!"
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

    # Randomly pick a template
    template = random.choice(templates)

    # For each slot, pick a random word from the appropriate list:
    det = random.choice(["The", "A"])  # small set of determiners
    person = random.choice(BAG_OF_WORDS["noun.person"])
    verb_stative = random.choice(BAG_OF_WORDS["verb.stative"])
    unk = random.choice(BAG_OF_WORDS["unknown"])
    animal = random.choice(BAG_OF_WORDS["noun.animal"])
    adj1 = random.choice(BAG_OF_WORDS["adj.all"])
    adj2 = random.choice(BAG_OF_WORDS["adj.all"])
    adj = random.choice(BAG_OF_WORDS["adj.all"])
    verb_motion = random.choice(BAG_OF_WORDS["verb.motion"])

    # Additional placeholders needed by some of the templates:
    det2 = random.choice(["the", "a", "some"])
    det3 = random.choice(["the", "a", "some"])
    adv = random.choice(BAG_OF_WORDS.get("adverb", ["quickly", "slowly", "quietly"]))
    adv2 = random.choice(BAG_OF_WORDS.get("adverb", ["quietly", "loudly", "suddenly"]))
    verb_communication = random.choice(BAG_OF_WORDS.get("verb.communication", ["tells", "discusses"]))
    verb_social = random.choice(BAG_OF_WORDS.get("verb.social", ["meets", "helps"]))
    noun_comm = random.choice(BAG_OF_WORDS.get("noun.communication", ["news", "information"]))
    noun_location = random.choice(BAG_OF_WORDS.get("noun.location", ["place", "park"]))
    noun_qty = random.choice(BAG_OF_WORDS.get("quantifier", ["Many", "Several"]))
    verb_possession = random.choice(BAG_OF_WORDS.get("verb.possession", ["has", "holds"]))
    noun_food = random.choice(BAG_OF_WORDS.get("noun.food", ["bread", "apple"]))
    noun_artifact = random.choice(BAG_OF_WORDS.get("noun.artifact", ["bag", "box"]))
    verb_perception = random.choice(BAG_OF_WORDS.get("verb.perception", ["sees", "hears"]))
    verb_creation = random.choice(BAG_OF_WORDS.get("verb.creation", ["makes", "produces"]))
    noun_state = random.choice(BAG_OF_WORDS.get("noun.state", ["chaos", "peace"]))
    noun_object = random.choice(BAG_OF_WORDS.get("noun.object", ["gift", "tool"]))
    adj3 = random.choice(BAG_OF_WORDS.get("adj.all", ["tall", "short"]))
    adj4 = random.choice(BAG_OF_WORDS.get("adj.all", ["happy", "sad"]))
    adj5 = random.choice(BAG_OF_WORDS.get("adj.all", ["glorious", "ominous"]))

    # Fill in the template:
    sentence = template.format(
        det=det,
        person=person,
        verb_stative=verb_stative,
        unk=unk,
        animal=animal,
        adj1=adj1,
        adj2=adj2,
        adj=adj,
        verb_motion=verb_motion,
        det2=det2,
        det3=det3,
        adv=adv,
        adv2=adv2,
        verb_communication=verb_communication,
        verb_social=verb_social,
        noun_comm=noun_comm,
        noun_location=noun_location,
        noun_qty=noun_qty,
        verb_possession=verb_possession,
        noun_food=noun_food,
        noun_artifact=noun_artifact,
        verb_perception=verb_perception,
        verb_creation=verb_creation,
        noun_state=noun_state,
        noun_object=noun_object,
        adj3=adj3,
        adj4=adj4,
        adj5=adj5
    )

    # Capitalize the first letter and ensure it ends with punctuation
    # (the template might already have punctuation, but let's handle it anyway)
    sentence = sentence[0].upper() + sentence[1:]
    if not sentence.endswith(('.', '!', '?')):
        sentence += '.'

    return sentence

def generate_sentences(n=5):
    """
    Generate n random sentences and return them as a list.
    """
    return [random_sentence() for _ in range(n)]

if __name__ == "__main__":
    # Example usage: print out a few random sentences
    sentences = generate_sentences(5)
    for s in sentences:
        print(s)
