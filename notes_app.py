ZERO_BASE_INDEX = 1
notes = []


def add_note():
    new_note = input("Enter note: ")
    notes.append(new_note)
    print("Note added!")


def show_notes():
    if not notes:
        print("No notes yet.")
        return
    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note}")


def delete_note():
    if not notes:
        print("No notes to delete.")
        return
    show_notes()
    to_delete = int(input("Enter the index of the note to delete: "))
    to_delete -= ZERO_BASE_INDEX  # Adjust for zero-based index
    if 0 <= to_delete < len(notes):
        deleted_note = notes.pop(to_delete)
        print(f"Deleted note: {deleted_note}")
    else:
        print("Invalid index number.")


def menu():

    while True:
        answer = input("""
        ==== Notes ====

        1. Add notes
        2. Show notes
        3. Delete notes
        4. Exit

        Choose:
        """)
        if answer == '1':
            add_note()
        elif answer == '2':
            show_notes()
        elif answer == '3':
            delete_note()
        elif answer == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


menu()
