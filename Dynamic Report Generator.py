# Dynamic Report Generator using OOP

# Decorator to format report output
def format_report(func):
    def wrapper(*args, **kwargs):
        print("\n" + "=" * 50)
        print("        DYNAMIC REPORT GENERATOR")
        print("=" * 50)
        func(*args, **kwargs)
        print("=" * 50)
        print("Report Generated Successfully!")
    return wrapper


class Report:
    # Class Variable
    templates = {
        "Business": "Professional Format",
        "Student": "Academic Format",
        "General": "Standard Format"
    }

    # Constructor
    def __init__(self, title, content, template):
        self.title = title
        self.content = content
        self.template = template

    # Class Method
    @classmethod
    def add_template(cls, name, style):
        cls.templates[name] = style
        print("Template added successfully!")

    # Magic Method
    def __str__(self):
        return (
            f"Title    : {self.title}\n"
            f"Content  : {self.content}\n"
            f"Template : {self.template}"
        )


# Decorated Function
@format_report
def display_report(report):
    print(report)


# ------------------ Main Program ------------------

while True:
    print("\n===== MENU =====")
    print("1. Create Report")
    print("2. Add Template")
    print("3. View Templates")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter Report Title: ")
        content = input("Enter Report Content: ")

        print("\nAvailable Templates:")
        for key in Report.templates:
            print("-", key)

        temp = input("Choose Template: ").strip()

        if temp in Report.templates:
            report = Report(
                title,
                content,
                f"{temp} ({Report.templates[temp]})"
            )
            display_report(report)
        else:
            print("Invalid Template!")

    elif choice == "2":
        name = input("Enter Template Name: ").strip()
        style = input("Enter Template Style: ").strip()
        Report.add_template(name, style)

    elif choice == "3":
        print("\nAvailable Templates:")
        for key, value in Report.templates.items():
            print(f"{key} --> {value}")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please try again.")