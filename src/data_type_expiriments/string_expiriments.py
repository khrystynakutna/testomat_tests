
hello_world = "Hello World"

def print_hello_world():
    print(hello_world)

def hello_to(name:str):
    print(f"Hello, {name}!")

print_hello_world()
hello_to("John")

name = "John"
print(name.lower())

name = "john test"
print(name.upper())

site = "https://www.google.com"
print(site.removeprefix("https://"))
print(site.removesuffix(".com"))
print(site)
print(site.startswith("https://"))
print(site.endswith(".com"))

email = ("test1@gmail.com, test2@gmail.com, test3@gmail.com, test4@gmail.com")
print(email.split(", "))

def check_protocol(actual_url: str):
    if actual_url.startswith("http://"):
        print(f"{actual_url} is insecure")
    else:
        print(f"{actual_url} is secure")

check_protocol("https://www.google.com")
check_protocol("http://www.google.com")