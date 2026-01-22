priser = {
    "hamburgare": 50,
    "pommes": 25,
    "läsk": 20,
    "milkshake": 30,
    "sallad": 45,
    "mcnuggets": 35
}

försäljning_per_dag = [
    {"hamburgare": 100, "pommes": 80, "läsk": 120, "milkshake": 50, "sallad": 30, "mcnuggets": 70},
    {"hamburgare": 90,  "pommes": 70, "läsk": 100, "milkshake": 40, "sallad": 25, "mcnuggets": 65},
    {"hamburgare": 120, "pommes": 100, "läsk": 150, "milkshake": 60, "sallad": 40, "mcnuggets": 90},
    {"hamburgare": 85,  "pommes": 75, "läsk": 110, "milkshake": 35, "sallad": 20, "mcnuggets": 60},
    {"hamburgare": 95,  "pommes": 85, "läsk": 130, "milkshake": 55, "sallad": 35, "mcnuggets": 75},
    {"hamburgare": 105, "pommes": 90, "läsk": 140, "milkshake": 65, "sallad": 45, "mcnuggets": 80},
    {"hamburgare": 110, "pommes": 95, "läsk": 160, "milkshake": 70, "sallad": 50, "mcnuggets": 85},
    {"hamburgare": 80,  "pommes": 60, "läsk": 90,  "milkshake": 30, "sallad": 20, "mcnuggets": 55},
    {"hamburgare": 115, "pommes": 100, "läsk": 170, "milkshake": 75, "sallad": 55, "mcnuggets": 95},
    {"hamburgare": 130, "pommes": 110, "läsk": 180, "milkshake": 80, "sallad": 60, "mcnuggets": 100}
]

inkomster_per_dag = []

for dag in försäljning_per_dag:
    dags_inkomst = 0 
    
    for produkt, antal in dag.items():
        
        
    
    inkomster_per_dag.append(dags_inkomst)
print("Inkomster per dag:", inkomster_per_dag)