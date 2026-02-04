def show_tasks(tasks: list[str]) -> None:
    #Prüft, ob die Aufgabenliste leer ist


    if not tasks:
        print("Keine Aufgaben vorhanden.")
        return

    for index, task in enumerate(tasks, start=1):
        #Gibt jede Aufgabe mit einer Nummer aus
        print(f"{index}. {task}")


tasks = []
    #Leere Liste zum Speichern der Aufgaben

while True:
    #Endlosschleife für das Menü
    print("\n1 - Aufgabe hinzufügen")
    print("2 - Aufgaben anzeigen")
    print("3 - Beenden")
    #Menü anzeigen


    choice = input("Bitte Option wählen: ")
        #Benutzereingabe abfragen

    if choice == "1":
        task = input("Neue Aufgabe eingeben: ")
        #Neue Aufgabe hinzufügen
        tasks.append(task) #Aufgabe zur Liste hinzufüge


    elif choice == "2":
        show_tasks(tasks)
        #Aufgaben anzeigen

    elif choice == "3":
        print("Programm beendet.")
        #Programm beenden
        break #Schleife verlassen
        

    else:
        print("Ungültige Eingabe. Bitte erneut versuchen.")
        #Ungültige Eingabe
    