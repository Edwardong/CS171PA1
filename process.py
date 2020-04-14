import re

""" input format:
    local event_name
    send P_i event_name """
def process_str(input):
    rule = re.compile(r"[^a-zA-Z0-9]")
    if input[:5] == "local":
        input_list = input.strip().split()
        for i in range(len(input_list)):
            input_list[i] = rule.sub('',input_list[i])
        return (input_list[0], input_list[1])
    else:
        receiver = input[5:7]
        message = input[8:]
        return ("send", receiver, message)

if __name__ == '__main__':
    # for testing
    # arg1 = "local Wakeup"
    # arg2 = "send p3 How are you doing?"
    # new_text = process_str(arg1)
    # print(new_text)