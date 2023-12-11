from openai import OpenAI

client = OpenAI()


def write_description(bio_prompt):

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a player participating in a DND campaign. You have just finished creating your "
                        "character and need to write a bio for your character. You are limited to 200 words."},
            {"role": "user",
             "content": bio_prompt}])

    return completion.choices[0].message
