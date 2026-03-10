# ** start of main.py **

distance_mi = 1
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if distance_mi > 0 and distance_mi <= 1 :
    if not is_raining :
        print("True")
    else:
        print("False")

if distance_mi > 1 and distance_mi <= 6 :
    if is_raining and not has_bike:
        print("False")
    elif not is_raining and not has_bike:
        print("False")
    elif has_bike and not is_raining:
        print("True")

if distance_mi > 6:
    if has_ride_share_app:
        print("True")
    elif has_car :
        print("True")
    elif not has_car or not has_ride_share_app:
        print("False")






# ** end of main.py **

