def the_file(file_system, target):
    for item in file_system:
        if isinstance(item, list):
            result = the_file(item, target)
            if result == "HOORAY":
                return result
        elif isinstance(item, str):
            if item == target:
                print("HOORAY")
                return "HOORAY"
    
    return None

file_system = [
    [
        "nothing.txt",
        "dog_pic.png",
        [
            "secret_plan.pdf"
        ]
    ],
    "notion.app",
    "slack.app",
    [
        "fun.txt",
        [
            "meaningless_file.txt",
            "chicken_dinner.txt"
        ],
        "not_fun.txt"
    ],
    "zoom.app"
]

target = "chicken_dinner.txt"

the_file(file_system, target)