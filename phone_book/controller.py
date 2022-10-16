import model
import view


def lets_go():
    user_choice = view.menu()
    if user_choice == 1:
        user_data = view.get_data_record()
        model.init_for_record(user_data)
        model.record()
    elif user_choice == 2:
        source = view.get_data_io(user_choice)
        model.import_data(source)
    elif user_choice == 3:
        destiny = view.get_data_io(user_choice)
        model.export_data(destiny)
    elif user_choice == 4:
        query = view.get_data_io(user_choice)
        result = model.search(query)
        view.show_search_result(result, query)
    elif user_choice == 5:
        data_for_show = model.init_for_show()
        view.show(data_for_show)
    elif user_choice == 6:
        return
    view.result_message(user_choice)
