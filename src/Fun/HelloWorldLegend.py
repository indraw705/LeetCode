import random, time

alfa = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
# alfa = " abcdefghijklmnopqrstuvwxyz"
# alfa = "dndra"
message = "$$ Pranita Narvekar $$"
out = ""
for i in range(len(message)-1):
    while out != message:
        new_ch = random.choice(alfa)
        out = out + new_ch
        print(f"{out}")
        time.sleep(.00001)
        if new_ch != message[i]:
            out = out[:-1]
            # if (out == message):
            #     print("++++ " + out + " ++++++++")
            #     break
        else:
            if i != len(message)-1:
                i = i + 1

        if out == message:
            break

print(out)

