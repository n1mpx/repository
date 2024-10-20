import re
import json


def correct_form_description(entity):
    sentences = [sentence.capitalize() for sentence in entity.lower().split(". ")]
    return ". ".join(sentences)

def correct_form_salary(entity):
    salary = str(round(float(entity), 3)).split('.')
    salary_int = salary[0]
    salary_float = salary[1] + "000"
    salary = f'{salary_int}.{salary_float[:2]}'
    return salary

def correct_form_info(entity):
    while '(' in entity or ')' in entity:
        entity = re.sub(r'\([^()]*\)', "", entity)
    return entity

function_mapping = {"description": correct_form_description,
            "salary": correct_form_salary,
            "key_phrase": lambda x: f"{x.upper()}!",
            "addition": lambda x: f"..{x.lower()}..",
            "reverse": lambda x: x[::-1],
            "company_info": correct_form_info,
            "key_skills": lambda x: x.replace("&nbsp", " ")}

text = input().split(';')
headings = input().split(', ')
text_dict = {}
result = {}

for entry in text:
    if entry:
        key, value = entry.split(':', 1)
        text_dict[key.strip()] = value.strip()

for header in headings:
    if header in text_dict:
        result[header] = function_mapping[header](text_dict[header])

result = json.dumps(result)
print(result)

