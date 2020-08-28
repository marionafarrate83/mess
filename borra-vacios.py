import os
#dirname = '\path\to\dir'

for root, dirs, files in os.walk("/home/mario/Documents/automation/mess", topdown=False):
    for name in dirs:
        folder = os.path.join(root, name)
        print(folder)
        if os.path.exists(folder) and os.path.isdir(folder):
            if not os.listdir(folder):
                print(f"Borrando directorio vacio {folder}.")
                os.rmdir(folder)
            else:
                print(f"Directorio {folder} no vacio.")
        else:
            print(f"El directorio {folder} no existe.")
