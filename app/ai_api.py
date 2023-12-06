from openai import OpenAI

client = OpenAI()


def write_description():
    name = "Micheal Wazowski JR"
    race = "dwarf"
    char_class = "wizard"
    alignment = "chaotic-good"
    notes = "My wizard has a weird affinity for black licorice"

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a player participating in a DND campaign. You have just finished creating your "
                        "character and need to write a bio for your character."},
            {"role": "user",
             "content": "Compose a character bio that is 100 words considering the character is named {}, is "
                        "a {} by race, {} by class, and has the alignment of {}. Also please consider these notes "
                        "from the user when writing about this character: {}".format(name, race, char_class, alignment, notes)}])

    return completion.choices[0].message
