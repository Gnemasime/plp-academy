# Step 1: Create a new text file and write to it

try:
    # Open the file in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write three lines of text to the file
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Line 3 with special characters: !@#$%\n")
        print("File 'my_file.txt' created and initial content written successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")

finally:
    print("Step 1 completed.\n")
  

# Step 2: Read and display the file contents

try:
    # Open the file in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read and print each line from the file
        print("Contents of 'my_file.txt':")
        for line in file:
            print(line, end="")  # end="" to avoid double spacing between lines

except FileNotFoundError:
    print("Error: File 'my_file.txt' not found.")

except PermissionError:
    print("Error: Permission denied to open 'my_file.txt'.")

finally:
    print("\nStep 2 completed.\n")


# Step 3: Append additional lines to the file

try:
    # Open the file in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three more lines of text to the file
        file.write("Additional line 4\n")
        file.write("56789\n")
        file.write("Line 6 appended with new data\n")
        print("Additional lines appended to 'my_file.txt' successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")

finally:
    print("Step 3 completed.\n")

# Step 4: Implement error handling

try:
    # Attempt to perform file operations within try blocks

    # Step 1: Create and write to the file
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Line 3 with special characters: !@#$%\n")
        print("File 'my_file.txt' created and initial content written successfully.")

    # Step 2: Read and display the file contents
    with open("my_file.txt", "r") as file:
        print("Contents of 'my_file.txt':")
        for line in file:
            print(line, end="")

    # Step 3: Append additional lines to the file
    with open("my_file.txt", "a") as file:
        file.write("Additional line 4\n")
        file.write("56789\n")
        file.write("Line 6 appended with new data\n")
        print("Additional lines appended to 'my_file.txt' successfully.")

except FileNotFoundError:
    print("Error: File 'my_file.txt' not found.")

except PermissionError:
    print("Error: Permission denied to open 'my_file.txt'.")

except Exception as e:
    print(f"Unexpected error: {e}")

finally:
    print("\nFile handling operations completed.")


