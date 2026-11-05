def main(dictionary):
    print("about aysPy")
    print("----------")

    print("aysPy directory:", dictionary["file_dir"])
    print("working directory:", dictionary["work_dir"])

if __name__ == "__main__":
    import json
    print("DEVELOPER MODE ACTIVE\nsysinfo")
    main(json.loads(input("enter a dictionary: ")))