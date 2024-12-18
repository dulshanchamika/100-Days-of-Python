def format_name(f_name , l_name):
    """Take a first and last name and format it in to the Title case"""
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"

formatted_name = format_name("dulshan", "CHAMIKA")
