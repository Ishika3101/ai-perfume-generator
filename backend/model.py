import pandas as pd
import numpy as np
import difflib

np.random.seed(42)

note_structure = {
    "top": [
        "limonene","citral","linalool","citronellol","menthol"
    ],
    "heart": [
        "geraniol","phenylethyl alcohol","anisaldehyde","eugenol","isoeugenol"
    ],
    "base": [
        "vanillin","coumarin","benzyl acetate","cashmeran","ambroxide","cedrol","vetiverol"
    ]
}

ingredient_data = [
("vanillin","COC1=CC=C(C=C1O)C=O"),
("ethylvanillin","CCOC1=CC=C(C=C1O)C=O"),
("coumarin","O=C1OC2=CC=CC=C2C=C1"),
("linalool","CC(C)=CCC=C(C)CO"),
("citral","CC(=C)CCC/C(C)=C/C=O"),
("limonene","CC1=CCC(CC1)=C(C)C"),
("patchoulol","CC1CCC2C(C1)CCC(C2)(C)O"),
("muscone","CC1CCCCCCCC(=O)CC1"),
("civetone","CCCCCCCCCC1=CCCC(=O)CCCC1"),
("benzyl acetate","CC(=O)OCC1=CC=CC=C1"),
("phenylethyl alcohol","OCCc1ccccc1"),
("geraniol","CC(C)=CCCC(C)=CCO"),
("citronellol","CC(C)CCC=C(C)CO"),
("cashmeran","CC1C(C2=C(C1(C)C)C(=O)CCC2)(C)C"),
("cedrol","CC1CCC2C(C1)C(C)(C)CCC2O"),
("vetiverol","CC1CCC2C(C1)CCC(C2)O"),
("ambroxide","CC1CCC2(C(C1)CCC2O)C"),
("benzyl alcohol","OCc1ccccc1"),
("anisaldehyde","COC1=CC=CC=C1C=O"),
("eugenol","COC1=CC=C(C=C1)CC=C"),
("isoeugenol","COC1=CC=C(C=C1)/C=C/C"),
("menthol","CC(C)C1CCC(CC1)C(C)O"),
("camphor","CC1(C2CCC1(C(=O)C2)C)C"),
("borneol","CC1(C2CCC(C1O)C2)C"),
("thymol","CC(C)C1=CC(=C(C=C1)O)C"),
("carvacrol","CC(C)C1=CC(=CC=C1)O"),
("nerol","CC(C)=CCCC(C)=CCO"),
("farnesol","CC(C)=CCCC(C)=CCCC(C)=CCO"),
("nerolidol","CC(C)=CCCC(C)=CCCC(C)=CCO"),
("hydroxycitronellal","CC(C)CC(CC=O)O"),
("benzyl benzoate","O=C(OCC1=CC=CC=C1)C2=CC=CC=C2"),
("methyl salicylate","COC(=O)C1=CC=CC=C1O"),
("salicylaldehyde","O=Cc1ccccc1O"),
("piperonal","O=COc1cc2ccccc2o1"),
("acetophenone","CC(=O)C1=CC=CC=C1"),
("methyl cinnamate","COC(=O)C=CC1=CC=CC=C1"),
("ethyl cinnamate","CCOC(=O)C=CC1=CC=CC=C1"),
("indole","C1=CC=C2C(=C1)C=CN2"),
("skatole","CC1=CNC2=CC=CC=C12"),
("beta ionone","CC1=CC(=O)C(C=C1)(C)C"),
("alpha ionone","CC1=CC(=O)C=C1C(C)C"),
("damascone","CC1=CC(=O)C(C=CC1)(C)C"),
("iso e super","CC1CCC(CC1)C2CCC(CC2)(C)C"),
("exaltolide","CCCCCCCCCCCCC=O"),
("tonalid","CC1=CC(=O)OC2=CC=CC=C12C"),
("fixolide","CC1=CC(=O)OC2=CC=CC=C12"),
("maltol","O=C1C=CC(=O)O1"),
("ethyl maltol","CCOC1=CC=CC=C1O"),
("vanillyl alcohol","COC1=CC=C(C=C1O)CO")
]

df = pd.DataFrame(ingredient_data, columns=["Name","SMILES"])
df["Name"] = df["Name"].str.lower()

preference_boost = {
    "sweet": ["vanillin","ethyl maltol","maltol","coumarin"],
    "fresh": ["limonene","linalool","citronellol"],
    "woody": ["vetiverol","cedrol","iso e super"],
    "luxury": ["ambroxide","cashmeran","fixolide"],
    "romantic": ["phenylethyl alcohol","geraniol","citronellol"],
    "masculine": ["vetiverol","cedrol","iso e super"],
    "feminine": ["geraniol","citronellol","phenylethyl alcohol"]
}

def generate_perfume(ingredients_input, preference):

    ingredients_input = [i.strip().lower() for i in ingredients_input]

    corrected = []
    for ing in ingredients_input:
        match = difflib.get_close_matches(ing, df["Name"], n=1, cutoff=0.6)
        if match:
            corrected.append(match[0])

    selected = df[df["Name"].isin(corrected)]

    if selected.empty:
        return {"formula": [], "pyramid": {"top": [], "heart": [], "base": []}}

    weights = np.random.rand(len(selected))
    weights = weights / weights.sum()

    for i, ing in enumerate(selected["Name"]):
        if preference in preference_boost and ing in preference_boost[preference]:
            weights[i] *= 1.2

    weights = weights / weights.sum()

    formula = []

    for ing, w in zip(selected["Name"], weights):
        formula.append({
            "ingredient": ing,
            "percentage": float(w * 100),
            "ml": float(w * 50)
        })

    top_notes = []
    heart_notes = []
    base_notes = []

    for ing in selected["Name"]:
        if ing in note_structure["top"]:
            top_notes.append(ing)
        elif ing in note_structure["heart"]:
            heart_notes.append(ing)
        else:
            base_notes.append(ing)

    return {
        "formula": formula,
        "pyramid": {
            "top": top_notes,
            "heart": heart_notes,
            "base": base_notes
        }
    }