from dispatch_event import register_handler


def file_manager_open():
    print("file_manager_open is called")


register_handler("file_manager_open", file_manager_open)
