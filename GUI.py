import tkinter as tk
from tkinter import scrolledtext, messagebox
from Chat_Bot import get_summer_response, is_exit_phrase

def send_message():
    try:
        user_input = entry.get()
        if user_input.strip() == "":
            return
        chat_window.insert(tk.END, f"You: {user_input}\n", "user")
        if is_exit_phrase(user_input):
            chat_window.insert(tk.END, "Bot: You're welcome! Good luck with your summer plans \n\n", "bot")
            entry.delete(0, tk.END)
            chat_window.see(tk.END)
            root.after(1500, root.destroy)  # Close after 1.5 seconds
            return
        response = get_summer_response(user_input)
        chat_window.insert(tk.END, f"Bot: {response}\n\n", "bot")
        entry.delete(0, tk.END)
        chat_window.see(tk.END)  # Auto-scroll to the latest message
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

try:
    # main window
    root = tk.Tk()
    root.title("Summer Assistant Bot")
    root.configure(bg='#f0f0f0')

    # chat window
    chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, state='normal', bg='white')
    chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Configure text tags for different message styles
    chat_window.tag_configure("user", foreground="blue")
    chat_window.tag_configure("bot", foreground="green")

    # input area
    entry = tk.Entry(root, width=50, font=('Arial', 10))
    entry.pack(padx=10, pady=(0, 10), fill=tk.X)
    entry.bind("<Return>", lambda event: send_message())

    # send button
    send_button = tk.Button(root, text="Send", command=send_message, bg='#4CAF50', fg='white', font=('Arial', 10))
    send_button.pack(pady=(0, 10))

    # Add welcome message
    chat_window.insert(tk.END, "Hi there! I'm your Summer Assistant Bot. Ask me anything about summer training or summer semester.\n\n", "bot")

    # run the application
    root.mainloop()
except Exception as e:
    print(f"Error starting GUI: {str(e)}")
    messagebox.showerror("Error", f"Failed to start GUI: {str(e)}")
