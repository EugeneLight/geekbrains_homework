import model
import view


def lets_go():
    user_choice = view.menu()
    if user_choice == 1:
        user_data = view.get_data_record()
        model.init_for_record(user_data)
        model.record()
    elif user_choice == 2:
        source = view.get_data_io()
        model.import_data(source)
    elif user_choice == 3:
        destiny = view.get_data_io()
        model.export_data(destiny)
    view.result(user_choice)
