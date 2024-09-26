from canvas import Canvas
from history import History

def main():
    canvas = Canvas()
    history = History()

    # Set canvas attributes
    canvas.set_content("Circle")
    canvas.set_color("Red")
    canvas.set_border("Dotted")
    print("Current Canvas: Content={}, Color={}, Border={}".format(canvas.get_content(), canvas.get_color(), canvas.get_border()))

    # Save state 1
    history.save_history_state(canvas.save())

    # Modify canvas attributes
    canvas.set_content("Rectangle")
    canvas.set_color("Blue")
    canvas.set_border("Solid")
    print("Modified Canvas: Content={}, Color={}, Border={}".format(canvas.get_content(), canvas.get_color(), canvas.get_border()))

    # Save state 2
    history.save_history_state(canvas.save())

    # Modify canvas attributes again
    canvas.set_content("Triangle")
    canvas.set_color("Green")
    canvas.set_border("Dashed")
    print("Modified Canvas Again: Content={}, Color={}, Border={}".format(canvas.get_content(), canvas.get_color(), canvas.get_border()))

    # Undo the last change
    canvas.restore(history.undo())
    print("After Undo 1: Content={}, Color={}, Border={}".format(canvas.get_content(), canvas.get_color(), canvas.get_border()))

    # Undo another change
    canvas.restore(history.undo())
    print("After Undo 2: Content={}, Color={}, Border={}".format(canvas.get_content(), canvas.get_color(), canvas.get_border()))


if __name__ == "__main__":
    main()
