## Read Json and convert to DataFrame using Pandas

df=pd.read_json(path,encoding='utf-8-sig')
df_refined = pd.concat([pd.json_normalize(page)  for page in  df["records"].tolist()], axis=0)#Normalize all json files
