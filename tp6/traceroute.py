"""
Valcke tristan - Écrit en partie avec MistralAI
conforme à la PEP8, formaté avec black et vérifié avec flake8
"""
import subprocess


def run_traceroute(target, progressive=False, output_file=None):
    # Commande tracert pour Windows
    command = ["tracert", target]

    try:
        # Si un fichier de sortie est spécifié
        if output_file:
            with open(output_file, "w") as f:
                process = subprocess.Popen(
                    command, stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE, text=True
                )
                for line in process.stdout:
                    if progressive:
                        print(line.strip())  # Afficher au fur et à mesure
                    f.write(line)  # Écrire dans le fichier
                process.communicate()
        else:
            process = subprocess.Popen(
                command, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, text=True
            )
            for line in process.stdout:
                if progressive:
                    print(line.strip())  # Afficher au fur et à mesure
            if not progressive:
                process.communicate()

    except FileNotFoundError:
        print("Erreur : La commande 'tracert' n'a pas été trouvée.")
    except Exception as e:
        print(
            f"Une erreur s'est produite lors de l'exécution de tracert : {e}"
            )


def main():
    # Demander à l'utilisateur l'URL ou l'adresse IP
    target = input("Veuillez entrer l'URL ou l'adresse IP cible : ")

    # Demander à l'utilisateur s'il veut l'affichage progressif
    progressive_input = (
        input("Souhaitez-vous afficher les"
              " résultats au fur et à mesure ? (oui/non) : ")
        .strip()
        .lower()
    )
    progressive = progressive_input == "oui"

    # Demander à l'utilisateur s'il veut
    # enregistrer les résultats dans un fichier
    output_file = (
        input("Souhaitez-vous enregistrer les "
              "résultats dans un fichier ? (oui/non) : ")
        .strip()
        .lower()
    )
    if output_file == "oui":
        output_file = input(
            "Veuillez entrer le nom du "
            "fichier de sortie (ex: traceroute.txt) : "
        )
    else:
        output_file = None

    # Appeler la fonction de traceroute avec les paramètres
    run_traceroute(target, progressive=progressive, output_file=output_file)


if __name__ == "__main__":
    main()
