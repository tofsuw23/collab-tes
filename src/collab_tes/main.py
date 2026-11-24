names = {
    0: "Alice",
    1: "Bob",
    2: "Kevin",
    3: "Eve"
}

def greet(name):
    print(f"Hello, {name}!")

def main():
    for i in range(len(names)):
        greet(names[i])

if __name__ == "__main__":
    main()
