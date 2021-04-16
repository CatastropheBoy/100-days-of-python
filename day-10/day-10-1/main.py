def format_name(fname, lname):
    fname = fname.title()
    lname = lname.title()
    return f"{fname} {lname}"

name = format_name("ryan", "SHEW")
print(name)