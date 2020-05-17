from os import listdir, system
import sys

""" Command that parse downloaded files from Blackboard activities
    into separated directories. It uses the student's code as classifier

Args:
    PATH (str): Path where the files were downloaded from blackboard.
    PATH_DEST (str):  Path where the files will be extracted and grouped.

Returns:
    Nothing
"""


def mapearArchivos(path):
    mapArchivos = {}

    arrArchivos = listdir(path)
    for nameFile in arrArchivos:
        if nameFile != ".DS_Store":
            codigo = nameFile.split("_")[1]
            if codigo not in mapArchivos:
                mapArchivos[codigo] = []
            mapArchivos[codigo].append(nameFile)

    return mapArchivos

def printInformation():
    print("Usage:")
    print("$ python clasentrega.py <PATH_ORIGIN> <PATH_DEST>")
    print("\tPATH_ORIGIN: Directory path where files from blackboard were downloaded.")
    print("\tPATH_DEST: Directory where files will be extracted and organized.")

def main():
    if len(sys.argv) < 3 or sys.argv[1] == "--help":
        printInformation()
        return 0

    PATH = sys.argv[1]
    PATH_DEST = sys.argv[2]
    mapArchivos = mapearArchivos(PATH)

    for codigo,archivos in mapArchivos.items():
        system('mkdir "{}/{}"'.format(PATH_DEST, codigo))
        #system('cd "{}/{}"'.format(PATH_DEST, codigo))
        for archivo in archivos:
            print('mv "{}/{}" "{}/{}"'.format(PATH, archivo, PATH_DEST, codigo))
            system('mv "{}/{}" "{}/{}"'.format(PATH, archivo, PATH_DEST, codigo))

            # Descomprimirlo
            if archivo.endswith(".zip"):
                system('unzip "{}/{}/{}" -d "{}/{}"'.format(PATH_DEST, codigo, archivo, PATH_DEST, codigo))




if __name__ == "__main__":
    main()
