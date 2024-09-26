from text_editor import TextEditor
from history import History

def main():
    editor = TextEditor()
    history = History()

    editor.set_content("Hello")
    print("Current content is: ", editor.get_content())

    history.save_history_state(editor.save())

    editor.set_content("Hello World")
    print("Current content is: ", editor.get_content())

    history.save_history_state(editor.save())

    editor.set_content("Hello Python")
    print("Current content is: ", editor.get_content())
   
    #undo last action
    editor.restore(history.undo())
    print("After Undo: ", editor.get_content())

    #undo last action to revert to original state
    editor.restore(history.undo())
    print("After Second Undo: ", editor.get_content())


if __name__ == "__main__":
    main()