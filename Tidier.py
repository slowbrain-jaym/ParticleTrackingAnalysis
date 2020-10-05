import pandas as pd 

target_folder = r"C:\Users\jamen\Google Drive\Everything\Results\P1\ParticleTracking\RawTrackResults\\"
filenames = ["GlassTest10_0.csv","GlassTest10_1.csv","GlassTest80.csv","GlassTest81.csv"]
test_numbers = [10,10,8,8]
write_folder = r"C:\Users\jamen\Google Drive\Everything\Results\P1\ParticleTracking\\"

dfs = []
for i in range(len(filenames)):
    df = pd.read_csv(target_folder + filenames[i])
    df["Test ID"] = test_numbers[i]
    dfs.append(df)

combined_df = pd.concat(dfs)
combined_df.reset_index(inplace = True)
combined_df.to_feather(write_folder+"AllParticleTracks.feather")