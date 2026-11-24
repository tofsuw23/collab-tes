names = {
    0: "Alice",
    1: "Bob",
}

def greet(name):
    print(f"Hello, {name}!")

def main():
    for i in range(len(names)):
        greet(names[i])

if __name__ == "__main__":
    main()
