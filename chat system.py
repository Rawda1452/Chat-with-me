users = {}
messages = {}
def register_user():
    username = input("Enter your username to register: ")
    if username in users:
        print("Username already exists.")
    else:
        users[username] = {'sent': [], 'received': []}
        print(f"User '{username}' registered successfully.")
def send_message():
    from_user = input("Enter your username: ")
    if from_user not in users:
        print(f"User '{from_user}' does not exist.")
        return
    to_user = input("Enter the recipient's username: ")
    if to_user not in users:
        print(f"User '{to_user}' does not exist.")
        return
    
    text = input("Enter your message: ")
    users[from_user]['sent'].append((to_user, text))
    users[to_user]['received'].append((from_user, text))
    if (from_user, to_user) not in messages:
        messages[(from_user, to_user)] = []
    messages[(from_user, to_user)].append(text)
    print("Message sent successfully.")

def view_messages():
    username = input("Enter your username to view messages: ")
    if username not in users:
        print(f"User '{username}' does not exist.")
        return
    sent_messages = users[username]['sent']
    received_messages = users[username]['received']

    print("Sent Messages:")
    for recipient, message in sent_messages:
        print(f"To {recipient}: {message}")
    
    print("\nReceived Messages:")
    for sender, message in received_messages:
        print(f"From {sender}: {message}")
def chat():
    while True:
        print("a. Register User")
        print("b. Send Message")
        print("c. View Messages")
        choice = input("Enter your choice: ")
        if choice == 'a':
            register_user()
        elif choice == 'b':
            send_message()
        elif choice == 'c':
            view_messages()
        else:
            print("Invalid choice. Please try again.")
chat()