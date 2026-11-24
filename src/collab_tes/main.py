names = {
    0: "Alice",
    1: "Bob",
    2: "Charlie",
    3: "Diana"
}

def greet(name):
    print(f"Hello, {name}!")

def main():
    for i in range(len(names)):
        greet(names[i])

if __name__ == "__main__":
    main()
