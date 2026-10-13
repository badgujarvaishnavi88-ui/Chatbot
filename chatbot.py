import tkinter as tk

def get_bot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if "hello" in user_input.split() or "hi" in user_input.split():
        return "Hello! How can I help you?"

    # Basic info
    elif "name" in user_input:
        return "I am your AI Customer Support Bot."
    elif "services" in user_input:
        return "We provide 24/7 customer support."

    # Problems
    elif "problem" in user_input:
        return "Please describe your issue."

    # Mental wellness responses
    elif "overthinking" in user_input:
        return "Try deep breathing, focus on the present, and avoid negative thoughts. Keep yourself busy with positive activities."

    elif "stress" in user_input:
        return "Take breaks, listen to music, exercise, and talk to someone you trust."

    elif "happy" in user_input or "how to stay happy" in user_input:
        return "Stay grateful, spend time with loved ones, and do things you enjoy."

    elif "sad" in user_input:
        return "It's okay to feel sad sometimes. Talk to someone, take rest, and do things you love."

    elif "motivation" in user_input:
        return "Believe in yourself! Small steps every day lead to big success."

    elif "confidence" in user_input:
        return "Practice self-belief, prepare well, and stop comparing yourself with others."

    # Exit
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."

    # Default
    else:
        return "Sorry, I didn't understand. Please try asking something else."

def send():
    user_msg = entry.get()
    chat.insert(tk.END, "You: " + user_msg + "\n")

    bot_reply = get_bot_response(user_msg)
    chat.insert(tk.END, "Bot: " + bot_reply + "\n\n")

    entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("AI Customer Support Chatbot")

chat = tk.Text(root, height=20, width=50)
chat.pack()

entry = tk.Entry(root, width=40)
entry.pack()

send_btn = tk.Button(root, text="Send", command=send)
send_btn.pack()

root.mainloop()
