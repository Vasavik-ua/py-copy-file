def copy_file(command: str) -> None:
    new_command = command.split(" ")
    if new_command[1] != new_command[2]:
        with (open(new_command[1], "r") as file_in,
              open(new_command[2], "w") as file_out):
            file_content = file_in.read()
            file_out.write(file_content)
