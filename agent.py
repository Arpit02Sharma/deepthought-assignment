# DeepThought Assignment
# ReflectBot AI Agent

def reflect_bot(priority_task_done, learning_done, sleep_hours, helped_someone):

    print("\n--- Daily Reflection Report ---\n")

    if priority_task_done:
        print("Priority task completed.")
    else:
        print("Priority task missed.")
        print("Suggestion: Complete it first tomorrow.")

    if learning_done:
        print("Learning progress maintained.")
    else:
        print("No learning today.")
        print("Suggestion: Study for 30 minutes tomorrow.")

    if sleep_hours < 7:
        print(" Low sleep detected.")
        print("Suggestion: Sleep earlier tonight.")
    else:
        print("Healthy sleep duration.")

    if helped_someone:
        print("Positive collaboration shown.")
    else:
        print("No collaboration today.")
        print("Suggestion: Help one person tomorrow.")

    print("\n--- End of Reflection ---")


# Example Run
reflect_bot(
    priority_task_done=False,
    learning_done=True,
    sleep_hours=6,
    helped_someone=False
)
