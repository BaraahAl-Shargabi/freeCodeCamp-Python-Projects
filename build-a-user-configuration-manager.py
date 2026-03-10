
test_settings = {
    'theme' : 'dark',
    'notifications': 'enabled',
}

# =================================

def add_setting(settings, new_pair):
    key = str(new_pair[0]).lower()
    value = str(new_pair[1]).lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


# ================================ 
    
def update_setting(settings, new_setting):
    key = str(new_setting[0]).lower()
    value = str(new_setting[1]).lower()

    if key in settings :
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

# ================================ 

def delete_setting(settings, deleted_setting):
    key = str(deleted_setting).lower()

    # value = str(deleted_setting[1]).lower()

    if key in settings :
        del settings[key]
        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"
        
# ================================ 

def view_settings(settings):
    if len(settings) == 0 :
        return "No settings available."

    result = "Current User Settings:\n"

    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"

    return result


