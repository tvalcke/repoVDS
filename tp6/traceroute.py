import argparse
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
    parser = argparse.ArgumentParser(description="Exécute un tracert "
                                     "vers une cible spécifiée.")
    parser.add_argument("target", help="URL ou adresse IP "
                        "cible pour le tracert")
    parser.add_argument(
        "-p", "--progressive", action="store_true",
        help="Afficher les résultats au fur et à mesure"
    )
    parser.add_argument(
        "-o", "--output", metavar="output_file",
        help="Fichier où enregistrer les résultats du tracert"
    )

    args = parser.parse_args()

    # Appeler la fonction de traceroute avec les arguments
    run_traceroute(
        target=args.target,
        progressive=args.progressive,
        output_file=args.output
    )


if __name__ == "__main__":
    main()
