def file_read_write():
    try:
        # Ask user for the filename
        filename = input("Enter the filename to read: ")
        
        # Try opening the file
        with open(filename, "r") as infile:
            content = infile.read()
        
        # Modify content (convert to uppercase here)
        modified_content = content.upper()
        
        # Write to a new file
        with open("output.txt", "w") as outfile:
            outfile.write(modified_content)
        
        print("✅ File processed successfully! Modified content saved to 'output.txt'.")
    
    except FileNotFoundError:
        print("❌ Error: The file was not found.")
    except PermissionError:
        print("❌ Error: Permission denied while trying to read the file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Run the function
file_read_write()
