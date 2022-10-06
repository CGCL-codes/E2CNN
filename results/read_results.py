import json
with open("finance_lowercase/result.json", "r", encoding="utf-8") as f:
    
    for line in f.readlines():
        spo_text = json.loads(line)
        ent_set = set()
        for spo in spo_text['triple_list_gold']:
            