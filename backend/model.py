import matplotlib
matplotlib.use("Agg")
import pandas as pd
import numpy as np
import difflib
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor
from scipy.optimize import differential_evolution
import base64
from io import BytesIO
import matplotlib.pyplot as plt

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

def get_descriptors(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    return [
        Descriptors.MolWt(mol),
        Descriptors.MolLogP(mol),
        Descriptors.TPSA(mol),
        Descriptors.NumHDonors(mol),
        Descriptors.NumHAcceptors(mol)
    ]

df["descriptors"] = df["SMILES"].apply(get_descriptors)
df = df.dropna()

X = np.array(df["descriptors"].tolist())
y = 0.4*X[:,1] + 0.3*(200-abs(X[:,0]-180))/200 + 0.2*(50-abs(X[:,2]-30))/50 + np.random.normal(0,0.03,len(X))

rf = RandomForestRegressor(n_estimators=150)
gb = GradientBoostingRegressor()
et = ExtraTreesRegressor(n_estimators=150)

rf.fit(X,y)
gb.fit(X,y)
et.fit(X,y)

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

    user_features = np.array(selected["descriptors"].tolist())

    boost = np.array([
        1.2 if ing in preference_boost[preference] else 1.0
        for ing in selected["Name"]
    ])

    pred = (rf.predict(user_features) + gb.predict(user_features) + et.predict(user_features)) / 3

    def objective(weights):
        weights = weights / weights.sum()
        score = np.dot(weights, pred * boost)
        penalty = 5 if np.max(weights) > 0.6 or np.min(weights) < 0.15 else 0
        return -(score - penalty)

    result = differential_evolution(objective, [(1,10)]*len(selected), seed=42)

    weights = result.x / result.x.sum()

    formula = []

    for ing, w in zip(selected["Name"], weights):
        formula.append({
            "ingredient": ing,
            "percentage": float(w * 100),
            "ml": float(w * 50)
        })

    # Create Pie Chart
    plt.figure(figsize=(5,5))
    plt.pie(weights, labels=selected["Name"], autopct='%1.1f%%')

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    chart = base64.b64encode(buffer.read()).decode("utf-8")

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
        "chart": chart,
        "pyramid": {
            "top": top_notes,
            "heart": heart_notes,
            "base": base_notes
        }
    }