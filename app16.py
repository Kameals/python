#dictionary


monthConversions = {
    "Jan": "January ",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    0: "Zero",
    1: "One",

}

print(monthConversions["Jan"])
print(monthConversions.get(0))
print(monthConversions.get("Luv", "Not a valid Key"))



